# Core Concepts of a Custom VC-Shell Application

Understanding a few core concepts is essential before diving into module development. These concepts define how your custom application interacts with the VC-Shell framework and how its different parts are organized.

For a visual understanding of the typical application layout, including the main UI areas like the sidebar, app bar, and content area, please refer to the **[Understanding Application Layout Guide](../Essentials/understanding-application-layout.md)**.

## Relationship with `@vc-shell/framework`

Your custom application is built *on top of* the `@vc-shell/framework`. The framework provides:

-   **Core Services and Composables**: A rich set of reusable utilities for common tasks like user authentication (`useUser`), permissions (`usePermissions`), internationalization (`useLanguages`), displaying notifications (`notification` service, `useNotifications`), managing API clients (`useApiClient`), and much more. You will import these directly from `@vc-shell/framework`.
-   **UI Components**: A library of pre-built Vue components (e.g., `VcButton`, `VcInput`, `VcTable`, `VcBlade`, `VcApp`) that ensure a consistent look and feel, adhering to the Virto Commerce design system. These are also imported from the framework.
-   **Architectural Patterns**: The framework promotes a modular architecture, a blade-based navigation system, and conventions for state management and routing.
-   **Build Tools and Configuration**: Standardized configurations for Vite, TypeScript, TailwindCSS, etc.

Your application consumes these framework features, extends them where necessary, and adds its unique business logic and UI through custom modules and components.

## The Importance of the Module-Based Architecture

VC-Shell applications are designed to be highly modular. A **module** is a self-contained unit of functionality that typically corresponds to a specific business domain or feature set (e.g., "Product Management", "Order Processing", "User Profiles").

**Benefits of Modularity:**

-   **Separation of Concerns**: Each module focuses on a specific area, making the codebase easier to understand, maintain, and test.
-   **Reusability**: Modules can potentially be reused across different applications (though custom app modules are often tailored).
-   **Team Collaboration**: Different teams can work on different modules independently, reducing conflicts.
-   **Scalability**: Easier to add new features as new modules or extend existing ones without impacting the entire application significantly.

Your application will be composed of one or more custom modules, alongside any core functionalities provided directly by the framework.


## Routing and Navigation

Routing in VC-Shell applications is handled by **Vue Router** but has a specific structure to support the framework's features, especially blade navigation. The framework integrates seamlessly with it. Here's an overview of the key concepts:

-   **Main Application Router (`src/router/`)**: This is where you define top-level routes for your application, such as the main application shell, standalone pages like login, and a "catch-all" route for blade navigation. The main configuration file is `src/router/routes.ts`.

-   **Module-Specific Routing & Blade Pages**: Most pages within modules are "blades." Their routes are automatically registered if they have a `url` property in their `defineOptions`. This allows modules to be self-contained without needing to modify the central router configuration for every new page.

-   **Application Layout vs. Standalone Pages**: Pages that should appear inside the main application interface (with a shared header and menu) must be defined as `children` of the main `App` route. Standalone pages like `Login` or `Invite` have their own layout and are defined as top-level routes.

For a detailed guide on how to configure `routes.ts`, add pages, and understand the routing mechanism for blades, please refer to the **[Routing and Navigation Configuration Guide](./routing-configuration.md)**.

## State Management Approaches

VC-Shell applications primarily leverage Vue 3's Composition API for state management, promoting a decentralized and composable approach:

-   **Local Component State**: Use `ref` and `reactive` for state that is local to a single component.
-   **Composables**: For state that needs to be shared between components or across a specific feature, create composables. These functions can encapsulate reactive state (`ref`, `reactive`, `computed`) and related logic. This is the most common pattern for shared state within modules or even across the application if a composable is placed in `src/composables/`.
-   **Provide/Inject**: For more deeply nested component trees or for providing services/state at a module or application level, Vue's `provide` and `inject` mechanism is used. The framework itself uses this for providing core services.

The default VC-Shell architecture encourages using the Composition API's built-in tools and composables for most state management needs, which aligns well with the modular structure.

## API Client Integration

Communicating with backend services is a crucial part of any application.

-   **Generated Clients (`src/api_client/`)**: As mentioned, this directory is for API clients generated from your backend's OpenAPI (Swagger) specification. The `@vc-shell/api-client-generator` tool is provided for this purpose.
-   **`useApiClient` Composable**: The framework provides the `useApiClient` composable from `@vc-shell/framework`. This composable is a factory that you use to get an instance of your API client (whether it's a platform client or a custom generated one). It handles aspects like injecting authentication tokens automatically.

For detailed information on generating, configuring, and using API clients, refer to the following guides:

-   [API Integration Overview](../Essentials/API-Integration/api-client-integration.md)
-   [Using `useApiClient`](../Essentials/Usage-Guides/using-api-clients-with-useapiclient.md)

Understanding these core concepts will provide a solid foundation as we move into the specifics of developing custom modules for your VC-Shell application.
