# Application Architecture and Best Practices

This guide explores best practices for structuring your VC-Shell application, organizing code, managing styles, and leveraging TypeScript to build robust and maintainable solutions. It assumes you have a foundational understanding of creating applications and developing modules as covered in the preceding guides.

## Application architecture

While the VC-Shell framework provides a solid structure, adhering to certain architectural best practices will help you build scalable, maintainable, and high-quality applications.

### Code organization

A well-organized codebase is crucial for long-term maintainability and team collaboration. Here are guidelines for structuring directories at both the application and module levels.

#### Application level (`src/`)

| Path                    | Description | Example                   |
|-------------------------|----------------------------------------|------------------------------------------------------------------------------------------|
| `src/api_client/`       | Primarily for API clients generated from OpenAPI specs (e.g., with `@vc-shell/api-client-generator`).<br> Avoid manually written data-fetching logic here; that belongs in composables.              | |
| `src/composables/`      | For **truly global** Vue composables shareable across modules or used app-wide. <br> If a composable is only used by one module, it belongs in that module's `composables/` directory. | `useGlobalSearch()`, `useFeatureFlag()`, or a composable that manages a global application state like a shopping cart (`useShoppingCart()`) |
| `src/locales/`          | Application-wide translation files. <br>These typically contain translations for the main application shell,<br> shared components (like login pages if not part of a module), and any text not specific to a particular module.  | **en.json**  |
| `src/modules/`          | The heart of your application's features. Each subdirectory is a self-contained module (covered in detail in [Developing custom VC-Shell modules](developing-custom-modules.md)). |  |
| `src/pages/`            | For global Vue components that act as pages and are **not** part of any specific module.               | **NotFoundPage.vue** (404 error), **UnauthorizedPage.vue** |
| `src/router/`           | Vue Router setup. **index.ts** initializes the Vue Router instance, **routes.ts** defines main application-level routes, including routes for authentication (login, reset password), the 404 page, and any other routes not handled by modules. Module routes are typically registered automatically via **createAppModule**. | **index.ts**, **routes.ts** |
| `src/services/`         | (Optional, create if needed) For plain TypeScript classes or functions that encapsulate application-wide business logic or interact with third-party services (not directly UI-related).<br> If a service is only used by one module, consider if it can be a simple utility function within that module or if its logic can be part of a module-specific composable. | **AnalyticsService.ts** that wraps a third-party analytics library, **LocalStorageService.ts**  for complex local storage interactions |
| `src/styles/`           | Global SCSS styles. **index.scss** imports Tailwind base, components, utilities. Define any custom global styles or overrides here.<br> You might have other SCSS partials here for global variables, mixins, or base styling. | **index.scss** or similar       |
| `src/types/`            | For global TypeScript type definitions, interfaces, and enums that are used across multiple modules or are fundamental to the application. <Module-specific types should reside within the respective module's `types/` directory.> | **CurrentUser.d.ts**, **GlobalSettings.d.ts**  |
| `src/utils/`            | (Optional, create if needed) For general-purpose utility functions that are not Vue composables and are shareable across the application. If a utility is only used by one module, it belongs in that module's **utils/** directory (create one if needed) or could even be a static method within a relevant class/composable. | Date formatting functions, string manipulation utilities, validation helpers (if not part of a composable like Vuelidate). |


#### Module level (`src/modules/your-module-name/`)

| Path                    | Description |
|-------------------------|------------ |
| `components/`           | For Vue components specific to and reusable within that module.|
| `composables/`          | For Vue composables containing business logic and state management specific to that module. |
| `locales/`              | Module-specific translation files. |
| `pages/`                | Vue components that act as pages or blades for the module, registered with the router.|
| `services/` (Optional, create if needed within a module)| If a module has complex, non-UI business logic that doesn't fit neatly into a composable, you might create a service class here. <br>   **Example**: A `ComplexCalculationService` within a finance module.|
| `types/` (Optional, create if needed within a module)| For TypeScript types, interfaces, and enums that are specific to this module's domain. |
| `utils/` (Optional, create if needed within a module) | For utility functions used only by this module.|

![Readmore](/platform/developer-guide/latest/custom-apps-development/media/readmore.png){: width="25"} [Developing custom VC-Shell modules](developing-custom-modules.md)



**General principles for code organization:**

*   **Colocation**: Keep related files together. If a component, its composable, its types, and its tests are all part of the same feature within a module, they should reside close to each other within that module's structure.
*   **High cohesion, low coupling**: Aim for modules and components that have a single, well-defined responsibility (high cohesion) and minimize direct dependencies on other unrelated modules/components (low coupling).
*   **Clear naming**: Use descriptive and consistent names for files, folders, variables, functions, and classes.

### Styling approach

Consistent and maintainable styling is key to a good user experience and developer productivity. VC-Shell applications primarily use SCSS and TailwindCSS.

#### Global styles (`src/styles/index.scss`)

Your application's **src/styles/index.scss** (or a similarly named main **SCSS** file) is the centralized entry point for managing global styles, including theme customization, TailwindCSS imports, and overrides.

This file typically brings together all foundational styling aspects of your app. Below are the key elements you’ll usually include or manage in it:

-   **Importing custom styles and theme definitions**: It's a common and recommended practice for **index.scss** to import a dedicated file for custom application-specific styles, new theme definitions, and overrides for existing themes. This file is often named **custom.scss** (or **_custom.scss** if structured as a SASS partial to be imported with `@use 'custom';`).
    ```scss
    // Example structure for src/styles/index.scss
    // 1. Import custom theme definitions and overrides first
    @use 'custom';

    // 2. Import Tailwind CSS base, components, and utilities
    @tailwind base;
    @tailwind components;
    @tailwind utilities;


    // 3. Other global application-specific styles (if any and not in custom.scss)
    ```
    
    Your **custom.scss** file is the primary location where you would:
    
    - Define CSS variable blocks for new themes (e.g., `:root[data-theme="your-new-theme"] { --primary-500: #0000FF; /* ... */ }`), or
    - Provide overrides for variables of existing themes (e.g., `:root[data-theme="light"] { --primary-500: #AA00BB; }`). 
    
    ![Readmore](/platform/developer-guide/latest/custom-apps-development/media/readmore.png){: width="25"} [Managing application themes with **useTheme**](../Essentials/Usage-Guides/managing-themes-with-usetheme.md)

-   **TailwindCSS imports**: This file should import TailwindCSS's base styles, components, and utilities, typically after your custom theme definitions to ensure correct cascade if Tailwind utilities also use CSS variables affected by themes.

    ```scss
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```

-   **Global SCSS variables**: If you use global SCSS variables (e.g., for utility mixins, or variables that are not part of the dynamic CSS custom property theming system), they can be defined here or in a separate imported partial (e.g., **_variables.scss**). These SCSS variables are distinct from the CSS Custom Properties used for runtime theming but can sometimes be used to help generate those CSS Custom Properties within your theme definitions in **custom.scss**.

    ```scss
    // Example: src/styles/_variables.scss
    // $custom-brand-color: #FF5733;
    // $global-border-radius: 4px;
    ```

    ```scss
    // Example: src/styles/index.scss
    // @use 'variables'; // Import custom variables

    @tailwind base;
    @tailwind components;
    @tailwind utilities;

    // ... rest of tailwind imports
    ```

-   **Third-party library overrides**: If you're using third-party libraries that inject their own styles, you might need to override them here to ensure they align with your application's design system.

#### Tailwind CSS usage and configuration

Tailwind CSS is the recommended utility-first CSS framework for styling VC-Shell applications. It allows for rapid UI development by composing utility classes directly in your templates.

The key principles for Tailwind CSS in VC-Shell are as follows:

* **Embrace utility-first**: Prioritize using Tailwind's utility classes (e.g., **tw-text-lg**, **tw-p-4**, **tw-flex**) directly in your Vue component templates.
* **Prefixing**: VC-Shell framework's Tailwind configuration uses the **tw-** prefix for all utility classes to avoid conflicts with other CSS or component library styles. Always use this prefix (e.g., **class="tw-bg-primary-500 tw-text-white"**).
*   **Configuration inheritance**: Your application's Tailwind configuration should extend the base configuration provided by `@vc-shell/framework`. This ensures consistency with the framework's design system (colors, spacing, fonts, etc.) and allows you to easily customize or extend it. The theme values (like specific shades for **primary-500**) are typically defined as CSS custom properties (e.g., `var(--primary-500)`) in theme-specific blocks (`:root[data-theme="..."]`). For framework-provided themes, these are in framework styles; for your custom themes or overrides, these definitions reside in your application's **custom.scss** file (or equivalent).
*   **Scoped styles for complex components**: While utility classes are preferred, for very complex component-specific styles that are hard to achieve with utilities alone, use `<style lang="scss" scoped>`. Within these scoped styles, you can still leverage Tailwind's theme values using the `@apply` directive (if needed, though direct utility usage is often cleaner) or CSS variables provided by the framework's theme (e.g., `var(--primary-500)`).
*   **Purging**: Ensure your **tailwind.config.ts** is correctly configured to scan your project files (**.vue**, **.ts**, etc.) so that unused Tailwind classes are removed from the production build, keeping your CSS bundle size optimized.

Example **tailwind.config.ts** (application level):

Your application's **tailwind.config.ts** should look similar to this, extending the framework's default configuration:

```typescript
// tailwind.config.ts
import type { Config } from "tailwindcss";
// Import the default configuration and content paths from the VC-Shell framework
import defaultConfig, { content as frameworkContent } from "@vc-shell/framework/tailwind.config";

const config: Config = {
  // Start with the framework's content paths and add your application-specific paths
          content: [
    ...frameworkContent, // Includes paths for framework components and UI elements
    "./src/**/*.{vue,js,ts,jsx,tsx}", // Scan your app's source files
    // Add paths to any other modules or packages that contain templates using Tailwind classes
  ],
  // Use the theme directly from the framework's default configuration.
  // This includes colors, spacing, typography, etc., defined by VC-Shell.
  theme: defaultConfig.theme, // Inherit the entire theme from the framework,
  // Crucially, use the "tw-" prefix as defined in the framework's configuration.
  // This is typically inherited if defaultConfig includes it, but explicitly stating it 
  // or ensuring it is part of defaultConfig is important.
  prefix: defaultConfig.prefix || "tw-", // Ensures "tw-" prefix is used
};

export default config;
```

Explanation:

*   `import defaultConfig, { content as frameworkContent } from "@vc-shell/framework/tailwind.config";`: This line is key. It imports the base Tailwind configuration and the default content paths from the VC-Shell framework.
*   `content`: You spread the `frameworkContent` and add your application-specific paths (like `./src/**/*.{vue,js,ts,jsx,tsx}`). This ensures Tailwind scans both framework components and your application components for used utility classes.
*   `theme`: By setting `theme: { ...defaultConfig.theme, ... }`, you inherit all the predefined spacing units, typography, etc., from the VC-Shell design system. 
*   `prefix: defaultConfig.prefix || "tw-"`: This line ensures that your application's Tailwind build uses the same `tw-` prefix as the framework. This is vital for consistency and avoiding CSS class name collisions.

**Using tailwind classes in Vue components:**

```vue
<template>
  <div class="tw-bg-neutral-100 tw-p-4 tw-rounded-lg tw-shadow">
    <h3 class="tw-text-xl tw-font-semibold tw-text-primary-700">
      My Styled Card
    </h3>
    <p class="tw-mt-2 tw-text-neutral-600">
      This component uses Tailwind utility classes with the `tw-` prefix.
    </p>
    <button
      class="tw-mt-4 tw-px-4 tw-py-2 tw-bg-primary-500 tw-text-white tw-rounded
             hover:tw-bg-primary-600 focus:tw-outline-none 
             focus:tw-ring-2 focus:tw-ring-primary-300"
    >
      Click me
    </button>
  </div>
</template>

<script lang="ts" setup>
// Component logic
</script>

<!-- For more complex, component-specific styles -->
<style lang="scss" scoped>
.my-custom-element {
  // You can still use CSS variables from the VC-Shell theme
  border-left: 4px solid var(--primary-500);
  background-color: var(--neutral-50); // Lighter neutral for background

  &:hover {
    border-left-color: var(--primary-700);
  }
}
</style>
```

By following this approach, your application will seamlessly integrate with VC-Shell's styling, benefit from a pre-configured design system, and maintain optimized CSS.

### Managing static assets (`public/` directory)

The **public/** directory in the root of your VC-Shell application is used for static assets that don't go through the Vite build process directly but need to be available at predictable URLs or are referenced directly in your `index.html`.

The **public/** includes:

-   **index.html**: While not strictly a static asset you add, **index.html** resides here and is the entry point for your SPA. Vite processes this file.
-   **favicon**: A favicon (e.g., **favicon.ico**).
-   **Global images**: Images that are referenced directly by URL and are not meant to be processed by Vite as part of your Vue components. These are typically placed in **public/img/** or **public/assets/img/**.

The **/public/** works as follows:

-   **Direct copy**: During the build process (`yarn build`), Vite copies all files from the **public/** directory to the root of your output directory (usually **dist/**).
-   **No hashing**: Unlike assets imported into your JavaScript/Vue components (which get hashed filenames for cache busting), files in **public/** retain their original names.
-   **Root path access**: Files in **public/** can be referenced from your **index.html** or JavaScript code using an absolute path starting from the base of your application. For example, if you have **public/img/logo.png**, you can reference it in **index.html** as **/img/logo.png** (assuming your application is served from the root of its domain).

Below is the example **public/** directory structure (aligned with **vendor-portal** common structure):

```
public/
├── assets/                     # General static assets folder
│   └── img/                    # Optional: for general static images
│       └── some-banner.jpg
├── img/
│   └── icons/                  # For favicon
│       └── favicon.ico
├── favicon.ico
```

#### When not to use `public/`

* **Component-specific images/assets**: Images, SVGs, fonts, or other assets that are directly used and styled within your Vue components should be placed in your `src/assets/` directory (or a module-specific `assets/` folder) and imported into your components. Vite will then process these assets, optimize them, and hash their filenames for better caching.

    ```vue
    <template>
      <img :src="MyImage" alt="Description" />
    </template>

    <script lang="ts" setup>
    import MyImage from '@/assets/images/my-component-image.png'; // Vite processes this
    </script>
    ```

* **Stylesheets (CSS/SCSS)**: These should always be part of your `src/styles/` or component styles and processed by Vite and PostCSS/SCSS.

* **JavaScript/TypeScript files**: All your application logic should be within `src/` and be part of the Vite build process.

**Base URL considerations:**

If your application is deployed under a nested public path (e.g., **https://example.com/my-app/**), you'll need to configure the `base` option in your **vite.config.ts**. When referencing assets from `public/` in your JavaScript code, you might need to be mindful of this base path. Vite automatically handles this for references in `index.html` and for imported assets within `src/`.

For most assets that are part of your application's UI and logic, prefer importing them directly within your `src/` directory. Reserve the `public/` directory for assets that genuinely need to be served statically from the root with unchanged filenames.

### TypeScript usage

Leveraging TypeScript effectively is paramount in building robust, scalable, and maintainable VC-Shell applications. The framework itself is built with TypeScript, and its usage is strongly encouraged for custom application development.

**Benefits of TypeScript in VC-Shell projects:**

*   **Type safety**: Catch errors during development rather than at runtime, leading to more stable applications.
*   **Improved developer experience**: Enhanced autocompletion, refactoring capabilities, and code navigation in modern IDEs.
*   **Better code quality and maintainability**: Clear contracts for functions and components make code easier to understand, debug, and extend.
*   **Alignment with framework**: Seamless integration with VC-Shell's typed APIs, composables, and services.

**Core recommendations:**

*   **Enable strict mode**: It's highly recommended to have `strict: true` (or its constituent flags like `strictNullChecks`, `noImplicitAny`, etc.) enabled in your `tsconfig.json`. This enforces a higher degree of type safety from the outset.
*   **Consistent typing**: Strive to type all parts of your application, including component props, emits, state, composable functions, and service methods.

#### Typing in Vue components (`<script setup lang="ts">`)

*   **`defineProps`**: Always use the generic form `defineProps<PropsInterface>()` for full type inference and IDE support.
    ```typescript
    interface Props {
      message: string;
      count?: number;
    }
    const props = withDefaults(defineProps<Props>(), {
      count: 0,
    });
    ```
*   **`defineEmits`**: Similarly, use the generic form `defineEmits<EmitInterface>()` for typed event handling.
    ```typescript
    interface Emits {
      (event: 'update', id: string, value: any): void;
      (event: 'close'): void;
    }
    const emit = defineEmits<Emits>();
    emit('update', 'item-1', { data: 'new data' });
    ```
*   **`defineSlots`** (Vue 3.3+): For typing the expected slots and their props.
    ```typescript
    interface Slots {
      default(props: { item: any; index: number }): any;
      header?(): any;
    }
    const slots = defineSlots<Slots>();
    ```
*   **Reactive state (`ref`, `reactive`, `computed`)**: TypeScript can often infer the types for these, but explicit typing can be beneficial for complex objects or when the initial value is `null` or `undefined`.
    ```typescript
    import { ref, reactive, computed } from 'vue';
    import type { Ref } from 'vue'; // Import Ref type if needed for explicit typing

    const count: Ref<number> = ref(0);
    const user = reactive<{ name: string; age: number | null }>({ name: 'John Doe', age: null });
    const doubledCount = computed<number>(() => count.value * 2);
    ```

#### Type declaration files (**.d.ts**)

*   **Global types (`src/types/` or `src/env.d.ts`)**: For types that are available globally in your application. This can include augmenting existing types or defining ambient modules. Your **env.d.ts** is a good place for Vite-specific environment variable typings.
*   **Module-specific types (`src/modules/your-module/types/`)**: Keep types relevant to a specific module within that module's directory structure. This promotes modularity and makes it easier to understand the data structures specific to that feature.
*   **API client types**: API client types are typically auto-generated into a specific directory (e.g., `src/api_client/`) and should be imported from there. Avoid redefining these types manually.

#### Adhering to VC-Shell framework specific rules

The VC-Shell framework and its associated tooling (like the API client generator) provide many types out-of-the-box.

*   **Utilize framework types**: When interacting with framework composables, services, or components, always use the types they expose. This ensures compatibility and leverages the type safety provided by the framework.

*   **API client**: As mentioned, your primary source for data transfer object (DTO) types related to backend APIs should be the generated API client. This ensures that your frontend types are always in sync with the backend API contract.

By diligently applying TypeScript's features, you can significantly improve the quality, robustness, and maintainability of your VC-Shell applications, making them easier to scale and collaborate on.
