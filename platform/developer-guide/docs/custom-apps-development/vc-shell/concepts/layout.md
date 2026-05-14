# Layout

VC-Shell ships a complete application chrome. Your app fills the regions; it does not redraw them.

The shell is composed by **VcApp**, which renders a desktop or mobile layout, a sidebar with menu, a top bar, and a workspace that hosts the blade stack. Apps customize the chrome by registering items through services such as `addMenuItem` and `registerDashboardWidget`, and by theming through CSS custom properties. You do not edit **VcApp** itself.

The shell separates structural layout from configurable content. The positions of the sidebar, top bar, and workspace stay constant, but their contents flow in from your bootstrap: menu entries, dashboard widgets, branding, and user-area buttons. Responsiveness is built in. **VcApp** swaps the internal desktop layout for the mobile layout based on viewport, and exposes the active state to every child component through `useResponsive`.

Theming flows through SCSS custom properties under **framework/assets/styles/theme/** and a Tailwind preset. Apps extend the framework Tailwind config and override CSS variables in their own stylesheet layer.

## The app chrome

**VcApp** renders the outer frame and provides a small set of named slots for the parts you can replace. Defaults exist for every slot, so most apps only set the props.

| Region | Default content | Slot |
| --- | --- | --- |
| Layout | Desktop or mobile shell with sidebar, top bar, and search. | `layout` |
| App hub | App switcher menu (when multiple apps are registered). | `app-hub` |
| Menu | Sidebar navigation list driven by `addMenuItem`. | `menu` |
| Sidebar header | Logo area. | `sidebar-header` |
| Sidebar footer | User avatar, name, role. | `sidebar-footer` |
| Workspace | Blade stack with optional AI agent panel. | `workspace` |

The default layout is picked automatically. `useResponsive` resolves `isDesktop` and `isMobile` from the viewport, and **VcApp** mounts either **DesktopLayout** or **MobileLayout** internally. The workspace below the chrome hosts the blade navigation stack whenever a `BladeStackKey` provider is present, which the bootstrap arranges for you.

## Customizing the menu

Sidebar entries are added with the standalone `addMenuItem` function during bootstrap. Register them before the shell mounts; **VcApp**'s bootstrap flushes pre-registered items into the live menu service once `provideMenuService` runs.

```typescript title="bootstrap.ts"
import { App, markRaw } from "vue";
import { addMenuItem, registerDashboardWidget } from "@vc-shell/framework";
import Welcome from "./components/dashboard-widgets/Welcome.vue";

export function bootstrap(app: App) {
  addMenuItem({
    title: "SHELL.MENU.DASHBOARD",
    icon: "lucide-home",
    priority: 0,
    url: "/",
  });

  addMenuItem({
    title: "Orders",
    icon: "fas fa-shopping-cart",
    routeId: "OrdersList",
    priority: 10,
  });

  registerDashboardWidget({
    id: "welcome-widget",
    name: "Welcome",
    component: markRaw(Welcome),
    size: { width: 6, height: 6 },
    position: { x: 0, y: 0 },
  });
}
```

`priority` controls order; lower values appear higher in the list. Use `routeId` for items that resolve to a registered blade, or `url` for direct routes. To add or badge entries from inside a mounted component, use `useMenuService()` instead.

![Readmore](../components/layout/vc-app.md){: width="25"} VcApp props, slots, and bootstrap contract.

![Readmore](../composables/services/useMenuService.md){: width="25"} Menu service API reference.

## Top bar widgets

The top bar holds a row of small interactive pieces such as a notification bell, a sync status indicator, or a language picker. Modules add their own widgets through `useAppBarWidget()`.

```typescript title="bootstrap.ts"
import { useAppBarWidget } from "@vc-shell/framework";
import { markRaw } from "vue";
import SyncStatusIndicator from "./components/SyncStatusIndicator.vue";

export function bootstrap() {
  const { register } = useAppBarWidget();

  register({
    id: "notifications",
    icon: "lucide-bell",
    title: "Notifications",
    order: 10,
    onClick: () => openNotifications(),
  });

  register({
    id: "sync-status",
    component: markRaw(SyncStatusIndicator),
    order: 1,
  });
}
```

Pass `icon` plus `onClick` for a default icon button, or pass `component` (wrapped in `markRaw`) to render a fully custom widget. Widgets are sorted by `order`; lower values render further left. If the registering code runs before the service is provided, use the standalone `addAppBarWidget()` function instead; pre-registered items flush automatically when the shell bootstraps.

![Readmore](../composables/services/useAppBarWidget.md){: width="25"} useAppBarWidget API reference.

## Settings menu

The shell hosts a settings page with its own sidebar. Modules contribute entries to that sidebar through `useSettingsMenu()`; each entry points to a Vue component rendered in the settings workspace. Use it for module-level configuration that does not warrant a top-level menu item.

```typescript title="bootstrap.ts"
import { useSettingsMenu } from "@vc-shell/framework";
import { markRaw } from "vue";
import CatalogGeneralSettings from "./components/settings/CatalogGeneralSettings.vue";
import CatalogSeoSettings from "./components/settings/CatalogSeoSettings.vue";

export function bootstrap() {
  const { register } = useSettingsMenu();

  register({
    id: "catalog-general",
    title: "General",
    icon: "lucide-settings",
    component: markRaw(CatalogGeneralSettings),
    group: "Catalog",
    priority: 1,
  });

  register({
    id: "catalog-seo",
    title: "SEO Settings",
    icon: "lucide-search",
    component: markRaw(CatalogSeoSettings),
    group: "Catalog",
    priority: 2,
  });
}
```

`group` clusters related entries into a labeled section in the settings sidebar; `priority` orders entries within a group. Wrap component references in `markRaw` to keep Vue from making the definition reactive. Register entries conditionally if access depends on permissions; the service does not gate items by itself.

![Readmore](../composables/services/useSettingsMenu.md){: width="25"} useSettingsMenu API reference.

## Theme and branding

Theming is driven by CSS custom properties scoped under `:root[data-theme="light"]` and `:root[data-theme="dark"]`. The framework ships full palettes for primary, secondary, accent, neutrals, plus state colors (warning, danger, success, info) and derived tokens for surfaces, shadows, overlays, and frosted glass.

```scss title="app.scss"
:root[data-theme="light"] {
  --primary-500: #0078d4;
  --primary-600: #006bbd;
  --app-background: var(--secondary-100);
}
```

Override variables in your own stylesheet layer rather than mutating framework files. Theme switching at runtime is wired through `useTheme`, which toggles the `data-theme` attribute on `:root` and persists the user choice.

Tailwind utilities are prefixed with `tw-` and inherit the framework preset. Extend the preset in your app's Tailwind config:

```typescript title="tailwind.config.ts"
import defaultConfig, { content } from "@vc-shell/framework/tailwind.config";

export default {
  prefix: "tw-",
  content: [...content, "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: defaultConfig.theme,
};
```

Branding (logo, app title, user avatar) is passed as props to **VcApp**. The sidebar header and footer can be replaced entirely via named slots if the default layout is not enough.

## Mobile vs desktop

The shell ships separate internal layouts for desktop and mobile, selected automatically by `useResponsive`. Inside a blade or widget, read the same composable to swap content or interaction patterns:

```vue title="OrdersBlade.vue"
<script setup lang="ts">
import { useResponsive } from "@vc-shell/framework";

const { isMobile, isDesktop } = useResponsive();
</script>

<template>
  <VcBlade title="Orders">
    <div
      v-if="isDesktop"
      class="tw-flex tw-gap-4"
    >
      <OrdersTable />
      <OrdersSummary />
    </div>
    <OrdersTable v-else />
  </VcBlade>
</template>
```

For CSS-only responsive adjustments, prefer Tailwind breakpoint prefixes (`md:`, `lg:`) instead of JavaScript-driven conditionals. Reserve `useResponsive` for cases where the markup itself must differ, for example, collapsing a two-pane layout into a single stack or disabling drag-and-drop on touch devices.

![Readmore](../composables/ui-state/useResponsive.md){: width="25"} useResponsive API reference.

## Common mistakes

!!! warning "Do not replace VcApp"
    The chrome is fixed by design. Customize through props, named slots, and services rather than forking **VcApp**. Replacing it bypasses the bootstrap that wires the menu service, sidebar state, blade stack, and notification store.

!!! warning "Forgetting markRaw on widget components"
    Dashboard widgets are stored in reactive registries. Wrap the component in `markRaw` when calling `registerDashboardWidget`, otherwise Vue makes the component definition reactive and console warnings flood the page.

!!! warning "Scoping theme overrides too narrowly"
    CSS custom properties propagate through inheritance. Declare overrides on `:root[data-theme="light"]` or `:root[data-theme="dark"]`, not on a single component selector. A scoped override changes one element but leaves nested shell pieces using framework defaults.
