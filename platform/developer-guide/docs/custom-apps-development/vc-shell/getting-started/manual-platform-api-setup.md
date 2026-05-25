# Manual Platform API Setup

Use this page when you want to do the same work as `/vc-app connect` and `/vc-app promote` without the AI skill. The manual path has three parts: configure the app runtime, generate API clients from Platform OpenAPI documents, and replace mock-backed module data with `useApiClient` calls.

## Prerequisites

Before you start, make sure you have:

- A VC-Shell app created with `create-vc-app`.
- A reachable Virto Commerce Platform URL.
- Platform modules installed for the APIs you want to call.
- Node.js 22 or higher and dependencies installed with `yarn install`.

## 1. Configure the App Runtime

Create or update `.env.local` in the app root:

```env
APP_PLATFORM_URL=https://admin.example.com
```

`.env.local` is for local runtime configuration. Do not commit machine-specific Platform URLs, credentials, or tokens.

Run the app and verify that sign-in reaches your Platform instance:

```bash
yarn serve
```

## 2. Choose Platform Modules

API clients are generated per Platform module. Use the module names exposed by your Platform installation, for example:

```text
VirtoCommerce.Catalog,VirtoCommerce.Orders
```

Use only the modules your app actually calls. Regenerating clients for every installed module creates a large `src/api_client/` folder and slows down review.

## 3. Configure API Generation

Keep API generation settings in the app's `.env` file when you want repeatable local and CI commands:

```env title=".env"
APP_PLATFORM_MODULES=[VirtoCommerce.Catalog,VirtoCommerce.Orders]
APP_API_CLIENT_DIRECTORY=./src/api_client/
APP_TYPE_STYLE=Interface
```

`.env` is the shared generation configuration. `.env.local` is the local runtime override. Keep secrets and machine-specific values out of `.env`; if the Platform URL differs per developer, put `APP_PLATFORM_URL` in `.env.local` or pass it in the shell when running the generator.

The minimal configuration above is enough for the default generation mode. By default, the generator writes TypeScript client files into `APP_API_CLIENT_DIRECTORY`; it does not create a generated API package or package metadata unless package mode is enabled.

The generator accepts the same options from `.env`, shell environment variables, or command-line arguments:

| Option | Purpose |
| --- | --- |
| `APP_PLATFORM_URL` | Platform URL used to discover module OpenAPI documents. |
| `APP_PLATFORM_MODULES` | Module list, for example `[VirtoCommerce.Catalog,VirtoCommerce.Orders]`. Spaces are allowed. |
| `APP_API_CLIENT_DIRECTORY` | Output directory for generated clients. |
| `APP_TYPE_STYLE` | DTO type style: `Interface` or `Class`. New apps should use `Interface`. |
| `VERBOSE` | Set to `true` for detailed generator and NSwag output. |

When an option is provided both as an environment variable and as a CLI argument, the environment variable wins.

Package mode is optional. Use it only when you intentionally maintain a generated API package under `src/api_client/`. Package mode is enabled with `--PACKAGE=true` or when `src/api_client/package.json` already exists. In that case, these additional options apply:

| Option | Purpose |
| --- | --- |
| `APP_PACKAGE_NAME` | Package name written into generated API package metadata. |
| `APP_PACKAGE_VERSION` | Package version written into generated API package metadata. |
| `APP_OUT_DIR` | Output directory used by the generated package metadata. |
| `APP_BUILD_DIR` | Directory where generated TypeScript files are compiled in package mode. |
| `SKIP_BUILD` | Set to `true` to skip the generated package build step. |

## 4. Generate API Clients With the Project Script

New VC-Shell apps include a `generate-api-client` script in `package.json`. If you keep configuration in `.env`, the script can stay generic:

```json title="package.json"
{
  "scripts": {
    "generate-api-client": "cross-env api-client-generator"
  }
}
```

Run the generator:

```bash
yarn generate-api-client
```

You can also keep the script self-contained by passing options directly:

```json title="package.json"
{
  "scripts": {
    "generate-api-client": "cross-env api-client-generator --APP_PLATFORM_MODULES='[VirtoCommerce.Catalog,VirtoCommerce.Orders]' --APP_API_CLIENT_DIRECTORY=./src/api_client/ --APP_TYPE_STYLE=Interface"
  }
}
```

If `APP_PLATFORM_URL` is not committed to `.env`, pass it at runtime:

```bash
APP_PLATFORM_URL=https://admin.example.com yarn generate-api-client
```

On PowerShell:

```powershell
$env:APP_PLATFORM_URL="https://admin.example.com"
yarn generate-api-client
```

The generator writes clients and DTO types under `src/api_client/`. Do not hand-edit generated files; regenerate them when the Platform API contract changes.

## 5. Generate API Clients Without a Project Script

If the app does not have a `generate-api-client` script, run the generator directly:

```bash
npx @vc-shell/api-client-generator \
  --APP_PLATFORM_URL=https://admin.example.com \
  --APP_PLATFORM_MODULES='[VirtoCommerce.Catalog,VirtoCommerce.Orders]' \
  --APP_API_CLIENT_DIRECTORY=./src/api_client/ \
  --APP_TYPE_STYLE=Interface
```

Add `--VERBOSE=true` when Platform discovery or NSwag generation fails.

## 6. Import Generated Clients

Use generated clients only through `useApiClient`. The framework provides the authenticated HTTP pipeline; direct client construction bypasses that integration.

```ts title="src/modules/orders/composables/useOrdersList.ts"
import { computed, ref } from "vue";
import { useApiClient, useAsync } from "@vc-shell/framework";
import { OrdersClient, type OrderSearchCriteria, type OrderSearchResult } from "../../../api_client/orders";

export function useOrdersList() {
  const { getApiClient } = useApiClient(OrdersClient);
  const result = ref<OrderSearchResult>();

  const { action: loadOrders, loading } = useAsync<OrderSearchCriteria>(async (query) => {
    const client = await getApiClient();
    result.value = await client.searchOrders(query);
  });

  return {
    items: computed(() => result.value?.results ?? []),
    loadOrders,
    loading,
  };
}
```

Generated DTOs use `Interface` style in new apps. Create request objects with object literals instead of `new SomeQuery()`.

## 7. Replace Mock Data Manually

When a module starts with local mock data, replace it in small steps:

1. Find the module composable that owns loading and saving.
2. Keep the blade template and emitted events unchanged.
3. Replace the mock array or timeout with a generated client call.
4. Map API response fields to the view model expected by the blade.
5. Run type-checking after each meaningful change.

```bash
yarn type-check
yarn build
```

Keep business-specific mapping in the module composable or a module-local adapter. Do not add custom methods to generated API client files.

## Troubleshooting

| Problem | Check |
| --- | --- |
| `APP_PLATFORM_URL is required` | Set `APP_PLATFORM_URL` in `.env`, pass it in the shell command, or pass `--APP_PLATFORM_URL=...`. |
| No client is generated for a module | Check the exact Platform module name and the `APP_PLATFORM_MODULES` list. |
| NSwag cannot reach the API document | Open the Platform URL in a browser and verify the module is installed and running. |
| `APP_TYPE_STYLE` error | Use exactly `Interface` or `Class`; the value is case-sensitive. |
| Type errors after regeneration | Check whether the backend contract changed and update the module composable or view model mapping. |

## Related

- [Manual CLI Start](manual-cli-start.md)
- [Connect to Platform](connect-to-platform.md)
- [Promote a Prototype to API](promote-prototype-to-api.md)
- [API Clients](../concepts/api-clients.md)
- [Data guide](../guides/data/index.md)
