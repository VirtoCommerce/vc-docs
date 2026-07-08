# Product Snapshot Module Architecture and Extensibility

The **Product Snapshot** module captures and stores product information at the moment an order is created. This ensures that customers and store operators always have access to the exact product details (prices, properties, images, descriptions) that were valid at the time of purchase, even if the product catalog is later modified or products are deleted.

A category manager updates or removes a product from the catalog, but existing orders still display the original product information through snapshots. If a snapshot does not exist for a given product, the system falls back to loading the current product data from the catalog.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-product-snapshot)

[![Download](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-product-snapshot/releases)

<br>
![Read more](media/readmore.png){: width="20"} [Using Product Snapshot](/platform/user-guide/latest/product-snapshot/overview)

## Key features

- **Automatic snapshot creation**: Listens for the `OrderChangedEvent` and asynchronously creates product snapshots when a new order is placed.
- **Full product data capture**: Stores product info, assets, properties, and editorial reviews as a serialized JSON document.
- **Configurability**: Snapshot creation can be enabled or disabled through a platform setting.
- **Catalog fallback**: Products not covered by a snapshot are loaded by xOrder's `OrderProductResolver.LoadProductsAsync` from the live catalog. The fallback is provided by xOrder, not by this module.
- **Granular permissions**: Access, create, read, update, and delete operations are controlled by dedicated permissions.
- **Extendable product snapshot page**: The module provides extension points (productSnapshotDetails metaform and widget-container) on the Product Snapshot details page to display custom information related to the snapshot, such as links to related orders or custom product attributes.
- **REST API**: Retrieve a product snapshot via `GET /api/product-snapshots/order/{orderId}/product/{productId}`.
- **GraphQL / Experience API integration**: The `LoadorderProductSnapshotMiddleware` transparently injects snapshots into the `ExternalOrderProducts` pipeline, so X-Order consumers receive snapshot data without additional queries.
- **Multi-database support**: SQL Server, MySQL, and PostgreSQL are supported out of the box.
- **Async snapshot creation (coming soon)**: Snapshot generation runs in the background to avoid impacting order processing performance. If snapshot creation fails, it is logged but does not block the order from being created.

## Architecture

Snapshots are written on both `Added` and `Modified` order change entries, so line items added to an existing order after creation are still captured. The handler ignores `Deleted` and `Unchanged` entries. A unique `(OrderId, ProductId)` constraint combined with the idempotent skip in the provider guarantees exactly one snapshot per product per order. Resaving an unchanged order is a no-op.

REST API calls go straight through `ICatalogProductSnapshotProvider`. GraphQL and xAPI calls are routed through xOrder's `IOrderProductResolver`, which launches the `ExternalOrderProducts` pipeline. `LoadorderProductSnapshotMiddleware` fills in frozen snapshots. Anything still missing falls through to xOrder's catalog fallback.

## Configuration

The module exposes a single setting in **appsettings.json**:

{%
   include-markdown "../../Configuration-Reference/appsettingsjson.md"
   start="<!--product-snapshot-start-->"
   end="<!--product-snapshot-end-->"
%}

## Default mode versus snapshot mode

When the Product Snapshot module is installed and enabled, order line items resolve product data through the snapshot pipeline instead of the live catalog. The two modes behave differently in ways that affect GraphQL queries and customizations.

### Quick comparison

| Aspect | Default mode | Snapshot mode |
|---|---|---|
| Data source | Live catalog (search index and domain services). | Frozen `CatalogProduct` stored at order creation. |
| Pipeline | `ExternalOrderProducts` is empty. Fallback is `OrderProductResolver.LoadProductsAsync`. | `LoadorderProductSnapshotMiddleware` is added to `ExternalOrderProducts`. Fallback runs only for line items without a snapshot. |
| Honors GraphQL `IncludeFields` | Yes. Dynamic, from `context.SubFields`. | No. Response group is fixed at capture time. |
| Consistency after catalog changes | Reflects current state. | Reflects order-time state. |
| Extra storage | None. | One row per line item. |

### What snapshot mode populates

Frozen by the snapshot:

* `Id`, `Name`, `Code`.
* `Properties` values, display names, and dictionary items.
* `Images` and `Assets`. URLs are frozen, so later CDN-path changes are not picked up.
* `Reviews` and editorial descriptions.

Not populated by the snapshot path. These need the catalog fallback or a middleware extension:

* `AllPrices`, `MinVariationPrice`.
* `Inventory`, `AllInventories`, `AvailableQuantity`.
* `Vendor`, `Rating`, `ReviewSummary`.
* `Variations`, `Associations`, `ReferencedAssociations`.
* `Outlines`, `Category`, `SeoInfos`.
* `IsInStock`, `IsAvailable`, `IsBuyable`. Computed against empty data, so usually `false`.
* `RelevanceScore`, `IsPurchased`, `InWishlist`, `WishlistIds`, indexed-variation bindings.

### GraphQL query examples

| Query fragment | Default mode | Snapshot mode |
|---|---|---|
| `product { name images { url } properties { name value } }` | Works. | Works. |
| `product { prices { list { amount } } }` | Works. | Empty. |
| `product { availabilityData { availableQuantity } }` | Works. | Zero. |
| `product { variations { id } }` | Works. | Empty. |
| `product { vendor { id name } }` | Works. | Null. |

### Choosing a mode

Use default mode when:

* You need current pricing, inventory, vendor, variations, or associations on the order page.
* Drift from catalog edits is acceptable.
* Historical fidelity is not required.

Use snapshot mode when:

* Audit or compliance requires point-in-time product data.
* Completed orders should not change when the catalog changes.
* You can tolerate empty dynamic fields, or you are willing to extend the middleware to compose snapshot data with live data.

### Trade-offs

Default mode gives a fully populated `ExpProduct` and honors GraphQL field selection dynamically, at the cost of catalog drift and heavier per-request work. A product deletion renders the order line as `null`.

Snapshot mode delivers stable, reproducible order pages and survives product deletion, at the cost of empty dynamic fields and ignored `IncludeFields` on the snapshot path. Legacy orders placed before the module was installed fall back to the live catalog, which reintroduces drift.

## Extensibility

The Product Snapshot module exposes extension points at two layers: the backend pipeline that produces the snapshot data, and the Platform Manager UI that displays it.

### Backend extension points

Three extension points are available when you need additional fields on the snapshot path:

* **Widen the captured response group.** Override `VirtoCatalogSnapshotProvider.ProductSnapshotResponseGroup` to include flags like `ItemAssociations`, `Variations`, or `Seo`. Only new orders pick up the wider snapshot.
* **Compose middleware.** Register additional middleware on the `ExternalOrderProducts` pipeline after `LoadorderProductSnapshotMiddleware` to hydrate dynamic fields (for example, live prices or inventory) on top of the frozen catalog data.
* **Override `OrderProductResolver`.** For call sites where live data must always win, subclass `OrderProductResolver` and route to the catalog fallback even when a snapshot exists.

### UI extension points (Platform Manager)

The Product Snapshot details blade exposes the `productSnapshotDetails` [metaform](../../Platform-Manager/Extensibility-Points/metaform.md) and a [widget container](../../Platform-Manager/Extensibility-Points/widgets.md), so other modules can add custom properties and widgets without modifying this module.

The code below uses AngularJS. It applies to the current Platform Manager admin SPA, not VC-Shell.

#### Adding custom properties via metaform

Register additional fields in your module's `module.js` `run` block:

```js
angular.module('YourModule')
    .run(['platformWebApp.metaFormsService', function (metaFormsService) {
        metaFormsService.registerMetaFields("productSnapshotDetails", [
            {
                name: "customWarrantyInfo",
                title: "Warranty Information",
                valueType: "ShortText"
            },
            {
                name: "isOversized",
                title: "Oversized Item",
                valueType: "Boolean"
            }
        ]);
    }]);
```

Registered fields appear at the bottom of the Product Snapshot details blade inside the `<va-metaform>` block. The field data is bound to the blade's `currentEntity` scope.

#### Adding widgets

Register widgets into the `productSnapshotDetails` widget container the same way:

```js
angular.module('YourModule')
    .run(['platformWebApp.widgetService', function (widgetService) {
        var widget = {
            controller: 'YourModule.YourWidgetController',
            template: 'Modules/$(YourModule)/Scripts/widgets/your-widget.html'
        };
        widgetService.registerWidget(widget, 'productSnapshotDetails');
    }]);
```



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../configuring-multiple-stores-on-virto-cloud">← Configuring multiple stores on Virto CLoud</a>
    <a href="../extending-cart-query-with-custom-parameter">Extending Cart query with custom parameter →</a>
</div>