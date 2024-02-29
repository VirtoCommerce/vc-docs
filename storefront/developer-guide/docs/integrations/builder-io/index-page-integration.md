# Overview

In this article, we will integrate `Builder.io CMS` into the index page of the `Virto Commerce vue-b2b-theme`. The integration will allow you to create and manage content in `Builder.io CMS` and display it in the `Virto Commerce vue-b2b-theme`.

To use `Builder.io CMS` with the page you need to follow these steps:

1. **Create page model**: First, you need to create a page model in the `Builder.io CMS` for the index page. The page model should define the properties of the index page and how it should be rendered in the `Builder.io CMS`.
2. **Add Builder.io to the page component**: After creating a page model, you need to add `Builder.io` to the page component in the `Virto Commerce vue-b2b-theme`. This will allow you to fetch content from `Builder.io` and display it in the index page.
3. **Create content**: After creating a page model, you can start creating content in the `Builder.io CMS`. You can create content by adding components to your page model and filling them with content.

## Create Page Model in Builder.io

First we will navigate to the `Models` menu where we will hit `Create Model` on the top right corner. You will be prompted with an dropdown to select the model type, we will select `Page`. After selecting the model type, we will be prompted with an input field to name the component, we will use `main page`, and description. After confirming the name, we will be redirected to the model editor where we should change preview URL to `http://localhost:YOUR_PORT` where `YOUR_PORT` is the port of your `Virto Commerce vue-b2b-theme` application.

![Main Page Block](../media/main-page-block-builder.png)

Now we can use this model to create the content for our index page, so we can proceed to create the page content. We will navigate to the `Content` menu and click on the `main page` in `Page models` section. Now click `New Entry` and select `main page` model from dropdown to create new page:

![Create New Content](../media/create-new-content-builder.png)

## Add Builder.io to the Page Component

To add `Builder.io` to the page component you need to add `RenderContent` into your template. As we want totally replace the content of the page with the content from `Builder.io` - we will use `v-if` directive to show `RenderContent` only when content is loaded.

=== "Template"

    ```html title="client-app/pages/index.vue"
    <template>
         <div v-if="canShowContent">
            <RenderContent model="main-page" :content="content" :api-key="apiKey" :custom-components="registeredComponents" />
        </div>
    </template>
    ```

=== "Script"

    As you can see we are using `main-page` as a content ID to fetch the content from Builder.io.

    ```typescript title="client-app/pages/index.vue"
    import { ref, shallowRef } from "vue";
    import { useI18n } from "vue-i18n";
    import { usePageHead } from "@/core/composables";
    import { getContent, RenderContent, isPreviewing } from "@builder.io/sdk-vue/vue3";
    import { useBuilder } from "@/shared/builder-io/composables/useBuilder";

    const { t } = useI18n();
    const { registeredComponents } = useBuilder();

    const canShowContent = shallowRef(true);

    const content = shallowRef(null);
    const pageNotFound = shallowRef(false);

    usePageHead({
        title: t("pages.home.meta.title"),
        meta: {
            keywords: t("pages.home.meta.keywords"),
            description: t("pages.home.meta.description"),
        },
    });

    onMounted(async () => {
        try {
            const result = await getContent({
                model: "main-page",
                apiKey: "121744b9a9944bae8c35aeef88a87ba0",
                userAttributes: {
                    urlPath: url,
                },
            });

            content.value = result;
            canShowContent.value = !!content.value || isPreviewing();
        } catch (e) {
            pageNotFound.value = true;
        }
    });
    ```

Now you can preview the index page in the `Builder.io` and start creating content for it.

## Create content

After adding `Builder.io` to the page component, you can start creating content in the `Builder.io CMS`. You can create content by adding components to your page model and filling them with content.

If you have already added custom components to `Builder.io`, you can use them to create content for the page. For more details on how to add custom components to Builder.io, you can read the article [Registering Custom Components](./registering-custom-components.md).

As a result, you will get integration of `Builder.io CMS` with the index page of `Virto Commerce vue-b2b-theme`:

![Builder.io Integration](../media/builderio-integration-index-page.png)
