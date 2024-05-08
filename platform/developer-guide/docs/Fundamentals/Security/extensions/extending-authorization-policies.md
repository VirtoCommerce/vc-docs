# Authorization Policies Extension

Virto Commerce supports extendng the existing authorization policies that are defined and checked in the API controllers and other locations. This article will tell you how to use various techniques to extend the authorization policy type without direct code modification.

[![Sample code](../media/sample-code.png)](https://github.com/VirtoCommerce/vc-module-order/tree/dev/samples/VirtoCommerce.OrdersModule2.Web/Authorization)

## Extend Existing Authorization Policies

Suppose you have authorization checks in the **Order Module**, and you want to enhance the default `OrderAuthorizationHandler` associated with the `OrderAuthorizationRequirement`. This extension aims to introduce a new policy that restricts orders based on their statuses, allowing certain users to view orders only with specific status(es).

![Readmore](../media/readmore.png){: width="25"} [Authorization Policies](https://docs.microsoft.com/en-us/aspnet/core/security/authorization/policies?view=aspnetcore-5.0)

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

To implement this extension:

1. Define a new authorization handler. Create a new class named `CustomOrderAuthorizationHandler` and utilize the existing `OrderAuthorizationRequirement` requirement for authorization checks:

    ```cs title="CustomOrderAuthorizationHandler.cs"
    public sealed class CustomOrderAuthorizationHandler : PermissionAuthorizationHandlerBase<OrderAuthorizationRequirement>
    {
        // Implementation details omitted for clarity
    }
    ```

1. Register the custom authorization handler in the Dependency Injection (DI) container to instruct ASP.NET Authorization to invoke it along with other handlers associated with the `OrderAuthorizationRequirement` requirement:

    ```cs title="Module.cs"
    public class Module : IModule
    {
        public void Initialize(IServiceCollection serviceCollection)
        {
            // Other code omitted for clarity 
            serviceCollection.AddTransient<IAuthorizationHandler, CustomOrderAuthorizationHandler>();
        }
    }
    ```

1. Execute authorization checks. The custom `CustomOrderAuthorizationHandler`, along with other registered handlers, will execute each time an `OrderAuthorizationRequirement` is checked, as demonstrated in the following code snippet:

    ```cs
    IAuthorizationService.AuthorizeAsync(User, data, new OrderAuthorizationRequirement());
    ```

Following these steps enables you to extend the existing authorization policies within the **Order Module**, allowing for more fine-grained control over order access based on their statuses.

![Readmore](../media/readmore.png){: width="25"} [Handling Secure Web API](https://github.com/VirtoCommerce/vc-platform/blob/master/docs/fundamentals/make-secure-webapi.md)