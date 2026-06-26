# Data

Recipes for the data layer behind a list blade: pagination, sorting, filtering, selection, custom cell rendering, and persisted table state.

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
import { OrdersClient, type OrderSearchCriteria, type OrderSearchResult } from "../../../api_client/orders";

export function useOrdersList(options?: { pageSize?: number; sort?: string }) {
  const { getApiClient } = useApiClient(OrdersClient);
  const pageSize = options?.pageSize ?? 20;

  const searchQuery = ref<OrderSearchCriteria>({ take: pageSize, sort: options?.sort });
  const searchResult = ref<OrderSearchResult>();

  const { action: loadOrders, loading } = useAsync<OrderSearchCriteria>(async (query) => {
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

- [useDataTablePagination API reference.](../../composables/data/useDataTablePagination.md)

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

`useDataTableSort` tracks the current sort field and direction, and exposes a `sortExpression` ref like `"createdDate:DESC"` ready to send to the API. `VcDataTable` reports sort changes through `v-model:sort-field` and `v-model:sort-order`; bind both to the composable's refs, then watch `sortExpression` and reload.

```ts title="Sort wiring"
import { useDataTableSort } from "@vc-shell/framework";

const { sortField, sortOrder, sortExpression } = useDataTableSort({
  initialField: "createdDate",
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

- [useDataTableSort API reference.](../../composables/data/useDataTableSort.md)

## Recipe: row selection and bulk actions

Set `selection-mode="multiple"` to render a checkbox column, bind `v-model:selection` to an array ref, and drive toolbar item state from the selected IDs. For server-paginated tables, also bind `v-model:select-all-active` and `:select-all="true"` so the user can select every record across all pages with a single click — the table fires `@select-all` and your bulk command sends an "all" flag instead of an ID list.

```vue title="Bulk delete with select-all across pages"
<template>
  <VcBlade :title="title" :toolbar-items="bladeToolbar" width="50%">
    <VcDataTable
      v-model:selection="selectedItems"
      v-model:select-all-active="allSelected"
      selection-mode="multiple"
      :select-all="true"
      :items="items"
      data-key="id"
      @select-all="allSelected = true"
    >
      <VcColumn id="name" :title="$t('LIST.NAME')" />
      <VcColumn id="price" :title="$t('LIST.PRICE')" type="money" />
    </VcDataTable>
  </VcBlade>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";

const selectedItems = ref<Item[]>([]);
const allSelected = ref(false);
const selectedIds = computed(() => selectedItems.value.map((i) => i.id).filter(Boolean));

const bladeToolbar = ref<IBladeToolbar[]>([
  {
    id: "remove",
    icon: "lucide-trash-2",
    title: computed(() => t("LIST.TOOLBAR.REMOVE")),
    disabled: computed(() => selectedIds.value.length === 0 && !allSelected.value),
    async clickHandler() {
      await removeItems({
        all: allSelected.value,
        ids: allSelected.value ? [] : selectedIds.value,
      });
      selectedItems.value = [];
      allSelected.value = false;
    },
  },
]);
</script>
```

Use `data-key="id"` so the table compares rows by identifier rather than reference. The `all: true` flag on the bulk command tells the API "delete every record matching the current filter" rather than enumerating IDs — much smaller payload, and the server applies the same access scope it would on a single delete. Clear `selectedItems` and `allSelected` after the bulk action completes.

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

## Recipe: file download from a binary endpoint

Generated clients expose binary endpoints (PDF invoices, ZIP exports, CSV reports) as methods that return `FileResponse`: a small wrapper around a `Blob` plus a suggested file name. The browser does not download the file on its own. Wrap the call in `useAsync` so the toolbar button shows a spinner, then trigger a download with a hidden anchor.

```ts title="composables/useOrderDetails.ts (extract)"
import { useApiClient, useAsync } from "@vc-shell/framework";
import { OrdersClient } from "../../../api_client/orders";

const { getApiClient: getOrderApiClient } = useApiClient(OrdersClient);

const { loading: pdfLoading, action: loadPdf } = useAsync(async () => {
  if (!item.value?.number) return;
  const response = await (await getOrderApiClient()).getInvoicePdf(item.value.number);

  const link = document.createElement("a");
  link.href = window.URL.createObjectURL(new Blob([response.data], { type: response.data.type }));
  link.setAttribute("download", response.fileName || `Invoice ${item.value.number}`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
});
```

`response.data` is a `Blob`; `response.fileName` comes from the `Content-Disposition` header when the Platform sets one. Fall back to a generated name when the header is absent. Bind `pdfLoading` to the toolbar button's `:loading` so the user gets feedback during large exports.

!!! tip
    Revoke the object URL with `URL.revokeObjectURL(link.href)` after a few seconds if the page stays open. Browsers hold the blob in memory until the document unloads otherwise.

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

## Recipe: persist sort, search, and pagination in the URL

The `state-key` **prop** above persists *column layout* (widths, order, visibility) to `localStorage`. To make the *view itself* — the current sort, search keyword, and page — survive a reload **and** travel in a shareable link, opt in to URL-query persistence by passing a `stateKey` **option** to the state composables. They read their initial value from the blade URL on creation and write changes back as you interact.

!!! note "Two different `state-key`s"
    The `state-key` **prop** on `VcDataTable` is column layout in `localStorage`. The `stateKey` **option** on `useDataTableSort` / `useTableSearch` / `useDataTablePagination` is view state in the URL query. They are independent stores; using the same string for both is fine and keeps things readable.

Two prerequisites:

- The blade must be **URL-addressable** — give it a `url` in `defineBlade`. For a non-routable or nested blade the query service is a no-op and nothing is persisted.
- Each `stateKey` must be **unique** among tables that can be visible at the same time (e.g. a list and a child list in the same stack), so their query params do not collide.

```ts title="pages/orders-list.vue (script)"
import { onMounted, watch } from "vue";
import { useBlade, useDataTableSort, useTableSearch, useDataTablePagination } from "@vc-shell/framework";
import { debounce } from "lodash-es";
import { useOrdersList } from "../composables/useOrdersList";

defineBlade({ name: "Orders", url: "/orders", isWorkspace: true });

const { items, loading, totalCount, loadOrders, searchQuery } = useOrdersList();

// Same stateKey across all three — one namespace per table.
const { sortField, sortOrder, sortExpression } = useDataTableSort({
  stateKey: "orders_list",
  initialField: "createdDate",
  initialDirection: "DESC",
});
const { searchValue } = useTableSearch({ stateKey: "orders_list" });
const pagination = useDataTablePagination({
  stateKey: "orders_list",
  pageSize: 20,
  totalCount,
});

// Initial load reads the values already restored from the URL.
const load = () =>
  loadOrders({
    sort: sortExpression.value,
    keyword: searchValue.value || undefined,
    skip: pagination.skip,
    take: 20,
  });

onMounted(() => load());

// A new keyword must reset to page 1 — otherwise a saved page beyond the
// filtered result set strands the reload on an empty page.
watch(searchValue, () => pagination.setPage(1));
watch([sortExpression, searchValue, () => pagination.skip], debounce(load, 300));
```

```vue title="pages/orders-list.vue (template fragment)"
<VcDataTable
  :items="items"
  :loading="loading"
  :pagination="pagination"
  :total-count="pagination.totalCount"
  :searchable="true"
  state-key="orders_list"
  v-model:sort-field="sortField"
  v-model:sort-order="sortOrder"
  v-model:search-value="searchValue"
  @pagination-click="pagination.goToPage"
>
  <VcColumn id="number" :title="$t('ORDERS.LIST.NUMBER')" :sortable="true" />
  <VcColumn id="createdDate" :title="$t('ORDERS.LIST.CREATED')" :sortable="true" type="date-ago" />
</VcDataTable>
```

The URL ends up with `?orders_list_sort=createdDate:ASC&orders_list_search=acme&orders_list_page=3`. Writes use `router.replace` (no extra history entries) and page 1 is encoded as *absent* rather than `_page=1`.

!!! warning "Always reset the page when search changes"
    `watch(searchValue, () => pagination.setPage(1))` is not optional. If the user is on page 3 and types a query that returns one page, leaving `_page=3` in the URL means the next reload requests page 3 of the filtered set — `skip` overshoots the results and the table shows an empty "nothing found" state. Resetting to page 1 drops `_page` from the URL and keeps the `(search, page)` pair consistent. The same applies to applying a filter.

### When pagination lives in the composable

If `useDataTablePagination` is created inside your list composable (so the page can drive `onPageChange`), thread the `stateKey` through as an option rather than hard-coding it — the blade still owns the key:

```ts title="composables/useOrdersList.ts (extract)"
export function useOrdersList(options?: { pageSize?: number; stateKey?: string }) {
  // ...
  const pagination = useDataTablePagination({
    stateKey: options?.stateKey,
    pageSize: options?.pageSize ?? 20,
    totalCount: computed(() => searchResult.value?.totalCount ?? 0),
    onPageChange: ({ skip }) => loadOrders({ ...searchQuery.value, skip }),
  });
  // ...
}
```

```ts title="pages/orders-list.vue"
const { items, pagination, loadOrders } = useOrdersList({ stateKey: "orders_list" });
```

Make sure the blade's **initial** load passes `skip: pagination.skip` (and `keyword`) so the restored page and keyword are actually applied on first paint — a load that ignores `skip` always shows page 1 regardless of the URL.

- [useDataTableSort API reference.](../../composables/data/useDataTableSort.md)
- [useTableSearch API reference.](../../composables/data/useTableSearch.md)
- [useDataTablePagination API reference.](../../composables/data/useDataTablePagination.md)

## Variations

| Variation | Change |
| --- | --- |
| Hide pagination. | Omit the `pagination` prop. |
| Server-side filtering. | Merge filter values into the search query, like `sort`. |
| Highlight the active row. | Bind `v-model:active-item-id` to the selected record ID. |
| Persist sort, search, and page in the URL. | Pass a `stateKey` option to the sort/search/pagination composables (see recipe above). |
| Fixed scroll height. | `:scrollable="true"` plus `scroll-height="400px"`. |
| Infinite scroll instead of pages. | `:infinite-scroll="true"` and listen to `@load-more`. |
| Empty state with a call to action. | `:empty-state="{ icon, title, actionLabel, actionHandler }"`. |
| Column visibility toggle. | `:column-switcher="true"` (or `"defined"` to limit to declared columns). |

- [VcDataTable full prop and event reference.](../../components/data-display/vc-data-table.md)

- [API clients and the `useApiClient` contract.](../../concepts/api-clients.md)
