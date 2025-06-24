# How-To: Adding Custom Pages and Menu Items

While VC-Shell's blade system is ideal for many workflows, you'll often need to create primary, non-blade pages like a main dashboard. This guide explains how to create a custom page, register it in the router, and add it to the main navigation menu using the recommended `bootstrap.ts` pattern.

## Prerequisites

-   Understanding of Vue 3 and Vue Router.
-   Familiarity with the `useMenuService` composable for adding menu items.
-   Knowledge of the application's entry point (`main.ts`) and routing (`router/routes.ts`).

## Core Concepts

Adding a custom page involves three main steps:
1.  **Creating the Page Component**: A standard Vue component for your page's content.
2.  **Registering the Route**: Adding the page to your application's `routes.ts` file so it has a URL.
3.  **Adding a Menu Item**: Using `useMenuService` to make the page discoverable in the main navigation menu.

A common and clean pattern is to centralize the registration of menu items, dashboard widgets, and other initial setup tasks in a dedicated `bootstrap.ts` file, which is then called from `main.ts`.

## Step 1: Create the Custom Page Component

First, create the Vue component for your new page. For this example, we'll create a simple dashboard page with a draggable dashboard component.

**Example: `src/pages/Dashboard.vue`**
```vue
<template>
<!-- You can place dashboard widgets or other content here -->
    <DraggableDashboard />
</template>

<script lang="ts" setup>
import { DraggableDashboard } from '@vc-shell/framework';
</script>
```

## Step 2: Register the Page Route

Next, you need to add a route for this page in your router configuration. Custom pages that should appear within the main application layout (with the header and sidebar) must be added as a child of the root `App` route.

**Example: `src/router/routes.ts`**
```typescript
import { RouteRecordRaw } from "vue-router";
import App from "../pages/App.vue"; // Assuming App.vue is your main layout
import Dashboard from "../pages/Dashboard.vue";

export const routes: RouteRecordRaw[] = [
  {
    path: "/",
    component: App,
    name: "App",
    meta: {
      root: true,
    },
    // Add your custom page as a child route
    children: [
      {
        path: "", // Setting path to '' makes it the default child route for '/'
        alias: "/", // `path: ''` makes this the default child route. `alias: '/'` ensures it also directly matches the root path. This is a Vue Router convention.
        name: "Dashboard",
        component: Dashboard,
        // No permissions needed for the main dashboard in this example
      },
      // ... other child routes like /reports, /settings etc.
    ],
  },
  // ... other top-level routes like /login
];
```
For more details on routing configuration, see the [Routing and Navigation Configuration guide](../../Guides/routing-configuration.md).

## Step 3: Add the Page to the Main Menu

To make your new page accessible from the UI, you should add it to the main navigation menu. The recommended approach is to use a `bootstrap.ts` file for this.

### Create `bootstrap.ts`

If you don't already have one, create a `src/bootstrap.ts` file. This file will export a function that handles setup tasks.

**Example: `src/bootstrap.ts`**
```typescript
import { addMenuItem, registerDashboardWidget } from "@vc-shell/framework";
import { App, markRaw } from "vue"; // Import App type for type-safety
import WelcomeWidget from "./components/dashboard-widgets/Welcome.vue"; // Example widget

// The bootstrap function takes the Vue app instance as an argument
export function bootstrap(app: App) {
  // 1. Add Dashboard to main menu
  addMenuItem({
    id: "dashboard", // A unique ID for the menu item
    title: "SHELL.MENU.DASHBOARD", // Use a translation key
    icon: "lucide-home", // Or any other icon
    priority: 0, // Lower numbers appear higher in the menu
    url: "/", // The URL of your page
  });

  // You can also register global dashboard widgets here
  registerDashboardWidget({
    id: "welcome-widget",
    name: "Welcome",
    component: markRaw(WelcomeWidget),
    size: { width: 6, height: 6 },
    position: { x: 0, y: 0 },
  });

  // ... other setup tasks like registering custom notification templates ...
}
```

### Call `bootstrap` from `main.ts`

Finally, import and call your `bootstrap` function in your application's entry point, `main.ts`. It's important to call `bootstrap(app)` **after** `app.use(router)` to ensure that all router functionalities are available to your bootstrap logic if needed.

**Example: `src/main.ts`**
```typescript
import { createApp } from "vue";
import VirtoShellFramework from "@vc-shell/framework";
import { router } from "./router";
import { bootstrap } from "./bootstrap"; // 1. Import bootstrap
import { RouterView } from "vue-router";

// ... other imports and setup ...

async function startApp() {
  // ... other startup logic like useUser, useLanguages ...

  const app = createApp(RouterView);

  app.use(VirtoShellFramework, {
    router,
    // ... other framework options
  });

  // ... register other plugins and modules ...
  
  app.use(router);

  bootstrap(app); // 2. Call bootstrap here

  await router.isReady();

  app.mount("#app");
}

startApp();
```

By following this pattern, you keep your setup logic organized and separate from the main application entry point, making it easier to manage as your application grows.

## Related Resources

-   [Building Navigation Menus with `useMenuService`](./building-navigation-menus-with-usemenuservice.md)
-   [Routing and Navigation Configuration](../../Guides/routing-configuration.md)
-   [Creating Interactive Dashboards with `useDashboard`](./creating-interactive-dashboards-with-usedashboard.md) 