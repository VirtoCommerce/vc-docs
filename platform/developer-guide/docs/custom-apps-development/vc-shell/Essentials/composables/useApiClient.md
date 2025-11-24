# useApiClient Composable

The `useApiClient` composable provides a standardized way to access API clients in VC-Shell applications. It serves as a factory for creating authenticated API client instances that can be used to make HTTP requests to backend services.

The `useApiClient` composable simplifies the process of creating and using API clients in your application by handling common concerns such as authentication token management and base URL configuration. It's particularly useful for accessing Platform APIs and custom API endpoints in a consistent manner.

## API reference

### Parameters

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `clientClass` | `constructor` | A class constructor for the API client type that extends `IAuthApiBase`. |

### Return value

The `useApiClient` composable returns an object with the following methods:

```typescript
interface UseApiClient<ApiClient extends IAuthApiBase> {
  getApiClient: () => Promise<ApiClient>;  // Returns a promise that resolves to an authenticated API client instance
}
```

### IAuthApiBase interface

API client classes used with this composable must implement the `IAuthApiBase` interface:

```typescript
interface IAuthApiBase {
  authToken: string;                                       // The authentication token
  setAuthToken(token: string): void;                       // Method to set the auth token
  getBaseUrl(defaultUrl: string, baseUrl: string): string; // Method to resolve the base URL
}
```

## Usage

### Basic usage

```typescript
import { useApiClient } from '@vc-shell/framework';
import { ProductsClient } from '@your-api-package';

const { getApiClient } = useApiClient(ProductsClient);
```

## Requirements

### API client class requirements

API client classes must implement the `IAuthApiBase` interface to be compatible with `useApiClient`:

- Must extend or implement `IAuthApiBase`
- Must have proper authentication token handling
- Must support base URL configuration
- Should be generated from OpenAPI/Swagger specifications

### Generated API clients

VC-Shell provides tools for generating compatible API client code. You can configure generation using environment variables or command line arguments:

**Using environment variables (.env file):**
```env
APP_PLATFORM_URL=https://api.example.com/
APP_PLATFORM_MODULES=[Platform, Cart, Orders]
APP_API_CLIENT_DIRECTORY=src/api-clients
APP_PACKAGE_NAME=@my-app/api-client
VERBOSE=true
```

**Using command line arguments:**
```bash
npm run generate-api-client --APP_PLATFORM_URL=https://api.example.com/ --APP_PLATFORM_MODULES='[Platform, Cart, Orders]' --APP_API_CLIENT_DIRECTORY=src/api-clients
```

!!! note
    Environment variables take precedence over command line arguments. This allows for better configuration management across different environments.


## Related Resources

- [API Client Integration](../API-Integration/api-client-integration.md) - Guide for generating API clients
- [Connecting to Platform](/platform/developer-guide/latest/custom-apps-development/vc-shell/How-tos/Connecting-to-Platform) - Guide for connecting to VirtoCommerce Platform
