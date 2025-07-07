# Create First VC-Shell Application

In this section we will show you how to scaffold a VC-Shell application on your local machine. The created project will use Vue 3 and Vite as the build setup.

**Prerequisites**:

* You have an up-to-date installation of Node.js.
* Your current working directory is set to the location where you want to create the application.

To create and install custom app:

1. Install and run the `create-vc-app` scaffolding tool using one of the following commands:

    === "With NPM"

        ```bash
        npm create @vc-shell/vc-app@latest
        ```

    === "With NPX"

        ```bash
        npx @vc-shell/create-vc-app@latest
        ```

    === "With Yarn"

        ```bash
        yarn create @vc-shell/vc-app
        ```

## Interactive Mode (Default)

1. Configure the options based on your requirements. If you are unsure about an option, simply choose **No** by clicking **Enter**:

    ```bash
    ✔ Project name: … *your-app-name*
    ✔ Base path: … /apps/*your-app-name*/
    ? Select module variant: › - Use arrow-keys. Return to submit.
    ❯   Classic view modules boilerplate
    Module name: › *your-module-name*
    ? Do you want to include additional module with sample data? › (y/N)

    Scaffolding app in /*your-app-name*...

    Done. You can now run application:

    cd vc-app
    yarn
    yarn serve
    ```

## Non-Interactive Mode

For automation, or when you want to skip prompts, you can use command line arguments:

```bash
npx @vc-shell/create-vc-app@latest my-app --variant classic --module-name "My Module" --mocks
```

### Available Options

| Option | Description | Default |
|--------|-------------|---------|
| `--name`, `--app-name` | Name of the application | Directory name |
| `--package-name` | Package name | App name (validated) |
| `--variant` | Module variant (classic\|dynamic) | `classic` |
| `--module-name` | Module name | App name in title case |
| `--base-path` | Base path for the application | `/apps/<app-name>/` |
| `--mocks` | Include additional module with sample data | `false` |
| `--overwrite` | Overwrite existing files without confirmation | `false` |
| `--help`, `-h` | Show help message | - |
| `--version`, `-v` | Show version | - |

### Examples

**Basic usage:**
```bash
npx @vc-shell/create-vc-app@latest my-app --variant classic
```

**With custom options:**
```bash
npx @vc-shell/create-vc-app@latest my-app --variant classic --module-name "My Module" --mocks
```

**Full non-interactive example:**
```bash
npx @vc-shell/create-vc-app@latest my-ecommerce-app \
  --variant classic \
  --module-name "Product Catalog" \
  --base-path "/apps/ecommerce/" \
  --package-name "@mycompany/ecommerce-app" \
  --mocks \
  --overwrite
```

**For CI/CD automation:**
```bash
npx @vc-shell/create-vc-app@latest $PROJECT_NAME \
  --variant classic \
  --module-name "$MODULE_NAME" \
  --overwrite
```

## Configuration

1. Once the application is created, go to the application folder and add Platform URL to the **.env.local** file under the **APP_PLATFORM_URL** variable:

    ```bash
    $ cd `*your-app-name*`
    $ echo "APP_PLATFORM_URL=https://your_platform_url_here" >> .env.local
    ```

1. Install the dependencies and start the development server:

Your first VC-Shell application is now ready to run!

![New app](../../media/new-app.png)

!!! note
    The example components in the generated application are written using the Vue Composition API and `<script setup>`.

!!! tip
    For an optimal development experience, we recommend using [Visual Studio Code](https://code.visualstudio.com/) with the [Volar extension](https://marketplace.visualstudio.com/items?itemName=Vue.volar).

!!! info "Getting Help"
    You can always get help for the scaffolding tool by running:
    ```bash
    npx @vc-shell/create-vc-app@latest --help
    ```

![Readmore](../../media/readmore.png){: width="25"} [Vite tools](https://vitejs.dev/)

![Readmore](../../media/readmore.png){: width="25"} [Vue Composition API](https://vuejs.org/guide/introduction.html#composition-api)

## Application folder structure

After the application is scaffolded, the folder structure will look as follows. This structure is designed to promote modularity and maintainability.

![Readmore](../../media/readmore.png){: width="25"} [Application architecture](../Guides/application-architecture-best-practices.md)

![Readmore](../../media/readmore.png){: width="25"} [Creating custom applications](../Guides/creating-custom-applications.md)

```css
├─ public                         // Static assets (images, fonts, etc.) that are served directly by the web server.
│  ├─ assets                      // Static images, fonts, etc., used inside the application.
│  └─ img
│     └─ icons                    // Icons used for favicons, PWA manifests, etc.
├─ src                            // Main application source code.
│  ├─ api_client                  // Auto-generated API client (e.g., from OpenAPI/Swagger).
│  │  └─...
│  ├─ composables                 // Application-wide Vue composables (reusable stateful logic).
│  │  └─...
│  ├─ locales                     // Localization files (e.g., en.json, es.json) for application-level translations.
│  │  └─ en.json
│  ├─ modules                     // The collection of custom business modules. This is where most of your application's features will reside.
│  │  └─ your-module-name/        // Example module folder.
│  │     ├─ components            // Components specific to this module.
│  │     │  ├─ notifications      // Dropdown notification templates for this module.
│  │     │  └─ ...
│  │     ├─ composables           // Composables specific to this module.
│  │     ├─ locales               // Locale files specific to this module.
│  │     ├─ pages                 // Blade components (pages) for this module.
│  │     └─ index.ts              // Module entry point, registers the module with the framework.
│  ├─ pages                       // Application-level pages (e.g., NotFound, Login - though login is often part of the framework).
│  │  └─...
│  ├─ router                      // Vue Router configuration (routes, guards).
│  │  └─ index.ts
│  ├─ styles                      // Global styles, TailwindCSS setup, custom themes.
│  │  ├─ index.scss               // Main SCSS file, imports Tailwind and custom styles.
│  │  └─ custom.scss              // (Optional) Your custom SCSS overrides and theme definitions.
│  ├─ types                       // Global TypeScript type definitions (.d.ts files).
│  │  └─ ...
│  ├─ App.vue                     // Root Vue component.
│  └─ main.ts                     // Main application entry point (initializes Vue, router, plugins, modules).
```

### Core concepts

It is helpful to understand some core concepts of the VC-Shell framework. These are covered extensively in the [Custom application core concepts guide](../Guides/custom-application-core-concepts.md). In brief:

*   **VC-Shell framework** (`@vc-shell/framework`): Provides the foundational UI, services (like navigation, notifications, API client integration), and architectural patterns for building administrative UIs.
*   **Modularity**: Applications are built as a collection of independent modules. Each module encapsulates a specific business domain or feature set. This is detailed in the [Developing custom modules guide](../Guides/developing-custom-modules.md).
*   **Blade navigation**: The primary UI paradigm. Blades are individual panels or pages that can be opened, closed, and stacked, providing a focused user experience for specific tasks.
*   **Routing**: Managed by Vue Router, integrated with the blade system.
*   **State management**: While VC-Shell doesn't enforce a specific global state management library like Pinia or Vuex out-of-the-box for custom apps, it provides patterns for managing local state within composables and communication between blades. Shared services and composables are common for cross-cutting concerns.
*   **API client integration**: Uses `useApiClient()` composable for easy integration with generated API clients.

Let's take a look at the modules directory as it represents the key concept in the application's architecture.

### Modules directory structure

A **module** is a self-contained unit that groups related functionality. It typically includes its own components, composables, localization files, and pages (blades). This structure ensures separation of concerns and makes the application easier to scale and maintain.

![Readmore](../../media/readmore.png){: width="25"} [Developing custom VC-Shell modules](../Guides/developing-custom-modules.md)

| Folder               	| Description                                                                                                                                            |
|--------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| components  	        | Contains Vue components that are specific to this module. These components are typically used within the module's blades or other module components. If a component needs to be used across multiple modules or globally, consider placing it in `src/components` or a shared UI library. |
| composables        	| Vue Composition API functions specific to this module. They encapsulate reactive logic, state management, or business rules relevant to the module's domain (e.g., fetching and managing data for a specific entity).                  	|
| locales      	        | Module-specific translation files (e.g., **en.json**, **es.json**). These are merged with application-level locales to provide localized content for the module's UI.<br> ![Readmore](../../media/readmore.png){: width="25"} [Internationalization](../Guides/internationalization.md) |
| pages                 | Contains the module's **blade** components. Blades are essentially Vue components that represent a distinct view or screen within the module, often corresponding to a specific route or a step in a workflow. They are registered with the framework to participate in navigation. |
| index.ts              | The entry point for the module. This file typically uses the `createAppModule` function from `@vc-shell/framework` to register the module's pages, locales, notification templates, and other components with the main application.     |


### Create new module

To create your own modules within the scaffolded application folder structure:

1.  Create a new folder for your module inside the **src/modules** directory. Choose a descriptive name that reflects its functionality (e.g., **products**, **orders**, **reviews**).
1.  Inside your module folder, create the standard subdirectories: **components**, **composables**, **locales**, and **pages**.
1.  Create an **index.ts** file in the root of your module folder. This will be the entry point for registering your module.

### Initialize new module in application

All modules are created as Vue plugins. The `@vc-shell/framework` provides a helper function, `createAppModule`, to simplify their creation and registration. This function takes the module's pages, locales, notification templates, and other module-specific components as arguments.

Here's an example of a typical module **index.ts**:

```typescript title="src/modules/your-module-name/index.ts" linenums="1"
// Import all blade components from the 'pages' directory
import * as pages from "./pages";
// Import all locale files from the 'locales' directory
import * as locales from "./locales";
// (Optional) Import notification templates if your module uses them
// import * as notificationTemplates from "./components/notifications";
// (Optional) Import any other components that need to be globally registered by this module
// import * as moduleComponents from "./components"; // e.g., components to be used in this module

// Import createAppModule from the VC-Shell framework
import { createAppModule } from "@vc-shell/framework";

// Define the module.
// The first argument is an object mapping page names to their constructors.
// The second argument is an object mapping locale names to their content.
// The third (optional) argument is for notification templates.
// The fourth (optional) argument is for other module-specific components.
export default createAppModule(
  pages,
  locales
  // notificationTemplates, // Uncomment if you have notification templates
  // moduleComponents       // Uncomment if you have other components to register
);

// It's good practice to also export key parts of your module for potential direct import elsewhere,
// though direct inter-module dependencies should be minimized.
export * from "./pages"; // Typically, blades are what other parts of the system might want to navigate to.
export * from "./composables"; // If you have composables that might be useful outside the module (use with caution).
// export * from "./components"; // Only if certain components are designed for external use.
export * from "./types"; // Exporting module-specific types is often necessary.
```

**Explanation of `createAppModule` arguments:**

| Argument                  | Description |
|---------------------------|-------------|
| `pages`                   | An object where keys are page (blade) names and values are the corresponding Vue component constructors (e.g., `Record<string, BladeInstanceConstructor>`).<br>These pages will be registered with the blade navigation system. |
| `locales`                 | An object where keys are locale codes (e.g., `"en"`, `"es"`) and values are objects containing the translation strings for that locale (e.g., `Record<string, Record<string, string>>`). <br>These will be merged with the application's global i18n instance. |
| `notificationTemplates` (optional) | An object mapping notification template names to their Vue component constructors.<br>Used for custom notification rendering. |
| `moduleComponents` (optional)      | An object mapping component names to their Vue component constructors. <br> These components will be registered globally. |


After creating your module's **index.ts**, you need to import and register it in your main application file (**src/main.ts**).

![Readmore](../../media/readmore.png){: width="25"} [Loading modules into main application](../Guides/developing-custom-modules.md#how-modules-are-loaded-into-the-main-application)

Your module is now ready for use within your application.

![Readmore](../../media/readmore.png){: width="25"} [Adding new module to navigation menu](../Essentials/Usage-Guides/building-navigation-menus-with-usemenuservice.md)
