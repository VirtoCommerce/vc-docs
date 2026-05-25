# Override Rounding Policy

To customize the rounding behavior in your application: 

1. Implement the interface `VirtoCommerce.CoreModule.Core.Currency.IMoneyRoundingPolicy`:
  
    ```csharp
    public class CustomMoneyRoundingPolicy : IMoneyRoundingPolicy
    {
        public decimal RoundMoney(decimal amount, Currency currency)
        {
            // Insert your rounding logic here
        }
    }
    ```

1. Register the custom rounding policy with the Dependency Injection (DI) container in the `Module.cs` file:

    ```csharp
    public void Initialize(IServiceCollection serviceCollection)
    {
        // Other initialization code...

        // Money rounding
        serviceCollection.AddTransient<IMoneyRoundingPolicy, CustomMoneyRoundingPolicy>();
    }
    ```

1. Ensure to replace the placeholder with your actual rounding logic in the `RoundMoney` method.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../upgrading-to-net8">← Upgrading to .NET 8 </a>
    <a href="../feature-flags">Using feature flags  →</a>
</div>