# Order Price Visibility

Order price visibility is decided by a dedicated service called `ICustomerOrderDataProtectionService`, not a side effect of authorization. It answers "may this user see prices on this order?" in one place: when the answer is no, price fields are zeroed on read and restored from storage on save.

The default rule checks the global **order:read_prices** permission, exposed as a single overridable method. A solution can decide by store, store type, organization, or anything else instead of an all-or-nothing permission.

## How it works

Every path that returns or persists an order goes through `ICustomerOrderDataProtectionService`: search, indexed search, get by ID, number, or outer ID, save, patch, export, and import. This makes it the single place to implement a custom price-visibility rule, rather than one of several places a resource happens to pass through authorization.

Orders carry a `WithPrices` field (`withPrices` on the wire), `false` when prices were stripped. A caller without price access receives the response group it asked for, with price fields zeroed and `withPrices: false`. Prices are hidden by masking the field values, not by rewriting the requested response group.

The Admin UI and other consumers read the `WithPrices` flag instead of re-deriving the rule from client-side permission checks, so they mask exactly what the server hid. Read the flag instead of checking **order:read_prices** in the client: the server is the single source of truth, and a custom rule works everywhere without the UI knowing about it.

## Change who may see prices

Resolve `ICustomerOrderDataProtectionService` instead of `ICustomerOrderService`, `ICustomerOrderSearchService`, or `IIndexedCustomerOrderSearchService` wherever you read or save an order on behalf of a signed-in user. It implements all three, so it is a drop-in replacement.

To change who may see prices, derive from `CustomerOrderDataProtectionService` and override one method:

```csharp title="SampleCustomerOrderDataProtectionService.cs"
protected virtual Task<bool> CanReadPrices(ClaimsPrincipal user, CustomerOrder order)
```

Register your subclass for `ICustomerOrderDataProtectionService`, and it takes over:

```csharp title="Module.cs"
serviceCollection.AddTransient<ICustomerOrderDataProtectionService, SampleCustomerOrderDataProtectionService>();
```

The method is called per order. The rule can depend on the order itself: its store, organization, or customer. A worked example using a store-type rule ships in [samples/VirtoCommerce.OrdersModule2.Web](https://github.com/VirtoCommerce/vc-module-order/tree/dev/samples/VirtoCommerce.OrdersModule2.Web).

### Related extension points

* `RemovePrices` / `RestorePrices`: override either to change which fields count as prices.
* `OrderAuthorizationHandler` lives in `...Data.Authorization` and is not sealed, so you can extend it to add your own scope rules. See [Authorization policies extension](../../extensions/extending-authorization-policies.md). Price visibility does not go through this handler; use the data protection service above for that.

## Apply the same pattern to another module

There is no single platform-wide interface for this; `ICustomerOrderDataProtectionService` is specific to the **Order** module. The Order module itself builds two more data protection services on the same idea: `IPaymentDataProtectionService` and `IShipmentDataProtectionService`. Both are built on a shared generic base: `OrderOperationDataProtectionService<TOperation, TCriteria, TResult>`. It defers to `ICustomerOrderDataProtectionService.CanReadPricesAsync` for the parent order.

This is the pattern to follow in another module:

1. Define an interface for your module that combines your entity's CRUD and search service interfaces. Follow the same pattern as `ICustomerOrderDataProtectionService`, which combines `ICustomerOrderService`, `ICustomerOrderSearchService`, and `IIndexedCustomerOrderSearchService`.
1. Implement it as a service that wraps the real CRUD/search services, masks the sensitive fields on every read path, and restores them from storage on save. This mirrors `CustomerOrderDataProtectionService`'s `ReduceDetailsForUser` / `RestoreDetailsForUser` methods.
1. Expose the visibility rule as a single overridable method, such as `CanReadPrices`. This lets other solutions replace it without touching the rest of the service.
1. Register the service for its interface in **Module.cs**. Resolve that interface everywhere the entity is read or saved on behalf of a signed-in user, instead of the raw CRUD/search services.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../scope-based-permissions">← Scope-based permissions </a>
    <a href="../restrict-admin-ui-access">Restrict admin UI access →</a>
</div>
