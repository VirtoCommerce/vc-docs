# Authorization in Virto Commerce

After authentication, [ASP.NET](http://ASP.NET) Core Web APIs need to authorize access. This process allows a service to make APIs available to the authenticated users, but not to all. Authorization can be provided based on user roles or on a custom policy, which might include inspecting claims or other heuristics.

Restricting access to an [ASP.NET](http://ASP.NET) Core MVC route is as easy as applying an `Authorize` attribute to the action method (or to the controller class, if all controller actions require authorization), as shown in the following example:

```csharp title="VirtoCommerce.Platform.Web\Controllers\Api\SecurityController.cs"
        [HttpGet]
        [Authorize]
        [Route("currentuser")]
        public async Task<ActionResult<UserDetail>> GetCurrentUser()
        {
            ...
        }
```

By default, adding an `Authorize` attribute without parameters will limit access to the authenticated users for that controller or action.

To further restrict an API to be available for only users with specific permissions, the attribute can be expanded to specify permissions the users must have assigned:

```csharp
[Authorize("{permission}")]
```

## Permission-based authorization

Typically, applications require more than just authenticated users. You would want to have users with different sets of permissions. The easiest way to achieve this is with the **role-based** authorization, where you can allow users to perform certain actions depending on their membership in a role.

For small applications, it might be perfectly fine to use **role-based** authorization; however, this does have some drawbacks. For instance, it would be difficult to add or remove roles because you would have to check every `Authorize` attribute with the role specified in the code, whenever you change roles.

You can implement more flexible authorization using permission claims. Instead of checking role membership, you would then check whether a user has a permission (**basic right**) to perform a certain action. Permission, in this case, is represented as a claim.

In order to make it easier to manage claims, you can group them in roles. The latest versions of [ASP.NET](http://ASP.NET) Core makes this possible with role claims.

This solution has the following benefits:

* It allows us you to add, remove, or delete roles without any changes to the code.
* You can redefine a role by changing its permissions.
* You can implement the administration UI to easily edit roles and permissions.

The Virto Commerce platform supports two main authorization strategy types for permission authorization:

* **Permission:** Basic right or permission. The system has a global list of predefined permissions . You can assign permissions to users via group permissions by creating a role and then assigning that role to a user.
	* [**Global permissions:**](global-permissions.md) Permissions that are checked without taking the requested resources into account. To check this sort of permissions, you need to operate permission names only, for example, `Authorize("{permission}")`.
	* [**Scoped**, **Imperative**, or **Resource-based permissions:**](scope-based-permissions.md) Whether the permissions are checked depends upon the resource being accessed. Consider a document that has an author property. Only the author is allowed to update the document. Consequently, the document must be retrieved from the data store before the authorization evaluation can occur. 
     
     ![Readmore](media/readmore.png){: width="25"} [Resource-based Authorization in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/security/authorization/resourcebased?view=aspnetcore-3.1).
* **Role:** A collection of permissions that could be assigned to roles (in their turn, roles  are assigned to users). Rather than assigning individual permissions directly to each user, permissions are grouped into roles. You can define one or more roles on your site, and then grant permissions to each role.
