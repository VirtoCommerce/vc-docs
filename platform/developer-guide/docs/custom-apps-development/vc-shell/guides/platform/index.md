# Platform

Recipes that connect a VC-Shell module to Virto Commerce Platform subsystems: real-time push, background jobs, notifications, asset upload, and dynamic properties. Each pattern follows what the vendor-portal modules actually do.

## Prerequisites

Before wiring a module to Platform subsystems, make sure you have:

- A VC-Shell app scaffolded and authenticated against a Platform instance. See [Connecting to Platform](../../getting-started/connecting-to-platform.md).
- A generated API client for the resource you read or write. See [API clients](../../concepts/api-clients.md).
- Familiarity with `defineAppModule` and the module registration lifecycle. See [Modules](../../concepts/modules.md).

## Recipe: SignalR for real-time updates

The SignalR plugin is installed once by the shell during bootstrap; modules never call `signalR` directly. Platform pushes `PushNotification` messages over `/pushNotificationHub`, the framework ingests them into a singleton store, and modules consume them in two ways: declaratively, by registering a notification type in `defineAppModule({ notifications })`, or imperatively from inside a blade, with `useBladeNotifications`.

```ts title="modules/products/index.ts"
import { defineAppModule } from "@vc-shell/framework";
import ProductCreatedDomainEvent from "./notifications/ProductCreatedDomainEvent.vue";

export default defineAppModule({
  blades: { ProductsListNew, ProductDetailsNew },
  locales,
  notifications: {
    ProductCreatedDomainEvent: {
      template: ProductCreatedDomainEvent,
      toast: { mode: "auto" },
    },
  },
});
```

A blade reacts to specific message types without owning the subscription:

```ts title="pages/orders-list.vue"
import { useBladeNotifications } from "@vc-shell/framework";

const { messages, unreadCount, markAsRead } = useBladeNotifications({
  types: ["OrderStatusChanged"],
  filter: (msg) => msg.creator === currentSellerId.value,
  onMessage: () => reload(),
});
```

The subscription is tied to the blade's effect scope. When the blade closes, the framework unsubscribes automatically. Module developers do not touch the raw SignalR connection.

![Readmore](../../plugins/signalr.md){: width="25"} SignalR plugin reference.

## Recipe: background jobs and Hangfire

Platform schedules long-running work (exports, imports, indexing, reindexing) through Hangfire and reports progress as `PushNotification` messages with an `isComplete` field. Subscribe to the job-specific notification type instead of polling. The toast controller has a dedicated `progress` mode that updates a single persistent toast as new messages stream in, then closes it when the job finishes.

```ts title="modules/catalog/index.ts"
notifications: {
  CatalogExportPushNotification: {
    toast: {
      mode: "progress",
      severity: (msg) => (msg.errorCount ? "error" : "info"),
      isComplete: (msg) => msg.finished === true,
    },
  },
},
```

Inside the blade that triggered the job, watch the result and refresh:

```ts title="pages/catalog-export.vue"
useBladeNotifications<ICatalogExportNotification>({
  types: ["CatalogExportPushNotification"],
  filter: (msg) => msg.jobId === currentJobId.value,
  onMessage: (msg) => {
    if (msg.finished) {
      downloadUrl.value = msg.downloadUrl;
      reload();
    }
  },
});
```

Polling with `useAsync` and `setInterval` is the fallback when SignalR is unavailable, not the default. Polling burns request budget and lags behind reality; reach for it only when the Platform endpoint refuses to emit a notification.

![Readmore](../../plugins/notifications.md){: width="25"} Notification system reference.

## Recipe: notifications subsystem

The notification subsystem has two surfaces. The first is declarative: a module's `notifications` config maps each `notifyType` to a toast mode and an optional Vue template. The second is imperative: the `notification` helper from `@vc-shell/framework` fires a one-off toast from any handler, callback, or error branch.

```ts title="pages/order-details.vue"
import { notification } from "@vc-shell/framework";

async function save() {
  try {
    await saveOrder(item.value);
    notification.success(t("ORDER.SAVED"));
    callParent("reload");
    closeSelf();
  } catch (err) {
    notification.error(t("ORDER.SAVE_FAILED"));
  }
}
```

`notification` exposes `success`, `error`, `warning`, and a default call signature. Use the declarative form for events that originate on Platform; use the imperative form for outcomes that originate in the blade. Mixing both inside the same flow is fine and common.

![Readmore](../../composables/notifications/useNotifications.md){: width="25"} useNotifications reference.

## Recipe: asset and file upload

Two organisms cover the upload surface. `VcImageUpload` handles a single image with drag-and-drop and lightbox preview; `VcGallery` handles an asset array with reorder. Both consume `ICommonAsset` shapes. The composable that owns upload mechanics is `useAssetsManager`, which wraps the lower-level `useAssets` with a two-way sync over a reactive ref.

```ts title="pages/offers-details.vue"
import { computed } from "vue";
import { useAssetsManager, usePopup } from "@vc-shell/framework";

const { showConfirmation } = usePopup();

const assets = useAssetsManager(
  computed({
    get: () => offer.value.images ?? [],
    set: (val) => {
      offer.value.images = val;
    },
  }),
  {
    uploadPath: () => `offers/${offer.value?.id ?? "new"}`,
    confirmRemove: () => showConfirmation(t("OFFERS.ALERTS.IMAGE_DELETE")),
  },
);
```

```vue title="pages/offers-details.vue"
<VcGallery
  :images="assets.items.value"
  @upload="assets.upload"
  @sort="assets.reorder"
  @remove="assets.remove"
/>
```

`uploadPath` is a function because the destination often depends on the entity's ID, which only exists after the first save. The composable evaluates it lazily on each upload. For a single avatar or logo field, wrap the value in a one-element computed array and bind to `VcImageUpload` instead.

![Readmore](../../composables/data/useAssetsManager.md){: width="25"} useAssetsManager reference.

## Recipe: dynamic properties for entities

Platform's dynamic-property system lets merchants add fields to a catalog object at runtime. `useDynamicProperties` resolves the right strategy per property type (short text, boolean, dictionary, measurement, color) and `VcDynamicProperty` renders the right control. Wire them up inside a details blade, grouping by property group ID for layout.

```vue title="components/property-group.vue"
<template>
  <VcCard
    v-for="[groupId, group] in groupEntries"
    :key="groupId"
    is-collapsable
    :header="groupHeaders[groupId]"
  >
    <VcDynamicProperty
      v-for="property in group"
      :key="property.id"
      :property="property"
      :model-value="getPropertyValue(property, currentLocale)"
      :options-getter="loadDictionaries"
      :measurements-getter="loadMeasurements"
      :current-language="currentLocale"
      :value-type="property.valueType ?? ''"
      :dictionary="property.dictionary"
      :multivalue="property.multivalue"
      :multilanguage="property.multilanguage"
      @update:model-value="(ev) => setPropertyValue({ property, ...ev })"
    />
  </VcCard>
</template>

<script setup lang="ts">
import { useApiClient, useDynamicProperties } from "@vc-shell/framework";
import { VcmpSellerCatalogClient } from "../../../api_client/virtocommerce.marketplacevendor";

const { getApiClient } = useApiClient(VcmpSellerCatalogClient);

const { getPropertyValue, setPropertyValue, loadDictionaries, loadMeasurements } =
  useDynamicProperties({
    searchDictionary: async (criteria) =>
      (await getApiClient()).searchPropertyDictionaryItems(criteria),
    searchMeasurements: async (measureId, locale) =>
      (await getApiClient()).searchMeasurements(measureId, locale),
  });
</script>
```

`setPropertyValue` mutates the property in place and cleans up empty value scaffolding, so `useBladeForm`'s deep comparison stays honest. Pass `dictionary` whenever you set a dictionary value, otherwise the composable cannot resolve `valueId` to its localized alias.

![Readmore](../../components/form/vc-dynamic-property.md){: width="25"} VcDynamicProperty component reference.

## Variations

| Variation | Approach |
| --- | --- |
| Toast on every event. | `notifications: { Event: { toast: { mode: "auto" } } }` in the module. |
| Silent storage, panel only. | `notifications: { Event: { toast: { mode: "silent" } } }`. |
| Custom template per event. | `notifications: { Event: { template: MyTemplate } }`. |
| Polling instead of SignalR. | `useAsync` plus `setInterval` in a composable; only when SignalR is unavailable. |

![Readmore](../../composables/forms/useDynamicProperties.md){: width="25"} useDynamicProperties reference.
