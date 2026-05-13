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

## More patterns

The vc-shell repo ships an AI-codegen knowledge base with deeper, generator-oriented recipes. Browse [`cli/vc-app-skill/runtime/knowledge/patterns/`](https://github.com/VirtoCommerce/vc-shell/tree/main/cli/vc-app-skill/runtime/knowledge/patterns) for templates covering list blades, details blades, toolbar conventions, SignalR notification templates, data tables, multilanguage fields, and dashboard widgets. The vendor-portal app under `apps/vendor-portal/src/modules/` is the canonical real-world reference for every recipe on this page.
