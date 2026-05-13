# Connecting to the Platform

## Prerequisites

- A running Virto Commerce Platform instance you can reach from your dev machine.
- A user account on that Platform with permissions for the data you intend to read.
- The Platform's OAuth client registered for your app's origin, with the correct callback URL and CORS configuration.

## Configure the URL

Uncomment `APP_PLATFORM_URL` in **.env.local** and point it at your Platform:

```bash title=".env.local"
APP_PLATFORM_URL=https://your-platform.example.com
```

**.env.local** is gitignored, so machine-specific URLs stay out of version control. Restart `yarn serve` after changing env files.

## Read the current user

```vue title="src/components/UserBadge.vue"
<script setup lang="ts">
import { useUser, VcAvatar } from "@vc-shell/framework";

const { user, isAuthenticated, isAdministrator, signOut } = useUser();
</script>

<template>
  <div v-if="isAuthenticated" class="tw-flex tw-items-center tw-gap-2">
    <VcAvatar :name="user?.userName" size="sm" />
    <span>{{ user?.userName }}</span>
    <span v-if="isAdministrator" class="tw-text-xs tw-font-semibold">Admin</span>
    <button @click="signOut">Sign out</button>
  </div>
</template>
```

`useUser()` is a shared composable — every caller reads from the same singleton, so a single request loads the user once. `loadUser()` is invoked from the generated `src/main.ts` during startup.

## First authenticated API call

```vue title="src/modules/sample/pages/list.vue"
<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useApiClient, useAsync, VcBlade, VcDataTable, VcColumn } from "@vc-shell/framework";
import { OrderClient, type CustomerOrder } from "../../../api_client/orders";

const { getApiClient } = useApiClient(OrderClient);
const orders = ref<CustomerOrder[]>([]);

const { loading, action: load } = useAsync(async () => {
  const client = await getApiClient();
  const result = await client.searchOrders({ skip: 0, take: 20 });
  orders.value = result.results ?? [];
});

onMounted(load);
</script>

<template>
  <VcBlade title="Orders" :loading="loading">
    <VcDataTable :items="orders">
      <VcColumn id="number" title="Number" />
      <VcColumn id="status" title="Status" />
    </VcDataTable>
  </VcBlade>
</template>
```

!!! tip
    `getApiClient()` is async. Call it inside each async function — never at the top of `<script setup>`. Storing the client outside an async block gives you a stale reference when tokens rotate.

For multiple clients in one blade, alias the destructured factory:

```ts
const { getApiClient: getOrderClient } = useApiClient(OrderClient);
const { getApiClient: getCustomerClient } = useApiClient(CustomerClient);
```

Full reference: [`useApiClient`](../composables/data/useApiClient.md). Pattern overview: [API Clients](../concepts/api-clients.md).

## Generate API clients

```bash
yarn generate:api-client
```

Reads OpenAPI documents exposed by `APP_PLATFORM_URL` and writes typed classes into `src/api_client/`. Re-run on schema changes. Hand-edits are overwritten.

## How authentication works

None of the following is your code. Wiring `app.use(VirtoShellFramework, ...)` installs it:

1. The user signs in through the bundled `VcAuthLayout` form.
2. The framework calls `POST /connect/token` with `grant_type=password`, stores the tokens in `localStorage` under `vc_auth_data`.
3. A `fetch` interceptor attaches `Authorization: Bearer <token>` and refreshes the token automatically when it is within 60 seconds of expiry.
4. The Vue Router auth guard reroutes anonymous users to the sign-in page.

## CORS and proxy

Two ways to make cross-origin requests work in development:

- **Same-origin proxy.** Configure Vite to proxy `/api` to the Platform. `APP_PLATFORM_URL` becomes the dev server origin; CORS does not apply.
- **Direct cross-origin.** Add `http://localhost:8080` to the Platform's allowed origins and verify preflight `OPTIONS` headers.

![Readmore](../concepts/api-clients.md){: width="25"} API clients in depth.

## Troubleshooting

!!! warning "Sign-in form returns 'Network error'"
    `APP_PLATFORM_URL` is wrong or unreachable.

!!! warning "401 on every API call after sign-in"
    The OAuth client on the Platform does not include the scopes the API endpoints require.

!!! warning "`CORS error: No 'Access-Control-Allow-Origin'`"
    The dev origin is not whitelisted. Add it, or set up a Vite dev proxy.

!!! warning "Tokens disappear on reload"
    `localStorage` was cleared (incognito tab, storage quota). The framework re-prompts sign-in automatically.

!!! warning "Generated clients fail to compile"
    Re-run `yarn generate:api-client` — the Platform schema likely changed.
