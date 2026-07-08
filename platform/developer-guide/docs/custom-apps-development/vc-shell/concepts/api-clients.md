# API Clients

VC-Shell apps talk to a Virto Commerce Platform through typed clients generated from the Platform's OpenAPI documents. The generator (`@vc-shell/api-client-generator`) emits one TypeScript class per Platform module under `src/api_client/`. Each class carries the type definitions for every request, response, and search query.

Application code never instantiates these classes directly. The `useApiClient(ClientCtor)` composable returns an async factory that constructs the client on demand. Authentication flows through the browser session cookie that the Platform sets at sign-in; the framework redirects to the login page when the session expires. Application code never attaches a token, tracks expiry, or builds an `Authorization` header.

## Quick start

A minimal list composable pulls orders from the Platform and exposes a `loading` ref for the blade:

```ts title="src/modules/orders/composables/useOrdersList.ts"
import { useApiClient, useAsync } from "@vc-shell/framework";
import { OrdersClient, type OrderSearchCriteria } from "../../../api_client/orders";

const { getApiClient } = useApiClient(OrdersClient);

const { action: loadOrders, loading } = useAsync(async (query: OrderSearchCriteria) => {
  const client = await getApiClient();
  searchResult.value = await client.searchOrders(query);
});
```

- [Full useApiClient reference.](../composables/data/useApiClient.md)

!!! warning "`getApiClient()` is async"
    Call it inside the function that needs the client, never at the top of `<script setup>`. A `const client = await getApiClient()` outside an async block holds a single instance for the lifetime of the component, which is fine for stable sessions but couples your code to one client object across reruns of the action.

## The useApiClient + useAsync pattern

The canonical shape across modules pairs `useApiClient` with `useAsync`. Each operation gets its own `useAsync` so loading and saving refs flow into the UI independently:

```ts
import { useApiClient, useAsync } from "@vc-shell/framework";
import { CatalogClient } from "../../../api_client/catalog";

const { getApiClient } = useApiClient(CatalogClient);

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

`useAsync` catches thrown errors and exposes them through the blade's error boundary. Inline form is fine when you only call one method per action: `await (await getApiClient()).updateOrder(command)`.

## Multiple clients in one blade

When a blade talks to several Platform modules, alias the destructured factory so names do not shadow each other:

```ts
const { getApiClient } = useApiClient(OrdersClient);
const { getApiClient: getOrderApiClient } = useApiClient(OrderModuleClient);
const { getApiClient: getStateMachineApiClient } = useApiClient(StateMachineClient);

const { action: loadOrder } = useAsync(async (id: string) => {
  const orders = await getApiClient();
  const order = await orders.getById(id);

  const stateMachine = await getStateMachineApiClient();
  stateMachineInstance.value = await stateMachine.searchInstances({ entityId: id });
});
```

## Generate clients

Regenerate the typed clients whenever the Platform schema changes. A scaffolded VC-Shell app exposes the generator as an npm script:

```bash
yarn generate-api-client
```

The command reads OpenAPI from the configured Platform URL and writes one `<module>.ts` file per Platform module into `src/api_client/`, plus a shared `authApiBase.ts`. Each file exports the client class along with the request, response, and search-query types. The output is committed; hand-edits are overwritten on the next run.

- [api-client-generator CLI reference.](../reference/cli/api-client-generator.md)

## Common mistakes

!!! warning "Hand-rolling an Authorization header"
    There is nothing to hand-roll. The Platform login endpoint sets a session cookie and the browser replays it. A token-attach wrapper around `useApiClient` is wasted code; if a call comes back unauthenticated, check sign-in and the cookie, not your interceptor.

!!! warning "Calling `getApiClient()` once at module load"
    The factory is async because it is expected inside an async action. Calling it at the top of `<script setup>` ties one client instance to the component for its whole lifetime. Prefer one `await getApiClient()` per action — it is cheap, and it keeps the call shape uniform with `useAsync`.

!!! warning "Reaching for a Platform client through raw `fetch`"
    For Platform endpoints, go through a generated client. Raw `fetch` bypasses the typed signatures and the framework error handling that `useAsync` relies on. Raw `fetch` is fine for third-party hosts.
