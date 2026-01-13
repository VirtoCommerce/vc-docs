# Routing and Navigation Configuration

VC-Shell uses Vue Router to manage navigation. Although many pages (blades) register their routes automatically, understanding the main configuration file `routes.ts` is crucial for setting up the main page, adding custom pages, and ensuring blade navigation works correctly.

## The `routes.ts` File

When creating a new application with `create-vc-app`, a basic `src/router/routes.ts` file is generated. It serves as the starting point for all navigation in your application.

```typescript
import { RouteRecordRaw } from "vue-router";
import App from "../pages/App.vue";
import { Invite, Login, ResetPassword, useBladeNavigation, ChangePasswordPage } from "@vc-shell/framework";

export const routes: RouteRecordRaw[] = [
  {
    path: "/",
    component: App,
    name: "App",
    meta: {
      root: true,
    },
    children: [],
    redirect: (to) => {
      if (to.name === "App") {
        return { path: "/{{ModuleName}}", params: to.params };
      }
      return to.path;
    },
  },
  // ...standalone auth pages...
  {
    path: "/:pathMatch(.*)*",
    component: App,
    beforeEnter: async (to) => {
      const { routeResolver } = useBladeNavigation();
      return routeResolver(to);
    },
  },
];
```

Let's look at the key parts of this configuration.

## Root Application Route

The central element is the root route:

```typescript
{
  path: "/",
  component: App,
  name: "App",
  meta: {
    root: true,
  },
  children: [
    // Pages that should be displayed inside the main shell are added here
  ],
  redirect: (to) => { /* ... */ },
}
```

- **`component: App`**: Specifies that the `App.vue` component is used as the main shell for this route and all its children. It contains common UI elements like the header, sidebar, and the main content area (`<router-view>`).
- **`children: []`**: This is an array for child routes. Any page added here will be rendered inside the `App` component.
- **`meta: { root: true }`**: **This is a critically important option!** It marks this route as the root for the blade navigation system. Without this meta-information, `useBladeNavigation` will not work correctly. You can read more about blade navigation in the [Blade Navigation Guide](../Essentials/Usage-Guides/working-with-blade-navigation.md).

## Adding Pages to the Main Application Layout

If you want to add a page that uses the common layout of your application (e.g., a Dashboard), you must add it to the `children` array of the root route.

**Example: Adding a Dashboard as the Main Page**

1.  Create your page component, for example, `src/pages/Dashboard.vue`.
2.  Modify `src/router/routes.ts` as follows:

```typescript
import { RouteRecordRaw } from "vue-router";
import App from "../pages/App.vue";
import { /* ... */ } from "@vc-shell/framework";
import Dashboard from "../pages/Dashboard.vue"; // 1. Import the component

export const routes: RouteRecordRaw[] = [
  {
    path: "/",
    component: App,
    name: "App",
    meta: {
      root: true,
    },
    children: [
      // 2. Add the route for the dashboard
      {
        path: "", // An empty path means this component will be displayed for the parent's path ("/")
        alias: "/", // `path: ''` makes this the default child route. `alias: '/'` ensures it also directly matches the root path. This is a Vue Router convention.
        name: "Dashboard",
        component: Dashboard,
      },
      // You can add other pages here as well
      // {
      //   path: "about", // will be available at /about
      //   name: "About",
      //   component: () => import("../pages/About.vue"),
      // }
    ],
    // 3. Remove the redirect, as the root path is now occupied by the dashboard
    // redirect: (to) => { ... },
  },
  // ... other routes
];
```

### Removing `redirect`

The initial template includes a `redirect` function that forwards the user from the root path (`/`) to the main module's page (`/{{ModuleName}}`).

If you add a component to the root path (`path: ""`), as in the dashboard example, you **must remove** this `redirect`, otherwise the user will never see your main page.

## Single-Module Application Setup

If your application contains only one module and you don't need a navigation menu with a single item, you can configure the app to redirect directly to your module's blade and hide the menu entirely.

### Step 1: Configure the Redirect

Keep or modify the `redirect` function in your root route to point to your module:

```typescript
{
  path: "/",
  component: App,
  name: "App",
  meta: {
    root: true,
  },
  children: [],
  redirect: (to) => {
    if (to.name === "App") {
      return { path: "/my-module", params: to.params };
    }
    return to.path;
  },
}
```

This ensures that when users navigate to the root path (`/`), they are automatically redirected to your module's blade (e.g., `/my-module`).

### Step 2: Hide the Navigation Menu

To hide the navigation menu, add the `disable-menu` prop to the `VcApp` component in your `App.vue`:

```vue
<template>
  <VcApp
    :is-ready="isReady"
    :logo="logoImage"
    title="My Single Module App"
    :version="version"
    disable-menu
  >
  </VcApp>
</template>
```

With this configuration:
- Users are automatically redirected to your module's blade on app load
- The navigation menu is hidden, providing a cleaner interface
- Users can still navigate using blade navigation within your module

## Blade Navigation and the Catch-All Route

The last route in the configuration deserves special attention:

```typescript
{
  path: "/:pathMatch(.*)*",
  component: App,
  beforeEnter: async (to) => {
    const { routeResolver } = useBladeNavigation();
    return routeResolver(to);
  },
}
```

This is a "catch-all" route. It is responsible for making blade navigation work. When you navigate to a URL that does not match any of the explicitly defined routes (including children), this `beforeEnter` handler comes into play. It uses `routeResolver` from `useBladeNavigation` to find a blade registered with the corresponding `url` in `defineOptions` and display it.

Thanks to this mechanism, modules can define their own blade pages, and they will be accessible by their URLs without needing to manually add each one to the `routes.ts` file.

## Standalone Pages

Routes for authentication pages (`Login`, `Invite`, etc.) are defined at the top level, not within the `children` of `App`, because they should not be displayed inside the main application shell. They have their own minimalist layout. 

Once you have configured the route, the next step is to add it to the navigation menu so users can find it. For a detailed guide on this process, see [How-To: Adding Custom Pages and Menu Items](../Essentials/Usage-Guides/adding-custom-pages-and-menu-items.md). 