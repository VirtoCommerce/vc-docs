Virto Commerce supports extendng the existing authorization policies that are defined and checked in the API controllers and other locations. This article will tell you how to use various techniques to extend the authorization policy type without direct code modification.

Click [here](https://github.com/VirtoCommerce/vc-module-order/tree/dev/samples/VirtoCommerce.OrdersModule2.Web/Authorization) to view or download our sample code.

## Extending Existing Authorization Policies

Let's assume we have the below authorization checks in the *Order Module*. Additionally, we want to extend the default `OrderAuthorizationHandler` that is associated with the `OrderAuthorizationRequirement` requirement called during the authorization check with a new policy limiting the resulting orders by their statuses. The purpose is to create a role that enables specific users to see orders only with specific status(es).

You can read more about how authorization policies work [here](https://docs.microsoft.com/en-us/aspnet/core/security/authorization/policies?view=aspnetcore-5.0).

`OrderModuleController.cs`
```C#
[HttpPost]
[Route("api/order/customerOrders/search")]
 public async Task<ActionResult<CustomerOrderSearchResult>> SearchCustomerOrder([FromBody] CustomerOrderSearchCriteria criteria)
        {
            var authorizationResult = await _authorizationService.AuthorizeAsync(User, criteria, new OrderAuthorizationRequirement(ModuleConstants.Security.Permissions.Read));
            if (!authorizationResult.Succeeded)
            {
                return Unauthorized();
            }
        }

```

In order to enable this extension, you need to define a new `CustomOrderAuthorizationHandler` class and use the same `OrderAuthorizationRequirement` requirement, as it is used in the original controller method for authorization check.

`CustomOrderAuthorizationHandler.cs`
```C#
 public sealed class CustomOrderAuthorizationHandler : PermissionAuthorizationHandlerBase<OrderAuthorizationRequirement>
    {
        //Code skipped for better clarity
    }
```

The next step is registering your handler in the DI to tell ASP.NET Authorization to call your handler along with others associated with the `OrderAuthorizationRequirement` requirement:

`Module.cs`
```C#
 public class Module : IModule
    {
        public void Initialize(IServiceCollection serviceCollection)
        {
            //Rest of code skipped for better clarity 
            serviceCollection.AddTransient<IAuthorizationHandler, CustomOrderAuthorizationHandler>();
        
        }
    }
```

After this point, the custom `CustomOrderAuthorizationHandler` along with other registered handlers will be executed each time when `OrderAuthorizationRequirement` is checked by this call:  

```C#
IAuthorizationService.AuthorizeAsync(User, data, new OrderAuthorizationRequirement());
```

## Additional Resources

You can also check out how to handle secure Web API [here](https://github.com/VirtoCommerce/vc-platform/blob/master/docs/fundamentals/make-secure-webapi.md).