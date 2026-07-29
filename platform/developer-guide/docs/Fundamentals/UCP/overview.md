# Virto Commerce UCP Module (Preview)

The Virto Commerce **UCP** module exposes HTTP APIs for Universal Commerce Protocol (UCP) on top of existing Virto Commerce Platform capabilities.

It provides public UCP endpoints for discovery, catalog, cart, checkout handoff, geography, and order tracking operations. Requests are adapted to in-process Virto Commerce xAPI calls and platform services without an additional HTTP hop inside the platform process. The module also exposes a Streamable HTTP MCP endpoint at `/ucp/mcp`.

Canonical public UCP endpoints are published without the `/api` prefix.

The UCP module is a protocol adapter. It does not replace the **Catalog**, **Cart**, **Orders**, **xAPI**, **Store**, or **Marketing** modules. It provides a compact UCP-oriented HTTP surface for external clients while delegating commerce behavior to existing Virto Commerce modules.

## Key features

The module provides the following capabilities:

* **UCP discovery profile**: `/.well-known/ucp` publishes supported capabilities, default store metadata, endpoint metadata, headers, auth shape, integration guidance, payment handlers, and structured error codes.
* **Catalog search and product details**: catalog search and product detail lookup through in-process **xCatalog** GraphQL.
* **Cart assembly**: create, buyer-scoped list, get, and full-state update through **xCart** GraphQL with UCP replacement semantics.
* **Checkout handoff**: checkout snapshot and hosted handoff with address prefill. Temporary handoff sessions are stored through `IDistributedCache` with TTL. Redis is recommended for production. An in-memory fallback is registered for local and single-node deployments.
* **Order tracking**: order status, totals, line items, and shipment tracking by order id, order number, or cart id after handoff.
* **Geography lookup**: country and region resolution through the platform `ICountriesService` for checkout address normalization.
* **Streamable HTTP MCP server**: `/ucp/mcp` with typed UCP commerce tools for the installed Frontend, built on the official C# MCP SDK.
* **Buyer context propagation**: header-based B2B buyer delegation through `X-Buyer-User-Id` and `X-Buyer-Organization-Id`.
* **Structured UCP errors**: machine-readable error codes with correlation id support.

!!! note
    New UCP features are coming soon: delivery and payment method selection, carrier-level shipment tracking, faceted catalog filters, and OAuth2 or OIDC buyer delegation. See the [Roadmap](#roadmap) for details.

## Quickstart. Connect Virto Start Cloud to Claude Desktop

This is the complete partner-facing setup for an existing Virto Start environment deployed in Virto Cloud. The Frontend host exposes the UCP endpoints. Virto Cloud routes the requests to the Platform application where this module runs.

Before starting, identify the exact Virto Commerce Store ID and the public Frontend host. The examples below use `B2B-store` and `store.example.com`.

To connect Virto Start Cloud to Claude Desktop:

1. [Install the module.](#install-module)
1. [Update the Virto Cloud environment.](#update-virto-cloud-environment)
1. [Verify the endpoint.](#verify-endpoint)
1. [Add the connector to Claude Desktop.](#add-connector-to-claude-desktop)
1. [Run the first smoke test.](#run-first-smoke-test)

### Install module

Install the UCP module in the Virto Start **Platform application**. The required module dependencies are listed in [Dependencies](#dependencies).

### Update Virto Cloud environment

In the Virto Cloud deployment repository, open **infra/environments.yml** and update the target environment. Add the UCP settings under `platform.config`. Then route `/ucp` and `/.well-known/ucp` from the Frontend host to `platform`:

```yaml title="environments.yml"
platform:
  config:
    UCP__DefaultStoreId: B2B-store
    UCP__DefaultCurrency: USD
    UCP__DefaultCultureName: en-US
    UCP__StorefrontOrigin: "https://store.example.com"
    UCP__UcpBaseUrl: "https://store.example.com/ucp/v1"
    UCP__HandoffUrlTemplate: "https://store.example.com/checkout?ucp_session={token}"
    UCP__HandoffTokenTtlMinutes: 15

routes:
  - host: store.example.com
    root: B2B-store
    paths:
      - path: /ucp
        route: platform
      - path: /.well-known/ucp
        route: platform
```

Replace `B2B-store` with the exact Store ID and `store.example.com` with the Virto Start Frontend host. Do not use the store display name as `UCP__DefaultStoreId`.

The `/ucp` route covers `/ucp/mcp` and all `/ucp/v1/*` endpoints. `/.well-known/ucp` needs its own route because it is outside the `/ucp` prefix.

Deploy the updated Virto Cloud environment. This restarts the Platform with the UCP configuration and applies the public routes.

### Verify endpoint

Open the Frontend discovery URL in a browser:

```text
https://store.example.com/.well-known/ucp
```

Before connecting Claude, verify that the response contains the following:

- The expected `default_store_id`.
- The expected store currency, language, and Frontend URL.
- The `mcp_tools` list with tools such as `get_store_capabilities` and `search_products`.
- The `endpoints.ucp_base_url` value equal to `https://store.example.com/ucp/v1`.

The remote MCP URL is:

```text
https://store.example.com/ucp/mcp
```

The Frontend host must be publicly reachable from Anthropic's cloud. A host restricted to a VPN or private network cannot be used as a Claude remote connector unless the network allows Anthropic's published IP ranges.

### Add connector to Claude Desktop

Remote MCP servers are configured as Claude custom connectors. Do not put this remote URL in **claude_desktop_config.json**. That file is for locally launched MCP servers.

For an individual Claude plan:

1. Open Claude Desktop and open **Customize --> Connectors**.
1. Select **+ --> Add custom connector**.
1. Set the name to `Virto Commerce UCP`.
1. Set the remote MCP server URL to `https://store.example.com/ucp/mcp`.
1. Select **Add**.
1. In a new conversation, select **+ --> Connectors** and enable the **Virto Commerce UCP** connector.

For a Team or Enterprise plan, an Owner must first add the URL under **Organization settings --> Connectors**. Each user can then connect to it and enable it for a conversation.

See Anthropic's [remote MCP custom connector guide](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) for the current Claude UI and network requirements.

### Run first smoke test

Start a new Claude conversation with the connector enabled and send the following prompt:

**Use the Virto Commerce UCP connector. First call get_store_capabilities. Then search for products matching "printer". Use the default store, currency,
and language published by the server. Ask me to select a store only if the server publishes multiple stores and no default_store_id.**

Claude should call `get_store_capabilities` and then `search_products` without asking for values already published by the server.

### Troubleshooting

The table below lists common issues and what to check.

| Symptom | Check |
| --- | --- |
| Claude cannot connect. | Confirm that the Cloud environment routes `/ucp` to `platform`, the Frontend host is public, and the updated environment was deployed. |
| `missing_store_id` | Confirm that `platform.config.UCP__DefaultStoreId` contains the exact Store ID and the updated environment was deployed. |
| Search returns no products. | Confirm that the store is open, the catalog is assigned to the store, prices and inventory exist, and the search index has been built. |
| Checkout opens the wrong host. | Configure `Store.SecureUrl` or `Store.Url`, or set `UCP__StorefrontOrigin` and `UCP__HandoffUrlTemplate`. |
| A Team or Enterprise user cannot add the connector. | Ask an organization Owner to add the custom connector first. |

## Configuration

Configuration is read from the `UCP` section of the **appsettings.json** file:

{% include-markdown "../../Configuration-Reference/appsettingsjson.md" start="<!--ucp-start-->" end="<!--ucp-end-->" %}

If `DefaultStoreId` is not configured, discovery reads open stores from the Store module. If one store is found, `/.well-known/ucp` returns it as `default_store_id`, `store`, and the only `stores[]` item. If multiple stores are found, discovery returns them in `stores[]` and the client must choose a store explicitly.

Checkout handoff URLs are built from the Virto Commerce Store URL (`Store.Url` or `Store.SecureUrl`) for the selected default store. `UCP:StorefrontOrigin` is a fallback for environments without Store URLs. `UCP:HandoffUrlTemplate` is an explicit override.

### Application settings

The module registers the following platform setting.

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `UCP.Enabled` | Boolean | `false` | Enables UCP module functionality. Registered in the platform settings under **UCP > General**. Not yet enforced by the current preview endpoints. |

### Permissions

The module registers the following permissions in the **UCP** group.

| Permission | Description |
| --- | --- |
| `ucp:access` | Access UCP module resources. |
| `ucp:create` | Create UCP data. |
| `ucp:read` | View UCP data. |
| `ucp:update` | Update UCP data. |
| `ucp:delete` | Delete UCP data. |

Public UCP protocol endpoints (`/.well-known/ucp`, `/ucp/v1/*`, `/ucp/mcp`) are anonymous protocol surfaces. These permissions are reserved for the module's administrative capabilities.

### Request flow

A UCP request is processed as follows:

1. A client calls a canonical UCP endpoint.
1. The controller accepts the HTTP request and delegates work to a UCP service.
1. The service normalizes the UCP request context: store, currency, culture, pagination, and buyer headers.
1. Catalog operations are translated to xCatalog GraphQL queries.
1. Cart operations are translated to xCart GraphQL queries and mutations.
1. `IXApiInProcessExecutor` runs GraphQL inside the current platform process.
1. The service maps xCatalog, xCart, Orders, Store, and platform dictionary data back to UCP response models.

Buyer delegation is header-based, through the following headers:

- `X-Buyer-User-Id`
- `X-Buyer-Organization-Id`

The service adds buyer claims to the principal used for xAPI execution. Delegated B2B context then flows through existing Virto Commerce authorization and context mechanisms.

## Module structure

The module is organized into the following projects.

| Project | Purpose |
| --- | --- |
| `VirtoCommerce.UCP.Core` | Protocol models, service contracts, module constants, options, and errors. |
| `VirtoCommerce.UCP.Data` | Provider-neutral UCP application services and integration logic. |
| `VirtoCommerce.UCP.ExperienceApi` | xAPI schema marker for the module. |
| `VirtoCommerce.UCP.Web` | Module entry point, controllers, filters, GraphQL executor, and DI registrations. |
| `VirtoCommerce.UCP.Tests` | Unit tests for discovery, catalog, cart, checkout handoff, geography, and order tracking behavior. |

The module does not define a UCP database model and does not run module database migrations.

## Dependencies

The module manifest declares the following runtime dependencies.

| Module | Version |
| --- | --- |
| `VirtoCommerce.Xapi` | `3.1001.0` |
| `VirtoCommerce.XCatalog` | `3.1000.0` |
| `VirtoCommerce.XCart` | `3.1016.0` |
| `VirtoCommerce.Store` | `3.1004.0` |
| `VirtoCommerce.Orders` | `3.1000.0` |
| `VirtoCommerce.Marketing` | `3.1000.0` |

Target framework: `.NET 10`.

## Web API

The module exposes the following canonical UCP endpoints. Each operation is also advertised in the discovery profile.

### Discovery

The discovery endpoint returns the UCP profile:

```http
GET /.well-known/ucp
```

The profile includes supported capabilities, default store metadata, endpoint metadata, headers, auth shape, integration guidance, payment handlers, and structured error codes. UCP operations are advertised as HTTP endpoints in `endpoints.operations`.

### Catalog search

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

### Product detail

The product detail endpoint returns a single product:

```http
GET /ucp/v1/catalog/products/{id}?store_id=store-acme&currency=USD&culture_name=en-US
```

The product response includes id, code, name, slug, image URL, brand, product type, price, list price, availability, attributes, and variations. If a product is not found, the endpoint returns the structured error `product_not_found`.

### Cart assembly

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

### Geography

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

### Checkout handoff

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

### Order tracking

The order tracking endpoints return order status after handoff:

```http
GET /ucp/v1/orders/{orderId}?buyer_id=user-42&culture_name=en-US
GET /ucp/v1/orders?cart_id={cartId}&buyer_id=user-42&culture_name=en-US
```

`track_order` returns order status, order number, totals, line items, shipment snapshot, payment snapshot, and shipment tracking fields when they are available in order data.

After hosted handoff, the client usually does not know `order_id` yet. The primary path is lookup by the original `cart_id`, matched against `CustomerOrder.ShoppingCartId` through Orders module services. If buyer context changed during guest checkout, the endpoint retries without buyer filters and still matches strictly by `cart_id`. If the order has not been created yet or is not found among recent orders, the endpoint returns the structured error `order_not_found`.

## MCP server

The module hosts a Streamable HTTP MCP server for AI shopping agents:

```http
POST /ucp/mcp
GET /ucp/mcp
```

The MCP server uses the official C# SDK `ModelContextProtocol.AspNetCore` with Streamable HTTP transport in stateless mode. It exposes typed UCP commerce tools for the Virto Commerce Frontend where this module is installed:

- `get_store_capabilities`
- `search_products`
- `get_product`
- `create_cart`
- `list_carts`
- `get_cart`
- `update_cart`
- `create_checkout`
- `update_checkout`
- `checkout_and_handoff`
- `get_payment_handlers`
- `handoff_checkout`
- `list_countries`
- `resolve_country`
- `list_regions`
- `track_order`

Commerce tools do not accept Frontend URLs. The MCP endpoint itself represents the target Virto Commerce UCP installation, and tools execute the module's local UCP services directly inside the platform process.

This follows the hosted-commerce MCP pattern. Install or configure the MCP remote for the Frontend you want the agent to operate on. Then use the typed tools for search, cart, checkout, geography, handoff, and order tracking.

## Error model

The module returns the following known UCP error codes:

- `invalid_request`
- `missing_store_id`
- `product_not_found`
- `cart_not_found`
- `order_not_found`
- `xapi_execution_failed`

Responses include a correlation id when available. The module reads `X-Correlation-Id` and falls back to the ASP.NET Core trace identifier.

## Build and test

Build and test the module with the following commands:

```powershell
dotnet build VirtoCommerce.UCP.sln
dotnet test VirtoCommerce.UCP.sln --no-build
```

Expected status:

- Build passes.
- Unit tests pass.

## Installation notes

For local Platform testing, install the following module id:

```text
VirtoCommerce.UCP
```

Recommended smoke checks after installation:

1. The module list contains `VirtoCommerce.UCP`.
1. `GET /.well-known/ucp` returns the UCP profile.
1. `POST /ucp/v1/catalog/search` returns catalog results for the configured store.
1. `GET /ucp/v1/catalog/products/{id}` returns product details or `product_not_found`.
1. `POST /ucp/v1/carts` creates an xCart-backed cart.
1. `GET /ucp/v1/carts` returns a buyer-scoped cart list.
1. `PUT /ucp/v1/carts/{cartId}` updates the final cart state.
1. `POST /ucp/v1/checkouts` creates a checkout snapshot.
1. `POST /ucp/v1/checkouts/{checkoutId}/handoff` returns a hosted checkout `continue_url`.
1. `POST /ucp/v1/internal/handoff/restore` restores the temporary handoff session.
1. `GET /ucp/v1/geography/countries/resolve?query=KZ` returns the platform country id for checkout address normalization.
1. `GET /ucp/v1/geography/countries/{countryId}/regions` returns regions when they exist in the platform dictionary.
1. After Frontend checkout, `GET /ucp/v1/orders?cart_id={cartId}&buyer_id={buyerId}` returns the order tracking snapshot.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../Background-Jobs/overview">← Background Jobs</a>
    <a href="../../Testing/testing">Testing →</a>
</div>
