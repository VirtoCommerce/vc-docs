# Extensions

Extension points are the framework's answer to one question: how does module A let module B inject UI into A without A knowing B exists at build time.

A host blade declares a named slot with `defineExtensionPoint("id")`. Consumer modules register components against that slot with `useExtensionPoint("id").add({ id, component, priority })`. The two sides never import each other. They share only a string name.

Registration is order independent. A consumer may register before the host has declared the slot, and the host receives a reactive, priority-sorted list once both sides have run. Extension points live in a shared reactive registry that resolves at runtime, which is what makes them safe for modules loaded through Module Federation in any sequence.

## Host: declaring an extension point

The host is the blade or component that owns a region of the UI and wants to allow customization. It calls `defineExtensionPoint` to publish the slot, then either renders the components itself or hands the slot to the `<ExtensionPoint>` component for default layout.

```vue title="AccountDetails.vue"
<template>
  <VcBlade title="Account Details">
    <form><!-- main form --></form>

    <ExtensionPoint
      v-if="account?.id"
      name="account:pricing-adjustments"
      separator
      gap="1rem"
    />
  </VcBlade>
</template>

<script setup lang="ts">
import { ExtensionPoint } from "@vc-shell/framework";
</script>
```

`<ExtensionPoint>` calls `defineExtensionPoint` for you. When you need programmatic access, call the composable directly:

```ts title="AccountDetails.vue"
import { defineExtensionPoint } from "@vc-shell/framework";

const { components, hasComponents } = defineExtensionPoint("account:pricing-adjustments", {
  description: "Pricing adjustment fields in the account details form",
});
```

`components` is a `ComputedRef` of registered entries sorted by priority. `hasComponents` is a boolean computed used to gate the surrounding markup.

## Consumer: registering a component

Consumer modules call `useExtensionPoint(name)` and add an entry. The natural place for this call is the module entry file, side by side with `defineAppModule`, or inside a composable invoked during install. Anywhere that runs before the host renders is fine.

```ts title="modules/pricing-adjustments/index.ts"
import { defineAppModule, useExtensionPoint } from "@vc-shell/framework";
import PricingAdjustmentFields from "./components/PricingAdjustmentFields.vue";

const { add } = useExtensionPoint("account:pricing-adjustments");

add({
  id: "pricing:adjustment-fields",
  component: PricingAdjustmentFields,
  props: { editable: true },
  priority: 10,
});

export default defineAppModule({});
```

Each entry has a unique `id`, a Vue `component`, optional `props` passed via `v-bind`, an optional `priority`, and optional `meta` for filtering. The `id` is the handle for replacement and removal.

The `meta` field is the way a single slot can host several kinds of contribution and let the host pick which ones render. Tag entries with anything that makes sense (`{ type: "action" }`, `{ section: "summary" }`), then pass `filter` to `<ExtensionPoint>` to render only the matching subset:

```ts title="Tagging an entry"
add({
  id: "orders:export-csv",
  component: ExportCsvButton,
  meta: { type: "action" },
});
```

```vue title="Rendering only entries with meta.type === 'action'"
<ExtensionPoint name="orders:toolbar" :filter="{ type: 'action' }" />
```

For type-safe `meta`, pass a generic to `defineExtensionPoint<{ type: 'action' | 'info' }>("orders:toolbar")` on the host side. For full control over rendering, `<ExtensionPoint>` also exposes a scoped slot with `components` and `hasComponents` — useful when the host needs custom wrappers around each entry.

## Add, replace, remove

The plugin-side API exposes two functions: `add` and `remove`. There is no separate `replace` call. `add` is idempotent on `id`: if an entry with the same `id` already exists, it is overwritten in place; otherwise it is appended.

```ts title="overrides.ts"
const { add, remove } = useExtensionPoint("account:pricing-adjustments");

add({ id: "pricing:adjustment-fields", component: BaseFields, priority: 10 });

// Same id, different component => replaces in place
add({ id: "pricing:adjustment-fields", component: EnhancedFields, priority: 10 });

// Remove by id
remove("pricing:adjustment-fields");
```

This shape makes the registry tolerant to hot reloads and to multiple modules touching the same slot. It also makes id collisions silent, which is why id discipline matters (see Common mistakes).

## Priority and ordering

The host receives entries sorted by `priority` in ascending order. Lower numbers render first. Default priority is `0`. Entries with equal priority preserve registration order.

```ts title="three-plugins.ts"
const { add } = useExtensionPoint("order:sidebar");

add({ id: "shipping:info", component: ShippingInfo, priority: 10 });
add({ id: "payment:info", component: PaymentInfo, priority: 20 });
add({ id: "notes:block", component: OrderNotes, priority: 30 });
// Render order: ShippingInfo, PaymentInfo, OrderNotes
```

!!! tip
    Reserve priority bands across the app, for example, framework slots use `0`, product modules use `10`–`90`, and overrides use `100+`. This keeps insertions predictable without renumbering every consumer.

## Example: extending account details with pricing adjustments

An `account-details` module ships an Account Details blade that knows nothing about pricing adjustments. A separate `pricing-adjustments` module adds editable adjustment fields below the standard form. The host module declares one slot; the consumer module registers one component.

Host blade:

```vue title="modules/account-details/pages/AccountDetails.vue"
<template>
  <VcBlade title="Account Details">
    <VcContainer>
      <!-- Standard fields: name, email, store -->
    </VcContainer>

    <ExtensionPoint
      v-if="account?.id"
      name="account:pricing-adjustments"
      wrapper-class="tw-p-2"
      separator
    />
  </VcBlade>
</template>

<script setup lang="ts">
import { ExtensionPoint } from "@vc-shell/framework";
</script>
```

Consumer module:

```ts title="modules/pricing-adjustments/index.ts"
import { defineAppModule, useExtensionPoint } from "@vc-shell/framework";
import PricingAdjustmentFields from "./components/PricingAdjustmentFields.vue";
import en from "./locales/en.json";

const { add } = useExtensionPoint("account:pricing-adjustments");

add({
  id: "pricing:adjustment-fields",
  component: PricingAdjustmentFields,
  props: { editable: true },
  priority: 10,
});

export default defineAppModule({ locales: { en } });
```

Injected component:

```vue title="modules/pricing-adjustments/components/PricingAdjustmentFields.vue"
<template>
  <div class="pricing-adjustment-fields">
    <h3>{{ $t("PRICING_ADJUSTMENTS.TITLE") }}</h3>
    <VcInput
      v-if="editable"
      v-model="discountLimit"
      label="Discount limit (%)"
    />
    <span v-else>{{ discountLimit }}%</span>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

defineProps<{ editable?: boolean }>();
const discountLimit = ref(5);
</script>
```

Drop the pricing-adjustments folder into the `modules` directory, restart the app, and the pricing fields appear under the account form. Remove the folder, and the slot is empty. Neither module imports the other.

- [Full extension points reference.](../plugins/extension-points.md)

## Common mistakes

!!! warning "Forgetting priority"
    `priority` defaults to `0`. When multiple modules omit it, ordering collapses to registration order, which depends on module load sequence. Set an explicit priority for every entry whose position matters.

!!! warning "Name collisions across modules"
    Two modules calling `add({ id: "fields", ... })` on the same slot overwrite each other silently because `add` is idempotent on `id`. Namespace ids by module, for example, `pricing:adjustment-fields` rather than `fields`. A shared constants file for slot names and ids removes the risk altogether.

!!! warning "Registering on a slot the host never declared"
    The store accepts registrations for unknown names without throwing. In development, a console warning appears: `Extension point "xyz" is not declared.` In production, the registration just sits in the registry and nothing renders. Verify the host actually called `defineExtensionPoint` (or `<ExtensionPoint name="...">`) with the exact same string, including casing and punctuation.

!!! warning "Accessing host reactive state from inside the extension component"
    The component you register runs inside the host blade but does not automatically see host state. Pass everything the component needs through `props` on the `add` call, or expose a shared composable. Reading host refs by reaching into the parent breaks isolation and crashes when the slot is rendered from a different host.
