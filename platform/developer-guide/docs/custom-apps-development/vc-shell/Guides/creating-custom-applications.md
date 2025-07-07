# Creating Custom VC-Shell Applications

This guide provides a comprehensive walkthrough on how to create new VC-Shell applications from scratch, understand their structure, and develop custom modules.

Custom VC-Shell applications allow you to build powerful, enterprise-grade solutions tailored to specific business needs, leveraging the robust foundation of the VC-Shell framework. The framework provides core functionalities, UI components, and architectural patterns, enabling developers to focus on implementing unique features and business logic.

This guide is intended for developers looking to:

- Create new applications using the VC-Shell ecosystem.

- Understand the standard architecture and project structure of a VC-Shell application.

- Develop and integrate custom modules into their applications.

## Prerequisites

Before you begin, ensure you have the following installed and configured:

-   **Node.js**: Version 22.x or later is recommended (as per project rules). You can download it from [nodejs.org](https://nodejs.org/).
-   **Yarn**: A JavaScript package manager. Yarn is commonly used in VC-Shell projects.
    -   Install Yarn: `npm install --global yarn`
-   **Basic knowledge of Vue.js 3**: Specifically the Composition API and `<script setup>` syntax.
-   **Basic knowledge of TypeScript**: VC-Shell applications are built with TypeScript for type safety and improved developer experience.

## Creating new application

The recommended way to create a new VC-Shell application is by using the official scaffolding tool: `@vc-shell/create-vc-app`. This tool generates a new project with the standard directory structure, necessary configurations, and boilerplate code to get you started quickly.

### Using `@vc-shell/create-vc-app`

This command-line tool will prompt you for several configuration options to tailor the new application to your needs.

#### Installation and execution

You can run the scaffolding tool directly using `npx`, `npm create`, or `yarn create`.

**With NPX:**
```bash
npx @vc-shell/create-vc-app@latest
```

**With NPM:**
```bash
npm create @vc-shell/vc-app@latest
```

**With Yarn:**
```bash
yarn create @vc-shell/vc-app
```
Using `@latest` ensures you are always using the most recent version of the generator.

#### Interactive mode

The generator will ask you a series of questions:

1.  **Project name:**
    -   Example: `my-awesome-app`
    -   This will be the name of the directory created for your application and is often used in the `package.json`.
1.  **Base path:**
    -   Example: `/apps/my-awesome-app/` (if you are in a monorepo structure) or `./` for the current directory.
    -   This defines where the project directory will be created relative to your current working directory.
1.  **Select module variant:**
    -   `Classic view modules boilerplate`: Traditional setup for modules with explicit page components.
1.  **Module name:**
    -   Example: `core-features` or `product-management`
    -   This will be the name of the initial sample module created within your application.
1.  **Do you want to include additional module with sample data? (y/N)**
    -   Choosing `y` (Yes) will include an extra module with pre-filled sample data and components, which can be very helpful for understanding how modules are structured and how data can be integrated. This is recommended for new users.

Once you answer these questions, the tool will scaffold the application in the specified directory.

**Example interaction:**
```bash
✔ Project name: … my-custom-storefront
✔ Base path: … ./
? Select module variant: › Classic view modules boilerplate
Module name: › storefront-main
? Do you want to include additional module with sample data? › Yes

Scaffolding app in /path/to/your/workspace/my-custom-storefront...

Done. You can now run application:

  cd my-custom-storefront
  yarn
  yarn serve
```

#### Non-interactive mode

For automation, or when you want to skip prompts, you can use command line arguments. This mode requires the `--variant` option to be specified.

```bash
npx @vc-shell/create-vc-app@latest my-app --variant classic --module-name "My Module" --mocks
```

**Available options:**

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

**Examples:**

**Basic usage:**
```bash
npx @vc-shell/create-vc-app@latest my-app --variant classic
```

**With custom options:**
```bash
npx @vc-shell/create-vc-app@latest my-ecommerce-app \
  --variant classic \
  --module-name "Product Catalog" \
  --base-path "/apps/ecommerce/" \
  --package-name "@mycompany/ecommerce-app" \
  --mocks
```

**Create in existing directory:**
```bash
npx @vc-shell/create-vc-app@latest . --name my-existing-project --variant classic --overwrite
```

**Getting help:**
```bash
npx @vc-shell/create-vc-app@latest --help
```

**Check version:**
```bash
npx @vc-shell/create-vc-app@latest --version
```

!!! tip "Non-interactive mode requirements"
    For non-interactive mode to work, you must specify the `--variant` option. If you don't provide this option, the tool will fallback to interactive mode.

!!! warning "Overwrite protection"
    By default, the tool will refuse to create an application in a non-empty directory. Use the `--overwrite` flag to force overwriting existing files.

### Understanding Generated Application Structure

After the scaffolding process, your new application directory will have a structure similar to this. Below is an overview of the key files and folders at the root of your application (`src/`):

```
my-custom-storefront/
├── public/                     # Static assets (images, favicons, etc.)
│   ├── assets/
│   └── img/
│       └── icons/
├── src/
│   ├── api_client/             # Generated API client(s) for backend communication
│   ├── composables/            # Application-level Vue composables (shared logic)
│   ├── locales/                # Application-level translation files (i18n)
│   │   └── en.json             # Example: English translations
│   ├── modules/                # Your custom application modules reside here
│   │   └── storefront-main/    # Example module generated by the tool
│   │       ├── components/
│   │       ├── composables/
│   │       ├── locales/
│   │       ├── pages/
│   │       └── index.ts        # Entry point for this module
│   ├── pages/                  # Application-level pages (e.g., NotFound)
│   ├── router/                 # Vue Router configuration
│   │   ├── index.ts
│   │   └── routes.ts
│   ├── styles/                 # Global styles and TailwindCSS initialization
│   │   └── index.scss
│   ├── types/                  # Application-specific TypeScript type definitions
│   │   └── index.d.ts
│   ├── App.vue                 # Root Vue component
│   ├── main.ts                 # Main application entry point (Vue app initialization)
│   └── env.d.ts                # TypeScript definitions for environment variables
├── .env                        # Default environment variables (usually committed)
├── .env.local                  # Local environment variables (not committed, overrides .env)
├── .gitignore
├── package.json                # Project dependencies and scripts
├── tailwind.config.ts          # TailwindCSS configuration
├── tsconfig.json               # TypeScript configuration
├── vite.config.ts              # Vite build tool configuration
└── yarn.lock                   # Yarn lock file
```

**Key directories in `src/`:**

*   **api_client/**: This directory is intended to house API client code, typically generated from OpenAPI (Swagger) specifications of your backend services.

    !!! success "Generating API Clients"
        Populating the `api_client/` directory is a crucial step after scaffolding your application. VC-Shell provides tools to generate TypeScript API clients directly from your platform's OpenAPI specification. These generated clients handle the communication with your backend services, providing type-safe methods for all API operations.

        ![Readmore](../../media/readmore.png){: width="25"} [API client integration guide](../Essentials/API-Integration/api-client-integration.md)

*   **composables/**: Contains application-wide Vue composables. These are reusable functions that encapsulate stateful logic, making it easy to share functionality across different components and modules. An example **useLogin.ts** might be generated here.
*   **locales/**: Stores JSON files for internationalization (i18n). Each file (e.g., **en.json**, **es.json**) contains key-value pairs for translations in a specific language.

    ![Readmore](../../media/readmore.png){: width="25"} [Adding new languages](../Essentials/Usage-Guides/adding-new-languages.md)

*   **modules/**: This is where the core business logic and features of your application are organized. Each subdirectory within **modules/** represents a distinct feature or domain of your application. We'll delve deeper into module development later.
*   **pages/**: Contains global application pages that are not part of a specific module, such as a "Not Found" (404) page or a generic "Unauthorized" page.
*   **router/**: Configures the Vue Router.
    *   **index.ts**: Initializes the router instance.
    *   **routes.ts**: Defines the main application routes, including routes for shared authentication pages and often placeholders or loading mechanisms for module routes.
*   **styles/**: Holds global stylesheets.
    *   `index.scss`: The main SCSS file where you can import TailwindCSS base styles, components, utilities, and define any custom global styles.
*   **types/**: For application-specific TypeScript declaration files (`.d.ts`) that are not tied to a particular module.

**Root files:**

*   **App.vue**: The root Vue component of your application. It typically includes the main layout structure, such as `VcApp` from the framework.
*   **main.ts**: The entry point of your application. This is where the Vue application instance is created, plugins (including `VirtoShellFramework`) are registered, the router is attached, and the app is mounted to the DOM.
*   **.env**, **.env.local**: Files for managing environment variables. `APP_PLATFORM_URL` is a crucial variable you'll set here.
*   **package.json**: Defines project metadata, dependencies (`@vc-shell/framework`, Vue, etc.), and scripts (`dev`/`serve`, `build`, `generate-api-client`).
*   **vite.config.ts**: Configuration for Vite, the build tool used by VC-Shell applications.
    *   VC-Shell applications typically use a shared Vite configuration generator (e.g., from a package like `@vc-shell/config-generator`, often located in the `configs/vite-config` directory of the monorepo). The scaffolding tool (`@vc-shell/create-vc-app`) usually sets up your application's **vite.config.ts** (or **.mts**) to import a function like `getApplicationConfiguration` from this shared generator. This function provides a pre-configured Vite setup that includes common settings for Vue, TypeScript, asset handling, and development server proxies.
    *   You can often pass custom options to `getApplicationConfiguration` to extend or override specific parts of the Vite configuration without rewriting it entirely. An example of this approach can be seen in the **vite.config.mts** file of the scaffolded application.
*   **tailwind.config.ts**: Configuration for TailwindCSS, allowing you to customize the utility classes, theme, etc.

### Initial configuration

After the application is scaffolded, a few initial setup steps are typically required.

#### Setting up .env.local

The most critical initial configuration is setting the URL of your Virto Commerce Platform instance.

1.  Navigate to your newly created application's root directory:
    ```bash
    cd your-app-name
    ```
1.  Create a **.env.local** file if it doesn't exist. This file is for local environment variables and is typically not committed to version control.
1.  Add the `APP_PLATFORM_URL` variable to **.env.local**:
    ```env
    APP_PLATFORM_URL=https://your-platform.govirto.com/
    ```
    Replace **https://your-platform.govirto.com/** with the actual URL of your Virto Commerce Platform backend. This URL is used by the application to communicate with the platform APIs (e.g., for authentication, data fetching).

#### Other environment variables

Your application might use other environment variables defined in `.env` or its variants (e.g., **.env.production**). Common examples include:

*   `APP_I18N_LOCALE`: Default application language (e.g., **en**).

*   `APP_I18N_FALLBACK_LOCALE`: Fallback language if a translation is missing (e.g., **en**).

*   `APP_INSIGHTS_INSTRUMENTATION_KEY`: For Azure Application Insights integration.

*   `APP_BASE_PATH`: Specifies the base path from which the application is served. This is crucial if your application is deployed in a subdirectory of a domain (e.g., **https://example.com/my-vc-app/**).

    *   For root deployments, set this to **/**.

    *   For subdirectory deployments, set it to the subdirectory path (e.g., `/my-vc-app/`).

    The **vite.config.ts** is typically pre-configured to use this variable to correctly set the base for Vite and Vue Router.

These are often pre-configured in the generated **.env** file, but you can override them in **.env.local** for your specific development setup.

### Running application

Once the project is scaffolded and configured, you can install dependencies and start the development server.

1.  **Install dependencies:**
    Navigate to the application directory in your terminal and run:
    ```bash
    yarn install
    ```
    (or `npm install` if you prefer NPM). This will download all the project dependencies defined in **package.json**.

1.  **Start development server:**
    ```bash
    yarn serve
    ```
    (or `npm run serve` if you prefer NPM).

This command will typically start a Vite development server, and you'll see output in the console indicating the local URL where your application is running (usually **https://localhost:8000** or a similar port). Open this URL in your web browser to see your new VC-Shell application.

At this point, you have a basic VC-Shell application running. The next steps involve understanding its core concepts and then developing custom modules to add specific features and functionalities.

