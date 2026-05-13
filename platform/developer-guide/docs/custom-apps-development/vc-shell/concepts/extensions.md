# Extensions

Extension points are the framework's answer to one question: how does module A let module B inject UI into A without A knowing B exists at build time.

A host blade declares a named slot with `defineExtensionPoint("id")`. Consumer modules register components against that slot with `useExtensionPoint("id").add({ id, component, priority })`. The two sides never import each other. They share only a string name.

Registration is order independent. A consumer may register before the host has declared the slot, and the host receives a reactive, priority-sorted list once both sides have run. This separates extension points from Vue's `<slot>`, which is compile-time and same-file, and from `provide` / `inject`, which is scoped to the component tree. Extension points live in an app-scoped reactive registry and resolve at runtime, which is what makes them safe for modules loaded through Module Federation in any sequence.

## Host: declaring an extension point

The host is the blade or component that owns a region of the UI and wants to allow customization. It calls `defineExtensionPoint` to publish the slot, then either renders the components itself or hands the slot to the `<ExtensionPoint>` component for default layout.

```vue title="SellerDetailsEdit.vue"
<template>
  <VcBlade title="Seller Details">
    <form><!-- main form --></form>

    <ExtensionPoint
      v-if="sellerDetails?.id"
      name="seller:commissions"
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

```ts title="SellerDetailsEdit.vue"
import { defineExtensionPoint } from "@vc-shell/framework";

const { components, hasComponents } = defineExtensionPoint("seller:commissions", {
  description: "Commission fee fields in the seller details form",
});
```

`components` is a `ComputedRef` of registered entries sorted by priority. `hasComponents` is a boolean computed used to gate the surrounding markup.

## Consumer: registering a component

Consumer modules call `useExtensionPoint(name)` and add an entry. The natural place for this call is the module entry file, side by side with `defineAppModule`, or inside a composable invoked during install. Anywhere that runs before the host renders is fine.

```ts title="modules/marketplace-commissions/index.ts"
import { defineAppModule, useExtensionPoint } from "@vc-shell/framework";
import CommissionFields from "./components/CommissionFields.vue";

const { add } = useExtensionPoint("seller:commissions");

add({
  id: "marketplace:commission-fields",
  component: CommissionFields,
  props: { editable: true },
  priority: 10,
});

export default defineAppModule({});
```

Each entry has a unique `id`, a Vue `component`, optional `props` passed via `v-bind`, an optional `priority`, and optional `meta` for filtering. The `id` is the handle for replacement and removal.

## Add, replace, remove

The plugin-side API exposes two functions: `add` and `remove`. There is no separate `replace` call. `add` is idempotent on `id`: if an entry with the same `id` already exists, it is overwritten in place; otherwise it is appended.

```ts title="overrides.ts"
const { add, remove } = useExtensionPoint("seller:commissions");

add({ id: "marketplace:commission-fields", component: BaseFields, priority: 10 });

// Same id, different component => replaces in place
add({ id: "marketplace:commission-fields", component: EnhancedFields, priority: 10 });

// Remove by id
remove("marketplace:commission-fields");
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

## Real example: customizing seller-details with marketplace-commissions

The vendor portal ships a Seller Details blade that knows nothing about commissions. A separate `marketplace-commissions` module adds commission rate fields below the standard form. The host module declares one slot; the consumer module registers one component.

Host blade:

```vue title="modules/seller-details/pages/SellerDetailsEdit.vue"
<template>
  <VcBlade title="Seller Details">
    <VcContainer>
      <!-- Standard fields: name, email, store -->
    </VcContainer>

    <ExtensionPoint
      v-if="sellerDetails?.id"
      name="seller:commissions"
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

```ts title="modules/marketplace-commissions/index.ts"
import { defineAppModule, useExtensionPoint } from "@vc-shell/framework";
import CommissionFields from "./components/CommissionFields.vue";
import en from "./locales/en.json";

const { add } = useExtensionPoint("seller:commissions");

add({
  id: "marketplace:commission-fields",
  component: CommissionFields,
  props: { editable: true },
  priority: 10,
});

export default defineAppModule({ locales: { en } });
```

Injected component:

```vue title="modules/marketplace-commissions/components/CommissionFields.vue"
<template>
  <div class="commission-fields">
    <h3>{{ $t("COMMISSIONS.TITLE") }}</h3>
    <VcInput
      v-if="editable"
      v-model="rate"
      label="Commission rate (%)"
    />
    <span v-else>{{ rate }}%</span>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

defineProps<{ editable?: boolean }>();
const rate = ref(5);
</script>
```

Drop the marketplace-commissions folder into the `modules` directory, restart the app, and the commission fields appear under the seller form. Remove the folder, and the slot is empty. Neither module imports the other.

![Readmore](../plugins/extension-points.md){: width="25"} Full extension points reference.

## Common mistakes

!!! warning "Forgetting priority"
    `priority` defaults to `0`. When multiple modules omit it, ordering collapses to registration order, which depends on module load sequence. Set an explicit priority for every entry whose position matters.

!!! warning "Name collisions across modules"
    Two modules calling `add({ id: "fields", ... })` on the same slot overwrite each other silently because `add` is idempotent on `id`. Namespace ids by module, for example, `marketplace:commission-fields` rather than `commission-fields`. A shared constants file for slot names and ids removes the risk altogether.

!!! warning "Registering on a slot the host never declared"
    The store accepts registrations for unknown names without throwing. In development, a console warning appears: `Extension point "xyz" is not declared.` In production, the registration just sits in the registry and nothing renders. Verify the host actually called `defineExtensionPoint` (or `<ExtensionPoint name="...">`) with the exact same string, including casing and punctuation.

!!! warning "Accessing host reactive state from inside the extension component"
    The component you register runs inside the host blade but does not automatically see host state. Pass everything the component needs through `props` on the `add` call, or expose a shared composable. Reading host refs by reaching into the parent breaks isolation and crashes when the slot is rendered from a different host.
