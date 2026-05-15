# API Clients

VC-Shell apps talk to a Virto Commerce Platform through typed clients generated from the Platform's OpenAPI documents. The generator (`@vc-shell/api-client-generator`) emits one TypeScript class per Platform module under `src/api_client/`; each class carries the type definitions for every request, response, and search query.

Application code never instantiates these classes directly. The `useApiClient(ClientCtor)` composable returns an async factory that resolves to a configured, authenticated client. The base URL is filled in from `APP_PLATFORM_URL`, the OAuth token is attached, and token rotation is handled automatically. The factory is paired with `useAsync` to provide loading and error refs that flow into `<VcBlade :loading>`, `<VcButton :loading>`, and error banners.

The standard composable shape across modules is: import the client class, call `useApiClient(ClientCtor)`, wrap each operation in `useAsync`, expose `items`, `loading`, and the action functions. Pagination plugs in via `useDataTablePagination`; sort strings come from `useTableSort`.

## Quick start

A minimal list composable pulls orders from the Platform and exposes a `loading` ref for the blade:

```ts title="src/modules/orders/composables/useOrdersList.ts"
import { useApiClient, useAsync } from "@vc-shell/framework";
import { VcmpSellerOrdersClient, type SearchOrdersQuery } from "../../../api_client/virtocommerce.marketplacevendor";

const { getApiClient } = useApiClient(VcmpSellerOrdersClient);

const { action: loadOrders, loading } = useAsync(async (query: SearchOrdersQuery) => {
  const client = await getApiClient();
  searchResult.value = await client.searchOrders(query);
});
```

![Readmore](../composables/data/useApiClient.md){: width="25"} Full useApiClient reference.

!!! warning "`getApiClient()` is async"
    Call it inside the function that needs the client, never at the top of `<script setup>`. A `const client = await getApiClient()` outside an async block is a stale reference once the token rotates.

## CRUD pattern

Wrap each operation in its own `useAsync` so the `loading` and `saving` refs flow into the UI independently:

```ts
import { useApiClient, useAsync } from "@vc-shell/framework";
import { VcmpSellerCatalogClient } from "../../../api_client/...";

const { getApiClient } = useApiClient(VcmpSellerCatalogClient);

const item = ref<Product>();

const { action: load, loading } = useAsync(async (id: string) => {
  const client = await getApiClient();
  item.value = await client.getProductById(id);
});

const { action: save, loading: saving } = useAsync(async () => {
  const client = await getApiClient();
  item.value = await client.updateProduct(item.value);
});

const { action: remove } = useAsync(async (ids: string[]) => {
  const client = await getApiClient();
  await client.deleteProducts(ids);
});
```

Inline form is fine when you only call one method per action: `await (await getApiClient()).updateOrder(command)`.

## Multiple clients in one blade

When a blade talks to several Platform modules, alias the destructured factory so names do not shadow each other:

```ts
const { getApiClient } = useApiClient(VcmpSellerOrdersClient);
const { getApiClient: getOrderApiClient } = useApiClient(OrderModuleClient);
const { getApiClient: getStateMachineApiClient } = useApiClient(StateMachineClient);

const { action: loadOrder } = useAsync(async (id: string) => {
  const orders = await getApiClient();
  const order = await orders.getById(id);

  const statemachine = await getStateMachineApiClient();
  stateMachine.value = await statemachine.searchInstances({ entityId: id });
});
```

## Search and pagination

Platform search endpoints take `{ keyword, skip, take, sort, ... }` and return `{ results, totalCount }`. Combine the client call with `useDataTablePagination` to drive `VcDataTable`:

```ts
import { useApiClient, useAsync, useDataTablePagination } from "@vc-shell/framework";

const { getApiClient } = useApiClient(VcmpSellerOrdersClient);

const searchQuery = ref<SearchOrdersQuery>({ take: 20 });
const searchResult = ref<CustomerOrderSearchResult>();

const { action: loadOrders, loading } = useAsync(async (q: SearchOrdersQuery = {}) => {
  searchQuery.value = { ...searchQuery.value, ...q };
  const client = await getApiClient();
  searchResult.value = await client.searchOrders(searchQuery.value);
});

const pagination = useDataTablePagination({
  pageSize: 20,
  totalCount: computed(() => searchResult.value?.totalCount ?? 0),
  onPageChange: ({ skip }) => loadOrders({ skip }),
});

const items = computed(() => searchResult.value?.results ?? []);
```

`useTableSort` produces the `sort` string (`"createdDate:DESC"`); pass it into the same `searchQuery`.

## Generate clients

Regenerate the typed clients whenever the Platform schema changes:

```bash
yarn generate:api-client
```

The command reads OpenAPI from `APP_PLATFORM_URL` and writes typed classes into `src/api_client/<platform-module>/`. Each module gets its own folder with the client class, the request and response types, and the search query types. The output is committed; hand-edits are overwritten on the next run.
