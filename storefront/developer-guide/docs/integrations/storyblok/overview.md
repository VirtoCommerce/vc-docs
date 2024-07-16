# Storyblok Integration

Storyblok is a headless CMS that provides a visual editor for creating and managing content. The integration with Storyblok allows you to create and manage content in Storyblok and display it in the Frontend Application.

[![video tutorial](media/video-tutorial-button.png)](https://youtu.be/W_-n8GQM9CA)

The integration is achieved through the use of the Storyblok API, which allows you to fetch content from Storyblok and display it in the Frontend Application. The integration also provides a way to manage content in Storyblok and update it in the Frontend Application. This guide explores how to integrate Storyblok with the Virto Commerce Frontend Application and provides a practical example of the integration.

## Integrate with Virto Commerce Frontend Application

To integrate with Virto Commerce Frontend Application:

1. Create a Storyblok account. Sign up for a free account on the [Storyblok website](https://www.storyblok.com/).
1. Create a space in Storyblok. A space is a container for your content, and it allows you to organize and manage your content in Storyblok.
1. Create custom components in Storyblok. This allows you to add existing components from the Frontend Application to Storyblok and use them to create content.
1. Create content in Storyblok. Add components to your space and fill them with content.
1. Fetch content in the Frontend Application using the Storyblok API. The Storyblok API provides a way to fetch content from Storyblok and display it in the Frontend Application. You can fetch content using Storyblok composable, where you should pass content ID. The Storyblok API returns the content as JSON, which you can then display in the Frontend Application.

![Readmore](media/readmore.png){: width="25"} [Storyblok documentation](https://www.storyblok.com/docs/guide/getting-started)

## Connect Storyblok with Virto Commerce Frontend Application

1. Install `@storyblok/vue`, Storyblok SDK for Vue 3:

    ```bash
    yarn add @storyblok/vue
    ```

1. Get your Storyblok API token from the Storyblok dashboard ( **Your space --> Settings --> Access Tokens**).

1. Use the API token in `client-app/app-runner.ts` as follows:

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

![Readmore](media/readmore.png){: width="25"} [Add a headless CMS to VueJS in 5 minutes](https://www.storyblok.com/tp/add-a-headless-CMS-to-vuejs-in-5-minutes#connecting-vue-to-storyblok)

## Next Steps

* [Catalog Menu Integration](catalog-menu-integration.md)
* [Category Page Integration](category-page-integration.md)
* [Footer Integration](footer-integration.md)
* [Index Page Integration](index-page-integration.md)
