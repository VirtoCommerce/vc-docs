# Builder.io Integration

`Builder.io` is a headless CMS that provides a visual editor for creating and managing content. The integration with `Builder.io` allows you to create and manage content in `Builder.io` and display it in the `Virto Commerce vue-b2b-theme.`

## Overview

The integration with `Builder.io` enables you to create and manage content in `Builder.io` and display it in the `Virto Commerce vue-b2b-theme`. The integration is achieved through the use of the `Builder.io API`, which allows you to fetch content from `Builder.io` and display it in the `vue-b2b-theme`. The integration also provides a way to manage content in `Builder.io` and update it in the `vue-b2b-theme`. This guide explores how to integrate Builder.io with the `Virto Commerce vue-b2b-theme` and provides a practical example of the integration.

## Integration with Virto Commerce vue-b2b-theme

The integration with the `Virto Commerce vue-b2b-theme` involves the following steps:

1. **Create a Builder.io account**: To get started with the integration, you need to create a `Builder.io` account. You can sign up for a free account on the [Builder.io website](https://www.builder.io/).
2. **Create a space**: Once you have created a `Builder.io` account, you need to create a space in `Builder.io`. A space is a container for your content, and it allows you to organize and manage your content in `Builder.io`.
3. **Create custom components**: After creating a space, you can start creating custom components in `Builder.io`. This will allow you to add existing components from the `Virto Commerce vue-b2b-theme` to `Builder.io` and use them to create content.
4. **Create content**: After creating a space, you can start creating content in `Builder.io`. You can create content by adding components to your space and filling them with content.
5. **Fetch content**: Once you have created content in `Builder.io`, you can fetch it in the `vue-b2b-theme` using the Builder.io API. The `Builder.io API` provides a way to fetch content from `Builder.io` and display it in the `vue-b2b-theme`. You can fetch content with use of `Builder.io` composable, where you should pass content ID. The `Builder.io API` returns the content as JSON, which you can then display in the `vue-b2b-theme`.
6. **Practical example**: To demonstrate the integration with `Builder.io`, we provide a practical examples of how to fetch content from `Builder.io` and display it in the `vue-b2b-theme`. The example involves creating a space in `Builder.io`, adding components to the space, fetching content from `Builder.io`, and displaying it in the vue-b2b-theme.

!!! note
    For more information about the `Builder.io` and its API, see the [Builder.io documentation](https://www.builder.io/c/docs/developers).

### Connecting Builder.io with Virto Commerce vue-b2b-theme

First of all, let’s install `@builder.io/sdk-vue`, Builder.io SDK for Vue 3:

```bash
yarn add @builder.io/sdk-vue@^0.3.1
```

We will use `@builder.io/sdk-vue` version `0.3.1`, as it's more stable and has better compatibility with the `Virto Commerce vue-b2b-theme`.

Next, you need to grab your Builder.io API token from the Builder.io dashboard. You can find it in the settings of your space **Settings > Public API Key**. You will need this key to authenticate your requests to the Builder.io API.

To facilitate the registration of custom components, we also need to create a composable `useBuilder`:

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

### Next steps

Now when you have integrated Builder.io with the `Virto Commerce vue-b2b-theme`, you can start creating and managing content in `Builder.io` and displaying it in the `vue-b2b-theme`. To learn more about how to use `Builder.io` in the `Virto Commerce vue-b2b-theme`, refer to our integration examples.

- [Catalog Menu Integration](./catalog-menu-integration.md)
- [Category Page Integration](./category-page-integration.md)
- [Footer Integration](./footer-integration.md)
- [Index Page Integration](./index-page-integration.md)
