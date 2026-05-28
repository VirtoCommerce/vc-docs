# Connect Virto Commerce to AI Agents via onX Adapter

The Virto Commerce onX adapter connects a Virto Commerce Platform instance to AI assistants such as Claude via the Model Context Protocol (MCP). It implements the Order Network eXchange (onX) standard, exposing order management, customer lookup, product catalog, inventory, fulfillment, and returns operations as AI-callable tools.

## Supported operations

| Category    | Tools                                                              |
|-------------|--------------------------------------------------------------------|
| Orders      | `create-sales-order`, `update-order`, `cancel-order`, `get-orders` |
| Fulfillment | `fulfill-order`, `get-fulfillments`                                |
| Customers   | `get-customers`                                                    |
| Products    | `get-products`, `get-product-variants`                             |
| Inventory   | `get-inventory`                                                    |
| Returns     | `create-return`, `get-returns`                                     |


## Prerequisites

Before installing the adapter, make sure you have:

* A running Virto Commerce Platform instance with its public URL.
* An [API key](/platform/user-guide/latest/security/api-key/) generated for a Virto Commerce user account with the [permissions listed below](#permissions).
* The store ID and, optionally, the catalog ID you want the adapter to scope to. If omitted, the adapter operates without a default scope.
* Node.js 18 or higher. The `from source` path additionally requires git and npm.
* The MCP client you intend to use, such as Claude Desktop, Claude Code, or any other client that supports the Model Context Protocol.

## Installation

There are two ways to set up the adapter. The configuration goes into your MCP client's settings file. For Claude Desktop, that file is **claude_desktop_config.json** in the following location:

| Operating system | Path |
| --- | --- |
| macOS | **~/Library/Application Support/Claude/claude_desktop_config.json** |
| Windows | **%APPDATA%\Claude\claude_desktop_config.json** |
| Linux | **~/.config/Claude/claude_desktop_config.json** |

If the file does not exist, create it. For Claude Code, see [Use with Claude Code](#use-with-claude-code) below.

=== "Via npx (no local clone needed)"

    This option requires no local clone. Add the following entry to your Claude Desktop configuration file (**claude_desktop_config.json**):

    ```json title="claude_desktop_config.json" hl_lines="14"
    {
      "mcpServers": {
        "cof-mcp": {
          "command": "npx",
          "args": [
            "--package=@virtocommerce/cof-mcp",
            "--package=@virtocommerce/mcp-onx",
            "--yes",
            "cof-mcp"
          ],
          "env": {
            "ADAPTER_TYPE": "npm",
            "ADAPTER_PACKAGE": "@virtocommerce/mcp-onx",
            "ADAPTER_CONFIG": "{\"apiUrl\":\"https://your-vc-instance.com\",\"apiKey\":\"YOUR_API_KEY\",\"workspace\":\"your-store-id\"}",
            "LOG_LEVEL": "info"
          }
        }
      }
    }
    ```


=== "From source"

    1. Clone the repository and build both the server and the adapter:

        ```bash
        git clone https://github.com/VirtoCommerce/vc-onX-adapter.git
        cd vc-onX-adapter

        # Build the server first — the adapter depends on it
        cd server && npm install && npm run build && cd ..

        # Build the adapter
        cd virtocommerce-adapter && npm install && npm run build && cd ..
        ```

    1. Then add the following entry to your **claude_desktop_config.json**:

        ```json title="claude_desktop_config.json" hl_lines="9"
        {
          "mcpServers": {
            "cof-mcp": {
              "command": "node",
              "args": ["/absolute/path/to/server/dist/index.js"],
              "env": {
                "ADAPTER_TYPE": "local",
                "ADAPTER_PATH": "/absolute/path/to/virtocommerce-adapter/dist/index.js",
                "ADAPTER_CONFIG": "{\"apiUrl\":\"https://your-vc-instance.com\",\"apiKey\":\"YOUR_API_KEY\",\"workspace\":\"your-store-id\"}",
                "LOG_LEVEL": "info"
              }
            }
          }
        }
        ```


## Restart and verify

After saving the configuration:

1. Quit Claude Desktop entirely. On macOS, use **Cmd + Q** or **Claude → Quit**. On Windows, right-click the tray icon and choose **Quit**. Closing the window is not enough; the MCP client needs a full restart to pick up the new configuration.
1. Reopen Claude Desktop. It loads the MCP server in the background.
1. Open a new chat. The onX tools (`get-orders`, `create-sales-order`, and the rest listed above) should appear in the tool list when you click the tools or attachments icon.
1. Try a test prompt to confirm the connection works, for example: *Use the onX adapter to list the most recent orders from my Virto Commerce store*.
1. If the tools do not appear, check Claude Desktop's MCP logs. Consult the Claude Desktop documentation for the log file location on your operating system; logs include the stderr output of each MCP server, which surfaces adapter startup errors such as missing environment variables, invalid `ADAPTER_CONFIG` JSON, or failed authentication against the Virto Commerce API.

## Use with Claude Code

Claude Code uses its own MCP server registration mechanism. Register the adapter with one CLI command:

```bash
claude mcp add --scope user virto-onx \
  --env ADAPTER_TYPE=npm \
  --env ADAPTER_PACKAGE=@virtocommerce/mcp-onx \
  --env 'ADAPTER_CONFIG={"apiUrl":"https://your-vc-instance.com","apiKey":"YOUR_API_KEY","workspace":"your-store-id"}' \
  --env LOG_LEVEL=info \
  -- npx --package=@virtocommerce/cof-mcp --package=@virtocommerce/mcp-onx --yes cof-mcp
```

The `--scope user` flag makes the adapter available across all Claude Code sessions on this machine. Use `--scope project` instead to commit the configuration to **.mcp.json** in a repository, so teammates inherit it automatically.

To verify, open Claude Code and run `/mcp` (or ask Claude Code to list the available MCP servers). The `virto-onx` server should appear in the list with a connected status.

## Configuration

The adapter is configured via the `ADAPTER_CONFIG` environment variable as a JSON string.

| Option          | Type       | Required | Default | Description                                                                          |
|-----------------|------------|----------|---------|--------------------------------------------------------------------------------------|
| `apiUrl`        | ==string== | Yes      | -       | Virto Commerce Platform URL.                                                         |
| `apiKey`        | ==string== | Yes      | -       | API key passed in the `api_key` header.                                              |
| `workspace`     | ==string== | No       | -       | Store ID <br> (scopes orders and shipments, auto-detects catalog)                        |
| `catalogId`     | ==string== | No       | -       | Catalog ID for product searches.<br>Auto-detected from the store if `workspace` is set. |
| `timeout`       | ==string== | No       | `30000` | Request timeout in milliseconds.                                                     |
| `retryAttempts` | ==string== | No       | `3`     | Maximum retry attempts for failed requests.                                          |
| `debugMode`     | ==string== | No       | `false` | Logs all API requests and responses to stderr.                                       |


## Permissions

The API key used must have the following Virto Commerce permissions:

| Area             | Permissions                                                            |
|------------------|------------------------------------------------------------------------|
| Order            | Read, Search, Create, Update                                           |
| Shipment         | Search                                                                 |
| Customer/Members | Read, Search                                                           |
| Catalog          | Search                                                                 |
| Inventory        | Search                                                                 |
| Platform         | Read (countries list)                                                  |
| Store            | Read (required when `workspace` is set)                                |
| Pricing          | Evaluate (optional for automatic price lookup during order creation) |

<br>
![Read more](media/readmore.png){: width="20"} [Permissions management](/platform/user-guide/latest/security/roles-and-permissions/#create-new-role-and-assign-permissions)

Try our interactive demo to explore the key features in action:

<div>
  <script async src="https://js.storylane.io/js/v2/storylane.js" data-verify-origin=""></script>
  <div class="sl-embed" style="position:relative;padding-bottom:calc(49.57% + 25px);width:100%;height:0;transform:scale(1)">
    <iframe loading="lazy" class="sl-demo" src="https://app.storylane.io/demo/4zux2o39dumz?embed=inline" name="sl-embed" allow="fullscreen" allowfullscreen style="position:absolute;top:0;left:0;width:100%!important;height:100%!important;border:1px solid rgba(63,95,172,0.35);box-shadow: 0px 0px 18px rgba(26, 19, 72, 0.15);border-radius:10px;box-sizing:border-box;"></iframe>
  </div>
</div>



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../upgrading-to-dot-net-10">← Upgrading to .NET10 </a>
    <a href="../adding-case-sensitive-search-support-for-postgre">Adding case-insensitive search support for PostgreSQL  →</a>
</div>