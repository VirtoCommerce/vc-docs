# Use Modules from Other Applications

This guide explains how to use modules from another custom application in your own project. It provides detailed instructions on initializing external modules, adding them to the navigation menu, and integrating them into your project.

In this guide, we'll use the example of the `vc-app-extend` project, which extends the functionality of the `vc-app` project located in the `sample` folder.

## Add Custom Application

To incorporate another custom application into your project:

1. [Install the dependencies.](Using-Modules-from-Other-Applications.md#installing-dependencies)
1. [Configure the external application as a plugin.](Using-Modules-from-Other-Applications.md#initializing-external-modules)
1. [Create a link in the navigation menu.](Using-Modules-from-Other-Applications.md#adding-a-module-to-the-navigation-menu)

### Install Dependencies

Let's assume you want to include modules from the `vc-app` application into your custom application, `vc-app-extend`. The package that contains these modules from `vc-app` is named `@vc-app/modules`. To add this dependency to your project, use the following command:

```bash
yarn add @vc-app/modules
```

### Initialize External Modules

After installing the dependency, you must initialize the `Offers` module from the `@vc-app/modules` package. To do this, navigate to `vc-app-extend/src` and import the package in the `main.ts` file as follows:

```typescript
import modules from "@vc-app/modules";
```

Since these modules are essentially Vue plugins and have an internal installation method, use the standard `Vue` method `use` for installation. In our example, we install the `Offers` module:

```typescript
import modules from "@vc-app/modules";

async function startApp() {
        ...
        const app = createApp(RouterView);
        app.use(VirtoShellFramework);

        // Import and initialize the Offers module from the @vc-app application
        app.use(modules.Offers.default, { router });

        app.use(router);
        ...
    }

startApp()
```

!!! warning
    Ensure that all modules, including external ones, are installed after `VirtoShellFramework` and before `Vue router`. The installation order should be as follows:

    1. `VirtoShellFramework`
    2. `modules`
    3. `Vue router`

In our example, we installed only one module. If you need to install all modules from the package, you can do so as follows:

```typescript
import modules from "@vc-app/modules";

async function startApp() {
        ...
        const app = createApp(RouterView);
        app use(VirtoShellFramework);

        // Import and initialize all available modules from the @vc-app application
        Object.values(modules).forEach(module => {
            app.use(module, { router });
        })

        app.use(router);
        ...
    }

startApp()
```

!!! note
    Notice that when initializing modules, we always pass the `router` as the second argument to the `use` method. This is necessary for the automatic registration of modules in the Vue routing system.


After completing all the steps, you will have the following result:
![Provided Offers](../../../media/added-offers-menu.png)

Now, the `Offers` module is ready for use!
