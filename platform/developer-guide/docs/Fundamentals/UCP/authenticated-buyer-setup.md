# Authenticate MCP Clients

[Quickstart](quickstart.md) connects an agent as an anonymous shopper over a public remote MCP connector. This page covers the other path: a locally bridged MCP client that signs a buyer in through OAuth. The agent can then shop, check out, and hand off as that signed-in B2B buyer.

Enabling this involves three separate configuration surfaces:

* **Platform authorization**, declaring the MCP endpoint as an OAuth-protected resource.
* **An OAuth client**, the credential the agent authenticates with.
* **Store and module settings**: which store an untagged call resolves to, and the handoff link's validity window.

## Configure Platform authorization

Declare the MCP endpoint as a protected resource. 
<br> 
![Read more](media/readmore.png){: width="20"} [OAuth-protected MCP resource](configuration.md#oauth-protected-mcp-resource)

## Register OAuth client for agent

Sign in to the Platform Manager as an administrator and open **Security** --> **OAuth applications**. This build has no dedicated screen for registering an MCP client there, so create the application from the browser console instead:

1. Open the browser's developer tools (F12) and go to the **Console** tab.
1. Run the following script, replacing the placeholders:

```javascript
(async () => {
  const api = angular.element(document.body).injector().get("platformWebApp.oauthapps");
  const app = await api.new().$promise;
  app.displayName = "<a descriptive name for this agent client>";
  app.clientType = "public";
  app.clientSecret = null;
  app.consentType = "systematic";
  app.redirectUris = ["<the callback URL your MCP client listens on>"];
  app.permissions = ["rsrc:{{FRONT_URL}}/ucp/mcp"];
  const saved = await api.save({}, app).$promise;
  console.log("CLIENT_ID:", saved.clientId);
  console.log("CLIENT_TYPE:", saved.clientType);
  console.log("REDIRECT_URIS:", saved.redirectUris);
  console.log("PERMISSIONS:", saved.permissions);
})().catch(console.error);
```

In the console output, check that:

* `CLIENT_TYPE` is `public`. A public client is issued no client secret and needs none.
* `REDIRECT_URIS` contains exactly the callback URL your agent client uses.
* `PERMISSIONS` contains `rsrc:{{FRONT_URL}}/ucp/mcp`. If this permission is missing after saving, the Platform build in use does not yet preserve it on save.

Record the printed `CLIENT_ID` for whoever configures the agent client. A public client has no `client_secret` to record.

## Configure store and module settings

Every MCP call must resolve to a store. Set [`UCP:DefaultStoreId`](configuration.md) so an agent call that omits `store_id` still resolves, or always pass `store_id` explicitly.

A minted handoff link stays redeemable only for a limited window, controlled by [`UCP:HandoffTokenTtlMinutes`](configuration.md).

## Wire MCP client

For a client that supports `mcp-remote` (for example, Claude Desktop):

1. Create two local files the client reads at startup:

    ```json title="client-info.json"
    { "client_id": "<CLIENT_ID>", "token_endpoint_auth_method": "none" }
    ```

    ```json title="client-metadata.json"
    { "scope": "openid profile offline_access", "token_endpoint_auth_method": "none" }
    ```

1. Add an entry to the client's MCP server configuration:

    ```json title="claude_desktop_config.json"
    {
      "mcpServers": {
        "ucp-authenticated": {
          "command": "npx",
          "args": [
            "-y",
            "mcp-remote",
            "{{FRONT_URL}}/ucp/mcp",
            "8766",
            "--host",
            "localhost",
            "--transport",
            "http-only",
            "--static-oauth-client-info",
            "@C:\\ucp\\client-info.json",
            "--static-oauth-client-metadata",
            "@C:\\ucp\\client-metadata.json",
            "--resource",
            "{{FRONT_URL}}/ucp/mcp",
            "--authorize-param",
            "prompt=login",
            "--auth-timeout",
            "600"
          ],
          "env": {
            "MCP_REMOTE_CONFIG_DIR": "C:\\ucp\\"
          }
        }
      }
    }
    ```

1. Fully restart the client.

Sign-in opens a browser at the storefront's authorization page. The buyer signs in, consents, and the client redirects back to the configured callback.

## Verify setup

Request the discovery manifest from both hosts:

```text
GET {{BACK_URL}}/.well-known/ucp
GET {{FRONT_URL}}/.well-known/ucp
```

Both must report the same MCP service endpoint.

Against that endpoint, call `tools/list` and confirm the tool list matches [MCP Server](mcp-server.md).

Confirm `get_store_capabilities.auth.authorization_server` matches the authorization endpoint you configured above.

If all three checks agree, an agent can discover the store. Once a buyer authorizes a registered client, the agent can shop, check out, and hand off as that buyer.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../configuration">← Configuration</a>
    <a href="../web-api">Web API →</a>
</div>