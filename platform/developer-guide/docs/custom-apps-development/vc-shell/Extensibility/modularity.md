# Modularity in VC-Shell Applications

The VC-Shell framework is designed with modularity at its core, allowing developers to build scalable and maintainable applications by breaking them down into independent, feature-specific modules. This guide focuses on the primary approach for creating and integrating modules within a custom VC-Shell application.

For a step-by-step guide on creating a module, refer to [Developing Custom VC-Shell Modules](../Guides/developing-custom-modules.md).
To see how modules fit into the broader application structure, see [Application Architecture Best Practices](../Guides/application-architecture-best-practices.md).

## Core Concepts of Application Modularity

* **Module as a Vue Plugin**: Each module you create is essentially a Vue plugin. The `@vc-shell/framework` provides helpers to structure and register these plugins.
* **Encapsulation**: Modules encapsulate a specific set of features, including their own pages (blades), components, composables, localization files, and routes.
* **Clear Entry Point**: Each module has an `index.ts` file that serves as its entry point, defining what the module provides to the application.
* **Simplified Registration**: The `createAppModule` function from `@vc-shell/framework` is the primary helper for packaging module assets (pages, locales, etc.).
* **Standard Integration**: Modules are integrated into the main application via `app.use()` in your `src/main.ts` file.

## Module Structure

A typical application module follows a conventional directory structure, as detailed in the [Developing Custom VC-Shell Modules guide](../Guides/developing-custom-modules.md#anatomy-of-a-module). Key parts include:

-   **`pages/`**: Contains Vue components representing blades (full-screen views or panels).
-   **`locales/`**: Holds translation files for the module.
-   **`composables/`**: Includes Vue Composition API functions specific to the module.
-   **`components/`**: Stores reusable Vue components used within the module.
    -   **`components/notifications/`**: (Optional) For custom notification templates.
-   **`index.ts`**: The module's entry point. This file uses `createAppModule` to bundle the module's parts and exports the configured module.

## Module Registration with `createAppModule`

The `createAppModule` function is a utility provided by `@vc-shell/framework` to streamline the creation of a module definition that can be easily registered with your Vue application.

**`src/modules/your-module-name/index.ts` example:**
```typescript
// Import all blade components from the 'pages' directory
import * as pages from "./pages";
// Import all locale files from the 'locales' directory
import * as locales from "./locales";
// (Optional) Import notification templates
import * as notificationTemplates from "./components/notifications";
// (Optional) Import other globally registered components from this module
import * as moduleComponents from "./components/exports";

import { createAppModule } from "@vc-shell/framework";

export default createAppModule(
  pages,
  locales,
  notificationTemplates, // Optional
  moduleComponents       // Optional
);

// It's good practice to also export key parts of your module
export * from "./pages";
export * from "./composables";
// export * from "./components"; // If some are designed for external use
export * from "./types";      // If you have module-specific types
```

**`createAppModule` Arguments:**

* **`pages`**: `Record<string, BladeInstanceConstructor>` - An object where keys are page (blade) names and values are the Vue component constructors.
    When a module is registered, the framework inspects these page components for a `defineOptions` block. If found, metadata like `url`, `name`, `menuItem`, and `permissions` are extracted and used to automatically configure routing and main menu entries.
* **`locales`**: `Record<string, Record<string, string>>` - An object where keys are locale codes (e.g., "en") and values are the translation dictionaries.
* **`notificationTemplates`** (Optional): `Record<string, Component>` - An object for custom notification rendering components.
* **`moduleComponents`** (Optional): `Record<string, Component>` - An object for other components from this module that need to be registered globally with `app.component()`. This is useful for components that are logically part of this module but need to be available for use in templates throughout the entire application or by other modules without explicit import (e.g., a shared widget). Components not listed here remain scoped to the module and must be explicitly imported where needed.

## Integrating Modules into the Application

Once your module is defined using `createAppModule`, you register it in your application's main entry point, typically `src/main.ts`.

**`src/main.ts` example:**
```typescript
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router"; // Your application's router instance
import { VirtoShellFramework } from "@vc-shell/framework";

// Import your custom modules
import * as myFirstModule from "./modules/my-first-module";
import * as mySecondModule from "./modules/my-second-module";
// ... other modules

const app = createApp(App);

// Initialize the VC-Shell Framework
// Note: The 'modules' array option in VirtoShellFramework is for a different kind of module loading,
// typically not used when using the app.use() pattern for each application module.
app.use(VirtoShellFramework, {
  router,
  // Provide other framework options if needed
});

// Register your application modules
app.use(myFirstModule.default, { router }); // Pass router instance if module pages use it
app.use(mySecondModule.default, { router });
// ... register other modules

app.use(router);
app.mount("#app");
```
The second argument to `app.use(module, options)` can be used to pass options to the module, with the `router` instance being a common requirement if the module's pages need to interact with or be registered by the router.

## Extension Points

VC-Shell provides various ways for modules to extend the application's UI and functionality. While the old `useModularity().registerModule()` detailed a specific way to hook into these, with the `createAppModule` approach, extensions are often handled more directly or declaratively.

### 1. Main Menu & Routing (Blades)

Pages (blades) within your module typically define their navigation aspects (menu item, URL, permissions) declaratively using `defineOptions` within the `<script setup>` block.

**Example in a Blade (`.vue` file in `pages/`):**
```vue
<script lang="ts" setup>
// ... other imports

defineOptions({
  name: "MyModulePageBlade", // Unique name for the blade
  url: "/my-module-page",    // URL for this blade
  menuItem: {
    title: "My Module Page",   // Text for the menu item (use i18n keys)
    icon: "material-widgets",  // Icon for the menu
    priority: 100,
    groupConfig: {
        id: "my-module-group",
        title: "My Module Group" // Menu group (use i18n keys)
    }
  },
  permissions: ["myModule:viewPage"], // Optional permissions
});

// ... rest of your blade logic
</script>
```
The framework processes these options when the module is registered and the blade components are recognized.

### 2. Settings Menu

To add items to the settings menu, use the `useSettingsMenu` composable. This is typically done when your module is initialized (e.g., can be called from your module's `index.ts` if it needs to run once, or from a specific blade/component's `setup` if context-dependent).

```typescript
// In a suitable place, e.g., a blade's setup or module's index.ts (if run once logic is needed)
import { useSettingsMenu } from '@vc-shell/framework';

const settingsMenu = useSettingsMenu();

settingsMenu.addMenuItem({
  title: 'My Module Settings', // Use i18n keys
  path: '/settings/my-module-settings', // Route to the settings blade
  icon: 'material-settings',
  priority: 100,
  // permissions: ['myModule:manageSettings'] // Optional
});
```

### 3. App Bar Widgets

Custom widgets on the main application bar are registered using the `useAppBarWidget` composable.

```typescript
import { useAppBarWidget } from '@vc-shell/framework';
import MyCustomWidgetComponent from '../components/MyCustomWidget.vue'; // Your widget component

const appBarWidget = useAppBarWidget();

appBarWidget.registerWidget({
  id: 'my-custom-app-bar-widget',
  component: MyCustomWidgetComponent,
  title: 'My Widget', // Tooltip or accessibility label
  priority: 100,
});
```
This registration can happen in a blade's `setup` script if the widget is tied to that blade's context, or more globally if the widget should always be present when the module is active (e.g., called from the module's `index.ts` after `createAppModule` if the module structure allows for such side effects, though often UI registrations are better tied to component lifecycles).

### 4. Blade Toolbar Items

Buttons and other controls on a blade's toolbar are primarily defined by passing an array of `IBladeToolbar` objects to the `toolbarItems` prop of the `VcBlade` component.

**Example directly in `VcBlade` template usage (e.g., within another component or blade):**
```vue
<template>
  <VcBlade
    title="My Blade with Toolbar"
    :toolbar-items="myToolbarActions"
    :closable="true"
    @close="handleClose"
  >
    <!-- Blade content -->
  </VcBlade>
</template>

<script lang="ts" setup>
import { VcBlade, type IBladeToolbar } from '@vc-shell/framework';
import { ref } from 'vue';

const myToolbarActions = ref<IBladeToolbar[]>([
  {
    id: 'action-save',
    title: 'Save', // Use i18n keys
    icon: 'material-save',
    type: 'button',
    priority: 10,
    action: () => {
      console.log('Save action triggered');
      // Call your save logic
    },
    // disabled: // reactive boolean for disabled state
    // visible: // reactive boolean for visibility
  },
  {
    id: 'action-refresh',
    title: 'Refresh',
    icon: 'material-refresh',
    type: 'button',
    priority: 20,
    action: () => {
      console.log('Refresh action triggered');
    },
  },
  // ... more toolbar items or menus
]);

function handleClose() {
  // Handle blade close
}
</script>
```

**Dynamic Registration with `useToolbar` (Advanced/External Control):**

For scenarios where toolbar items need to be dynamically added or modified from code outside the direct parent of `VcBlade` (e.g., from a deeply nested component, a separate service, or in response to application-wide events), the `useToolbar` composable provides direct imperative control.

```vue
// Inside a component or composable that needs to modify a specific blade's toolbar externally
import { useToolbar } from '@vc-shell/framework';
// import { onMounted } from 'vue'; // Or other lifecycle hooks/triggers

const toolbar = useToolbar();
const targetBladeName = 'NameOfTheTargetBlade'; // This must match the 'name' in defineOptions of the target blade

function addExternalToolbarItem() {
  toolbar.registerToolbarItem({
    id: 'my-external-tool',
    title: 'External Action', // Use i18n keys
    icon: 'material-extension',
    onClick: () => {
      console.log('External tool for ' + targetBladeName + ' clicked!');
    },
    priority: 100,
  }, targetBladeName);
}

// Call addExternalToolbarItem() when appropriate, e.g., on component mount, after an event, etc.
// onMounted(() => { 
//   addExternalToolbarItem();
// });

// To remove an item:
// toolbar.removeToolbarItem('my-external-tool', targetBladeName);

// To clear all items for a blade (use with caution):
// toolbar.clearToolbar('target-blade-name');
```
This imperative approach is powerful but should be used judiciously, as defining toolbar items directly via props is generally simpler and more declarative for common use cases.

## Inter-Module Communication

While modules aim for encapsulation, some level of interaction might be necessary. Key principles include:

-   **Blade Navigation**: The primary method for transitioning between features offered by different modules is via `useBladeNavigation().openBlade()`.
-   **Shared Services/Composables**: For genuinely global state or functionality, consider application-level composables (`src/composables/`) rather than direct cross-module imports.
-   **Events**: For decoupled communication, Vue's provide/inject or a lightweight event bus can be used, though sparingly.

A detailed discussion on inter-module communication strategies and anti-patterns can be found in the [Developing Custom VC-Shell Modules guide under "Inter-Module Communication"](../Guides/developing-custom-modules.md#inter-module-communication).

## Best Practices for Module Development

* **Keep Modules Focused**: Each module should have a clear, well-defined purpose.
* **Minimize Inter-Module Dependencies**: Aim for loose coupling. If modules need to interact, prefer communication via shared services, events, or Vue's provide/inject, rather than direct imports of components or composables from *within* another module's specific business logic. Blade navigation (`openBlade`) is the primary way to transition between features offered by different modules.
* **Leverage `defineOptions`**: For blades, use `defineOptions` extensively for declarative registration of routes and menu items.
* **Use Composables for Logic**: Encapsulate business logic and state management within composables, keeping your Vue components (blades/pages) focused on presentation.
* **Localization**: Provide translations for all user-facing strings within your module's `locales` directory.
* **Documentation**: Document the purpose of your module, its public API (if any composables/components are meant for external use), and how to configure it.
* **Consider Performance**:
    *   Utilize code-splitting (dynamic imports for routes/blades) where appropriate, which Vite often handles automatically for route components.
    *   Be mindful of the size of assets included in your module.
* **Error Handling**: Implement robust error handling, especially for API calls within your composables.
* **Clear Naming**: Use consistent and descriptive naming for your modules, files, components, and composables.

By following these principles and leveraging the `createAppModule` workflow, you can build robust, scalable, and maintainable applications with VC-Shell. 
