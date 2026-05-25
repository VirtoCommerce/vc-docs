# Promote a Prototype to API

When `/vc-app design` or `/vc-app generate` creates a module before API clients exist, the module can use mock data. After connecting the app to Platform, use `/vc-app promote <module>` to replace the mock source with generated API clients.

## Run promote

```text
/vc-app promote products
```

The skill validates the prototype marker, discovers generated API clients, maps mock fields to API fields, rewrites the composable, updates affected locales, and runs type checking.

## What changes

The module keeps its blade structure and user workflow. The data source changes from mock data to authenticated Platform calls through `useApiClient`.

```ts
import { useApiClient, useAsync } from "@vc-shell/framework";
import { ProductsClient } from "../../api_client/catalog";

const { getApiClient } = useApiClient(ProductsClient);

const { action: loadProducts, loading } = useAsync(async (query) => {
  const client = await getApiClient();
  return client.searchProducts(query);
});
```

## After promotion

- Review field mappings and labels.
- Keep business-specific transformation outside `src/api_client/`.
- Add tests around the module composable.
- Re-run type checking and the app build.

- [Data loading patterns.](../guides/data/index.md)
