# Build a Production Module

Use this guide after the AI-generated module runs locally and you are ready to turn it into production code. The goal is a module that loads data through Platform API clients, opens stable blades, respects permissions, and can survive regeneration of API clients.

## Prerequisites

Before you start, make sure you have:

- A VC-Shell app created with `/vc-app design` or `create-vc-app`.
- A module generated with `/vc-app generate <module>`.
- A Platform URL configured through `APP_PLATFORM_URL`.
- API clients generated under `src/api_client/`.

## 1. Keep the Generated Module Boundary

The generated module is the ownership boundary. Keep pages, composables, locale files, permissions, and route definitions under `src/modules/<module>/` unless another module truly shares the same behavior.

```text
src/modules/orders/
  composables/
  locales/
  pages/
  index.ts
```

Do not move list loading, blade state, or module-specific form logic into app-level folders while the code is still owned by one module. Shared app-level code is useful only after two or more modules use it.

## 2. Replace Mock Data With API Clients

Run `/vc-app promote <module>` when the module still uses generated mock data. Promotion should leave one clear data path: UI calls a module composable, the composable calls a generated API client, and the API client handles Platform authentication through the framework.

```ts title="src/modules/orders/composables/useOrdersList.ts"
import { computed, ref } from "vue";
import { useApiClient, useAsync, useDataTablePagination } from "@vc-shell/framework";
import { OrdersClient, type OrderSearchCriteria, type OrderSearchResult } from "../../../api_client/orders";

export function useOrdersList() {
  const { getApiClient } = useApiClient(OrdersClient);
  const query = ref<OrderSearchCriteria>({ take: 20 });
  const result = ref<OrderSearchResult>();

  const { action: load, loading } = useAsync<OrderSearchCriteria>(async (nextQuery) => {
    query.value = { ...query.value, ...nextQuery };
    const client = await getApiClient();
    result.value = await client.searchOrders(query.value);
  });

  const pagination = useDataTablePagination({
    pageSize: 20,
    totalCount: computed(() => result.value?.totalCount ?? 0),
    onPageChange: ({ skip }) => load({ ...query.value, skip }),
  });

  return {
    items: computed(() => result.value?.results ?? []),
    load,
    loading,
    pagination,
  };
}
```

Keep generated API client files untouched. If you need business-specific behavior, wrap the generated client in a module composable instead of editing `src/api_client/`.

## 3. Stabilize Blades and Routes

Blade names are global identifiers. Prefix them with the module and entity so two modules cannot register the same blade name.

```ts title="src/modules/orders/pages/index.ts"
import OrdersList from "./orders-list.vue";
import OrderDetails from "./order-details.vue";

export const blades = {
  OrdersList,
  OrderDetails,
};
```

Use one blade for one user task. A list blade should not own edit-form state; a details blade should not own table pagination for another blade.

## 4. Wire Permissions and Localization

Treat generated permissions and locale keys as a draft. Keep permission strings product-owned and predictable.

```ts title="src/modules/orders/index.ts"
export const permissions = {
  view: "orders:order:view",
  edit: "orders:order:edit",
};
```

Localize module UI with module-prefixed keys such as `ORDERS.LIST.TITLE` and `ORDERS.DETAILS.SAVE`. Avoid generic keys like `TITLE` or `SAVE` inside module locale files because they are hard to audit later.

## 5. Verify Production Behavior

Before handing the module to QA or another team, run the same checks you expect CI to run:

```bash
yarn type-check
yarn lint
yarn build
```

Then run the app against a real Platform environment and verify:

- Empty, loading, success, and error states.
- Pagination, sorting, and filters.
- Permission-gated actions.
- Unsaved-change guards in edit blades.
- Locale keys in every supported language.

## Production Checklist

- The module no longer reads from mock arrays.
- API calls go through `useApiClient`.
- API client files under `src/api_client/` are generated and unedited.
- Blade names include the module prefix.
- Permission strings match the Platform permission model.
- Table state has a stable `state-key` only when persistence is intentional.
- Business-specific examples in docs or comments are marked as pseudo-code when they use placeholder clients.

## Related

- [Generate an app from a prompt](../getting-started/generate-app-from-prompt.md)
- [Promote a prototype to API](../getting-started/promote-prototype-to-api.md)
- [Data guide](data/index.md)
- [Blades guide](blades/index.md)
- [Best practices](best-practices.md)
