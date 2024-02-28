# Storyblok Integration

Storyblok is a headless CMS that provides a visual editor for creating and managing content. The integration with Storyblok allows you to create and manage content in Storyblok and display it in the Virto Commerce Storefront.

## Overview

The integration with Storyblok enables you to create and manage content in Storyblok and display it in the Virto Commerce Storefront. The integration is achieved through the use of the Storyblok API, which allows you to fetch content from Storyblok and display it in the Storefront. The integration also provides a way to manage content in Storyblok and update it in the Storefront. This guide explores how to integrate Storyblok with the Virto Commerce Storefront and provides a practical example of the integration.

## Integration with Virto Commerce Storefront

The integration with the Virto Commerce Storefront involves the following steps:

1. **Create a Storyblok account**: To get started with the integration, you need to create a Storyblok account. You can sign up for a free account on the [Storyblok website](https://www.storyblok.com/).
2. **Create a space**: Once you have created a Storyblok account, you need to create a space in Storyblok. A space is a container for your content, and it allows you to organize and manage your content in Storyblok.
3. **Create custom components**: After creating a space, you can start creating custom components in Storyblok. This will allow you to add existing components from the Virto Commerce Storefront to Storyblok and use them to create content.
4. **Create content**: After creating a space, you can start creating content in Storyblok. You can create content by adding components to your space and filling them with content.
5. **Fetch content**: Once you have created content in Storyblok, you can fetch it from the Storefront using the Storyblok API. The Storyblok API provides a way to fetch content from Storyblok and display it in the Storefront. You can fetch content with use of Storyblok composable, where you should pass content ID. The Storyblok API returns the content as JSON, which you can then display in the Storefront.
6. **Practical example**: To demonstrate the integration with Storyblok, we provide a practical examples of how to fetch content from Storyblok and display it in the Storefront. The example involves creating a space in Storyblok, adding components to the space, fetching content from Storyblok, and displaying it in the Storefront.

!!! note
    For more information about the Storyblok and its API, see the [Storyblok documentation](https://www.storyblok.com/docs/guide/getting-started).

### Connecting Storyblok with Virto Commerce Storefront

First of all, let’s install `@storyblok/vue`, Storyblok SDK for Vue 3:

```bash
yarn add @storyblok/vue
```

Next, you need to grab your Storyblok API token from the Storyblok dashboard. You can find it in the settings of your space **Settings > Access Tokens**.

Then use the API token in `client-app/app-runner.ts` to like in this example:

```typescript title="client-app/app-runner.ts" linenums="1"
import { createApp } from "vue";
import App from "./App.vue";
import { StoryblokVue, apiPlugin } from "@storyblok/vue";

export default async () => {
    // ...
    const app = createApp(App);

    app.use(StoryblokVue, {
        accessToken: "27ZV5dT9mXG6tEbHraoJSwtt",
        use: [apiPlugin],
    });

    app.mount('#app');
}
```

Also you need to add Vue 3 `Suspense` component to your `client-app/App.vue` like in this example:

```html title="client-app/App.vue"
<template>
  <Head>
    <link rel="icon" :href="$cfg.favicon_image" />
  </Head>

  <component :is="layout">
    <Suspense>
      <template #default>
        <RouterView />
      </template>

      <template #fallback>
         <VcLoaderOverlay />
      </template>
    </Suspense>
  </component>

  <ModalHost />
  <NotificationsHost />
</template>
```

!!! note
    For more information about connecting Storyblok with Vue apps, see the [Add a headless CMS to VueJS in 5 minutes](https://www.storyblok.com/tp/add-a-headless-CMS-to-vuejs-in-5-minutes#connecting-vue-to-storyblok).

### Next steps

Now when you have integrated Storyblok with the Virto Commerce Storefront, you can start creating and managing content in Storyblok and displaying it in the Storefront. o learn more about how to use Storyblok in the Virto Commerce Storefront, refer to our integration examples.

- [Categories Menu Integration](./catalog-menu-integration.md)
- [Category Page Integration](./category-page-integration.md)
- [Footer Integration](./footer-integration.md)
- [Index Page Integration](./index-page-integration.md)
