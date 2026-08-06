# Extend Pricing Module

The Pricing module is extended through dependency injection (DI) service overrides and domain events, not through a provider-registration mechanism. This article lists the real extension points and shows how to plug in a custom pricing engine.

!!! warning
    Unlike tax, payment, and shipping providers, the Pricing module has **no** provider-registration API. There is no `IPricingProviderRegistrar` and no `RegisterPricingProvider` method. Custom pricing logic is plugged in by overriding `IPricingEvaluatorService` in the DI container, as shown below.

## Extension points

| Extension point | Kind | Use it to |
| --- | --- | --- |
| `IPricingEvaluatorService` | Service | Replace price and price list evaluation with a custom engine. |
| `IPricingPriorityFilterPolicy` | Policy | Change which price wins when several price lists match. |
| `IPriceService`, `IPricelistService`, `IPricelistAssignmentService` | CRUD services | Wrap or override create, read, update, and delete operations for prices, price lists, and assignments. |
| `PriceChangingEvent` / `PriceChangedEvent` and the pricelist and assignment equivalents | Domain events | React to pricing changes for validation, synchronization, or audit. |
| Domain model and database extension | Extensibility framework | Add custom properties to pricing entities. |

All of these services are registered as transient by the Pricing module, so a later registration of the same interface replaces the default implementation.

## Plug in custom pricing engine

The main entry point for price calculation is `IPricingEvaluatorService`:

```csharp title="IPricingEvaluatorService.cs"
namespace VirtoCommerce.PricingModule.Core.Services;

public interface IPricingEvaluatorService
{
    // Evaluate pricelists for the context. Resulting pricelists are ordered by priority.
    Task<IList<Pricelist>> EvaluatePriceListsAsync(PriceEvaluationContext evalContext);

    // Evaluate product prices. Returns all prices, or one price per currency, depending on evalContext.
    Task<IList<Price>> EvaluateProductPricesAsync(PriceEvaluationContext evalContext);
}
```

To integrate an external pricing engine, implement this interface and map the external result to Virto Commerce `Price` objects:

```csharp
public class ExternalPricingEvaluatorService : IPricingEvaluatorService
{
    private readonly IExternalPricingClient _client;

    public ExternalPricingEvaluatorService(IExternalPricingClient client)
    {
        _client = client;
    }

    public async Task<IList<Pricelist>> EvaluatePriceListsAsync(PriceEvaluationContext evalContext)
    {
        // Return the price lists that apply to this context, ordered by priority.
    }

    public async Task<IList<Price>> EvaluateProductPricesAsync(PriceEvaluationContext evalContext)
    {
        var externalPrices = await _client.GetPricesAsync(evalContext.ProductIds, evalContext.CustomerId);

        return externalPrices
            .Select(p => new Price
            {
                ProductId = p.ProductId,
                List = p.ListPrice,
                Sale = p.SalePrice,
                Currency = p.Currency,
            })
            .ToList();
    }
}
```

Register your implementation in the `Module.cs` file of your custom module. Because the last registration wins, this replaces the default `PricingEvaluatorService`:

```csharp
public void Initialize(IServiceCollection serviceCollection)
{
    // Overrides the default IPricingEvaluatorService implementation.
    serviceCollection.AddTransient<IPricingEvaluatorService, ExternalPricingEvaluatorService>();
}
```

!!! note
    For your override to win, your module must initialize **after** the Pricing module. Add a dependency on `VirtoCommerce.Pricing` in your **module.manifest** so your module loads later in the dependency order.

## Adjust price selection

When several price lists match a request, `IPricingPriorityFilterPolicy` decides which prices are kept. Override it to change that rule:

```csharp
public class CustomPricingPriorityFilterPolicy : IPricingPriorityFilterPolicy
{
    public IEnumerable<Price> FilterPrices(IEnumerable<Price> prices, PriceEvaluationContext evalContext)
    {
        // Choose which prices win when multiple price lists apply to the same product.
    }
}
```

Register it the same way, replacing the default `DefaultPricingPriorityFilterPolicy`:

```csharp
serviceCollection.AddTransient<IPricingPriorityFilterPolicy, CustomPricingPriorityFilterPolicy>();
```

## React to price and price list changes

The Pricing module raises domain events before and after prices, price lists, and assignments are saved. Each event inherits `GenericChangedEntryEvent<T>` and carries the changed entries with their old and new state.

| Event | Raised |
| --- | --- |
| `PriceChangingEvent` / `PriceChangedEvent` | Before and after prices are saved. |
| `PricelistChangingEvent` / `PricelistChangedEvent` | Before and after price lists are saved. |
| `PricelistAssignmentChangingEvent` / `PricelistAssignmentChangedEvent` | Before and after pricelist assignments are saved. |

Handle an event by implementing `IEventHandler<T>`:

```csharp
public class PriceChangedEventHandler : IEventHandler<PriceChangedEvent>
{
    public Task Handle(PriceChangedEvent message)
    {
        foreach (var entry in message.ChangedEntries)
        {
            // entry.EntryState, entry.OldEntry, and entry.NewEntry describe the change.
        }

        return Task.CompletedTask;
    }
}
```

Register the handler in your `Module.cs` file:

```csharp
public void Initialize(IServiceCollection serviceCollection)
{
    serviceCollection.AddTransient<PriceChangedEventHandler>();
}

public void PostInitialize(IApplicationBuilder appBuilder)
{
    appBuilder.RegisterEventHandler<PriceChangedEvent, PriceChangedEventHandler>();
}
```

![Readmore](media/readmore.png){: width="25"} [Using domain events](/platform/developer-guide/latest/Fundamentals/Event-Driven-Development/using-domain-events)

## Extend pricing data model

To store extra data on pricing entities, use the standard extensibility framework rather than a pricing-specific mechanism.

![Readmore](media/readmore.png){: width="25"} [Extending domain models](/platform/developer-guide/latest/Tutorials-and-How-tos/Tutorials/extending-domain-models)

![Readmore](media/readmore.png){: width="25"} [Extending the database model](/platform/developer-guide/latest/Tutorials-and-How-tos/Tutorials/extending-database-model)

![Readmore](media/readmore.png){: width="25"} [Pricing module source code](https://github.com/VirtoCommerce/vc-module-pricing)


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../overriding-rounding-policy">← Overriding rounding policy </a>
    <a href="../feature-flags">Using feature flags →</a>
</div>