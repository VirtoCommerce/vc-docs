# Data

Recipes for the data layer behind a list blade: pagination, sorting, filtering, selection, custom cell rendering, and persisted table state. Each recipe is trimmed from the vendor-portal orders module and the sample-module CLI template.

## Prerequisites

Before wiring data into a table, make sure you have:

- A list blade scaffolded. See [Blades guide](../blades/index.md).
- An API client generated for the resource you list. See [API clients](../../concepts/api-clients.md).
- Familiarity with the **VcDataTable** component. See [VcDataTable reference](../../components/data-display/vc-data-table.md).

## Recipe: server-side paginated list

For any dataset that does not fit in memory, page on the server. Pair `useDataTablePagination` with `useApiClient` and `useAsync`. The composable owns the search query, page size, and total count; the page binds the returned pagination object straight to `VcDataTable`.

```ts title="composables/useOrdersList.ts"
import { computed, ref } from "vue";
import { useAsync, useApiClient, useDataTablePagination } from "@vc-shell/framework";
import {
  VcmpSellerOrdersClient,
  type SearchOrdersQuery,
  type CustomerOrderSearchResult,
} from "../../../api_client/virtocommerce.marketplacevendor";

export function useOrdersList(options?: { pageSize?: number; sort?: string }) {
  const { getApiClient } = useApiClient(VcmpSellerOrdersClient);
  const pageSize = options?.pageSize ?? 20;

  const searchQuery = ref<SearchOrdersQuery>({ take: pageSize, sort: options?.sort });
  const searchResult = ref<CustomerOrderSearchResult>();

  const { action: loadOrders, loading } = useAsync<SearchOrdersQuery>(async (query) => {
    searchQuery.value = { ...searchQuery.value, ...(query || {}) };
    const client = await getApiClient();
    searchResult.value = await client.searchOrders(searchQuery.value);
  });

  const pagination = useDataTablePagination({
    pageSize,
    totalCount: computed(() => searchResult.value?.totalCount ?? 0),
    onPageChange: ({ skip }) => loadOrders({ ...searchQuery.value, skip }),
  });

  return {
    items: computed(() => searchResult.value?.results ?? []),
    pagination,
    searchQuery,
    loadOrders,
    loading,
  };
}
```

```vue title="pages/orders-list.vue (template fragment)"
<VcDataTable
  :loading="loading"
  :items="items"
  :pagination="pagination"
  :total-count="pagination.totalCount"
  @pagination-click="pagination.goToPage"
>
  <VcColumn id="number" :title="$t('ORDERS.LIST.NUMBER')" />
  <VcColumn id="customerName" :title="$t('ORDERS.LIST.CUSTOMER')" />
  <VcColumn id="total" :title="$t('ORDERS.LIST.TOTAL')" type="money" />
</VcDataTable>
```

The composable returns `pagination` as a single reactive object exposing `currentPage`, `pages`, `skip`, `pageSize`, `totalCount`, and `goToPage`. Pass the whole object to the `pagination` prop and wire `pagination-click` to `pagination.goToPage`.

![Readmore](../../composables/data/useDataTablePagination.md){: width="25"} useDataTablePagination API reference.

## Recipe: client-side filtering

When the dataset is small (under ~500 rows) and already loaded, filter in a `computed` over the items array. This keeps the UI responsive without a round trip.

```ts title="Client-side filter"
const keyword = ref("");

const filteredItems = computed(() => {
  const q = keyword.value.trim().toLowerCase();
  if (!q) return items.value;
  return items.value.filter((item) => item.name.toLowerCase().includes(q));
});
```

```vue title="Bind to VcDataTable"
<VcDataTable v-model:search-value="keyword" :items="filteredItems" :searchable="true" />
```

Trade-off: simpler wiring, but pagination over `filteredItems` becomes meaningless because `totalCount` reflects only the loaded page. For anything that paginates on the server, build the filter into the search query instead.

## Recipe: sorting integration

`useTableSort` tracks the current sort property and direction, and exposes a `sortExpression` ref like `"createdDate:DESC"` ready to send to the API. `VcDataTable` reports sort changes through `v-model:sort-field` and `v-model:sort-order`; pipe both into the composable's handler, then watch `sortExpression` and reload.

```ts title="Sort wiring"
import { useTableSort } from "@vc-shell/framework";

const { sortExpression } = useTableSort({
  initialProperty: "createdDate",
  initialDirection: "DESC",
});

onMounted(() => loadOrders({ ...searchQuery.value, sort: sortExpression.value }));

watch(sortExpression, (value) => {
  loadOrders({ ...searchQuery.value, sort: value });
});
```

```vue title="Bind sort to the table"
<VcDataTable
  v-model:sort-field="sortField"
  v-model:sort-order="sortOrder"
  :items="items"
>
  <VcColumn id="number" :title="$t('ORDERS.LIST.NUMBER')" :sortable="true" />
  <VcColumn id="createdDate" :title="$t('ORDERS.LIST.CREATED')" :sortable="true" type="date-ago" />
</VcDataTable>
```

Mark sortable columns with `:sortable="true"`. Override the backend field with `sort-field` on `VcColumn` when it differs from the column `id`.

![Readmore](../../composables/data/useTableSort.md){: width="25"} useTableSort API reference.

## Recipe: row selection and bulk actions

Set `selection-mode="multiple"` to render a checkbox column, bind `v-model:selection` to an array ref, and drive toolbar item state from the selected IDs.

```vue title="Bulk delete toolbar"
<template>
  <VcBlade :title="title" :toolbar-items="bladeToolbar" width="50%">
    <VcDataTable
      v-model:selection="selectedItems"
      selection-mode="multiple"
      :items="items"
      data-key="id"
    >
      <VcColumn id="name" :title="$t('LIST.NAME')" />
      <VcColumn id="price" :title="$t('LIST.PRICE')" type="money" />
    </VcDataTable>
  </VcBlade>
</template>

<script setup lang="ts">
const selectedItems = ref<Item[]>([]);
const selectedIds = computed(() => selectedItems.value.map((i) => i.id).filter(Boolean));

const bladeToolbar = computed<IBladeToolbar[]>(() => [
  {
    id: "remove",
    icon: "lucide-trash-2",
    title: t("LIST.TOOLBAR.REMOVE"),
    disabled: computed(() => selectedIds.value.length === 0),
    async clickHandler() {
      await removeItems({ ids: selectedIds.value });
      selectedItems.value = [];
    },
  },
]);
</script>
```

Use `data-key="id"` so the table compares rows by identifier rather than reference. Clear `selectedItems` after the bulk action completes; otherwise the checkboxes keep pointing at stale objects.

## Recipe: custom cell renderer

Two paths for custom cells. The `#body` slot on `VcColumn` overrides just the cell value while keeping the column's sort, filter, and width behavior. A full column override drops the column from the auto-generated layout and replaces it end to end. Reach for `#body` first.

```vue title="Slot a custom badge into one cell"
<VcColumn
  id="status"
  :title="$t('ORDERS.LIST.STATUS')"
  :sortable="true"
  type="status"
>
  <template #body="{ data }">
    <OrderStatusBadge :status="data.status" />
  </template>
</VcColumn>
```

The slot props are `{ data, field, index }`. Use the full column type (`type="status"`, `type="money"`, `type="date-ago"`) when one of the built-in formatters fits; only slot a `#body` when the row needs a component the formatter cannot produce.

!!! tip
    For inline edit cells, slot `#editor` instead of `#body`. The `editorCallback` it receives commits the edited value back to the row.

## Recipe: state persistence

Pass `state-key` and `VcDataTable` persists column widths, order, sort, filters, and visibility under that key. Use one key per logical table; the persistence layer namespaces it automatically.

```vue title="Persist table state"
<VcDataTable
  :items="items"
  state-key="ORDERS"
  state-storage="local"
  :column-switcher="true"
>
  <VcColumn id="number" :sortable="true" />
  <VcColumn id="customerName" :sortable="true" />
  <VcColumn id="total" type="money" :sortable="true" />
</VcDataTable>
```

`state-storage` defaults to `"local"` (survives reload) and accepts `"session"` for tab-scoped state. Keep `state-key` stable across releases. Renaming it discards every user's saved column layout.

![Readmore](../../concepts/state-persistence.md){: width="25"} State persistence in depth.

## Variations

| Variation | Change |
| --- | --- |
| Hide pagination. | Omit the `pagination` prop. |
| Server-side filtering. | Merge filter values into the search query, like `sort`. |
| Highlight the active row. | Bind `v-model:active-item-id` to the selected record ID. |
| Fixed scroll height. | `:scrollable="true"` plus `scroll-height="400px"`. |
| Infinite scroll instead of pages. | `:infinite-scroll="true"` and listen to `@load-more`. |
| Empty state with a call to action. | `:empty-state="{ icon, title, actionLabel, actionHandler }"`. |
| Column visibility toggle. | `:column-switcher="true"` (or `"defined"` to limit to declared columns). |

![Readmore](../../components/data-display/vc-data-table.md){: width="25"} VcDataTable full prop and event reference.

![Readmore](../../concepts/api-clients.md){: width="25"} API clients and the `useApiClient` contract.
