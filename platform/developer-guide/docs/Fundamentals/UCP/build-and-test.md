# Build and Test

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
    <a href="../mcp-server">← MCP server</a>
    <a href="../../Testing/testing">Testing →</a>
</div>
