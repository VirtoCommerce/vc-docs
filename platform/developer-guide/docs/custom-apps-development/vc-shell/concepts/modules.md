# Modules

A module is the unit of feature packaging in VC-Shell: a self-contained Vue plugin that bundles blades, routes, menu items, notification handlers, and translations for one bounded subdomain.

Modules exist to make features composable. A standalone app bundles its modules at build time. A host app loads remote modules at runtime via Module Federation, with semver compatibility filtering. Either way, the host calls `app.use(myModule)` and the install function registers blades in the `BladeRegistry`, creates routes, attaches menu items, registers notification types, and merges locale bundles.

Two modules never import from each other directly. Cross-module wiring goes through extension points or the menu service. That is what lets a remote module ship independently and still slot into a host without name collisions.

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
├─ locales/          Translation bundles per language.
└─ notifications/    Notification template components (optional).
```

Dashboard widgets are not registered through `defineAppModule`. They use `registerDashboardWidget(...)`. See [Modularity plugin reference](../plugins/modularity.md).

## API

`defineAppModule` takes a single options object. Every field is optional, so `defineAppModule({})` is valid for modules that only register dashboard widgets or extension contributions.

```ts
defineAppModule({
  blades?:      Record<string, Component>;
  locales?:     Record<string, object>;
  notifications?: ModuleNotificationsConfig;
  notificationTemplates?: Record<string, Component>; // legacy
});
```

| Option | Purpose |
| --- | --- |
| `blades`. | Record of blade components. Keys serve as fallback names when `defineBlade` does not set one. |
| `locales`. | Record keyed by language code (`{ en, de }`). Each value is a translation object. |
| `notifications`. | Notification type configurations (toast mode, severity, custom templates). |
| `notificationTemplates`. | Legacy path. Use `notifications` for new code. |

Returns a standard Vue plugin: `{ install(app) { ... } }`.

!!! note "Legacy adapter"
    `createAppModule(pages, locales, notificationTemplates, components)` delegates to `defineAppModule`. Migrate on touch: `defineAppModule({ blades: pages, locales })`.

## Lifecycle

When `app.use(module)` runs, the install function executes synchronously and in this order:

1. **Blade registration.** Each blade lands in `BladeRegistry`. With `url` and `menuItem` set, the menu service registers a sidebar entry.
2. **Notification registration (new API).** Entries in `notifications` go into the notification store.
3. **Legacy notification compatibility.** If only `notificationTemplates` is provided, or a blade has a deprecated `notifyType`, the framework keeps the old behavior and emits a deprecation warning.
4. **Locale merge.** Translation bundles are merged into the global `vue-i18n` instance.

Blades are registered first so menu items can reference them; locales come last because they are purely additive. Full step-by-step including the legacy shims: [Modularity plugin reference](../plugins/modularity.md#module-lifecycle).

![Readmore](../plugins/modularity.md){: width="25"} Modularity plugin reference.

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
  permissions: ["seller:orders:view"],
  menuItem: {
    title: "ORDERS.MENU.TITLE",
    icon: "lucide-shopping-cart",
    priority: 10,
    permissions: ["seller:orders:view"],
  },
});
</script>
```

| Property | Default | Notes |
| --- | --- | --- |
| `name`. | Export key. | Unique key in `BladeRegistry`. Always set explicitly. |
| `url`. | `undefined`. | URL path. A route is created when set. |
| `isWorkspace`. | `false`. | `true` for top-level workspaces. |
| `routable`. | `true`. | Whether a router route is created. |
| `permissions`. | `undefined`. | Required permission strings. Flow into route guard and menu visibility. |
| `menuItem`. | `undefined`. | Sidebar menu config. Created only when `url` is also set. |

Child blades, the details panels opened from a list, skip `url`, `isWorkspace`, and `menuItem`. They are opened programmatically via `openBlade(...)`.

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

![Readmore](../plugins/notifications.md){: width="25"} Notifications plugin reference.

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

### Dashboard-only module

```ts
import { defineAppModule, registerDashboardWidget } from "@vc-shell/framework";
import { markRaw } from "vue";
import SalesChart from "./components/SalesChart.vue";

registerDashboardWidget({
  id: "sales-chart",
  name: "Sales overview",
  component: markRaw(SalesChart),
  size: { width: 12, height: 8 },
});

export default defineAppModule({});
```

`defineAppModule({})` returns a valid plugin with no blades. Dashboard widgets are registered separately; the registration bus survives until the framework picks them up at bootstrap.

### Module that extends another module

A module can register components against an extension point declared by another module. The host blade declares `<ExtensionPoint name="seller:commissions" />`; the contributing module calls `useExtensionPoint("seller:commissions").add({ id, component, priority })`. See [Extensions](extensions.md).

## When to split

Split when the unit has independent lifecycle, ownership, or release cadence:

- A bounded subdomain (orders, customers, inventory) deserves its own module.
- A cross-cutting capability used by several apps should be its own publishable module.
- A remote add-on loaded at runtime via Module Federation is necessarily its own module.

Stay in one module when the boundary is organizational. A single module with subfolders is cheaper than two modules with implicit dependencies.

## Module Federation

Remote module manifest:

```json title="frontend-module manifest"
{
  "id": "orders-remote",
  "entry": "https://cdn.example.com/orders/remoteEntry.js",
  "version": "1.4.0",
  "compatibleWith": {
    "dependencies": { "@vc-shell/framework": ">=2.0.0 <3.0.0" }
  }
}
```

The host fetches the registry from `POST /api/frontend-modules`, filters by semver, loads compatible remotes in parallel, resolves the exported Vue plugin from each, and installs with `app.use(...)`. Shared dependencies (`@vc-shell/mf-config`) keep Vue, Vue Router, `vue-i18n`, and the framework as singletons across remotes. Full flow: [Architecture overview](../introduction/architecture-overview.md#module-federation).

## Common mistakes

!!! warning "Forgetting `defineBlade` (or `defineOptions({ name }))` in a blade"
    The blade falls back to the export key as its name and ships without a route or menu entry.

!!! warning "Duplicate blade names across modules"
    `BladeRegistry` silently overwrites the earlier registration. Prefix names with the module domain (`OrdersList`, not `List`).

!!! warning "Forgetting `markRaw()` on a dashboard widget component"
    Vue treats the component definition as reactive, triggering warnings and pointless rerenders.

!!! warning "Missing locale namespace"
    Two modules that both register `MENU.TITLE` collide; the second wins.

!!! warning "Using `createAppModule` for new code"
    Deprecated; does not accept the typed `notifications` option.
