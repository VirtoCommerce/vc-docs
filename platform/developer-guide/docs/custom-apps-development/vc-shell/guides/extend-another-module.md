# Extend Another Module's UI

Add a widget, a toolbar button, or a block of UI to a blade or page that another module owns, without changing that module's code.

## Prerequisites

Before extending another module, make sure you have:

- A VC-Shell module built with `defineAppModule`. See [Modules](../concepts/modules.md).
- The name of the blade you want to extend: the `name` passed to `defineBlade` in the owning module, for example `OrderDetails`.

## Choose the tool

| You want to add | Use | The owning module must |
| --- | --- | --- |
| A widget in the blade's widget sidebar | `registerExternalWidget({ targetBlades })` | nothing |
| A button in the blade toolbar | `registerExternalToolbarItem({ targetBlades })` | nothing |
| UI at a specific place inside a blade or page (a form field, a section, a link under the login form) | `useExtensionPoint(name).add(...)` | declare the place with `<ExtensionPoint name="...">` |

Widgets and toolbar buttons attach to a blade by its name. Every blade has a widget sidebar and a toolbar, so the owning module does not need to prepare anything. For any other place, the owning module decides where extensions may appear by declaring an extension point.

All three registrations run once, in the contributing module's `install()`. They do not depend on module load order: an item registered before the target blade opens appears when it opens.

## Recipe: add a widget to another module's blade

```ts title="src/modules/shipping/index.ts"
import { defineAppModule, registerExternalWidget } from "@vc-shell/framework";
import { markRaw } from "vue";
import ShippingWidget from "./components/ShippingWidget.vue";

export default defineAppModule({
  blades: pages,
  locales,
  install() {
    registerExternalWidget({
      id: "ShippingWidget",
      component: markRaw(ShippingWidget),
      targetBlades: ["OrderDetails", "ReturnDetails"],
      isVisible: (blade) => !!blade?.param,
    });
  },
});
```

`targetBlades` lists blade names. The match is case-insensitive. The widget shows on every open instance of each listed blade. `isVisible` receives the blade descriptor, so the widget can stay hidden while the blade creates a new entity and has no id yet.

For data loading and refresh inside the widget component, see [Inject a widget from a remote module](blades/index.md#recipe-inject-a-widget-from-a-remote-module).

## Recipe: add a toolbar button to another module's blade

```ts title="src/modules/quality/index.ts"
import { defineAppModule, i18n, registerExternalToolbarItem } from "@vc-shell/framework";
import { computed } from "vue";

export default defineAppModule({
  blades: pages,
  locales,
  install() {
    registerExternalToolbarItem({
      id: "quality-check",
      title: computed(() => i18n.global.t("QUALITY.TOOLBAR.CHECK")),
      icon: "lucide-sparkles",
      targetBlades: ["Products"],
      permissions: ["quality:check"],
      priority: -100,
      clickHandler: () => runQualityCheck(),
    });
  },
});
```

The item accepts the same fields as a blade's own toolbar items: `permissions`, `isVisible`, `disabled`, `shortcut`. `title` is shown as is, so pass a `computed` over `i18n.global.t` to keep it translated when the language changes.

Buttons are sorted by `priority`, highest first. The blade's own buttons get `0`, `-1`, `-2` and so on in their declared order, so an item with the default `0` lands right after the first one. Use a large negative value such as `-100` to put the item at the end. If the blade defines its own item with the same `id`, the blade's item wins.

To put a button on every blade, register it under `"*"` with `registerToolbarItem(item, "*")`.

!!! note
    `registerExternalToolbarItem` is available starting with the VC-Shell release that follows 2.7.0. On 2.7.0 and earlier, toolbar items registered by blade name do not render.

## Recipe: add UI at a place another module exposes

An extension point is a named place in a blade or page. The owning module (the host) renders `<ExtensionPoint>` where extensions may appear. Other modules (plugins) add components to it by name. The two sides share only the name string.

### Host: declare the extension point

An order details blade lets other modules add fields to its form:

```vue title="order-details.vue (host module)"
<template>
  <VcForm>
    <!-- ...order fields... -->

    <ExtensionPoint
      v-if="order?.id"
      name="order:details-fields"
      wrapper-class="tw-p-2"
    />
  </VcForm>
</template>

<script setup lang="ts">
import { ExtensionPoint } from "@vc-shell/framework";
</script>
```

Name extension points as `<area>:<place>`, for example `order:details-fields` or `customer:sidebar`. A host can render nothing for a point that has no registrations, so declaring one costs nothing until a plugin uses it.

`<ExtensionPoint>` props:

| Prop | Purpose |
| --- | --- |
| `name` | Extension point name. Required. |
| `filter` | Render only components whose `meta` matches every key, for example `{ type: "action" }`. |
| `wrapper-class` | CSS class for the wrapper around the components. |
| `separator`, `separator-class` | Render an `<hr>` before the components when there are any. |
| `gap` | Gap between the components. |

For custom rendering, use the default scoped slot, which receives `components` and `hasComponents`, or call `defineExtensionPoint(name)` in the host's `<script setup>`.

### Plugin: register a component

A loyalty module adds a points field to that form:

```ts title="src/modules/loyalty/index.ts (plugin module)"
import { useExtensionPoint } from "@vc-shell/framework";
import { LoyaltyPointsField } from "./components";

export default {
  install() {
    const { add } = useExtensionPoint("order:details-fields");

    add({
      id: "loyalty-points",
      component: LoyaltyPointsField,
    });
  },
};
```

`add` accepts:

| Field | Purpose |
| --- | --- |
| `id` | Unique within the extension point. Adding the same `id` again replaces the component. `remove(id)` removes it. |
| `component` | Vue component to render. |
| `props` | Props bound to the component. |
| `priority` | Sort order, lower first. Default `0`. |
| `meta` | Free-form tags for the host's `filter`. |

### Framework extension points

The framework declares its own extension points. Use the `ExtensionPoints` constants instead of raw strings:

| Constant | Name | Where |
| --- | --- | --- |
| `ExtensionPoints.AUTH_AFTER_FORM` | `auth:after-form` | Login page, below the sign-in form |

For example, a self sign-up module adds a button to the login page:

```ts title="src/modules/sign-up/index.ts"
import { useExtensionPoint, ExtensionPoints } from "@vc-shell/framework";
import { SignUpButton } from "./components";

export default {
  install() {
    const { add } = useExtensionPoint(ExtensionPoints.AUTH_AFTER_FORM);

    add({
      id: "sign-up-button",
      component: SignUpButton,
      priority: 10,
      meta: { type: "action" },
    });
  },
};
```

## Common mistakes

!!! warning "Using the blade URL or a route name in targetBlades"
    `targetBlades` matches the blade `name` from `defineBlade`, not its `url` and not a kebab-case variant. `"order-details"` does not match a blade named `OrderDetails`.

!!! warning "Expecting a registration to go away with a component"
    `registerExternalWidget` and `registerExternalToolbarItem` are global and stay for the app's lifetime. Call them from the module's `install()`. For an item that should exist only while one of your own blades is open, use `useBladeWidgets()` or the blade's `toolbar-items` instead.

!!! warning "Extension point name typo"
    The registry accepts any name and does not warn about a name no host declares: the registration stays in the registry and nothing renders. Check that both sides use the same string, including case and punctuation, or use the `ExtensionPoints` constants for framework points.

!!! warning "Forgetting markRaw on a widget component"
    Wrap the component passed to `registerExternalWidget` in `markRaw`. Without it, Vue makes the component definition reactive and logs a performance warning.

## Related

- [Blade recipes, including widgets from a remote module.](blades/index.md)
- [Expose an extension point from your module.](modules-and-extensions/index.md#recipe-expose-an-extension-point-in-your-module)
- [Extensions concept.](../concepts/extensions.md)
- [Extension Points plugin reference.](../plugins/extension-points.md)
- [useToolbar reference.](../composables/services/useToolbar.md)
- [useWidgets reference.](../composables/services/useWidgets.md)
