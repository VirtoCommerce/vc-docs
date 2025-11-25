# Navigating Your VC-Shell Application: A Comprehensive Overview

VC-Shell employs a flexible and multi-layered navigation system designed to provide a seamless user experience, especially in complex applications. This guide serves as a high-level map to the various navigation mechanisms available, directing you to more detailed documentation for each specific feature. Understanding these concepts will help you build intuitive and efficient workflows for your users.

## Core Navigation Systems

VC-Shell applications utilize several primary systems for navigation:

### Page-Based Routing (Vue Router)

At its foundation, VC-Shell uses Vue Router for traditional page-based navigation. This system is configured in the `src/router/routes.ts` file and is used for:

- Defining the main application layout.
- Registering primary pages, like a main dashboard, that render within the application.
- Handling standalone pages, such as login or password reset pages.

This is the primary mechanism for assigning a persistent URL to a view.

For a complete guide on setting up **routes.ts**, adding pages, and understanding critical options like `meta: { root: true }`, see [Routing configuration](./../Guides/routing-configuration.md)

### Blade Navigation System

The "blade" system is a hallmark of VC-Shell, offering a powerful way to manage contextual, slide-in panels. Blades allow users to drill down into details or access related tasks without losing their place in the main workflow.

While blades are components managed by `useBladeNavigation`, they can also be accessed via direct URLs. This is made possible by a "catch-all" route in **routes.ts** that uses a resolver to find and display the correct blade.

![Readmore](/platform/developer-guide/latest/custom-apps-development/media/readmore.png){: width="25"} [Primary composable. UseBladeNavigation](./shared/components/blade-navigation.md)

![Readmore](/platform/developer-guide/latest/custom-apps-development/media/readmore.png){: width="25"} [Working with blade navigation](./Usage-Guides/working-with-blade-navigation.md)

![Readmore](/platform/developer-guide/latest/custom-apps-development/media/readmore.png){: width="25"} [UI components. VC-blade](./ui-components/vc-blade.md)

![Readmore](/platform/developer-guide/latest/custom-apps-development/media/readmore.png){: width="25"} [Router integration details](./../Guides/routing-configuration.md)

### Main Application Menu (Sidebar/App Menu)

The primary navigation menu provides top-level entry points into your application's modules and key features. Menu items can be registered for both router pages and blades.

![Readmore](/platform/developer-guide/latest/custom-apps-development/media/readmore.png){: width="25"} [Building navigation menus with usemenuservice](./Usage-Guides/building-navigation-menus-with-usemenuservice.md)

![Readmore](/platform/developer-guide/latest/custom-apps-development/media/readmore.png){: width="25"} [Adding custom pages and menu items](./Usage-Guides/adding-custom-pages-and-menu-items.md)

## Choosing the Right Navigation System

VC-Shell offers multiple navigation tools, and choosing the right one depends on the context:

-   **Vue Router**: Use for primary application pages that represent distinct sections or when a unique browser URL is essential for direct access, bookmarking, or sharing (e.g., main dashboard, settings sections, login page).
-   **Blade Navigation (`useBladeNavigation`)**: Ideal for contextual tasks, detail views, or multi-step workflows that slide in over the current view without a full page reload. Blades excel at master-detail patterns and keeping users within a specific workflow.
-   **Main Application Menu (`useMenuService`)**: For top-level navigation, providing users with access to major modules and workspaces.

These systems work together. For example, a menu item registered via `useMenuService` might link to a standard page route (like `/dashboard`). Another menu item, often registered automatically from a blade's `defineOptions`, will navigate to a URL (e.g., `/products`) that is then resolved by the router's "catch-all" mechanism to open the corresponding blade.

## Key Navigational UI Components & Features

Beyond the core systems, VC-Shell offers several UI components and composables that enhance navigation and user orientation:

### Breadcrumbs

Breadcrumbs provide users with a clear trail of their navigation path, allowing them to easily understand their current location within the application's hierarchy and navigate back to previous levels.

![Readmore](/platform/developer-guide/latest/custom-apps-development/media/readmore.png){: width="25"} [Implementing navigational breadcrumbs with usebreadcrumbs](./Usage-Guides/implementing-navigational-breadcrumbs-with-usebreadcrumbs.md)

![Readmore](/platform/developer-guide/latest/custom-apps-development/media/readmore.png){: width="25"} [UI component. VC breadcrumbs](./ui-components/vc-breadcrumbs.md)

### App Bar Widgets

The application's top bar can be extended with custom widgets. These widgets can serve as quick access points to features, display status information, or trigger actions, contributing to the overall navigation and interaction flow.

![Readmore](/platform/developer-guide/latest/custom-apps-development/media/readmore.png){: width="25"} [Adding app bar widgets with useappbarwidget](./Usage-Guides/adding-app-bar-widgets-with-useappbarwidget.md)

### Settings Menu

VC-Shell applications often feature a dedicated settings area. The framework provides tools to manage and extend this settings menu, allowing modules to register their own settings pages.

![Readmore](/platform/developer-guide/latest/custom-apps-development/media/readmore.png){: width="25"} [Managing settings menu with usesettingsmenu](./Usage-Guides/managing-settings-menu-with-usesettingsmenu.md)

### Blade Toolbar Items

Toolbars within blades provide contextual actions relevant to the blade's content. These are crucial for in-blade navigation and task execution.

![Readmore](/platform/developer-guide/latest/custom-apps-development/media/readmore.png){: width="25"} [Managing blade toolbars with usetoolbar](./Usage-Guides/managing-blade-toolbars-with-usetoolbar.md)

## Programmatic Navigation

In addition to user-initiated navigation through UI elements, you will often need to navigate programmatically:

- **Vue Router**: Use `router.push()` or `router.replace()` for navigating to standard page routes.
    ```typescript
        import { useRouter } from 'vue-router';
        const router = useRouter();
        router.push({ name: 'MyPageRouteName' });
    ```

- **Blade Navigation**: Use the `openBlade` method from `useBladeNavigation` to programmatically open, control, and pass parameters to blades.
    ```typescript
        import { useBladeNavigation } from '@vc-shell/framework';
        const { openBlade } = useBladeNavigation();
        openBlade({ blade: { name: 'MyTargetBlade' }, param: 'someId' });
    ```

Refer to the specific guides linked above for more details on programmatic control within each system.

