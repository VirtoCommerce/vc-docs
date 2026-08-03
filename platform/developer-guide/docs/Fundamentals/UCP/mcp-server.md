# UCP MCP Server

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


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../web-api">← Web API</a>
    <a href="../build-and-test">Build and test →</a>
</div>
