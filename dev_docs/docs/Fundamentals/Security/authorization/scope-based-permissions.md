# Scope-based, Imperative, or Resource-based Authorization

Imperative permissions are permissions that depend on the resource being accessed. Consider an order that has a store property. You need the user to be able to view only the orders belonging to a particular store. Consequently, the order must be retrieved from the data store before the authorization evaluation can occur.

Permission check based on the `[Authorize]` attribute evaluation occurs before data binding and before the execution of the API action that loads the order. For these reasons, declarative authorization with an `[Authorize]` attribute does not suffice. Instead, you can invoke a custom authorization method, a style known as *imperative authorization*.

## Defining New Permission Scope

Let's see how the resource-based authorization works using the following example.

Suppose we need to restrict user access to only the orders created in a particular store. To enable this authorization check-in code and allow it to assign this permission for end authorization role, we should do the following:

Define the new `OrderSelectedStoreScope` class derived from `PermissionScope`. The object of this type will be used in the role management UI and hold the store identifier selected by the user. It can then be used for future authorization check.

```csharp title="VirtoCommerce.OrdersModule.Web/Authorization/OrderSelectedStoreScope.cs"
 /// <summary>
    /// Restricts access rights to orders that belong to a particular store
    /// </summary>
    public sealed class OrderSelectedStoreScope : PermissionScope
    {
        public string StoreId => Scope;
    }
```

The **StoreId** property will contain the ID of the store selected by the user in the role management UI.

To register the scope and make the **global** permission **scope-based**, you need to add the following code to your **Module.cs** file:

```csharp title="VirtoCommerce.OrdersModule.Web/Scripts/module.cs"
public void PostInitialize(IApplicationBuilder appBuilder)
    {
        ...
        var permissionsProvider = appBuilder.ApplicationServices.GetRequiredService<IPermissionsRegistrar>();
        permissionsProvider.WithAvailabeScopesForPermissions(new[] {
                                                                        "order:read",
                                                                    }, new OrderSelectedStoreScope());
        ...
```

With this code, you register the `order:read` permission in the system and associate it with the `OrderSelectedStoreScope` scope. The next step is to register the presentation template for `OrderSelectedStoreScope`, which allows to user configure permission scope setting in the role manager:

```js title="VirtoCommerce.OrdersModule.Web/Scripts/order.js"
//A large part of the code is removed for clarity reasons
angular.module(moduleName, []).run( ['platformWebApp.permissionScopeResolver', 'platformWebApp.bladeNavigationService', function(scopeResolver, bladeNavigationService) {
 //Registering permission scope templates used for scope bounded definition in the role management UI
        var orderStoreScope = {
            type: 'OrderSelectedStoreScope',
            title: 'Only for orders in selected stores',
            selectFn: function (blade, callback) {
                var newBlade = {
                    id: 'store-pick',
                    title: this.title,
                    subtitle: 'Select stores',
                    currentEntity: this,
                    onChangesConfirmedFn: callback,
                    dataPromise: stores.query().$promise,
                    controller: 'platformWebApp.security.scopeValuePickFromSimpleListController',
                    template: '$(Platform)/Scripts/app/security/blades/common/scope-value-pick-from-simple-list.tpl.html'
                };
                bladeNavigationService.showBlade(newBlade, blade);
            }
        };
        scopeResolver.register(orderStoreScope);
}] );
```

After these steps, the global `order:read` permission can be additionally restricted to work only for the selected stores in the role assignment.

This step shows you how to declare scope-based permissions in the code and how to define UI templates to configure the additional parameters for these scopes in the manager. In the next section, we will show how to use these permissions in authorization checks within the API controllers.

### Writing Scope-based Authorization Handler

Writing a handler for scope-based authorization is not much different from writing a plain requirement handler. You need to create a custom requirement class and implement a requirement handler class derived from `PermissionAuthorizationHandlerBase`:

```csharp title="VirtoCommerce.OrdersModule.Web/Authorization/OrderAuthorizationHandler.cs"
public sealed class OrderAuthorizationHandler : PermissionAuthorizationHandlerBase<OrderAuthorizationRequirement>
{
    ...

      protected override async Task HandleRequirementAsync(AuthorizationHandlerContext context, OrderAuthorizationRequirement requirement)
        {
            //Call the base handler first to check the user has a global permission for this action
            await base.HandleRequirementAsync(context, requirement);

            if (!context.HasSucceeded)
            {
                //If we are here, this means the user does not have a global assigned "oder:read" permission, and we need to try to check the scope-based permissions
                var userPermission = context.User.FindPermission(requirement.Permission/*order:read*/, _jsonOptions.SerializerSettings);
                if (userPermission != null)
                {
                    //Read the scopes from the role assignment
                    var storeSelectedScopes = userPermission.AssignedScopes.OfType<OrderSelectedStoreScope>();   
                    //Get all store IDs from scopes                
                    var allowedStoreIds = storeSelectedScopes.Select(x => x.StoreId).Distinct().ToArray();

                    if (context.Resource is OrderOperationSearchCriteriaBase criteria)
                    {
                        //Enforce the authorization policy by modifying the search criteria object being trasferred through adding the store IDs received from the role scopes
                        criteria.StoreIds = allowedStoreIds;                       
                        context.Succeed(requirement);                        
                    }
                }
            }
}
```

In this implementation, we load all `StoreSelectedScope` objects assigned to the `order:read` permission in the role definition, and then use the store identifiers retrieved from these scopes to change `CustomerOrderSearchCriteria` for enforcing the policy to return only orders for the stores defined in the permission scopes.

### Checking Scope-based Permissions

Since Virto security is based on the default [ASP.NET](http://ASP.NET) Core security mechanics, we can use [IAuthorizationService](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authorization.iauthorizationservice) and custom authorization policy handlers for any imperative authorization check.

```csharp title="VirtoCommerce.OrdersModule.Web/Controllers/Api/OrderModuleController.cs"
  [HttpGet]
        [Route("{id}")]
        public async Task<ActionResult<CustomerOrder>> GetById(string id, [FromRoute] string respGroup = null)
        {
            var searchCriteria = new CustomerOrderSearchCriteria
            {
                Ids = new[] { id },
                ResponseGroup = respGroup
            }
            //in this line, we use IAuthorizationService _authorizationService to check the 'order:read' permission for the specific resource, CustomerOrderSearchCriteria, where the policy handler can modify the provided criteria and remove or add the stores the user has access to.
            var authorizationResult = await _authorizationService.AuthorizeAsync(User, searchCriteria, new OrderAuthorizationRequirement("order:read"));
            if (!authorizationResult.Succeeded)
            {
                return Unauthorized();
            }
            var result = await _searchService.SearchCustomerOrdersAsync(searchCriteria);

            return Ok(result.Results.FirstOrDefault());
        }
```

In this example, `CustomerOrderSearchCriteria` to be secured with `AuthorizeAsync` overload is invoked to determine whether the current user is allowed to query the orders by the provided search criteria. `AuthorizeAsync` gets the following tree parameters:

+   **User**: Currently authenticated user with claims
+   **Criteria**: Object that is secured and probably changed inside the authorization handler in accordance with the user restrictions 
+ The new instance of the `OrderAuthorizationRequirement` type with the permission that needs to be checked

As a result, the authorization handler will check and change the criteria to return only the orders with the stores the current users can view.
