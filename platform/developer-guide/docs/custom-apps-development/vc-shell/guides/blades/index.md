# Blades

Recipes for the blade shapes you actually build: list, details, blade widgets, confirmation, and decorated blades.

## Prerequisites

Before working with blades, make sure you have:

- A VC-Shell app scaffolded and running. See [Generate an app from a prompt](../../getting-started/generate-app-from-prompt.md) or [Manual CLI start](../../getting-started/manual-cli-start.md).
- Familiarity with `defineBlade` and `useBlade`. See [Blade navigation in depth](../../concepts/blade-navigation.md).
- An API client generated for the resource you list or edit. See [API clients](../../concepts/api-clients.md).

## Recipe: list blade with VcDataTable

A list blade declares `isWorkspace: true`, loads a page of data through `useApiClient` and `useAsync`, drives `VcDataTable` with `useDataTablePagination`, and opens a child details blade on row click. The composable owns the API call and pagination state; the page owns table layout and toolbar.

```ts title="composables/useOrdersList.ts"
import { useAsync, useApiClient, useDataTablePagination } from "@vc-shell/framework";
import { OrdersClient, type OrderSearchCriteria, type OrderSearchResult } from "../../../api_client/orders";

export function useOrdersList(options?: { pageSize?: number }) {
  const { getApiClient } = useApiClient(OrdersClient);
  const pageSize = options?.pageSize ?? 20;
  const searchQuery = ref<OrderSearchCriteria>({ take: pageSize });
  const searchResult = ref<OrderSearchResult>();

  const { action: loadOrders, loading } = useAsync<OrderSearchCriteria>(async (query) => {
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

- [VcDataTable reference.](../../components/data-display/vc-data-table.md)

## Recipe: details blade with form

A details blade receives `param` (the record ID) from `useBlade`, loads the record on mount, and exposes save and cancel through `toolbar-items`. Wrap the data in `useBladeForm` to get the dirty-tracking, `canSave`, and close-confirmation guard wired in one call. After a successful save, call `setBaseline()` to seal the saved state, `callParent("reload")` to refresh the list, then `replaceWith` to switch from "new" to "edit" mode (or `closeSelf()` if the flow ends).

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
import { computed, ref, onMounted } from "vue";
import { useBlade, useBladeForm, type IBladeToolbar } from "@vc-shell/framework";
import { useI18n } from "vue-i18n";

defineBlade({ name: "OrderDetails", url: "/order" });

const { t } = useI18n();
const { param, options, callParent, closeSelf, replaceWith } = useBlade<{ item?: CustomerOrder }>();
const { item, loading, loadOrder, saveOrder } = useOrderDetails();

const form = useBladeForm({
  data: item,
  closeConfirmMessage: computed(() => t("ORDER.UNSAVED_CHANGES")),
});

const bladeToolbar = ref<IBladeToolbar[]>([
  {
    id: "save",
    title: computed(() => t("ORDER.SAVE")),
    icon: "lucide-save",
    disabled: computed(() => !form.canSave.value),
    async clickHandler() {
      const saved = await saveOrder(item.value);
      form.setBaseline();
      callParent("reload");
      if (!param.value && saved?.id) {
        await replaceWith({ name: "OrderDetails", param: saved.id });
      } else {
        closeSelf();
      }
    },
  },
]);

onMounted(async () => {
  if (param.value) {
    await loadOrder(param.value);
    form.setBaseline();
  } else if (options.value?.item) {
    item.value = options.value.item;
    form.markReady();
  }
});
</script>
```

`useBladeForm` watches `item` deeply and toggles `form.canSave` once the form is both modified and valid. `setBaseline()` re-snapshots after save; `markReady()` flips the form into a "modified vs setup-time snapshot" mode for new records preloaded from `options`. `replaceWith` swaps the create blade for the edit blade at the same stack position, so the URL becomes routable and refresh-safe.

`useBlade` is generic over the `options` payload, so `options.value.item` is typed. The list blade can preload data into the child to avoid a round trip.

- [useBladeForm reference.](../../composables/forms/useBladeForm.md)
- [Forms concept.](../../concepts/forms.md)

- [useBlade API reference.](../../composables/blade-navigation/useBlade.md)

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

Use `useBladeWidgets` when the widget's data comes from the host bundle: the host blade and its widget composables ship together. For widgets contributed by a **separate bundle** (a Module Federation remote, a third-party plugin), see [Recipe: inject a widget from a remote module](#recipe-inject-a-widget-from-a-remote-module) below.

- [useBladeWidgets reference.](../../composables/blade-navigation/useBladeWidgets.md)

## Recipe: counter widget linking to a filtered list

A common product-details pattern: a sidebar widget shows a live count of related entities, the user clicks it, and a filtered list blade opens. Two pieces: a small composable that owns the count, and a widget declaration that binds count to `badge` and uses `onClick` to open the linked blade with a filter in `options`.

```ts title="src/modules/products/widgets/useReviewCount.ts"
import { ref, onMounted, watch, type Ref } from "vue";
import { useApiClient, useAsync } from "@vc-shell/framework";
import { ReviewsClient } from "../../../api_client/reviews";
import type { Product } from "../../../api_client/catalog";

export function useReviewCount(item: Ref<Product | undefined>) {
  const { getApiClient } = useApiClient(ReviewsClient);
  const count = ref(0);

  const { loading, action: load } = useAsync(async () => {
    if (!item.value?.id) return;
    const client = await getApiClient();
    const result = await client.searchReviews({ productId: item.value.id });
    count.value = result.totalCount ?? 0;
  });

  onMounted(() => load());
  watch(() => item.value?.id, () => load());

  return { count, loading, refresh: load };
}
```

Register the widget through `useBladeWidgets`; bind `badge` to the count ref so it updates reactively, and pass the parent's item in `options` so the child list opens pre-filtered:

```ts title="src/modules/products/composables/useProductWidgets.ts"
import { useBlade, useBladeWidgets } from "@vc-shell/framework";
import type { Ref, ComputedRef } from "vue";
import type { Product } from "../../../api_client/catalog";
import { useReviewCount } from "../widgets/useReviewCount";

interface Options {
  item: Ref<Product | undefined>;
  isVisible: ComputedRef<boolean>;
}

export function useProductWidgets({ item, isVisible }: Options) {
  const { openBlade } = useBlade();
  const { count: reviewsCount, loading, refresh } = useReviewCount(item);

  return useBladeWidgets([
    {
      id: "ReviewsWidget",
      icon: "lucide-message-square",
      title: "PRODUCTS.PAGES.DETAILS.WIDGETS.REVIEWS",
      badge: reviewsCount,
      loading,
      isVisible,
      onClick: () =>
        openBlade({
          name: "ReviewsList",
          options: { productId: item.value?.id },
        }),
      onRefresh: refresh,
    },
  ]);
}
```

On the receiving side, the `ReviewsList` blade reads `options.productId` from `useBlade()` and applies it as the initial filter on the table. The badge stays in sync because the count composable watches the parent item id and refetches when it changes.

- [useBladeWidgets reference.](../../composables/blade-navigation/useBladeWidgets.md)
- [useBlade reference.](../../composables/blade-navigation/useBlade.md)

## Recipe: inject a widget from a remote module

When a widget ships in a **separate bundle** — a Module Federation remote, an npm-published plugin, a partner integration — the host blade has no compile-time knowledge of it. Use this recipe when the widget code and the blade code do not live in the same `src/` tree. For widgets that ship in the same bundle as the blade, prefer [useBladeWidgets](#recipe-blade-widgets-with-usebladewidgets) above.

The contributing module registers a full Vue component against a list of target blade names through `registerExternalWidget`. The framework then renders the component in the sidebar of any matching blade, with no change required on the host side.

```ts title="src/index.ts (remote MF module)"
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

`targetBlades` is the global blade-name list this widget attaches to. `isVisible` runs against the live blade state, so the widget can hide itself for the "create" flow and appear only after the entity has an id. `markRaw` keeps the component definition out of Vue's reactivity system.

Inside the widget component, call `useWidgetTrigger` to publish a refresh handler the host can invoke from `refreshAll`:

```vue title="ShippingTracker.vue"
<script setup lang="ts">
import { useWidgetTrigger } from "@vc-shell/framework";

const status = ref<string>();

async function load() {
  status.value = await shippingClient.getStatus(orderId.value);
}

useWidgetTrigger({ id: "ShippingTracker", onRefresh: load });
</script>
```

The host blade does not know the widget exists at build time, so there is no `useBladeWidgets` call wiring it. The framework discovers external widgets through the registry and renders them automatically. Use this pattern for any contribution that crosses a bundle boundary.

- [useWidgets service reference.](../../composables/services/useWidgets.md)
- [Module Federation concept.](../../concepts/module-federation.md)

## Recipe: confirmation

For yes-or-no questions, use `usePopup().showConfirmation`, not a blade. Confirmations are modal interruptions, not navigable state; opening a blade for "Are you sure?" adds a sidebar entry the user must dismiss. Always await the result.

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

- [usePopup reference.](../../composables/notifications/usePopup.md)

## Recipe: blade banners

For information the user should see above the form — a read-only notice, a missing-prerequisite warning, a "saved" confirmation — render a `<VcBanner>` inline in the blade body. Static or condition-driven banners belong in the template; the blade lifecycle does not have to know about them.

```vue title="Inline banner driven by state"
<template>
  <VcBlade :title="title" :toolbar-items="bladeToolbar" width="50%">
    <VcBanner
      v-if="item?.isReadOnly"
      variant="info"
    >
      {{ $t("ORDER.READ_ONLY_BANNER") }}
    </VcBanner>

    <VcBanner
      v-if="hasIncompleteShipping"
      variant="warning"
    >
      {{ $t("ORDER.SHIPPING_INCOMPLETE") }}
    </VcBanner>

    <!-- form body -->
  </VcBlade>
</template>
```

For banners that appear in response to a runtime event (a long-running job completed, a partial save succeeded), use the imperative `addBanner` from `useBlade()`. The call returns an ID you can later pass to `removeBanner` to dismiss the entry.

```vue title="Dynamic banner via addBanner"
<script setup lang="ts">
import { useBlade } from "@vc-shell/framework";

const { addBanner, removeBanner } = useBlade();

let pendingBannerId: string | undefined;

async function runImport() {
  pendingBannerId = addBanner({
    variant: "info",
    message: t("IMPORT.IN_PROGRESS"),
  });
  try {
    await importFile();
    if (pendingBannerId) removeBanner(pendingBannerId);
    addBanner({ variant: "success", message: t("IMPORT.DONE") });
  } catch {
    if (pendingBannerId) removeBanner(pendingBannerId);
    addBanner({ variant: "danger", message: t("IMPORT.FAILED") });
  }
}
</script>
```

Variants are `info`, `success`, `warning`, `danger`. Inline `<VcBanner v-if>` covers most cases; reach for `addBanner` only when the banner's lifecycle is not naturally expressible as a reactive condition.

- [VcBanner reference.](../../components/feedback/vc-banner.md)
- [useBlade reference — banner methods.](../../composables/blade-navigation/useBlade.md)

## Recipe: skeleton loading state

While the initial data is still in flight, set `:loading="true"` on `VcBlade`. The framework renders skeleton placeholders for the header, toolbar, and content zones, so the blade looks structurally complete from the moment it opens.

```vue title="Skeleton during initial load"
<template>
  <VcBlade :title="title" :loading="loading" :toolbar-items="bladeToolbar" width="50%">
    <VcForm><!-- ... --></VcForm>
  </VcBlade>
</template>

<script setup lang="ts">
const { item, loading, loadItem } = useOrderDetails();

onMounted(async () => {
  if (param.value) await loadItem({ id: param.value });
});
</script>
```

Drive `loading` from your data composable. When the data composable aggregates several requests with `useLoading(a, b, c)`, the blade stays in skeleton until all of them complete. After the initial load, leave `loading` at `false` even for subsequent refetches — replacing the body with skeleton on every refresh makes the blade feel laggy. Use a toolbar spinner or the row-level loading state on `VcDataTable` for incremental updates instead.

- [VcBlade reference.](../../components/layout/vc-blade.md)
- [useLoading reference.](../../composables/ui-state/useLoading.md)

## Recipe: attach assets to a details blade

Entities with attached files — product images, downloadable resources, document scans — bind their asset array through `useAssetsManager`. The composable wraps upload, remove, and reorder against a writable computed bound to the entity. There are two presentation shapes:

- **Inline gallery** when assets are a primary part of the entity (product images shown on the details blade itself).
- **AssetsWidget** when assets are a secondary concern. The widget shows a count badge in the blade's right rail and opens the framework's built-in `AssetsManager` blade on click.

The framework ships the `AssetsManager` blade pre-registered via `AssetsManagerModule` — you do not declare it; you just `openBlade({ name: "AssetsManager", options: { manager, disabled } })`.

### Inline gallery on the blade

```vue title="pages/product-details.vue"
<script setup lang="ts">
import { computed } from "vue";
import { useBlade, useAssetsManager, usePopup } from "@vc-shell/framework";

const { openBlade } = useBlade();
const { showConfirmation } = usePopup();
const { item } = useProductDetails();

const images = computed({
  get: () => item.value?.images ?? [],
  set: (next) => {
    if (item.value) item.value.images = next;
  },
});

const gallery = useAssetsManager(images, {
  uploadPath: () => `/catalog/${item.value?.id}`,
  confirmRemove: () => showConfirmation("Delete the selected images?"),
});

function onEditAsset(asset: AssetLike) {
  openBlade({
    name: "AssetsDetails",
    options: {
      asset,
      assetEditHandler: gallery.updateItem,
      assetRemoveHandler: gallery.remove,
    },
  });
}
</script>

<template>
  <VcBlade title="Product">
    <VcCard header="Images">
      <VcGallery
        :images="images"
        :loading="gallery.loading.value"
        @upload="gallery.upload"
        @remove="gallery.remove"
        @sort="gallery.reorder"
        @edit="onEditAsset"
      />
    </VcCard>
  </VcBlade>
</template>
```

The writable computed is the contract: getter reads `item.value.images`, setter writes back. `useAssetsManager` mutates the array through that channel, so `useModificationTracker` (via `useBladeForm`) sees the change as a real edit and lights the unsaved-changes guard.

### AssetsWidget that opens the built-in manager

When assets are not the main attraction, expose them as a sidebar widget. The badge surfaces the asset count; clicking the widget pushes the framework's `AssetsManager` blade onto the stack.

```ts title="widgets/use-product-widgets.ts"
import { computed, markRaw, type ComputedRef, type Ref } from "vue";
import { useBlade, useBladeWidgets, useAssetsManager, usePopup } from "@vc-shell/framework";

export function useProductWidgets(opts: {
  item: Ref<Product | undefined>;
  disabled: ComputedRef<boolean>;
  isVisible: ComputedRef<boolean>;
}) {
  const { openBlade } = useBlade();
  const { showConfirmation } = usePopup();

  const files = computed({
    get: () => opts.item.value?.files ?? [],
    set: (next) => {
      if (opts.item.value) opts.item.value.files = next;
    },
  });

  const manager = useAssetsManager(files, {
    uploadPath: () => `/files/${opts.item.value?.id}`,
    confirmRemove: () => showConfirmation("Delete selected files?"),
  });

  return useBladeWidgets([
    {
      id: "ProductFilesWidget",
      icon: "lucide-paperclip",
      title: "PRODUCTS.WIDGETS.FILES",
      badge: computed(() => opts.item.value?.files?.length ?? 0),
      isVisible: opts.isVisible,
      onClick: () =>
        openBlade({
          name: "AssetsManager",
          options: {
            manager: markRaw(manager),
            disabled: opts.disabled.value,
          },
        }),
    },
  ]);
}
```

`markRaw(manager)` is required: without it Vue makes the entire manager deeply reactive, which both fails type contracts and pessimizes upload performance. The widget composable runs once during the details blade's `setup`, with `isVisible` set to `false` while the user is still on the "create" form so the widget does not flash empty before the entity has an id.

A single blade can host both shapes. Each call to `useAssetsManager` operates on its own writable computed, so an inline gallery for product images and an AssetsWidget for downloadable files coexist without interfering — they bind to different fields on the same entity.

- [VcGallery reference.](../../components/data-display/vc-gallery.md)
- [useAssetsManager reference.](../../composables/data/useAssetsManager.md)
- [useBladeWidgets reference.](../../composables/blade-navigation/useBladeWidgets.md)

## Variations

| Variation | Change |
| --- | --- |
| Full-width workspace. | `width="100%"` on `VcBlade`. |
| Read-only mode. | Filter `toolbar-items` to hide write actions and set form fields to `:readonly`. |
| Sticky header actions. | Render buttons inside the `actions` slot of `VcBlade`. |
| Custom loading state. | Drive the `loading` prop yourself and hide body content with `v-if` while it is true. |

- [Blade navigation in depth.](../../concepts/blade-navigation.md)

- [VcBlade component reference.](../../components/layout/vc-blade.md)
