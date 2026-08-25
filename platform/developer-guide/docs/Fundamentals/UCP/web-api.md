# UCP Web API

The module exposes the following canonical UCP endpoints. Each operation is also advertised in the discovery profile.

## Discovery

The discovery endpoint returns the UCP profile:

```http
GET /.well-known/ucp
```

The profile includes supported capabilities, default store metadata, endpoint metadata, headers, auth shape, integration guidance, payment handlers, and structured error codes. UCP operations are advertised as HTTP endpoints in `endpoints.operations`.

## Catalog search

The catalog search endpoint returns products for a store:

```http
POST /ucp/v1/catalog/search
```

Example request:

```json
{
  "query": "iphone",
  "context": {
    "store_id": "store-acme",
    "currency": "USD",
    "language": "en-US"
  },
  "filters": {
    "price": {
      "min": 50000,
      "max": 100000
    }
  },
  "pagination": {
    "limit": 10
  }
}
```

UCP prices and price filters use minor units. For example, `$700.00` is represented as `70000`.

## Product detail

The product detail endpoint returns a single product:

```http
GET /ucp/v1/catalog/products/{id}?store_id=store-acme&currency=USD&culture_name=en-US
```

The product response includes id, code, name, slug, image URL, brand, product type, price, list price, availability, attributes, and variations. If a product is not found, the endpoint returns the structured error `product_not_found`.

## Cart assembly

The cart assembly endpoints create and manage buyer carts:

```http
POST /ucp/v1/carts
GET /ucp/v1/carts?store_id=store-acme&currency=USD&culture_name=en-US&buyer_id=user-42
GET /ucp/v1/carts/{cartId}?store_id=store-acme&currency=USD&culture_name=en-US
PUT /ucp/v1/carts/{cartId}
```

`create_cart` creates a cart through the xCart `addItem` mutation, then applies coupons through `addCoupon`.

`list_carts` is a Virto extension over the xCart `carts` query. It requires buyer context through `X-Buyer-User-Id` or `context.buyer_id` / `buyer_id` and does not return a global anonymous cart list.

`update_cart` follows UCP replacement semantics. The request describes the desired final cart state, and the adapter computes the required xCart mutations:

- `addItem`
- `changeCartItemQuantity`
- `removeCartItem`
- `addCoupon`
- `removeCoupon`

To remove a line item, omit it from `line_items` or pass an existing `line_items[].id` with `quantity: 0`.

## Geography

The geography endpoints resolve countries and regions:

```http
GET /ucp/v1/geography/countries?query=United%20States&limit=10
GET /ucp/v1/geography/countries/resolve?query=KZ
GET /ucp/v1/geography/countries/{countryId}/regions
```

Geography endpoints are thin adapters over the platform `ICountriesService`:

- `list_countries` returns platform countries and supports simple search by `id` or `name`.
- `resolve_country` accepts ISO2, ISO3, or platform country name and returns the platform country id, for example `KZ -> KAZ`.
- `list_regions` returns platform regions or provinces for a resolved country id.
- `city` is not resolved through a dictionary and remains a free-text checkout address field.

MCP clients should use these endpoints before checkout when country or region data comes from natural language input. This avoids guessing and preserves the existing Frontend and xCart address contracts.

## Checkout handoff

The checkout handoff endpoints prepare a checkout and hand off to the hosted Frontend:

```http
POST /ucp/v1/checkouts
PATCH /ucp/v1/checkouts/{checkoutId}
GET /ucp/v1/checkouts/{checkoutId}/payment-handlers
POST /ucp/v1/checkouts/{checkoutId}/handoff
POST /ucp/v1/internal/handoff/restore
```

The current checkout flow is hosted-only:

- `create_checkout` creates a checkout snapshot from the cart.
- If the request contains `shipping_address` or `billing_address`, the module applies them to xCart before creating the snapshot.
- `update_checkout` updates address hints before payment and applies addresses to xCart.
- `checkout_and_handoff` creates the checkout snapshot and immediately returns the hosted checkout `continue_url`. MCP clients should prefer it when the buyer is ready to pay or continue to Frontend checkout.
- `handoff_checkout` returns a `continue_url` with an opaque `ucp_session`.
- `storefront_restore` validates `ucp_session` and reads the session payload from distributed cache. It checks expiration and returns cart and checkout context to the Frontend.
- Shipping method and payment details are completed in Frontend checkout.

`ucp_session` is an opaque random session token. The checkout context, cart context, address snapshot, payment hint, and expiration timestamp are stored server-side through `IDistributedCache` with absolute expiration based on `UCP:HandoffTokenTtlMinutes`. The module registers `AddDistributedMemoryCache()` as a fallback, so handoff works without Redis in local or single-node deployments. In production multi-node deployments, the platform distributed cache should be Redis-backed so handoff restore works across nodes and sessions survive process restarts.

`shipping_address` and `billing_address` are applied to the cart through the xCart `addOrUpdateCartAddress` mutation and are also stored in the temporary handoff session payload. Before writing an address, UCP normalizes `country_code` through the platform `ICountriesService`. If the selected country has regions, `region` and `region_id` are normalized through `GetCountryRegionsAsync`.

If `shipping_address` or `billing_address` is passed to UCP, `first_name` and `last_name` are required. The module returns `invalid_request` when the recipient name is missing. For best hosted checkout UX, also pass `postal_code`, `email`, and `phone` when available.

`notes` are not treated as a delivery address. If the request contains an address only in `notes`, the response includes the warning `shipping_address_not_notes`. The next `update_checkout` or `handoff_checkout` call should include a structured `shipping_address`.

Example handoff request:

```json
{
  "cart_id": "cart-1",
  "context": {
    "store_id": "store-acme",
    "currency": "USD",
    "language": "en-US",
    "buyer_id": "ucp-anonymous-123"
  },
  "buyer": {
    "email": "buyer@example.com"
  },
  "shipping_address": {
    "first_name": "Ada",
    "last_name": "Buyer",
    "line1": "1 Main St",
    "city": "Seattle",
    "region_id": "WA",
    "region": "Washington",
    "postal_code": "98101",
    "country_code": "US",
    "country_name": "United States",
    "phone": "555-0100",
    "email": "buyer@example.com"
  },
  "billing_address": {
    "first_name": "Ada",
    "last_name": "Buyer",
    "line1": "1 Main St",
    "city": "Seattle",
    "region_id": "WA",
    "region": "Washington",
    "postal_code": "98101",
    "country_code": "US",
    "country_name": "United States",
    "phone": "555-0100",
    "email": "buyer@example.com"
  },
  "payment_handler": "hosted_checkout"
}
```

## Order tracking

The order tracking endpoints return order status after handoff:

```http
GET /ucp/v1/orders/{orderId}?buyer_id=user-42&culture_name=en-US
GET /ucp/v1/orders?cart_id={cartId}&buyer_id=user-42&culture_name=en-US
```

`track_order` returns order status, order number, totals, line items, shipment snapshot, payment snapshot, and shipment tracking fields when they are available in order data.

After hosted handoff, the client usually does not know `order_id` yet. The primary path is lookup by the original `cart_id`, matched against `CustomerOrder.ShoppingCartId` through Orders module services. If buyer context changed during guest checkout, the endpoint retries without buyer filters and still matches strictly by `cart_id`. If the order has not been created yet or is not found among recent orders, the endpoint returns the structured error `order_not_found`.

## Error model

The module returns the following known UCP error codes:

- `invalid_request`
- `missing_store_id`
- `product_not_found`
- `cart_not_found`
- `order_not_found`
- `xapi_execution_failed`

Responses include a correlation id when available. The module reads `X-Correlation-Id` and falls back to the ASP.NET Core trace identifier. This is the same id used to locate the request's [OpenTelemetry trace](configuration.md#observability).


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../configuration">← Configuration</a>
    <a href="../mcp-server">MCP server →</a>
</div>
