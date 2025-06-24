# API Client Integration

This guide covers the end-to-end process of generating, customizing, and using API clients for VC-Shell applications.

VC-Shell provides a flexible framework for working with APIs:

* **Generating API clients** from OpenAPI/Swagger specifications.
* **Using built-in and custom API clients** in your applications.
* **Extending and overriding API clients** for custom functionality.

## Generate API clients

### Prerequisites

* Node.js 22 or higher
* .NET Core 6.0 (particularly if you are using MacOS or Linux)

### Set up client generation

1. Add the necessary dependencies to your project:

    === "Using command"

        ```bash
        yarn add @vc-shell/api-client-generator cross-env
        ```
        <br>
        `cross-env` runs scripts that set and use environment variables across platforms.

    === "Manually"

        Add the dependencies to your project's **package.json**:

        ```json title="vc-app/package.json" linenums="1"
        {
            ...
            "devDependencies": {
                ...
                "@vc-shell/api-client-generator": "latest",
                "cross-env": "latest",
                ...
            }
        }
        ```

1. Configure client generation in your project. Inside your project's **package.json** file, add a `"generate-api-client"` command to the list of scripts:

    ```json title="vc-app-extend/package.json" linenums="1"
    {
        "scripts": {
            ...
            "generate-api-client": "cross-env api-client-generator --APP_PLATFORM_MODULES='[Virtocommerce.MarketplaceVendor,Virtocommerce.Catalog,Virtocommerce.Orders]' --APP_API_CLIENT_DIRECTORY=./src/api_client/"
        }
    }
    ```

    Available configuration options:

    | Option | Description | Type | Example |
    |--------|-------------|------|---------|
    | `--APP_PLATFORM_MODULES` | Platform modules with namespaces to generate API client | `string[]` | `--APP_PLATFORM_MODULES='[Virtocommerce.MarketplaceVendor,Virtocommerce.Orders,Virtocommerce.Catalog]'` |
    | `--APP_API_CLIENT_DIRECTORY` | Output directory for generated API clients | `string` | `--APP_API_CLIENT_DIRECTORY=./src/api_client/` |
    | `--APP_PLATFORM_URL` | Platform URL to obtain client API configs | `string` | `--APP_PLATFORM_URL=https://vcmp-dev.govirto.com/` |
    | `--APP_PACKAGE_NAME` | Package name for generated API clients | `string` | `--APP_PACKAGE_NAME=@api-client` |
    | `--APP_PACKAGE_VERSION` | Package version for generated API clients | `string` | `--APP_PACKAGE_VERSION=1.1.0` |
    | `--APP_OUT_DIR` | Output directory for generated API clients | `string` | `--APP_OUT_DIR=./src/api_client/` |
    | `--APP_BUILD_DIR` | Directory where TypeScript files will be compiled | `string` | `--APP_BUILD_DIR=lib` (default is "dist") |
    | `--SKIP_BUILD` | Skip build step | `boolean` | `--SKIP_BUILD=true` |
    | `--VERBOSE` | Enable verbose logging | `boolean` | `--VERBOSE=true` |

1. Configure Platform URL in your project's **.env** file:

    ```
    APP_PLATFORM_URL=https://vcmp-dev.govirto.com/
    ```

    !!! note
        Alternatively, you can specify the Platform URL as a command option when running the generator.

1. Generate the API clients using the following command:

    ```bash
    yarn generate-api-client
    ```

This generates TypeScript client classes that extend the `AuthApiBase` class, making them compatible with the VC-Shell authentication system.

## Key features of API client generator

The generator includes several advanced features that make working with API clients more efficient:

### Smart configuration merging

When updating an existing API client, the generator intelligently merges configuration files:
- Preserves custom package.json fields (name, version, description, etc.)
- Maintains custom tsconfig.json settings
- Intelligently updates exports to keep existing paths

### Multiple API exports

The generator effectively handles multiple API clients:
- Creates standardized exports with both short and full module names
- Prevents duplicate module exports
- Works with incremental generation (can add new APIs without breaking existing ones)

### Smart root export handling

The generator intelligently handles root exports based on the API modules count:
- With a single API module, it becomes the root export
- With multiple API modules, only subpath exports are used
- Preserves existing root exports when possible

### Error handling and debugging

For troubleshooting API client generation:
- Enable verbose logging with `--VERBOSE=true`
- Check connectivity to the platform URL
- Verify the specified platform modules exist
- Ensure target directories have proper permissions

## Using API clients

### Basic usage

Custom API clients can be used with the `useApiClient` composable just like the built-in platform clients:

```typescript
import { useApiClient } from '@vc-shell/framework';
import { CustomApiClient } from './api_client';

export default {
  setup() {
    const { getApiClient } = useApiClient(CustomApiClient);
    
    async function fetchItems() {
      const client = await getApiClient();
      return client.getItems();
    }
    
    return { fetchItems };
  }
}
```

### Automated package creation

The API client generator automatically creates a fully configured package structure that's ready to use. When you run the generator:

1. It generates TypeScript API client files based on the Platform API
2. Automatically compiles TypeScript to JavaScript (including declaration files)
3. Creates or updates a properly configured `package.json` with:
   - Customizable name via `--APP_PACKAGE_NAME`
   - Configurable version via `--APP_PACKAGE_VERSION`
   - Intelligent exports configuration
   - Type definitions
   - Build metadata
4. Generates a properly configured `tsconfig.json` file

This eliminates the need for manual package setup, saving development time and reducing configuration errors.

### Generated package usage

After generating the API client, it's ready to use as a local package:

1. Add it to your application's workspace configuration (if using workspaces):

    ```json title="vc-app/package.json" linenums="1"
    {
        "workspaces": [
          "./src/api_client"
        ]
    }
    ```

1. Add it as a dependency in your application:

    ```bash
    yarn add @your-app/api-client
    ```

1. Import and use the generated clients:

    ```typescript
    // For a single API module
    import { CustomApiClient } from '@your-app/api-client';

    // For multiple API modules
    import { CatalogClient } from '@your-app/api-client/catalog';
    import { OrdersClient } from '@your-app/api-client/orders';
    ```

### Custom package configuration

You can further customize the generated package by:

1. Specifying a custom package name and version during generation:

    ```bash
    yarn generate-api-client --APP_PACKAGE_NAME=@your-app/api --APP_PACKAGE_VERSION=1.1.0
    ```

1. Adding custom scripts, dependencies, or other fields to the generated `package.json` file:

    ```json
    {
      "scripts": {
        "build": "tsc",
        "generate-types": "tsc --emitDeclarationOnly --declaration"
      },
      "peerDependencies": {
        "@vc-shell/framework": "^1.1.0"
      }
    }
    ```

The generator will preserve these custom fields when regenerating the API client.

## Best practices

* **Type safety**: Always define TypeScript interfaces for your API request and response models.
* **Error handling**: Implement consistent error handling in your custom API clients.
* **Authentication**: Utilize the authentication mechanisms provided by the VC-Shell framework.
* **OpenAPI generation**: Whenever possible, generate clients from OpenAPI specifications for consistency.
* **Versioning**: Include API version information in your custom clients to make version changes explicit.
* **Reuse**: Prefer existing API clients when possible, extending them only when necessary.
* **Testing**: Create unit tests for custom API clients, especially for extended functionality.
