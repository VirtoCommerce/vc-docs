# Blades

Recipes for the five blade shapes you actually build: list, details, wizard, confirmation, and decorated. Each recipe is lifted from the vendor-portal source and trimmed to the load-bearing lines.

## Prerequisites

Before working with blades, make sure you have:

- A VC-Shell app scaffolded and running. See [Create your app](../../getting-started/create-your-app.md).
- Familiarity with `defineBlade` and `useBlade`. See [Blade navigation in depth](../../concepts/blade-navigation.md).
- An API client generated for the resource you list or edit. See [API clients](../../concepts/api-clients.md).

## Recipe: list blade with VcDataTable

A list blade declares `isWorkspace: true`, loads a page of data through `useApiClient` and `useAsync`, drives `VcDataTable` with `useDataTablePagination`, and opens a child details blade on row click. The composable owns the API call and pagination state; the page owns table layout and toolbar.

```ts title="composables/useOrdersList.ts"
import { useAsync, useApiClient, useDataTablePagination } from "@vc-shell/framework";
import { VcmpSellerOrdersClient, type SearchOrdersQuery } from "../../../api_client/virtocommerce.marketplacevendor";

export function useOrdersList(options?: { pageSize?: number }) {
  const { getApiClient } = useApiClient(VcmpSellerOrdersClient);
  const pageSize = options?.pageSize ?? 20;
  const searchQuery = ref<SearchOrdersQuery>({ take: pageSize });
  const searchResult = ref<CustomerOrderSearchResult>();

  const { action: loadOrders, loading } = useAsync<SearchOrdersQuery>(async (query) => {
    searchQuery.value = { ...searchQuery.value, ...(query || {}) };
    searchResult.value = await (await getApiClient()).searchOrders(searchQuery.value);
  });

  const pagination = useDataTablePagination({
    pageSize,
    totalCount: computed(() => searchResult.value?.totalCount ?? 0),
    onPageChange: ({ skip }) => loadOrders({ ...searchQuery.value, skip }),
  });

  return { items: computed(() => searchResult.value?.results ?? []), pagination, loading, loadOrders };
}
```

```vue title="pages/orders-list.vue"
<template>
  <VcBlade :title="$t('ORDERS.PAGES.LIST.TITLE')" :toolbar-items="bladeToolbar" width="30%">
    <VcDataTable
      v-model:active-item-id="selectedItemId"
      :loading="loading"
      :items="items"
      :pagination="pagination"
      :total-count="pagination.totalCount"
      state-key="ORDERS"
      @row-click="onItemClick"
      @pagination-click="pagination.goToPage"
    >
      <VcColumn id="number" :title="$t('ORDERS.LIST.NUMBER')" :sortable="true" />
      <VcColumn id="customerName" :title="$t('ORDERS.LIST.CUSTOMER')" />
      <VcColumn id="total" :title="$t('ORDERS.LIST.TOTAL')" type="money" />
      <VcColumn id="status" :title="$t('ORDERS.LIST.STATUS')" type="status" />
    </VcDataTable>
  </VcBlade>
</template>

<script setup lang="ts">
defineBlade({ name: "Orders", url: "/orders", isWorkspace: true });

const { openBlade } = useBlade();
const { items, pagination, loadOrders, loading } = useOrdersList({ pageSize: 20 });
const selectedItemId = ref<string>();

onMounted(() => loadOrders());

async function onItemClick(event: { data: CustomerOrder }) {
  await openBlade({ name: "OrderDetails", param: event.data.id, options: { item: event.data } });
}
</script>
```

The workspace flag pins the blade to the sidebar; child blades open to its right.

![Readmore](../../components/data-display/vc-data-table.md){: width="25"} VcDataTable reference.

## Recipe: details blade with form

A details blade receives `param` (the record ID) from `useBlade`, loads the record on mount, and exposes save and cancel through `toolbar-items`. After a successful save, call `callParent("reload")` to refresh the list, then `closeSelf()` if the flow ends. The list blade exposes `reload` via `exposeToChildren`.

```vue title="pages/order-details.vue"
<template>
  <VcBlade :loading="loading" :title="title" :toolbar-items="bladeToolbar" width="70%">
    <VcForm class="tw-space-y-4">
      <VcField :label="$t('ORDER.NUMBER')" :model-value="item?.number" type="text" />
      <VcField :label="$t('ORDER.STATUS')" :model-value="item?.status" type="text" />
    </VcForm>
  </VcBlade>
</template>

<script setup lang="ts">
defineBlade({ name: "OrderDetails", url: "/order" });

const { param, options, callParent, closeSelf } = useBlade<{ item?: CustomerOrder }>();
const { item, loading, loadOrder, saveOrder } = useOrderDetails();

const bladeToolbar = computed<IBladeToolbar[]>(() => [
  {
    id: "save",
    title: t("ORDER.SAVE"),
    icon: "lucide-save",
    async clickHandler() {
      await saveOrder(item.value);
      callParent("reload");
      closeSelf();
    },
  },
]);

onMounted(async () => {
  if (param.value) await loadOrder(param.value);
  else if (options.value?.item) item.value = options.value.item;
});
</script>
```

`useBlade` is generic over the `options` payload, so `options.value.item` is typed. The list blade can preload data into the child to avoid a round trip.

![Readmore](../../composables/blade-navigation/useBlade.md){: width="25"} useBlade API reference.

## Recipe: blade widgets with useBladeWidgets

Blade widgets are sidebar entries scoped to a single blade: counters, status indicators, related-entity launchers. They share the blade's lifetime and disappear when it closes. This is distinct from dashboard widgets, registered globally with `registerDashboardWidget` and rendered on the home Dashboard.

The preferred API is `useBladeWidgets`, which takes an array of headless declarations and registers and unregisters them with the blade. No `VcWidget` markup is needed; the framework renders entries automatically.

```vue title="pages/order-details.vue"
<script setup lang="ts">
import { useBlade, useBladeWidgets } from "@vc-shell/framework";

const offersCount = ref(0);

async function reloadOffers() {
  const result = await offersApi.search({ orderId: item.value?.id });
  offersCount.value = result.totalCount;
}

const { refresh, refreshAll } = useBladeWidgets([
  {
    id: "OffersWidget",
    icon: "lucide-tag",
    title: "ORDER.WIDGETS.OFFERS",
    badge: offersCount,
    isVisible: computed(() => !!item.value?.id),
    onClick: () => openBlade({ name: "OffersList" }),
    onRefresh: reloadOffers,
  },
]);

async function save() {
  await saveOrder(item.value);
  refreshAll();
}
</script>
```

Each declaration carries an `icon`, `title`, optional reactive `badge` and `isVisible`, plus `onClick` and `onRefresh` callbacks. Call `refreshAll()` after a save to recompute every widget's data, or `refresh(id)` for one. Widgets without `onRefresh` are skipped silently.

To add a full-component widget from another module, register at module load with `registerExternalWidget`, then call `useWidgetTrigger` inside the widget to expose its refresh handler, and `injectBladeContext` to read the host blade's reactive item.

```ts title="src/modules/shipping/index.ts"
import { registerExternalWidget } from "@vc-shell/framework";
import { markRaw } from "vue";
import ShippingTracker from "./widgets/ShippingTracker.vue";

registerExternalWidget({
  id: "ShippingTracker",
  component: markRaw(ShippingTracker),
  targetBlades: ["OrderDetails"],
  isVisible: (blade) => !!blade?.param,
});
```

The low-level `useWidgets` service and singular `registerWidget` exist for framework infrastructure and rarely appear in app code.

![Readmore](../../composables/blade-navigation/useBladeWidgets.md){: width="25"} useBladeWidgets reference.

![Readmore](../../composables/services/useWidgets.md){: width="25"} useWidgets service reference.

## Recipe: wizard blade

A wizard chains blades. Step one collects input and opens step two with `openBlade`, passing data through `options`. Step two reads `options`, lets the user refine, then either steps forward or calls `closeSelf` to return to step one. The final step submits, then calls `closeChildren` from the root to dismiss every step at once.

```ts title="Step 1 → Step 2"
const { openBlade } = useBlade();

async function next() {
  await openBlade({
    name: "ImportPreview",
    options: { file: selectedFile.value, mappings: mappings.value },
  });
}
```

```ts title="Step 2 reads options, submits, closes the chain"
const { options, closeSelf, callParent } = useBlade<{
  file: File;
  mappings: Record<string, string>;
}>();

async function back() {
  closeSelf();
}

async function submit() {
  await importApi.run(options.value!.file, options.value!.mappings);
  callParent("closeChildren");
}
```

The root blade exposes `closeChildren` (from `useBlade`) through `exposeToChildren`, so any descendant can collapse the whole branch in one call.

## Recipe: confirmation

For yes-or-no questions, use `usePopup().showConfirmation`, not a blade. Confirmations are modal interruptions, not navigable state; opening a blade for "Are you sure?" adds a sidebar entry the user must dismiss and breaks back-button intuition. Always await the result.

```ts title="Confirm before delete"
const { showConfirmation } = usePopup();

async function remove(ids: string[]) {
  const ok = await showConfirmation(t("ORDERS.ALERTS.DELETE_CONFIRMATION", { count: ids.length }));
  if (!ok) return;
  await removeItems({ ids });
  await reload();
}
```

The signature is `showConfirmation(message: string | Ref<string>): Promise<boolean>`. Reach for a full blade only when the confirmation needs structured input, multi-step review, or its own URL.

![Readmore](../../composables/notifications/usePopup.md){: width="25"} usePopup reference.

## Recipe: custom toolbar, banner, skeleton

Three knobs decorate a blade: `toolbar-items` for actions, `addBanner` for inline alerts, and the `loading` prop for skeleton placeholders. Toolbar items are static or computed arrays; banners are dynamic and tied to the blade's lifetime; skeleton is a single boolean.

```vue title="Banner + skeleton + toolbar"
<template>
  <VcBlade :title="title" :loading="loading" :toolbar-items="bladeToolbar" width="50%">
    <!-- body renders only after loading flips to false -->
  </VcBlade>
</template>

<script setup lang="ts">
const { addBanner, removeBanner } = useBlade();

onMounted(() => {
  if (item.value?.isReadOnly) {
    addBanner({ variant: "info", message: t("ORDER.READ_ONLY_BANNER") });
  }
});

const bladeToolbar = computed<IBladeToolbar[]>(() => [
  { id: "refresh", title: t("REFRESH"), icon: "lucide-refresh-cw", clickHandler: reload },
]);
</script>
```

`addBanner` accepts `variant: "danger" | "warning" | "info" | "success"` plus `message`, and returns an ID you can pass to `removeBanner`. The `loading` prop renders skeleton placeholders for header, toolbar, and content zones; toggle it off when initial data arrives.

## Variations

| Variation | Change |
| --- | --- |
| Full-width workspace. | `width="100%"` on `VcBlade`. |
| Read-only mode. | Filter `toolbar-items` to hide write actions and set form fields to `:readonly`. |
| Sticky header actions. | Render buttons inside the `actions` slot of `VcBlade`. |
| Custom loading state. | Drive the `loading` prop yourself and hide body content with `v-if` while it is true. |

![Readmore](../../concepts/blade-navigation.md){: width="25"} Blade navigation in depth.

![Readmore](../../components/layout/vc-blade.md){: width="25"} VcBlade component reference.
