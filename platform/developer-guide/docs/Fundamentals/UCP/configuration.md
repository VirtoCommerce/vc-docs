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

## Observability

The **UCP** module reports its telemetry through the **OpenTelemetry** module. Add `VirtoCommerce.UCP` to `OpenTelemetry.Sources` for tracing and to `OpenTelemetry.Meters` for metrics. Add `Experimental.ModelContextProtocol` to `OpenTelemetry.Sources` as well to trace requests coming through the MCP server.

With both enabled, one correlated trace follows a REST or MCP request through the UCP operation and the xAPI GraphQL call it triggers. Downstream SQL, Elasticsearch, and HTTP spans complete the same trace. Failed operations are tracked as errors on their span, not only logged.

The meter exports the following counters.

| Metric | Description |
| --- | --- |
| `vc.ucp.operation.count` | UCP operations handled, by endpoint and outcome. |
| `vc.xapi.call.count` | xAPI GraphQL calls made on behalf of a UCP operation. |
| `vc.xapi.failed_call.count` | xAPI GraphQL calls that failed. |
| `vc.xapi.graphql.error.count` | GraphQL-level errors returned inside an otherwise successful xAPI response. |
| `vc.dependency.call.count` | Downstream dependency calls (SQL, Elasticsearch, HTTP) made while handling a UCP operation. |

Two `UCP.Observability` settings tune what gets recorded:

* `InputCaptureMode` controls whether request and response payloads are attached to a trace. The default value `ErrorsOnly` attaches input only for failed operations. A rejected request and its terminal log then share the same trace id. Successful calls carry no raw input.
* `EnableApplicationInsightsCompatibilityBridge` re-emits UCP dependency telemetry in the legacy Application Insights shape alongside OpenTelemetry. Keep it `false` for a plain OpenTelemetry setup. Turning it on together with OpenTelemetry produces duplicate UCP dependencies.

!!! note
    The **Application Insights** module is an optional dependency, declared through `VirtoCommerce.OpenTelemetry`. The **UCP** module package is self-contained for this integration and starts normally when **Application Insights** is not installed.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../quickstart">← Quickstart</a>
    <a href="../web-api">Web API →</a>
</div>
