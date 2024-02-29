# Overview

In this article, we will explore how to register any custom component in the `Builder.io CMS`. The registration of custom components allows you to use any UI components like `Slider` in the `Builder.io CMS` when creating content.

## How to Register Custom Components

To register a custom component in the `Builder.io CMS`, you need to follow these steps:

1. **Create a reference**: First, you need to create a `reference` for the custom component you want to register. The wrapper component should be a `*.ts` file and describe the inputs—or the props—that you would like to be editable in the `Visual Editor`.
2. **Register the component**: After creating the `reference`, you need to register it with use of `useBuilder` composable, which we created [here](./overview.md#connecting-builderio-with-virto-commerce-vue-b2b-theme). This will make the custom component available for use in the `Builder.io CMS`.
3. **Provide this list of components to the `RenderContent` component:**: Once the component is registered, you need to provide this list of components to the `RenderContent` component. This will allow you to use the custom component in the `Builder.io CMS`.

## Example

### Registering a Slider Component in Application

Let's consider an example of how to register a `Slider` component in the `Builder.io CMS`. First, you need to create a reference for the `Slider` component:

```typescript title="@/shared/builder-io/components/custom/slider.ts" linenums="1"
import Slider from "../../../static-content/components/slider.vue";

export const slider = {
  component: Slider,
  name: "Slider",
  inputs: [
    {
      name: "slides",
      type: "list",
      defaultValue: [],
      subFields: [
        {
          name: "image",
          type: "string",
        },
      ],
    },
  ],
};
```

Next, you need to register the `slider` component with the `useBuilder` composable:

```typescript title="client-app/app-runner.ts" linenums="1"
import { createApp } from "vue";
import App from "./App.vue";
import * as builderSharedComponents from "@/shared/builder-io/components/custom";

export default async () => {
    // ...
    const app = createApp(App);

    const { registerCustomComponents } = useBuilder();

    registerCustomComponents(builderSharedComponents);

    app.mount('#app');
}
```

Finally, you need to provide this list of components to the `RenderContent` component:

```typescript linenums="1"
<template>
    <RenderContent :custom-components="registeredComponents" />
</template>

<script setup>
import { RenderContent } from "@builder.io/sdk-vue/vue3";
import { useBuilder } from "@/shared/builder-io/composables/useBuilder";

const { registeredComponents } = useBuilder();
```

The `Slider` component is now registered and available for use in the `Builder.io CMS`. You can now use the `Slider` component when creating content in the `Builder.io CMS`:

![Slider Component in Builder.io CMS](./../media//slider-component-builder.png)
