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
- `link_buyer_identity`
- `logout_buyer`

Commerce tools do not accept Frontend URLs. The MCP endpoint itself represents the target Virto Commerce UCP installation, and tools execute the module's local UCP services directly inside the platform process.

This follows the hosted-commerce MCP pattern. Install or configure the MCP remote for the Frontend you want the agent to operate on. Then use the typed tools for search, cart, checkout, geography, handoff, order tracking, and buyer identity.

Every tool call requires a `store_id` argument (or a `context.store_id`), unless [`UCP:DefaultStoreId`](configuration.md) is configured. Without either, a call fails with `missing_store_id`:

```json title="400 missing_store_id"
{
  "error": "missing_store_id",
  "message": "store_id or context.store_id is required when UCP:DefaultStoreId is not configured."
}
```

## Anonymous and authenticated buyers

`create_cart` works without an `Authorization` header and mints an anonymous buyer id matching `ucp-anonymous-<32 hex>`. Pass that same `buyer_id` back on later calls to resume the same cart.

To act as a signed-in B2B buyer instead, call `link_buyer_identity` with a bearer token minted against the MCP resource.

![Read more](media/readmore.png){: width="20"} [Authenticating MCP clients](authenticated-buyer-setup.md)

The returned `buyer_id` resolves to the Platform user id. `organization_id` is read only from the token: an `organization_id` argument passed alongside it is ignored, not trusted.

`logout_buyer` ends the OAuth session. It does not invalidate a handoff link minted before the call, since the link's own TTL governs its validity independently of the session that created it.

## Checkout envelopes

`create_checkout`, `handoff_checkout`, and `checkout_and_handoff` each return `continue_url` at a different place in the response. A client that reads one path against all three gets `undefined` from the other two.

| Tool | Envelope | `continue_url` path |
| --- | --- | --- |
| `create_checkout` | `{ ucp, checkout, messages }` | Absent, no `continue_url` anywhere. |
| `handoff_checkout` | `{ result, last_checkout, next_step_after_payment }` | `result.checkout.continue_url` |
| `checkout_and_handoff` | `{ ok, cart_id, buyer_id, checkout, handoff, continue_url, next_step_after_payment }` | `continue_url` (top level) and `handoff.checkout.continue_url` (both present, equal) |

`checkout.id` equals `cart_id`. `create_checkout`'s snapshot total lives at `checkout.cart.totals.total.amount`; the `checkout` object itself carries no top-level `total` or `totals` field.

`checkout_and_handoff` requires `shipping_address` whenever the cart carries no address yet, and also `buyer_id` for an anonymous cart in that case. Omitting a required field fails the checkout rather than falling back to a default.

The response's `continue_url` is host-matched to `endpoints.handoff_url_template` from discovery, and `expires_at` is the mint time plus the store's [handoff TTL](configuration.md).

## Handoff restore

Opening `continue_url` redeems the handoff. An authenticated restore is attempted anonymously first and retried on `401` only, so budget for two round trips on that path.

| Condition | Response |
| --- | --- |
| Fresh, valid link; buyer or anonymous context matches | `200`, lands on `/cart/{cartId}?ucp_handoff=1` |
| Same link redeemed again | `400 invalid_request`: "ucp_session is invalid or expired." |
| Past its TTL | `400 invalid_request`, same message as replayed or forged |
| Unknown or forged token | `400 invalid_request`, same message; no cart, buyer, or line data to leak |
| Different buyer, same organization | `403 buyer_context_mismatch`: "Buyer context does not match the authenticated Platform identity." |

A replayed token, an expired one, and a forged one all return the identical message. The three are not distinguishable from the response alone.

## Error contract

A missing or invalid argument returns `invalid_request` naming the field rather than a bare trace id. This applies to a nested argument too:

```json title="create_cart with an empty line item"
{ "line_items": [{}] }
```
```text
invalid_request: line_items[].product_id is required.
```

```json title="search_products against an unknown store"
{ "store_id": "NO-SUCH-STORE" }
```
```text
invalid_request: store_id does not identify an existing store.
```


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../web-api">← Web API</a>
    <a href="../build-and-test">Build and test →</a>
</div>