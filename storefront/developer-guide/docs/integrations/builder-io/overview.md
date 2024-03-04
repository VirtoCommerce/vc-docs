# Builder.io Integration

Builder.io is a headless CMS that provides a visual editor for creating and managing content. The integration with Builder.io allows you to create and manage content in Builder.io and display it in the **Virto Commerce vue-b2b-theme**. The integration is achieved through the use of the Builder.io API, which allows you to fetch content from Builder.io and display it in the **vue-b2b-theme**. The integration also provides a way to manage content in Builder.io and update it in the **vue-b2b-theme**. 

This guide explores how to integrate Builder.io with the **Virto Commerce vue-b2b-theme** and provides a practical example of the integration.

## Integrate with Virto Commerce vue-b2b-theme

To integrate with the **Virto Commerce vue-b2b-theme**:

1. Create a Builder.io account. Sign up for a free account on the [Builder.io website](https://www.builder.io/).
2. Create a space in Builder.io. A space is a container for your content, and it allows you to organize and manage your content in Builder.io.
3. Create custom components in Builder.io. This allows you to add existing components from the **Virto Commerce vue-b2b-theme** to Builder.io and use them to create content.
4. Create content in Builder.io by adding components to your space and filling them with content.
5. Fetch content in the **vue-b2b-theme** using the Builder.io API. The Builder.io API provides a way to fetch content from Builder.io and display it in the **vue-b2b-theme**. You can fetch content using Builder.io composable, where you should pass content ID. The Builder.io API returns the content as JSON, which you can then display in the **vue-b2b-theme**.

![Readmore](media/readmore.png){: width="25"} [Builder.io documentation](https://www.builder.io/c/docs/developers)

## Connect Builder.io with Virto Commerce vue-b2b-theme

To connect Builder.io with **VC vue-b2b-theme**:

1. Install `@builder.io/sdk-vue`, Builder.io SDK for Vue 3. We use `@builder.io/sdk-vue` version 0.3.1, as it is more stable and has better compatibility with the **Virto Commerce vue-b2b-theme**.

    ```bash
    yarn add @builder.io/sdk-vue@^0.3.1
    ```

1. Get your Builder.io API token from the Builder.io dashboard (**Your space --> Settings --> Public API Key**). You will use this key to authenticate your requests to the Builder.io API.

1. To facilitate registration of the custom components, create a composable `useBuilder`:

    ```typescript title="shared/builder-io/composables/useBuilder.ts" linenums="1"
    const registeredComponents = [];

    export const useBuilder = () => {

      function registerCustomComponents(components) {
        for (const [, component] of Object.entries(components)) {
          registeredComponents.push(component);
        }
      }

      return {
        registeredComponents,
        registerCustomComponents,
      };
    };
    ```

## Next Steps

* [Catalog Menu Integration](catalog-menu-intergration.md)
* [Category Page Integration](category-page-integration.md)
* [Footer Integration](footer-integration.md)
* [Index Page Integration](index-page-integration.md)
