# UCP Configuration

Configuration is read from the `UCP` section of the **appsettings.json** file:

{% include-markdown "../../Configuration-Reference/appsettingsjson.md" start="<!--ucp-start-->" end="<!--ucp-end-->" %}

If `DefaultStoreId` is not configured, discovery reads open stores from the Store module. If one store is found, `/.well-known/ucp` returns it as `default_store_id`, `store`, and the only `stores[]` item. If multiple stores are found, discovery returns them in `stores[]` and the client must choose a store explicitly.

Checkout handoff URLs are built from the Virto Commerce Store URL (`Store.Url` or `Store.SecureUrl`) for the selected default store. `UCP:StorefrontOrigin` is a fallback for environments without Store URLs. `UCP:HandoffUrlTemplate` is an explicit override.

## Application settings

The module registers the following platform setting.

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `UCP.Enabled` | Boolean | `false` | Enables UCP module functionality. Registered in the platform settings under **UCP > General**. Not yet enforced by the current preview endpoints. |

## Permissions

The module registers the following permissions in the **UCP** group.

| Permission | Description |
| --- | --- |
| `ucp:access` | Access UCP module resources. |
| `ucp:create` | Create UCP data. |
| `ucp:read` | View UCP data. |
| `ucp:update` | Update UCP data. |
| `ucp:delete` | Delete UCP data. |

Public UCP protocol endpoints (`/.well-known/ucp`, `/ucp/v1/*`, `/ucp/mcp`) are anonymous protocol surfaces. These permissions are reserved for the module's administrative capabilities.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../quickstart">← Quickstart</a>
    <a href="../web-api">Web API →</a>
</div>
