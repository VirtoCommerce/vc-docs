# Modularity: Create Application Modules with `createAppModule`

The VC-Shell framework promotes a modular architecture where applications are composed of distinct, manageable units called modules. The primary mechanism for defining and integrating these modules into your application is the `createAppModule` function, found within `@vc-shell/framework`.

This function simplifies the process of registering a module's pages (blades), components, localization resources, and notification templates with the main application.

Instead of manually configuring routes, global components, and i18n messages for each part of your module, `createAppModule` provides a declarative way to specify these elements. When the returned module definition is used with `app.use()`, VC-Shell handles the necessary registrations.

## Use `createAppModule`

The `createAppModule` function accepts several arguments, allowing you to define the different aspects of your module:

```typescript
// Example: my-feature-module/index.ts
import { createAppModule } from "@vc-shell/framework";
import type { BladeInstanceConstructor } from "@vc-shell/framework/shared/components/blade-navigation/types"; // For typing pages

// 1. Import your module's pages (Vue components, often blades)
import MyFeatureListPage from "./pages/my-feature-list-page.vue";
import MyFeatureDetailsPage from "./pages/my-feature-details-page.vue";

// 2. Import locale messages
import en from "./locales/en.json";
import de from "./locales/de.json";

// 3. Import custom notification templates (if any)
import MyCustomNotification from "./notifications/my-custom-notification.vue";

// 4. Import global components specific to this module (if any)
import MyModuleGlobalWidget from "./components/my-module-global-widget.vue";

// Define pages (blades) for the module
const pages: Record<string, BladeInstanceConstructor> = {
  MyFeatureListPage,
  MyFeatureDetailsPage,
  // Add other pages here
};

// Define locales
const locales = {
  en,
  de,
};

// Define notification templates
const notificationTemplates = {
  MyCustomNotification,
  // Add other notification templates here
};

// Define module-specific global components
const moduleComponents = {
  MyModuleGlobalWidget,
  // Add other global components here
};

// Create the module definition
const MyFeatureModule = createAppModule(
  pages,
  locales,
  notificationTemplates,
  moduleComponents
);

export default MyFeatureModule;
```

### Arguments explained

1.  **`pages`** (Required, `Record<string, BladeInstanceConstructor>`)
    *   An object where keys are typically the component names and values are the Vue component constructors for your module's pages. These pages are often "blades" in VC-Shell terminology.
    *   **Automatic routing**: If a page component has a `url` property (e.g., `MyFeatureListPage.url = "/my-feature";`), `createAppModule` will automatically register it with the Vue Router. The route name will be derived from the component's name or its URL.
    *   **Menu integration**: If a page component has a `menuItem` property (an object defining menu item attributes like `title`, `icon`, `permissions`), it will be automatically added to the application's main menu via `useMenuService`.
    *   **Permissions**: Page components can define a `permissions` array. These permissions will be associated with the automatically generated route and can be used by `usePermissions` for access control.
    *   **Blade properties**: Properties like `isBlade = true` (implicitly set for components registered as blades) and `isWorkspace` are used by the blade navigation system.

1.  **`locales`** (Optional, `Record<string, object>`)
    *   An object where keys are locale codes (e.g., `"en"`, `"de"`) and values are the corresponding JSON-like objects containing translation strings for your module.
    *   **Automatic merging**: These locales are automatically merged into the global `vue-i18n` instance when the module is registered, making them available throughout the application via `$t()` or `useI18n()`.

1.  **`notificationTemplates`** (Optional, `Record<string, Component & { notifyType?: string }>`)
    *   An object for registering custom Vue components to be used as templates for specific notification types.
    *   The component should have a `notifyType` static property that matches the notification type it handles.
    *   When a notification of that type is triggered, this template will be used for rendering.

1.  **`moduleComponents`** (Optional, `Record<string, Component>`)
    *   An object where keys are component names and values are Vue component constructors.
    *   **Global Registration**: Components provided here are registered globally with `app.component()`. This is useful for components that need to be available throughout the application or are used by other modules but are logically part of this module.

### Register module

Once you have defined your module using `createAppModule`, you register it with your Vue application instance, typically in your `main.ts` or a dedicated module registration file:

```typescript
// Example: main.ts
import { createApp } from "vue";
import App from "./App.vue";
import VcShellFramework from "@vc-shell/framework";
import MyFeatureModule from "./modules/my-feature-module"; // Assuming the previous example
// ... other imports

const app = createApp(App);

app.use(VcShellFramework, { /* framework options */ });
app.use(MyFeatureModule); // Register your custom module

// ...
app.mount("#app");
```

## Benefits of using `createAppModule`

*   **Simplified configuration**: Reduces boilerplate for registering routes, components, and locales.
*   **Encapsulation**: Keeps module-specific configurations (routes, locales, etc.) within the module itself.
*   **Convention over configuration**: Follows VC-Shell's established patterns for module integration.
*   **Dynamic capabilities**: While `createAppModule` is often used for statically imported modules, it lays the groundwork for more dynamic module loading scenarios handled by other parts of the modularity plugin.
*   **Clear structure**: Provides a clear and consistent structure for defining module contents.

## Key takeaways

*   `createAppModule` is the standard way to prepare your feature or shared modules for integration into a VC-Shell application.
*   It handles the registration of pages (with routing and menu items), localization resources, custom notification templates, and global components.
*   Always ensure your page components have the necessary static properties (`url`, `menuItem`, `permissions`) if you want `createAppModule` to handle their integration automatically.

This approach streamlines module development and helps maintain a clean, organized, and extensible codebase.

