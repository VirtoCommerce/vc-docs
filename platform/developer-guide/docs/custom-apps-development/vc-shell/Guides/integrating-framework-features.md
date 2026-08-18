# Integrating Framework Features in Your Custom Application

Once you have a grasp of creating applications, developing modules, and understanding architectural best practices, the next step is to effectively integrate the rich set of features provided by the `@vc-shell/framework`. This framework offers numerous composables (Vue Composition API functions) and services designed to accelerate development and provide common functionalities out-of-the-box.

This guide provides an overview of the key framework features and, crucially, directs you to the detailed "How-To" guides located in the `Essentials/Usage-Guides/` directory for in-depth explanations and usage examples.

## Introduction to VC-Shell Composables and Services

The `@vc-shell/framework` is packed with utilities to handle common application concerns. These are generally exposed as Vue composables (functions you call within your component's `setup` script or other composables) or, in some cases, as injectable services.

Key categories of features include:

-   **UI & Layout Management**: Tools for building and controlling the user interface, navigation elements, and overall application layout (e.g., app bar, side menus, dashboards, blades, popups). Provides consistency and accelerates UI development.
-   **Navigation & Routing**: Helpers for managing application navigation, breadcrumbs, and menu services, ensuring intuitive user flows.
-   **Data Handling & API Interaction**: Utilities for making API calls, managing asynchronous operations, and working with API clients, simplifying backend communication.
-   **User Management & Permissions**: Functions for accessing user information, checking permissions, and controlling access to features, crucial for security and personalization.
-   **Notifications & User Feedback**: Services for displaying toast notifications and managing push notifications, enhancing user engagement and awareness.
-   **State Management & Events**: Composables for managing global or local loading states, handling browser events, and more, facilitating reactive and dynamic applications.
-   **Forms & Validation**: Support for implementing form validation within your application's views (often blades), improving data quality.
-   **Modularity & Plugins**: Core mechanisms for module registration, internationalization (i18n), and other plugin-based extensions, enabling scalable and extensible applications.
-   **Error Handling & Telemetry**: Centralized error handling and integration with application insights for monitoring, leading to more robust applications.
-   **Settings & Configuration**: Tools for managing application and user settings, allowing for customization and flexibility.

Instead of re-implementing these common patterns, you should always look to the framework first. This not only saves development time but also ensures consistency with the broader VC-Shell ecosystem.
