# Overview

=== "For new users"

    Virto Commerce Frontend is a single-page web application (SPA) with a fresh look on ecommerce solutions. This is where common B2B and B2C scenarios are combined with the most bleeding-edge technologies to deliver blazing-fast and fully functional solutions. It implements common business use cases needed for a vast majority of projects we build.

    Virto Commerce Frontend is designed to be used as-is within the actual Virto Commerce Platform. You can modify it by implementing desired components, pages, and shared logic to correspond with your project goals.

    [Deploy Frontend Application](deployment.md)


=== "For current Storefront and Theme users"

    As of July 2024, Virto Commerce Storefront and Theme have been replaced with the Frontend Application. 
    
    !!! note
        Current users now have the following options:

        1. Migrate to the new storefrontless architecture [on your own](migration-on-azure.md) or with our [assistance](https://help.virtocommerce.com/support/home).
        1. Continue using the Storefront with the [1.62 version](https://github.com/VirtoCommerce/vc-theme-b2b-vue/tree/support/1.62), which will receive updates until the end of 2024. After that, while it will still be possible to use the Storefront, no further updates will be provided.
    
    The primary objective of the new Virto Commerce Frontend Architecture is to simplify and expedite the development of ecommerce solutions based on the Virto Commerce Platform. This architecture replaces the custom **vc-storefront** with a standard load balancer, such as **nginx** or **Azure Load Balancer**. All business logic previously handled by **vc-storefront** is now integrated into the Platform through xAPI modules. This change ensures that developing business logic for client applications is now consistent with platform development.

    Virto Commerce Frontend (B2B-Theme 2.x) is now a Single Page Application (SPA) stored in static resources. The load balancer is configured to route requests from the client machine to both static content and xAPI endpoints. Additionally, this architecture supports the integration and utilization of third-party SPA applications.


![Frontend application](media/desktop.png)

[![Storefront demo site](media/public-demo-site.png)](https://virtostart-demo-store.govirto.com/)


## Technologies used

- **[Vue3](https://vuejs.org/):** Progressive frontend framework with its key features allowing one to build fast applications.
    
- [**TypeScript**](https://www.typescriptlang.org/)**:** All components and composables have type definitions, so that IDE could help you build clean and working code.
    
- [**TailwindCSS**](https://tailwindcss.com)**:** The most popular and growing CSS framework providing wonderful flexible structure to speed up styling.
    
- **Husky + ESLint + Prettier:** Autoformat, check, and fix your code and prevent ugly code style within repository.
    
- [**Vite**](https://vitejs.dev/)**:** Faster than Webpack, it is used to develop code with HMR benefits and build for production.
    
- [**GraphQL**](https://graphql.org/) **:** Use flexible GraphQL queries and mutations to safely work with back end.

## Key non-functional features

- **Development performance**: Achieve rapid development using the most effective solution. Deploy the SPA in seconds and start modifying code with [HMR features](https://vitejs.dev/guide/api-hmr).

- **Client performance**: Reach and maintain high performance metrics as provided by Google PageSpeed Insights.

- **[Atomic design pattern](../../../platform/developer-guide/Back-End-Architecture/atomic-architecture)**: Base the UI on Atoms, Molecules, and Organisms, combined within Pages and shared Components for high code reusability.

- **Fully responsive**: Ensure the application works seamlessly on multiple devices, from desktops to mobile phones, providing an excellent UI and UX.

- **Simple styling and customization**: Use TailwindCSS for straightforward and convenient CSS usage, minimizing code and leveraging a highly customizable framework.

- **Fully aligned with Virto Commerce Platform**: Integrate the SPA with the [Virto Commerce Platform](https://github.com/VirtoCommerce/vc-platform) to support all common B2B and B2C scenarios.

## Application structure

```json
├── assets                           // Scripts, styles and other assets compiled and minified for production.
|
├── client-app                       // The main folder for the application.
|   ├── assets                       // Assets needed to be precompiled during building.
|   |   └──...
|   |
|   ├── core                         // Common utilities and shared logic that can be used by any pages and libraries.
|   |   ├── api/graphql              // GraphQL Models aligned with the Virto Backoffice.
|   |   |   └──...
|   |   ├── composables              // Core composables (app-level shared logic).
|   |   |   └──...
|   |   ├── directives               // Core Vue directives.
|   |   |   └──...
|   |   ├── plugins                  // Core Vue plugins.
|   |   |   └──...
|   |   ├── enums                    // Core enums.
|   |   |   └──...
|   |   ├── types                    // Core types.
|   |   |   └──...
|   |   ├── utilities                // Some miscellaneous utils.
|   |   |   └──...
|   |   └── constants.ts             // Global-available constants (DO NOT USE, will be removed later).
|   |
|   ├── pages                        // Set of application pages used within Application router.
|   |   └──...
|   |
|   ├── public                       // Statically served files
|   |   └── static
|   |       ├── icons                // Icons used for favicons, PWA, etc.
|   |       └── images               // Static images used inside the application.
|   |
|   ├── router                       // SPA routing configuration.
|   |   └──...
|   |
|   ├── shared                       // A set of shared files grouped by their domain context.
|   |   ├── catalog                  // Grouping context (ex.: catalog browsing).
|   |   |   ├── components           // The collection of components specific for this domain context.
|   |   |   |   └──...
|   |   |   ├── composables          // The collection of shared logic written using Composable API pattern.
|   |   |   |   └──...
|   |   |   ├── types                // Types used in this context.
|   |   |   |   └──...
|   |   |   ├── utils                // Utilities and helpers specific for this context.
|   |   |   |   └──...
|   |   |   └── index.ts             // Entry point for this context used as library.
|   |   |
|   |   └──...
|   |
|   ├── ui-kit                       // Atoms, Molecules, Organisms and their types, used within the whole application.
|   |   └──...
|   |
|   ├── App.vue                      // Main Application component. Use it as a wrapper for routable pages.
|   ├── env.d.ts                     // Definition file to provide IDE IntelliSense support.
|   ├── main.ts                      // Application entry point. Main initialization script.
|   ├── shims-acceptjs.d.ts          // Definition file to provide IDE IntelliSense support for Accept.js (Authorize.net).
|   ├── shims-graphql.d.ts           // Definition file to provide IDE IntelliSense support for importing *.graphql files.
|   ├── shims-vue.d.ts               // Definition file to provide IDE IntelliSense support for importing *.vue files.
|   ├── vue.d.ts                     // Definition file to provide IDE IntelliSense support for additional global Vue properties.
|   └── vue-router.d.ts              // Definition file to provide IDE IntelliSense support for additional global Vue Router properties.
|
├── config
|   ├── menu.json
|   └── settings_data.json
|   
├── locales                          // Locale files used to provide translated content.
|   └──...
|
├── modules                          // Auxiliary build files that run in the Node environment.
|   └──...                           // Modules with their own components, APIs, and logic.
|
├── scripts                          // Auxiliary build files that run in the Node environment.
|   └──...
|
├── .babelrc                         // Babel configuration for storybook
├── .browserslistrc                  // Browserslist config file to support actual versions of browsers.
├── .commitlintrc.json               // Config for Conventional commit hook.
├── .dependency-cruiser.cjs
├── .dependency-graph.cjs
├── .editorconfig                    // Common editor settings to sync codestyle.
├── .env                             // Envfile to define different Environment Variables.
├── .env.local                       // Local envfile to override Environment Variables.
├── .eslintignore                    // Ignore some files from ESlint.
├── .eslintrc.cjs                    // ESlint configuration file.
├── .gitattributes                   // Set attributes to specified path in Git.
├── .gitignore                       // Ignore some files from Git.
├── .npmrc                           // Node.js package manager settings and Node.js restrictions
├── .prettierignore                  // Ignore some files from Prettier.
├── .prettierrc.json                 // Config for Prettier.
├── .yarnrc.yml                      // Yarn package manager configuration
├── graphql-codegen
|   └── generator.ts                 // Generate GraphQL types 
├── index.html                       // Vite Development entry point.
├── LICENSE.txt
├── package.json                     // NPM Package description.
├── postcss.config.cjs               // PostCSS configuration for Tailwind.
├── README.md                        // This file.
├── sonar-project.properties
├── tailwind.config.ts               // TailwindCSS configuration file.
├── tsconfig.app.json                // Typescript configuration for application.
├── tsconfig.json                    // Main TypeScript configuration file.
├── tsconfig.node.json               // Typescript configuration for Node.js.
├── tsconfig.vitest.json
├── vite.config.ts                   // Vite configuration file.
├── vitest.config.ts
└── yarn.lock                        // Yarn dependencies lock file.

```

## Key functionalities

The key functionalities include:

* [Registration and signing in.](../../../storefront/user-guide/registration_and_signing_in/create-account)
* [Password management.](../../../storefront/user-guide/registration_and_signing_in/password-management)
* [Managing personal and corporate accounts.](../../../storefront/user-guide/account/overview)
* [Managing quote requests.](../../../storefront/user-guide/shopping/submit-quotes)
* [Managing lists.](../../../storefront/user-guide/shopping/lists)
* [Access assignment.](../../../storefront/user-guide/account/company-members)
* [Product comparison.](../../../storefront/user-guide/shopping/compare-products)
* [Bulk orders.](../../../storefront/user-guide/shopping/bulk-orders)
* [Intuitive navigation.](../../../storefront/user-guide/navigation/homepage-layout)
* [Buying digital and physical products.](../../../storefront/user-guide/shopping/checkout-process) 
* [Searching and filtering products.](../../../storefront/user-guide/shopping/searching-for-products)
* [Managing push messages.](../../../storefront/user-guide/account/notifications)
* [Reviewing products.](../../../storefront/user-guide/account/review-products)


<br>
<br>
********

<div style="display: flex; justify-content: flex-end;">
    <a href="architecture">Architecture →</a>
</div>

