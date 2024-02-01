# Extending Authorization Policies

Virto Commerce supports extendng the existing authorization policies that are defined and checked in the API controllers and other locations. This article will tell you how to use various techniques to extend the authorization policy type without direct code modification.

Click [here](https://github.com/VirtoCommerce/vc-module-order/tree/dev/samples/VirtoCommerce.OrdersModule2.Web/Authorization) to view or download our sample code.

## Extending Existing Authorization Policies

Let's assume below are authorization checks in the **Order Module**. Additionally, we want to extend the default `OrderAuthorizationHandler` that is associated with the `OrderAuthorizationRequirement` requirement called during the authorization check with a new policy limiting the resulting orders by their statuses. The purpose is to create a role that enables certain users to see orders only with certain status(es).

![Readmore](../media/readmore.png){: width="25"} [Authorization policies](https://docs.microsoft.com/en-us/aspnet/core/security/authorization/policies?view=aspnetcore-5.0).

```cs title="OrderModuleController.cs"
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

To enable this extension, define a new `CustomOrderAuthorizationHandler` class and use the same `OrderAuthorizationRequirement` requirement, as it is used in the original controller method for authorization check:

```cs title="CustomOrderAuthorizationHandler.cs"
 public sealed class CustomOrderAuthorizationHandler : PermissionAuthorizationHandlerBase<OrderAuthorizationRequirement>
    {
        //Code skipped for better clarity
    }
```

Register your handler in the DI to tell ASP.NET Authorization to call your handler along with others associated with the `OrderAuthorizationRequirement` requirement:

```cs title="Module.cs"
 public class Module : IModule
    {
        public void Initialize(IServiceCollection serviceCollection)
        {
            //Rest of code skipped for better clarity 
            serviceCollection.AddTransient<IAuthorizationHandler, CustomOrderAuthorizationHandler>();
        
        }
    }
```

The custom `CustomOrderAuthorizationHandler` along with other registered handlers will be executed each time when `OrderAuthorizationRequirement` is checked by this call:  

```cs
IAuthorizationService.AuthorizeAsync(User, data, new OrderAuthorizationRequirement());
```

![Readmore](../media/readmore.png){: width="25"} [Handling secure Web API](https://github.com/VirtoCommerce/vc-platform/blob/master/docs/fundamentals/make-secure-webapi.md).