# Connect Virto Start Cloud to Claude Desktop

This is the complete partner-facing setup for an existing Virto Start environment deployed in Virto Cloud. The Frontend host exposes the UCP endpoints. Virto Cloud routes the requests to the Platform application where this module runs.

Before starting, identify the exact Virto Commerce Store ID and the public Frontend host. The examples below use `B2B-store` and `store.example.com`.

To connect Virto Start Cloud to Claude Desktop:

1. [Install the module.](#install-module)
1. [Update the Virto Cloud environment.](#update-virto-cloud-environment)
1. [Verify the endpoint.](#verify-endpoint)
1. [Add the connector to Claude Desktop.](#add-connector-to-claude-desktop)
1. [Run the first smoke test.](#run-first-smoke-test)

## Install module

Install the UCP module in the Virto Start **Platform application**. The required module dependencies are listed in [Dependencies](overview.md#dependencies).

## Update Virto Cloud environment

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

## Verify endpoint

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

## Add connector to Claude Desktop

Remote MCP servers are configured as Claude custom connectors. Do not put this remote URL in **claude_desktop_config.json**. That file is for locally launched MCP servers.

For an individual Claude plan:

1. Open Claude Desktop and open **Customize --> Connectors**.
1. Select **+ --> Add custom connector**.
1. Set the name to `Virto Commerce UCP`.
1. Set the remote MCP server URL to `https://store.example.com/ucp/mcp`.
1. Select **Add**.
1. In a new conversation, select **+ --> Connectors** and enable the **Virto Commerce UCP** connector.

The Virto Commerce UCP connector is now available in the conversation.

For a Team or Enterprise plan, an Owner must first add the URL under **Organization settings --> Connectors**. Each user can then connect to it and enable it for a conversation.

See Anthropic's [remote MCP custom connector guide](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) for the current Claude UI and network requirements.

## Run first smoke test

Start a new Claude conversation with the connector enabled and send the following prompt:

**Use the Virto Commerce UCP connector. First call get_store_capabilities. Then search for products matching "printer". Use the default store, currency,
and language published by the server. Ask me to select a store only if the server publishes multiple stores and no default_store_id.**

Claude should call `get_store_capabilities` and then `search_products` without asking for values already published by the server.

## Troubleshooting

The table below lists common issues and what to check.

| Symptom | Check |
| --- | --- |
| Claude cannot connect. | Confirm that the Cloud environment routes `/ucp` to `platform`, the Frontend host is public, and the updated environment was deployed. |
| `missing_store_id` | Confirm that `platform.config.UCP__DefaultStoreId` contains the exact Store ID and the updated environment was deployed. |
| Search returns no products. | Confirm that the store is open, the catalog is assigned to the store, prices and inventory exist, and the search index has been built. |
| Checkout opens the wrong host. | Configure `Store.SecureUrl` or `Store.Url`, or set `UCP__StorefrontOrigin` and `UCP__HandoffUrlTemplate`. |
| A Team or Enterprise user cannot add the connector. | Ask an organization Owner to add the custom connector first. |


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../overview">← Overview</a>
    <a href="../configuration">Configuration →</a>
</div>
