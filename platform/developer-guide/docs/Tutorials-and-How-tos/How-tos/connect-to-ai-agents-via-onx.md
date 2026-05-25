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


## Installation

There are two ways to set up the adapter.

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

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../upgrading-to-dot-net-10">← Upgrading to .NET10 </a>
    <a href="../adding-case-sensitive-search-support-for-postgre">Adding case-insensitive search support for PostgreSQL  →</a>
</div>