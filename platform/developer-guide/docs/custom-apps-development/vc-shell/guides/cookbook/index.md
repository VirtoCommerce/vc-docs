# Cookbook

Quick recipes for everyday VC-Shell tasks. Each one is self-contained, so read the recipe you need and ignore the rest.

Every snippet below is lifted or adapted from the **vendor-portal** sample app and the framework source. Composable names, options, and return shapes are real and current.

## Show a confirmation before closing a blade

Block close until the user confirms when there are unsaved changes. Combine `onBeforeClose` with `usePopup().showConfirmation`.

```vue title="ProductDetails.vue"
<script setup lang="ts">
import { useBlade, usePopup } from "@vc-shell/framework";

const { onBeforeClose } = useBlade();
const { showConfirmation } = usePopup();
const isModified = ref(false);

onBeforeClose(async () => {
  if (!isModified.value) return false;
  const confirmed = await showConfirmation("Discard unsaved changes?");
  return !confirmed;
});
</script>
```

The guard returns `true` to **prevent** closure and `false` to **allow** it, matching Vue Router's `beforeRouteLeave`. Always negate the user's confirmation.

![Readmore](../../composables/blade-navigation/useBlade.md){: width="25"} Full `useBlade` API and guard semantics.

## Warn before browser tab close (useBeforeUnload)

Stop the user from accidentally closing the browser tab when a form has unsaved changes. `useBeforeUnload(modified)` accepts a `ComputedRef<boolean>` and registers a `beforeunload` listener that fires the browser's standard "Leave site?" prompt whenever the ref is `true`. This is the browser-level twin of `onBeforeClose` from `useBlade()`. Pair them so the user is protected whether they click the blade close button or close the whole tab.

```vue title="src/modules/orders/pages/order-details.vue"
<script setup lang="ts">
import { computed, ref } from "vue";
import { useBeforeUnload, useBlade, usePopup } from "@vc-shell/framework";

const original = ref({ name: "" });
const draft = ref({ name: "" });
const isModified = computed(() => JSON.stringify(original.value) !== JSON.stringify(draft.value));

useBeforeUnload(isModified);

const { onBeforeClose } = useBlade();
const { showConfirmation } = usePopup();

onBeforeClose(async () => {
  if (!isModified.value) return false;
  return !(await showConfirmation("Discard unsaved changes?"));
});
</script>
```

The composable always uses the browser's native dialog. The wording is fixed by the browser and cannot be customized, which is a deliberate antiphishing restriction. Reach for `useBeforeUnload` only for browser-level closes; use `onBeforeClose` for in-app blade navigation. Reset whatever drives `isModified` after a successful save, otherwise the prompt keeps appearing.

![Readmore](../../composables/utilities/useBeforeUnload.md){: width="25"} `useBeforeUnload` reference.

## Pass selected rows from a list to a details blade

Use `param` for the entity id, which lands in the URL for deep linking. Use `options` for richer preloaded data, which stays in `history.state` only.

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
  permissions: ["seller:orders:view"],
  menuItem: {
    title: "ORDERS.MENU.TITLE",
    icon: "lucide-shopping-cart",
    priority: 1,
  },
});
</script>
```

For finer-grained checks inside a blade, use `usePermissions().hasAccess(...)` to toggle individual toolbar buttons or sections.

![Readmore](../../concepts/permissions-model.md){: width="25"} How permissions flow from the Platform to the UI.

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

`useToolbar()` registers buttons in the current blade's toolbar and cleans them up on unmount. Use `updateToolbarItem` to toggle state without re-registering, and `isVisible` for reactive visibility.

```vue title="ItemDetails.vue"
<script setup lang="ts">
import { computed, watch } from "vue";
import { useToolbar, useAsync } from "@vc-shell/framework";

const { registerToolbarItem, updateToolbarItem } = useToolbar();
const hasChanges = computed(() => form.isDirty);

const { loading: saving, action: save } = useAsync(async () => {
  await saveItem();
});

registerToolbarItem({
  id: "save",
  title: "Save",
  icon: "lucide-save",
  clickHandler: () => save(),
  isVisible: hasChanges,
  priority: 100,
});

watch(saving, (busy) => {
  updateToolbarItem("save", { disabled: busy });
});
</script>
```

The button only appears while the form is dirty and becomes disabled mid-save without flicker.

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

![Readmore](../../composables/ui-state/useLoading.md){: width="25"} `useLoading` reference.

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

![Readmore](../../composables/ui-state/useBreadcrumbs.md){: width="25"} `useBreadcrumbs` reference.

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

![Readmore](../../composables/notifications/useNotifications.md){: width="25"} The full notification system and SignalR integration.

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

![Readmore](../../concepts/blade-navigation.md){: width="25"} The blade stack model in depth.

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
    `query` rides the URL and survives a refresh; `options` rides `history.state` only. Use `query` for shareable filter state (search term, page size, status). Use `options` for preloaded payloads that are too large or too sensitive for the URL.

!!! warning "Legacy setNavigationQuery is deprecated"
    The v1 adapter still ships `setNavigationQuery` and `getNavigationQuery` for backward compatibility, but both log a deprecation warning. New code should pass `query` to `openBlade` / `replaceWith` and read it from `useBlade().query`.

## More patterns

The vc-shell repo ships an AI-codegen knowledge base with deeper, generator-oriented recipes. Browse [`cli/vc-app-skill/runtime/knowledge/patterns/`](https://github.com/VirtoCommerce/vc-shell/tree/main/cli/vc-app-skill/runtime/knowledge/patterns) for templates covering list blades, details blades, toolbar conventions, SignalR notification templates, data tables, multilanguage fields, and dashboard widgets. The vendor-portal app under `apps/vendor-portal/src/modules/` is the canonical real-world reference for every recipe on this page.
