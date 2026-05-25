
# Scope-based Authorization

Scope-based permissions, also known as imperative or resource-based permissions, depend on the resource being accessed. Consider an order that includes a store property. You may want users to view only the orders belonging to a specific store. Consequently, authorization evaluation must occur after retrieving the order from the data store.

The `[Authorize]` attribute evaluates permission checks before data binding and executing the API action that loads the order. Due to this, declarative authorization with an `[Authorize]` attribute alone may not suffice. Instead, you can utilize a custom authorization method, known as imperative authorization.

## Define new permission scope

Let's explore how resource-based authorization works through the following example:

Suppose we want to restrict user access to orders created in a specific store. To enable this authorization check in the code and assign this permission for end-user roles, follow these steps:

1. Create a new class named `OrderSelectedStoreScope`, derived from `PermissionScope`. This class will hold the store identifier selected by the user in the role management UI.

    ```csharp title="VirtoCommerce.OrdersModule.Web/Authorization/OrderSelectedStoreScope.cs"
    public sealed class OrderSelectedStoreScope : PermissionScope
    {
        public string StoreId => Scope;
    }
    ```

1. To register the scope and make the global permission scope-based, add the following code to your **Module.cs** file:

    ```csharp title="VirtoCommerce.OrdersModule.Web/Scripts/module.cs"
    public void PostInitialize(IApplicationBuilder appBuilder)
    {
        // Other configurations...

        var permissionsProvider = appBuilder.ApplicationServices.GetRequiredService<IPermissionsRegistrar>();
        permissionsProvider.WithAvailabeScopesForPermissions(new[] {
                                                                        "order:read",
                                                                    }, new OrderSelectedStoreScope());

        // Other configurations...
    }
    ```

1. Register the presentation template for `OrderSelectedStoreScope` to allow users to configure permission scope settings in the role manager:

    ```js title="VirtoCommerce.OrdersModule.Web/Scripts/order.js"
    angular.module(moduleName, []).run( ['platformWebApp.permissionScopeResolver', 'platformWebApp.bladeNavigationService', function(scopeResolver, bladeNavigationService) {
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

After these steps, the global `order:read` permission can be further restricted to work only for selected stores in role assignments.


### Write scope-based authorization handler

Writing a handler for a scope-based authorization is not much different from writing a plain requirement handler. You need to create a custom requirement class and implement a requirement handler class derived from `PermissionAuthorizationHandlerBase`:

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

### Check scope-based permissions

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

* **User**: Currently authenticated user with claims.
* **Criteria**: Object that is secured and probably changed inside the authorization handler in accordance with the user restrictions. 
* The new instance of the `OrderAuthorizationRequirement` type with the permission that needs to be checked.

As a result, the authorization handler will check and change the criteria to return only the orders with the stores the current users can view.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../authorization/global-permissions">← Global permissions </a>
    <a href="../../encryption-and-signing-credentials ">Encryption and signing credentials →</a>
</div>

