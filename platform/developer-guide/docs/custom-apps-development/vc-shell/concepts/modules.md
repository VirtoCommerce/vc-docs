# Modules

A module is the unit of feature packaging inside a VC-Shell application: a self-contained unit that bundles blades, routes, menu items, notification handlers, and translations for one bounded subdomain.

Application modules live in `src/modules/` and are bundled with the app. The app imports each module from its entry point and installs it; the framework reads the module's declarations and adds the blades, routes, menu entries, notification handlers, and locale bundles to the running app.

Modules keep their internals private by default. Cross-module UI wiring goes through extension points, the menu service, or explicit public exports from the module entry point. A module may expose composables from its `index.ts` as a deliberate frontend contract; consumers should import that public export instead of reaching into another module's private folder structure.

A module is produced by `defineAppModule()`, which returns a standard Vue plugin:

```ts title="src/modules/orders/index.ts"
import { defineAppModule } from "@vc-shell/framework";
import * as blades from "./pages";
import * as locales from "./locales";
import OrderCreatedEvent from "./notifications/OrderCreatedEvent.vue";

export default defineAppModule({
  blades,
  locales,
  notifications: {
    OrderCreatedDomainEvent: {
      template: OrderCreatedEvent,
      toast: { mode: "auto" },
    },
  },
});

export * from "./pages";
export * from "./composables";
```

## Layout

A module is a folder with a predictable shape. The `index.ts` is the entry point; the rest is convention.

```text
src/modules/orders/
├─ index.ts          defineAppModule({ blades, locales, notifications }).
├─ pages/            Blade components.
├─ composables/      Module-scoped logic (useList, useDetails).
├─ components/       Module-scoped Vue components.
├─ widgets/          Blade widgets, widget definitions, and widget-specific composables.
├─ utilities/        Module-scoped helper functions (optional).
├─ locales/          Translation bundles per language.
└─ notifications/    Notification template components (optional).
```

Dashboard widgets are registered with `registerDashboardWidget(...)`, not through the `defineAppModule` options object. Widget components can live under `components/`; widget composition logic often lives under `widgets/`.

## API

`defineAppModule` takes a single options object. Every field is optional, so `defineAppModule({})` is valid when a folder must still be installed through module discovery but has no blades, locales, or notifications of its own.

| Option | Purpose |
| --- | --- |
| `blades`. | Record of blade components. Keys serve as fallback names when `defineBlade` does not set one. |
| `locales`. | Record keyed by language code (`{ en, de }`). Each value is a translation object. |
| `notifications`. | Notification type configurations (toast mode, severity, custom templates). See [Notifications](notifications.md). |

- [Modularity plugin reference.](../plugins/modularity.md)

## Blade static properties

A blade declares routing, menu, and permissions through static properties consumed by `defineAppModule` during install:

```vue title="src/modules/orders/pages/OrdersList.vue"
<script setup lang="ts">
import { useBlade, VcBlade } from "@vc-shell/framework";

defineBlade({
  name: "OrdersList",
  url: "/orders",
  isWorkspace: true,
  routable: true,
  permissions: ["orders:order:view"],
  menuItem: {
    title: "ORDERS.MENU.TITLE",
    icon: "lucide-shopping-cart",
    priority: 10,
    permissions: ["orders:order:view"],
  },
});
</script>
```

| Property | Default | Notes |
| --- | --- | --- |
| `name`. | Export key. | The global lookup key used by `openBlade({ name: ... })`. Always set explicitly. |
| `url`. | `undefined`. | URL path for opening or restoring the blade from navigation. |
| `isWorkspace`. | `false`. | `true` for top-level workspaces. |
| `routable`. | `true`. | Whether the blade may be opened from a URL when the URL points to it. Set `false` for blades that should only be opened programmatically. |
| `permissions`. | `undefined`. | Required permission strings. Flow into route guard and menu visibility. |
| `menuItem`. | `undefined`. | Sidebar menu config. Created only when `url` is also set. |

Child blades, such as details panels opened from a list, are usually opened programmatically via `openBlade(...)`. They may define `url` when direct URL navigation or restore should be supported, or omit `url` when they should only be reachable from parent UI. They usually do not define `isWorkspace` or `menuItem`.

## Notifications

The `notifications` option binds SignalR event names from the Platform to presentation policies. Each entry chooses how an incoming message surfaces in the UI: a toast, a progress indicator, a silent panel entry, or a fully custom template.

```ts
notifications: {
  OrderCreatedEvent: { toast: { mode: "auto" } },
  OrderFailedEvent: {
    template: OrderFailedNotification,
    toast: { mode: "auto", severity: "error" },
  },
  ExportProgressEvent: {
    toast: {
      mode: "progress",
      isComplete: (msg) => msg.finished === true,
      completedType: (msg) => (msg.errorCount > 0 ? "error" : "success"),
    },
  },
  AuditLogEvent: { toast: false },
},
```

Full schema: [Modularity plugin reference](../plugins/modularity.md#registering-notification-types).

- [Notifications plugin reference.](../plugins/notifications.md)

## Locales

Translation bundles ship with the module and merge into the global `vue-i18n` instance during install. Keys must be namespaced under the module domain to keep two modules from overwriting each other's labels.

```ts
import en from "./locales/en.json";
import de from "./locales/de.json";

export default defineAppModule({ blades, locales: { en, de } });
```

```json title="src/modules/orders/locales/en.json"
{
  "ORDERS": {
    "MENU": { "TITLE": "Orders" },
    "PAGES": {
      "LIST": { "TITLE": "Orders list", "TABLE": { "TOTALS": "Total orders" } }
    }
  }
}
```

!!! warning "Always namespace under the module name"
    `ORDERS.PAGES.LIST.TITLE`, not `PAGES.LIST.TITLE`. Without a prefix, modules collide on common keys.

!!! tip "Use i18n keys, not literal strings, in blade configs"
    `menuItem.title: "ORDERS.MENU.TITLE"` lets the menu service resolve labels at render time and respond to locale changes without re-running module install.

## Recipes

Common module shapes, from the smallest valid plugin to one that contributes into another module's extension point.

### Minimal module

```ts
import { defineAppModule } from "@vc-shell/framework";
import HelloWorld from "./pages/HelloWorld.vue";

export default defineAppModule({ blades: { HelloWorld } });
```

### CRUD module

Workspace list blade plus a child details blade. The list exposes `reload`; the details calls `callParent("reload")` after save. Full code: [Modularity plugin, CRUD example](../plugins/modularity.md#module-with-crud-blades-list--details).

### Dashboard widget registration

```ts title="src/dashboard/registerSalesWidget.ts"
import { registerDashboardWidget } from "@vc-shell/framework";
import { markRaw } from "vue";
import SalesChart from "./components/SalesChart.vue";

registerDashboardWidget({
  id: "sales-chart",
  name: "Sales overview",
  component: markRaw(SalesChart),
  size: { width: 12, height: 8 },
});
```

The important part is that this file is imported during application startup, before the dashboard service reads registered widgets. If your app only discovers feature folders through `src/modules/*` default exports, wrapping a widget-only folder in `defineAppModule({})` is a valid integration shim, but it is not required by dashboard registration itself.

### Module that extends another module

A module can register components against an extension point declared by another module. The host blade declares `<ExtensionPoint name="account:pricing-adjustments" />`; the contributing module calls `useExtensionPoint("account:pricing-adjustments").add({ id, component, priority })`. See [Extensions](extensions.md).

## When to split

Split when the unit has independent lifecycle, ownership, or release cadence:

- A bounded subdomain (orders, customers, inventory) deserves its own module.
- A cross-cutting capability used by several apps should be its own publishable module.

Stay in one module when the boundary is organizational. A single module with subfolders is cheaper than two modules with implicit dependencies.

## Common mistakes

!!! warning "Forgetting `defineBlade` in a blade"
    The blade falls back to the export key as its name and ships without a route or menu entry.

!!! warning "Duplicate blade names across modules"
    Registering two blades under the same name throws at module install time and halts the app. Prefix blade names with the module domain (`OrdersList`, not `List`) so two unrelated modules cannot collide on a generic word.

!!! warning "Duplicate dashboard widget ids"
    `registerDashboardWidget` throws when called twice with the same `id`. Prefix widget ids the same way (`orders:sales-chart`, not `sales-chart`).

!!! warning "Forgetting `markRaw()` on a dashboard widget component"
    Vue treats the component definition as reactive, triggering warnings and pointless rerenders.

!!! warning "Missing locale namespace"
    Two modules that both register `MENU.TITLE` collide; the second wins.
