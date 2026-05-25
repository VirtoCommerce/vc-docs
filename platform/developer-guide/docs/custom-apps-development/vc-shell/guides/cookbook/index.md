# Cookbook

Quick recipes for everyday VC-Shell tasks. Each one is self-contained, so read the recipe you need and ignore the rest.

Every snippet below focuses on one framework pattern and uses neutral module names. Composable names, options, and return shapes follow the current VC-Shell APIs.

## Show a confirmation before closing a blade

For details blades — the common case — let `useBladeForm` wire the guard for you. Pass `closeConfirmMessage` and the framework handles both the in-app close and the browser tab unload, both reading the form's dirty state.

```vue title="OrderDetails.vue"
<script setup lang="ts">
import { computed } from "vue";
import { useBladeForm } from "@vc-shell/framework";
import { useI18n } from "vue-i18n";

const { t } = useI18n();
const { item, loadItem, saveItem } = useOrderDetails();

const form = useBladeForm({
  data: item,
  closeConfirmMessage: computed(() => t("ORDER.UNSAVED_CHANGES")),
});
</script>
```

That is the whole recipe for a form blade. The popup, the tab-close prompt, and the dirty tracking all hang off `useBladeForm`.

For a blade with unsaved state outside a form — a kanban board, a wizard with custom state, an editor not backed by `useBladeForm` — fall back to the lower-level guard. Register `onBeforeClose` and return `true` to block, `false` to proceed:

```vue title="KanbanBoard.vue"
<script setup lang="ts">
import { ref } from "vue";
import { useBlade, usePopup } from "@vc-shell/framework";

const { onBeforeClose } = useBlade();
const { showConfirmation } = usePopup();
const hasPendingMoves = ref(false);

onBeforeClose(async () => {
  if (!hasPendingMoves.value) return false;
  const confirmed = await showConfirmation("Discard pending moves?");
  return !confirmed;
});
</script>
```

The guard returns `true` to **prevent** closure and `false` to **allow** it. Always negate the user's confirmation.

- [useBladeForm reference.](../../composables/forms/useBladeForm.md)
- [Full `useBlade` API and guard semantics.](../../composables/blade-navigation/useBlade.md)

## Warn before browser tab close (useBeforeUnload)

For form blades, you do not need to wire this yourself. `useBladeForm` registers `useBeforeUnload(isModified)` automatically (set `autoBeforeUnload: false` if you ever need to turn it off). Recipe above already covers the typical case.

Reach for `useBeforeUnload` directly only when the unsaved state lives **outside** a form — a kanban board, a wizard, a custom editor not backed by `useBladeForm`. Pair it with `onBeforeClose` so the user is protected whether they close the blade or the whole tab:

```vue title="src/modules/orders/pages/board.vue"
<script setup lang="ts">
import { ref } from "vue";
import { useBeforeUnload, useBlade, usePopup } from "@vc-shell/framework";

const hasPendingMoves = ref(false);

useBeforeUnload(hasPendingMoves);

const { onBeforeClose } = useBlade();
const { showConfirmation } = usePopup();

onBeforeClose(async () => {
  if (!hasPendingMoves.value) return false;
  return !(await showConfirmation("Discard pending moves?"));
});
</script>
```

The composable always uses the browser's native dialog. The wording is fixed by the browser and cannot be customized, which is a deliberate antiphishing restriction. Reset whatever drives the modified flag after a successful save, otherwise the prompt keeps appearing.

- [`useBeforeUnload` reference.](../../composables/utilities/useBeforeUnload.md)

## Pass selected rows from a list to a details blade

Use `param` for the entity id. Use `options` for richer preloaded data that should stay runtime-only and should not be encoded in the URL.

```vue title="orders-list.vue"
<script setup lang="ts">
import { useBlade } from "@vc-shell/framework";

const { openBlade } = useBlade();

async function onItemClick(event: { data: CustomerOrder }) {
  const item = event.data;
  await openBlade({
    name: "OrderDetails",
    param: item.id,
    options: { item },
  });
}
</script>
```

On the child blade, type the options with a generic so you skip manual casting.

```vue title="order-details.vue"
<script setup lang="ts">
import { useBlade } from "@vc-shell/framework";

interface OrderOptions {
  item?: CustomerOrder;
}

const { param, options } = useBlade<OrderOptions>();
const preloaded = options.value?.item; // typed as CustomerOrder | undefined
</script>
```

## Refresh a list after a modification in a child blade

The parent exposes a `reload` method through `exposeToChildren`. The child invokes it via `callParent` after a successful save.

```vue title="orders-list.vue (parent)"
<script setup lang="ts">
const { exposeToChildren } = useBlade();
const { loadOrders, searchQuery } = useOrdersListNew();

async function reload() {
  await loadOrders(searchQuery.value);
}

exposeToChildren({ reload });
</script>
```

```vue title="order-details.vue (child)"
<script setup lang="ts">
const { callParent, closeSelf } = useBlade();

async function onSave() {
  await saveOrder();
  await callParent("reload");
  await closeSelf();
}
</script>
```

The child blade does not import the parent. The messaging system routes the call by name through the blade stack.

## Gate a workspace blade with a permission

Declare required permissions on the blade itself. The menu service hides the menu item and the blade refuses to open for users without access.

```vue title="orders-list.vue"
<script setup lang="ts">
defineBlade({
  name: "Orders",
  url: "/orders",
  isWorkspace: true,
  permissions: ["orders:order:view"],
  menuItem: {
    title: "ORDERS.MENU.TITLE",
    icon: "lucide-shopping-cart",
    priority: 1,
  },
});
</script>
```

For finer-grained checks inside a blade, use `usePermissions().hasAccess(...)` to toggle individual toolbar buttons or sections.

- [How permissions flow from the Platform to the UI.](../../concepts/permissions-model.md)

## Open a blade from a dashboard widget

Outside a blade context, only `openBlade` is available. The other methods (`closeSelf`, `callParent`, `onBeforeClose`) throw at runtime, so do not destructure them.

```vue title="OrdersDashboardCard.vue"
<script setup lang="ts">
import { useBlade } from "@vc-shell/framework";

const { openBlade } = useBlade();

function goToOrders() {
  openBlade({ name: "Orders", isWorkspace: true });
}

function viewOrder(id: string) {
  openBlade({ name: "OrderDetails", param: id });
}
</script>
```

Pass `isWorkspace: true` to replace the whole stack with the target workspace, which is the right choice for top-level navigation.

## Add a toolbar button conditionally

A blade declares its toolbar as a `ref<IBladeToolbar[]>([...])` and passes it to `<VcBlade :toolbar-items>`. The framework filters items by `permissions` and `isVisible` before render, and re-reads reactive fields whenever they change, so visibility and disabled state follow the form state automatically.

```vue title="ItemDetails.vue"
<script setup lang="ts">
import { computed, ref } from "vue";
import { useAsync, VcBlade, type IBladeToolbar } from "@vc-shell/framework";

const hasChanges = computed(() => form.isDirty);

const { loading: saving, action: save } = useAsync(async () => {
  await saveItem();
});

const bladeToolbar = ref<IBladeToolbar[]>([
  {
    id: "save",
    title: "Save",
    icon: "lucide-save",
    clickHandler: () => save(),
    isVisible: hasChanges,
    disabled: computed(() => saving.value),
  },
]);
</script>

<template>
  <VcBlade :toolbar-items="bladeToolbar" />
</template>
```

The button appears only while the form is dirty and becomes disabled mid-save — both are reactive without any `watch` or `updateToolbarItem` plumbing.

## Combine loading flags from several sources

`useAsync().loading` is one flag per action. When a blade depends on several async sources, OR them into a single flag with `useLoading(...refs)` and bind that to `VcBlade`'s `:loading` prop.

```vue title="order-details.vue"
<script setup lang="ts">
import { useAsync, useLoading } from "@vc-shell/framework";

const { loading: orderLoading, action: loadOrder } = useAsync(fetchOrder);
const { loading: customerLoading, action: loadCustomer } = useAsync(fetchCustomer);
const { loading: lineItemsLoading, action: loadLineItems } = useAsync(fetchLineItems);

const isLoading = useLoading(orderLoading, customerLoading, lineItemsLoading);
</script>
```

The result is `true` while any input ref is `true`. Use it for the blade overlay; keep the per-action refs for granular UI, such as a spinner inside one button.

- [`useLoading` reference.](../../composables/ui-state/useLoading.md)

## Set a dynamic blade title

The `VcBlade` shell takes a `:title` prop directly. Bind it to a `computed` and the header re-renders as the underlying entity changes.

```vue title="order-details.vue"
<template>
  <VcBlade
    :title="bladeTitle"
    :loading="loading"
    width="70%"
  >
    <!-- content -->
  </VcBlade>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";

const item = ref<CustomerOrder | undefined>();
const bladeTitle = computed(() => item.value?.number ?? "New order");
</script>
```

For breadcrumbs and the blade stack, expose the same title with `defineExpose({ title: bladeTitle })` so the navigation chrome can read it.

## Show navigational breadcrumbs in a blade

Register a breadcrumb in the blade stack with `useBreadcrumbs().push`. The composable deduplicates by `id` and trims the trail automatically when the user clicks a previous breadcrumb.

```vue title="order-details.vue"
<script setup lang="ts">
import { computed, onBeforeUnmount } from "vue";
import { useBlade, useBreadcrumbs } from "@vc-shell/framework";

const { openBlade, param } = useBlade();
const { push, remove } = useBreadcrumbs();

const crumbId = `order-${param.value}`;

push({
  id: crumbId,
  title: computed(() => `Order #${order.value?.number ?? ""}`),
  clickHandler: () => openBlade({ name: "OrderDetails", param: param.value }),
});

onBeforeUnmount(() => remove([crumbId]));
</script>
```

Include the blade `param` in the breadcrumb `id` so two open instances of the same blade type do not overwrite each other. Pair every `push` with a `remove` on unmount, otherwise stale entries accumulate. To run custom logic before the trail trims, return `false` from `clickHandler`.

- [`useBreadcrumbs` reference.](../../composables/ui-state/useBreadcrumbs.md)

## Display a success toast after save

The `notification` helper is a plain singleton, so it works inside or outside a blade. Toasts render in the global container regardless of which blade triggered them.

```vue title="order-details.vue"
<script setup lang="ts">
import { notification } from "@vc-shell/framework";

async function onSave() {
  try {
    await saveOrder();
    notification.success("Order saved");
  } catch (err) {
    notification.error((err as Error).message);
  }
}
</script>
```

Use `notification.success`, `notification.error`, `notification.warning`, or the default `notification(...)` for an info-style toast. Pass `{ timeout: 5000 }` as the second argument to override the default lifetime.

The toast helper is **not** the same as push notifications. It fires in-app feedback that never reaches the bell dropdown. For real-time platform events, register the type in `defineAppModule({ notifications })` and subscribe with `useBladeNotifications`.

- [Notifications concept page — three surfaces.](../../concepts/notifications.md#three-surfaces-three-apis)
- [Notifications plugin reference — toast helper.](../../plugins/notifications.md)

## Refresh a list when a push notification arrives

When a record can change from somewhere else (another tab, a background job, a different blade), subscribe to the relevant notification type and re-fetch. The subscription is scoped to the blade — when the blade closes, it stops listening automatically.

```vue title="src/modules/offers/pages/offers-list.vue"
<script setup lang="ts">
import { useBladeNotifications } from "@vc-shell/framework";

const { loadOffers } = useOffers();

useBladeNotifications({
  types: ["OfferCreatedDomainEvent", "OfferDeletedDomainEvent"],
  onMessage: () => loadOffers(),
});
</script>
```

Pass an array of types when several events should trigger the same refresh. Use the `filter` option to narrow further — for example, only events whose `sellerId` matches the current view. The default toast and dropdown entry still fire from the module's Level 1 config; the blade just adds its own reaction.

- [useBladeNotifications reference.](../../composables/notifications/useBladeNotifications.md)

## Drive a long-running progress toast

For a long job (import, export, indexation), let the blade own a single toast that updates as `processedCount` rises and resolves to success or error when `finished` flips. Suppress the auto-toast in the module config and steer the toast manually:

```ts title="src/modules/import/index.ts"
import { defineAppModule } from "@vc-shell/framework";

export default defineAppModule({
  // ...
  notifications: {
    ImportPushNotification: { toast: { mode: "silent" } },
  },
});
```

```vue title="src/modules/import/pages/import-process.vue"
<script setup lang="ts">
import { ref } from "vue";
import { notification, useBladeNotifications } from "@vc-shell/framework";

let toastId = ref<string>();

useBladeNotifications<ImportPushNotification>({
  types: ["ImportPushNotification"],
  onMessage: (msg) => {
    const content = msg.profileName ? `${msg.profileName}: ${msg.title}` : msg.title;

    if (!toastId.value) {
      toastId.value = notification(content, { timeout: false });
    } else if (!msg.finished) {
      notification.update(toastId.value, { content });
    } else {
      notification.update(toastId.value, {
        content,
        timeout: 5000,
        type: msg.errorCount ? "error" : "success",
        onClose: () => (toastId.value = undefined),
      });
    }
  },
});
</script>
```

`notification(message, opts)` returns a toast id; `notification.update(id, ...)` mutates the same toast in place instead of stacking new ones. `mode: "silent"` keeps the event in the bell dropdown history but suppresses the framework's own toast, leaving the blade in full control of what the user sees.

- [useBladeNotifications reference.](../../composables/notifications/useBladeNotifications.md)
- [Notifications plugin reference — toast modes.](../../plugins/notifications.md)

## Scope broadcasts to the current user

Platform broadcasts go to every connected client. In a multi-tenant app — vendor portal, seller back office, organization-scoped admin — install a broadcast filter at bootstrap so each user sees only the broadcasts that mention them. The filter runs once per incoming broadcast; targeted (one-to-one) messages bypass it entirely.

```vue title="src/pages/App.vue"
<script setup lang="ts">
import { onMounted } from "vue";
import { useBroadcastFilter, useUser } from "@vc-shell/framework";

const { user } = useUser();
const { setBroadcastFilter } = useBroadcastFilter();

onMounted(() => {
  setBroadcastFilter((msg) => msg.creator === user.value?.userName);
});
</script>
```

Filter on the field your platform uses to identify the originator — `creator` in the vendor portal example, but it could be `sellerId`, `organizationId`, or any payload field that survives the broadcast. Install once at app mount; if your app supports user switching, watch the user and re-install accordingly.

- [useBroadcastFilter reference.](../../composables/notifications/useBroadcastFilter.md)
- [Notifications concept page — broadcast vs targeted.](../../concepts/notifications.md#broadcast-vs-targeted)

## Cover a blade with a preview, then return

`coverWith` opens a new blade on top of the current one without destroying it. Closing the preview reveals the original blade in its previous state, which is ideal for read-only previews and side panels.

```vue title="product-details.vue"
<script setup lang="ts">
import { useBlade } from "@vc-shell/framework";

const { coverWith } = useBlade();
const product = ref<Product>();

async function onPreview() {
  await coverWith({
    name: "ProductPreview",
    param: product.value?.id,
  });
}
</script>
```

Use `replaceWith` instead when the new blade should permanently take the slot, for example switching from a create form to the edit view of a freshly created entity.

- [The blade stack model in depth.](../../concepts/blade-navigation.md)

## Persist filter state in the URL with query

A list workspace can mirror its filters in the address bar so refreshing or sharing the URL restores the same view. Use the `query` field on `openBlade` to seed initial filters, read them back through `useBlade().query`, and call `replaceWith` (same `name`, same `param`) to write updated filters without growing the history stack.

```vue title="orders-list.vue"
<script setup lang="ts">
import { onMounted, reactive, watch } from "vue";
import { useBlade } from "@vc-shell/framework";

defineBlade({ name: "Orders", url: "/orders", isWorkspace: true });

const { query, replaceWith, name } = useBlade();

const filters = reactive({
  search: query.value?.search ?? "",
  status: query.value?.status ?? "",
});

onMounted(() => loadOrders(filters));

watch(filters, (next) => {
  loadOrders(next);
  replaceWith({
    name: name.value,
    query: {
      ...(next.search ? { search: next.search } : {}),
      ...(next.status ? { status: next.status } : {}),
    },
  });
});
</script>
```

`query` is a read-only `ComputedRef<Record<string, string> | undefined>` on the blade descriptor. The framework writes the entries to the address bar verbatim, so keep keys short and values URL-safe. Use `replaceWith` (not `openBlade`) so the back button still steps out of the workspace instead of cycling through every keystroke.

!!! note "query vs options"
    `query` rides the URL and survives a refresh. Use `query` for shareable filter state (search term, page size, status). Use `options` for runtime-only payloads that are too large or too sensitive for the URL.

!!! warning "Legacy setNavigationQuery is deprecated"
    The v1 adapter still ships `setNavigationQuery` and `getNavigationQuery` for backward compatibility, but both log a deprecation warning. New code should pass `query` to `openBlade` / `replaceWith` and read it from `useBlade().query`.

## Custom notification template

Render a SignalR push notification with your own Vue component instead of the default toast layout. The notification type is registered in `defineAppModule({ notifications })` with a `template` reference; the template reads the current payload through `useNotificationContext()`.

```vue title="src/modules/orders/notifications/OrderCreatedDomainEvent.vue"
<template>
  <NotificationTemplate
    :color="style.color"
    :title="notification.title ?? ''"
    :icon="style.icon"
    :notification="notification"
  >
    <VcHint
      v-if="notification.description"
      class="tw-mb-1"
    >
      {{ notification.description }}
    </VcHint>
  </NotificationTemplate>
</template>

<script lang="ts" setup>
import { NotificationTemplate, useNotificationContext } from "@vc-shell/framework";
import { VcHint } from "@vc-shell/framework/ui";
import { computed } from "vue";

const notificationRef = useNotificationContext();
const notification = computed(() => notificationRef.value);

const style = {
  color: "var(--success-400)",
  icon: "lucide-package",
};
</script>
```

```ts title="src/modules/orders/index.ts"
import { defineAppModule } from "@vc-shell/framework";
import * as pages from "./pages";
import * as locales from "./locales";
import OrderCreatedDomainEvent from "./notifications/OrderCreatedDomainEvent.vue";

export default defineAppModule({
  blades: pages,
  locales,
  notifications: {
    OrderCreatedDomainEvent: {
      template: OrderCreatedDomainEvent,
      toast: { mode: "auto" },
    },
  },
});
```

The dropdown renders your template; the toast still follows the `toast` config (mode, severity, timeout). Use `useNotificationContext<T>()` with a generic when your notification carries extra fields beyond the base `PushNotification` shape.

- [Notifications concept.](../../concepts/notifications.md)
- [useNotifications reference.](../../composables/notifications/useNotifications.md)

## Dashboard widget with DashboardWidgetCard

Wrap the widget content in `DashboardWidgetCard` so it inherits the framework's header, loading state, and action area. The component is registered through `registerDashboardWidget` in the module entry; the registration accepts the size in the 12-column grid.

```vue title="src/modules/orders/components/OrdersDashboardCard.vue"
<template>
  <DashboardWidgetCard
    :header="$t('ORDERS.WIDGET.TITLE')"
    icon="lucide-package"
    :loading="loading"
  >
    <template #actions>
      <VcButton
        size="sm"
        variant="ghost"
        @click="openWorkspace"
      >
        {{ $t("ORDERS.WIDGET.ALL") }} &rarr;
      </VcButton>
    </template>

    <template #stats>
      <DashboardStatItem
        :value="totalCount"
        :label="$t('ORDERS.WIDGET.ALL')"
      />
      <DashboardStatItem
        :value="openCount"
        :label="$t('ORDERS.WIDGET.OPEN')"
        variant="success"
      />
    </template>
  </DashboardWidgetCard>
</template>

<script setup lang="ts">
import { DashboardWidgetCard, useBlade } from "@vc-shell/framework";
import { VcButton } from "@vc-shell/framework/ui";

const { openBlade } = useBlade();

const totalCount = ref(0);
const openCount = ref(0);
const loading = ref(false);

function openWorkspace() {
  openBlade({ name: "OrdersList", isWorkspace: true });
}
</script>
```

```ts title="src/modules/orders/index.ts"
import { defineAppModule, registerDashboardWidget } from "@vc-shell/framework";
import { markRaw } from "vue";
import OrdersDashboardCard from "./components/OrdersDashboardCard.vue";

registerDashboardWidget({
  id: "orders-widget",
  name: "Orders",
  component: markRaw(OrdersDashboardCard),
  size: { width: 6, height: 6 },
});

export default defineAppModule({ blades, locales });
```

The grid is 12 columns wide, so common widths are `3` (quarter), `4` (third), `6` (half), and `12` (full). The `#actions` slot sits in the card header on the right; `#stats` shows a compact metric strip above the default `#content` slot.

- [Layout concept — Dashboard widgets.](../../concepts/layout.md#dashboard-widgets)
- [useDashboard reference.](../../composables/services/useDashboard.md)
