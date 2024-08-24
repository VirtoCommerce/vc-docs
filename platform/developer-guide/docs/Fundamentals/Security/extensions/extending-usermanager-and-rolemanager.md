# ASP.NET Identity UserManager and RoleManager Extension

Virto Commerce has a custom implementation of default `UserManager` and `RoleManager`, which is [VirtoCommerce.Platform.Web.Security.CustomUserManager](https://github.com/VirtoCommerce/vc-platform/blob/dev/src/VirtoCommerce.Platform.Security/CustomUserManager.cs) and [VirtoCommerce.Platform.Web.Security.CustomRoleManager](https://github.com/VirtoCommerce/vc-platform/blob/dev/src/VirtoCommerce.Platform.Security/CustomRoleManager.cs), respectively.

## Override UserManager with custom implementation

The Virto Commerce custom User Manager is registered in the DI as the `UserManager` type and a factory method, which allows using UserManager within the scoped requests.

```csharp title="module.cs"
public void Initialize(IServiceCollection serviceCollection) 
{
  ...
  serviceCollection.AddScoped<UserManager<ApplicationUser>, MyCustomUserManager>();
  ...
}
```

Custom `RoleManager` is registered similarly.

## Usage

You can get both user and role managers by adding the respective factory to your service constructor:

```csharp
 public class MyCoolService 
    {
        private readonly Func<UserManager<ApplicationUser>> _userManagerFactory;
        private readonly Func<RoleManager<Role>> _roleManagerFactory;

        public MyCoolService(Func<UserManager<ApplicationUser>> userManagerFactory, Func<RoleManager<Role>> roleManagerFactory)
        {
            _userManagerFactory = userManagerFactory;
            _roleManagerFactory = roleManagerFactory;
        }

        public void DoMyCoolWork()
        {
            using var userManager = userManagerFactory();
            using var roleManager = roleManagerFactory();
            ...
        }
    }
```

!!! note
	In common cases, you do not need to get User or Role Manager directly by type. You can use factories instead.

![Readmore](../media/readmore.png){: width="25"} [UserManager TUser Class in ASP.NET Core Identity](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.identity.usermanager-1?view=aspnetcore-6.0)
    
![Readmore](../media/readmore.png){: width="25"} [RoleManager TRole Class in ASP.NET Core Identity](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.identity.rolemanager-1?view=aspnetcore-6.0)
    
![Readmore](../media/readmore.png){: width="25"} [Custom User Management in ASP.NET Core MVC with Identity](https://codewithmukesh.com/blog/user-management-in-aspnet-core-mvc/)
