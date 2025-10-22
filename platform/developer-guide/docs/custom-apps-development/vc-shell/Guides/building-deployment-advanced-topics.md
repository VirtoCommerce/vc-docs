# Building, Deployment and Advanced Topics for VC-Shell Applications

This guide covers essential aspects of building your VC-Shell application for production, managing environment variables, considerations for deployment, and a brief overview of advanced topics like overriding framework components, performance optimization, and testing strategies.

## Build application

Once your development is complete, you need to build your application to generate optimized static assets that can be deployed to a web server.

### Vite build process overview

VC-Shell applications use **Vite** as the build tool. When you run the build command, Vite performs several key operations:

-   **Code bundling**: It processes your application code (Vue components, TypeScript/JavaScript files, CSS/SCSS) and bundles it into a few optimized JavaScript and CSS files.
-   **Tree shaking**: Unused code (dead code) is eliminated from the final bundles, reducing their size.
-   **Minification**: JavaScript, CSS, and HTML files are minified (whitespace removed, variable names shortened where possible) to further reduce file sizes.
-   **Asset hashing**: Filenames of generated assets (JS, CSS, images imported in components) typically include a hash (e.g., `app.a1b2c3d4.js`). This hash changes when the content of the file changes, allowing for effective cache busting. Browsers can safely cache these assets indefinitely, and when you deploy a new version with changed files, the new filenames will force a fresh download.
-   **index.html processing**: Vite processes your `public/index.html` file, injecting links to the generated JS and CSS bundles.
-   **Static asset copying**: Files from the `public/` directory are copied as-is to the output directory.
-   **Transpilation**: TypeScript is compiled to JavaScript, and modern JavaScript features might be transpiled to ensure broader browser compatibility (based on your `tsconfig.json` and Vite/Babel configuration, though Vite primarily targets modern browsers by default).

The result is a set of highly optimized static files ready for deployment.

### Build commands

The standard command to build your VC-Shell application is usually defined as a script in your **package.json** file.

-   **Using Yarn:**
    ```bash
    yarn build
    ```
-   **Using NPM:**
    ```bash
    npm run build
    ```

This command invokes Vite's build process. You'll see output in your terminal indicating the progress and the final size of the generated assets.

**Build modes & environment variables:**

Vite supports different build modes (e.g., `production`, `development`, `staging`). By default, `yarn build` usually runs in `production` mode. Environment variables loaded from **.env** files (like **.env.production**) are made available during the build process, allowing you to configure aspects like API URLs or feature flags specifically for the production build.

### Output directory (`dist/`)

By default, Vite places the output of the build process into a directory named `dist/` in the root of your project.

**Typical `dist/` directory structure:**

```
dist/
├── assets/                     # Hashed JS, CSS, and image files
│   ├── index.x1y2z3.css
│   └── ...                     # Other assets
├── img/                        # Files copied from public/img/
│   └── icons/                  # Files copied from public/img/icons/
│       ├── favicon.ico         # Favicon
│       └── ...                 # Other icons
├── types/                      # TypeScript type definitions
├── index.x1y2z3.js            # Main JS bundle
├── index.html                  # Processed HTML entry point
└── ...                         # Other files and folders copied from public/
```

-   The `assets/` subdirectory within `dist/` typically contains the hashed CSS files, and any image assets that were imported and processed by Vite.
-   Other files and folders from your `public/` directory are copied directly into `dist/`, maintaining their original structure relative to `public/`.

This `dist/` directory contains everything you need to deploy your application.

## Environment variables

Environment variables are crucial for configuring your application differently across various environments (development, staging, production) without changing your codebase. Vite has built-in support for managing environment variables through **.env** files.

### How .env files work

Vite uses `dotenv` to load environment variables from files in your project root. Here's how different **.env** files are typically used and prioritized:

-   **`.env`**: 
    -   This file is for default environment variables.
    -   It **can be committed** to your version control system (Git).
    -   It's loaded in all environments unless overridden by more specific files.
    -   Example: `APP_NAME=My VC-Shell App`

-   **`.env.local`**: 
    -   This file is for local overrides during development.
    -   It **should NOT be committed** to version control (it's usually in `.gitignore`).
    -   It overrides variables set in `.env`.
    -   Useful for sensitive information like local API keys or for machine-specific settings.
    -   Example: `APP_PLATFORM_URL=http://localhost:8080/platform` (overriding a default platform URL).

-   **`.env.[mode]`** (e.g., `.env.development`, `.env.production`, `.env.staging`):
    -   These files are for mode-specific environment variables.
    -   `[mode]` corresponds to the Vite mode the application is running in (e.g., `development` for `yarn serve`, `production` for `yarn build` by default).
    -   They **can be committed** to version control.
    -   They override variables set in `.env` but are overridden by `.env.local` (if it also defines the same variable for the current mode).
    -   Example (`.env.production`): 
        ```env
        APP_PLATFORM_URL=https://your-production-platform.com/
        APP_INSIGHTS_INSTRUMENTATION_KEY=your-prod-instrumentation-key
        ```

-   **`.env.[mode].local`** (e.g., `.env.production.local`):
    -   This file provides local overrides for a specific mode.
    -   It **should NOT be committed** to version control.
    -   It has the highest priority, overriding variables from `.env`, `.env.[mode]`, and `.env.local` (for that specific mode).
    -   Useful for temporarily overriding production settings locally for testing a production-like build.

**Loading priority (highest to lowest for a given `mode`):**

1.  `.env.[mode].local`
2.  `.env.local` (if not specific to a mode, loaded if no mode-specific `.env.local` exists)
3.  `.env.[mode]`
4.  `.env`

**Variable naming conventions:**

Only variables prefixed with `VITE_` are exposed to your client-side source code (e.g., `VITE_API_URL`). This is a security measure by Vite to prevent accidental exposure of sensitive environment variables.

However, VC-Shell applications often use non-prefixed variables as well (e.g., `APP_PLATFORM_URL`, `APP_I18N_LOCALE`). These are typically used by the application setup in **main.ts** or **vite.config.ts** and might not be directly exposed to the client-side bundle unless explicitly handled.

If you need to access an environment variable in your client-side code (Vue components, composables), **ensure it is prefixed with `VITE_`** in your `.env` files.

### Accessing environment variables in App

In your client-side code (Vue components, TypeScript files within `src/`), you can access environment variables (those prefixed with `VITE_`) using `import.meta.env`:

```typescript
// Example: Accessing an API URL in a composable
// Make sure VITE_API_BASE_URL is defined in your .env file(s)

const apiUrl = import.meta.env.VITE_API_BASE_URL;

if (apiUrl) {
  console.log("API Base URL:", apiUrl);
} else {
  console.warn("VITE_API_BASE_URL is not defined!");
}

// Example in a Vue component's setup script
<script lang="ts" setup>
const appVersion = import.meta.env.VITE_APP_VERSION; // e.g., VITE_APP_VERSION=1.0.0
</script>

<template>
  <footer v-if="appVersion">
    App Version: {{ appVersion }}
  </footer>
</template>
```

**Important considerations:**

-   **Build-time replacement**: `import.meta.env` variables are replaced with their actual values at build time. This means they are static values embedded in your bundled code. They cannot be changed dynamically at runtime without a new build.
-   **Security**: Never store sensitive secrets (like private API keys meant for server-side use) in `VITE_` prefixed variables, as they will be embedded in the client-side bundle and visible to anyone inspecting your application's code.
-   **Type safety**: By default, `import.meta.env` variables are not type-safe. You can extend TypeScript's `ImportMetaEnv` interface in an `env.d.ts` file (usually in `src/`) to get type checking and autocompletion for your custom environment variables:
    ```typescript
    // src/env.d.ts
    interface ImportMetaEnv {
      readonly VITE_API_BASE_URL: string;
      readonly VITE_APP_VERSION: string;
      // Add other VITE_ prefixed variables here
    }

    interface ImportMeta {
      readonly env: ImportMetaEnv;
    }
    ```
    This helps catch typos and ensures you are using the correct variable names.

Environment variables are a powerful tool for managing application configuration across different deployment stages. Understanding how Vite handles `.env` files and how to access these variables securely is essential for a smooth development and deployment workflow.

## Deployment considerations

Deploying your VC-Shell application involves serving the static files generated by the build process and ensuring correct configuration for the target environment.

### Serving static files

Your VC-Shell application, once built, consists entirely of static assets (HTML, CSS, JavaScript, images, etc.) located in the `dist/` directory. These files can be served by any static web server or hosting platform.

### Base URL configuration via environment variable

If your application is deployed to a subdirectory of a domain (e.g., `https://example.com/my-vc-app/`) instead of the root, you need to configure the base URL. In VC-Shell applications, this is typically managed via the `APP_BASE_PATH` environment variable.

-   **`.env` files**: Set the `APP_BASE_PATH` in your environment files (e.g., `.env`, `.env.production`, `.env.local`).
    ```env
    # Example for deploying to /my-vc-app/
    APP_BASE_PATH=/my-vc-app/
    ```
    If the application is served from the root of the domain, `APP_BASE_PATH` should typically be set to `/`.

-   **Vite Configuration (`vite.config.ts`)**: The generated `vite.config.ts` in a VC-Shell application is usually pre-configured to use this environment variable. It might look something like this:
    ```typescript
    import { getApplicationConfiguration } from "@vc-shell/config-generator";
    import process from "node:process";

    const mode = process.env.APP_ENV as string;

    export default getApplicationConfiguration({
      resolve: {
        alias: {
          // Application-specific aliases can be added here
        },
      },
    });
    ```
    The `getApplicationConfiguration` function (imported from a shared package like `@vc-shell/config-generator`) provides a standardized base Vite setup. Your application's `vite.config.ts` then calls this function, potentially passing in application-specific overrides or additions. This ensures common Vite settings (like Vue integration, essential plugins, and development server proxies) are consistently applied, while still allowing for per-project customization. The `APP_BASE_PATH` environment variable is used to set the `base` option for Vite.

-   **Impact**:
    -   Vite will use the value of `APP_BASE_PATH` to adjust asset paths in the generated `index.html` and bundled files, making them relative to this base path.
    -   Vue Router, when properly configured within the VC-Shell framework, will also use this base path for its routing, ensuring that navigation works correctly within the subdirectory.
    -   This approach allows you to manage the base path per environment without changing the core Vite configuration file for each deployment scenario.

### Platform connectivity

Your deployed VC-Shell application needs to communicate with the Virto Commerce Platform backend.

-   **`APP_PLATFORM_URL`**: This environment variable is critical. Ensure it is correctly set in your production environment (e.g., via your hosting provider's environment variable settings or in your `.env.production` file if it's bundled, though server-side env vars are safer for such URLs).
    -   This URL must be publicly accessible from your users' browsers.
-   **CORS (Cross-Origin Resource Sharing)**: The Virto Commerce Platform must be configured to allow requests from the domain where your VC-Shell application is hosted. If CORS is not correctly set up on the Platform side, API requests from your Frontend Application will be blocked by the browser.
    -   Ensure your application's deployment domain is added to the allowed origins in the Platform's CORS policy.
-   **Authentication**: 
    -   Authentication flows rely on correct redirect URIs. Ensure that the redirect URIs configured in your identity provider and your application settings match your deployment URL(s).
    -   The `useApiClient` composable in `@vc-shell/framework` handles attaching authentication tokens to API requests, but the initial authentication handshake needs proper configuration.


### Internationalization (i18n)

VC-Shell applications typically use `vue-i18n` for internationalization.

*   **Setup:**
    *   `vue-i18n` is usually configured in a dedicated plugin (e.g., `framework/core/plugins/i18n.ts`).
    *   Locale files (JSON or YAML) are typically stored in `locales/` directories at the application level and within each module (e.g., `src/locales/en.json`, `src/modules/my-module/locales/en.json`).
*   **Usage in components:**
    *   Use the `$t` function (globally available or from `useI18n` composable) in templates and scripts.
        ```vue
        <template>
          <h1>{{ $t('greetings.hello') }}</h1>
          <button @click="changeLocale('fr')">{{ $t('actions.changeToFrench') }}</button>
        </template>

        <script setup lang="ts">
        import { useI18n } from 'vue-i18n';

        const { t, locale } = useI18n();

        function Greet() {
          console.log(t('greetings.welcome'));
        }

        function changeLocale(newLocale: string) {
          locale.value = newLocale;
        }
        </script>
        ```
*   **Locale key structure:** Follow a consistent naming convention for your translation keys (e.g., `namespace.key` or `page.section.label`).
*   **Lazy loading translations:** For large applications with many languages, configure `vue-i18n` to lazy load locale messages to reduce the initial bundle size. This involves fetching translation files only when a specific language is requested.
    ```typescript
    // Example in i18n setup
    async function loadLocaleMessages(locale: string) {
      const messages = await import(`../locales/${locale}.json`);
      return messages.default;
    }
    // ... then configure vue-i18n to use this function
    ```
*   **Pluralization and number formatting:** Leverage `vue-i18n`'s capabilities for handling pluralization and formatting numbers and dates according to locale conventions.


## Conclusion

This series of guides has walked you through the process of creating custom applications and modules using the VC-Shell framework. From setting up your initial application scaffolding with `@vc-shell/create-vc-app` to diving deep into module development, application architecture, framework features, and advanced topics you should now have a solid foundation for building robust and scalable solutions.

VC-Shell provides a powerful and flexible platform. By leveraging its modular architecture, rich set of composables and services, and adhering to the established best practices, you can efficiently develop enterprise-grade applications tailored to your specific needs.

Remember that the key to successful development with VC-Shell lies in understanding its core concepts, embracing modularity, and continuously referring to the framework's documentation as you build.
