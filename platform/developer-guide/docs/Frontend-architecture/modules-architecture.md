# Modules Architecture

This document provides an overview of the Virto Commerce frontend modules architecture. The modular approach provides:

* **Scalability:** Easily add new features without affecting existing ones.  
* **Maintainability:** Isolated codebases simplify management and debugging.  
* **Modularity:** Modules in the **/modules** folder can be removed without affecting the Core.  
* **Control:** Decision-makers have clear oversight.  


## Key concepts

The key concepts of modules architecture are as follows:

| Concept                   | Description                                                                                       |
|---------------------------|---------------------------------------------------------------------------------------------------|
| Core                      | The main application that includes the API, router, builder, and other systems.                  |
| Module                    | An additional functionality developed with minimal impact on the Core. It is a self-contained feature area within the application. Each module encapsulates its own components, services, APIs, and other related code. |
| Extensions                | Extension points that belong to the Core, also called **holes** or **sockets**. <br> **Existing extensions**: <br> - client-app/shared/common/composables/useCustomProductComponents.ts <br> - client-app/shared/layout/composables/useCustomAccountLinkComponents.ts <br> - client-app/shared/layout/composables/useCustomMobileMenuLinkComponents.ts <br> - client-app/shared/layout/composables/useCustomHeaderLinkComponents.ts <br> - client-app/shared/layout/composables/useCustomMobileHeaderComponents.ts                  |
| Module management system  | A decision-making point and business logic handler. It is represented as [settings_data.json](https://github.com/VirtoCommerce/vc-frontend/blob/ce852a790b0cc8b0ba9b01e3fde3187c3d1bf2bd/client-app/config/settings_data.json) at the bundle level and as an array of modules in the **getStore** request at the store level. It can be considered a form of **Feature flags**.  |
| Type generation system    | Handles the generation of types and constants for GraphQL API.                                   |


![Key concepts](media/platform-acrhitecture.png)

## Module folder structure

A well-structured module ensures clarity and ease of maintenance. Below is the recommended module structure:

```json
your-module/
├── api/ // All API-related code, including GraphQL schemas and generated types. 
│   ├── graphql/
│   │   └── types.ts
├── components/ // Vue components specific to the module.
│   └── YourComponent.vue
├── composables/ // Vue composables (hooks) for shared logic within the module
│   └── useYourFeature.ts
├── pages/ // Module-specific pages that integrate with the application's routing.
│   ├── YourModulePage.vue
│   └── index.ts
├── localization/ // Localization files for supporting multiple languages.
│   ├── en.json
│   └── de.json
├── types/ // TypeScript interfaces and types for the module.
│   └── index.ts
└── index.ts // Entry point exporting public APIs (mainly init function).
```


## Type generation system

Each module typically includes its own GraphQL types, often defined in a **types.ts** file within an **api/graphql** folder. These types are generated using the following npm command:

```bash
yarn generate:graphql-types
```

This command triggers the execution of the generator.ts script, which is responsible for generating the types.ts files for both the core application and the independent modules.

The **scripts/graphql-codegen/generator.ts** file also plays a crucial role in handling standalone GraphQL schemas. It includes an array called **independentModules**, where each object represents a separate GraphQL schema that needs to be generated independently:

```csharp
{
    name: "YourModule",
    apiPath: "client-app/modules/your-module/api/graphql",
    schemaPath: `${process.env.APP_BACKEND_URL}/graphql/your-module`,
},
```

### Routes registration

Modules register their routes through the **init** function within the module. This function is called during the application's initialization phase, typically in the **app-runner.ts**.

Each module should export an **init** function that accepts the router and other necessary dependencies (e.g., i18n).

```csharp
// modules/your-module/index.ts
import { Router } from "vue-router";
import { I18n } from "@/i18n";

// Define your components
const YourModulePage = () => import("./pages/YourModulePage.vue");
// By using () => import('./pages/YourModulePage.vue'), you ensure that Vue Router can handle the component as a lazy-loaded route, which is the intended usage pattern.

export async function init(router: Router, i18n: I18n): Promise<void> {
  const route = {
    path: "/your-module",
    name: "YourModule",
    component: YourModulePage,
    beforeEnter(to: any, from: any, next: Function) {
      // Add any route guards or logic here
      next();
    },
  };

  router.addRoute(route);
}
```

??? "Example of initialization function usage"
    To integrate a module into the main application, you need to import the module's **init** function and call it within the app's runner. Below is an example of how to do this:


    ```csharp
    // client-app/app-runner.ts

    // Import the module's init function
    import { init as initYourModule } from "@/modules/your-module";

    ...

    initYourModule(router, i18n);
    ```


## Best practices

To ensure consistency and high quality across all modules, follow these best practices:

* Consistent structure:
    * Adhere to the recommended folder structure.
    * Keep related files grouped together.

* Isolate module logic:
    * Avoid cross-module dependencies unless necessary.
    * Use the module's composables for shared logic.

* Type safety:
    * Define clear TypeScript types in the **types/** directory.
    * Ensure all API interactions use generated GraphQL types.

* Documentation:
    * Document public APIs, components, and composables.
    * Keep the **README.md** updated with relevant information.

* Naming conventions:
    * Use clear and descriptive names for files and functions.
    * Follow the project's naming guidelines.

* Testing:
    * Write unit and integration tests for module functionalities.
    * Ensure tests are located alongside the code they test.


Happy coding! 🚀