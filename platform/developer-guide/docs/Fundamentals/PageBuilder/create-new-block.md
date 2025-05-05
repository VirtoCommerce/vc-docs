# Create new block

This tutorial will show you how to create a new block. We are going to create a simple block that displays selected products on the frontend:

![Draft block](media/draft-design.png)


## Create block descriptor

Every block starts with a descriptor file. This is a JSON file that defines the block’s structure, behavior, and settings. Descriptor files are located at the following path: **vc-frontend/blob/dev/client-app/builder-preview/schemas/sections/block-alias.json**.

Let's name our block **demo-product-list** and create a file called **demo-product-list.json**, with the following content:

```json title="demo-product-list.json"
{
  "name": "Demo products list",
  "icon": "inventory_2",
  "displayField": "name",
  "settings": [
    {
      "id": "title",
      "label": "Title",
      "type": "string",
      "default": "Title for products"
    },
    {
      "id": "content",
      "label": "Promo text",
      "type": "markdown",
      "resultType": "markdown",
      "default": "Some text"
    }
  ]
}
```

At this stage, we’ve added two settings fields. Additional properties will be added later.

## Add block to template descriptor

Since frontend can include multiple templates, we need to specify which templates our block can be used with.

In this case, we’ll add the block to the page template descriptor. To do this, open the file located at
**/vc-frontend/blob/dev/client-app/builder-preview/schemas/templates/product.json**, and include our block in the **sections** array:

```json title="product.json"
{
  ...
  "sections": [
    ...
    "demo-product-list"
  ]
  ...
}
```

## Add block layout

The layout defines the HTML structure and logic for our block. Since we use a Vue.js-based solution, the layout should be implemented as a Vue component.

1. Create a new **vc-frontend/blob/dev/client-app/shared/static-content/components/demo-product-list.vue** file with the following content:


    ```vue title="demo-product-list.vue"
    <template>
    <div class="pt-6 pb-16">
        <div class="w-full max-w-screen-2xl mx-auto px-5 md:px-12">
        <h2 class="text-2xl">{{ model.title }}</h2>
        <div class="text-lg">
            <VcMarkdownRender :src="model.content" class="text-gray-500"></VcMarkdownRender>
        </div>
        </div>
    </div>
    </template>

    <script setup lang="ts">
    defineProps({
    model: {
        type: Object,
        required: true,
    },
    });
    </script>
    ```

1. Register the new block in the frontend. Open the **vc-frontend/blob/dev/client-app/shared/static-content/components/index.ts** file and add the following line:

    ```ts title="index.ts"
    ...
    import DemoProductList from "./demo-product-list.vue";

    const templateBlocks: { [key: string]: Component } = {
    ...
    "demo-product-list": DemoProductList,
    };
    ...
    ```

1. Recompile the Frontend application by running:

    ```bash
    yarn run build
    ```

## Add block to page

To add the newly created block to a page:

1. Create a new **products-promo** page as described [here](getting-started.md#run).

1. Add your block to the page:

    ![Add block](media/add-new-block.gif){: style="display: block; margin: 0 auto;" }

After adding the block, it will be visible in the preview area:

![Design block](media/fill-new-block.png)

# Add product property to block

To make the block display specific products, we need to update its settings to include a product selection field. 

Open the block settings file and add the following configuration to the **settings** array:

```json
{
  ...
  "settings": [
    ...
    {
      "id": "products",
      "label": "Products",
      "type": "list",
      "default": [],
      "displayField": "product.name",
      "element": [
        {
          "id": "product",
          "label": "Product",
          "type": "select",
          "equalKey": "id",
          "request": {
            "url": "/graphql",
            "method": "post",
            "body": {
              "operationName": null,
              "variables": {},
              "query": "{products(storeId:\"{{location.params.storeId}}\"){items{id,code,name,imgSrc,prices{currency,list{formattedAmount}}}}}"
            },
            "cacheable": true,
            "response": {
              "result": "data.products.items"
            },
            "label": "name"
          }
        }
      ]
    }
  ]
}
```

We now can get select products from the list:

![Get product](media/list-of-products.png){: style="display: block; margin: 0 auto;" }

## Configure products list layout

To visually display the selected products, we need to update the block layout with the following markup:

```vue
<div class="flex flex-row justify-center space-x-4">
  <div v-for="item in model.products" :key="item.product?.id" :product="item">
    <div v-show="item.product" class="flex flex-col w-48">
      <VcImage
        :src="item.product.imgSrc"
        :alt="item.product.name"
        size-suffix="md"
        class="w-full h-full rounded object-cover object-center select-none space-x-4"
      />
      <div class="flex flex-row space-x-4">
        <div class="grow truncate">{{ item.product.name }}</div>
        <div class="whitespace-nowrap">{{ item.product.prices[0].list.formattedAmount }}</div>
      </div>
    </div>
  </div>
</div>
```

And here’s the final result:

![result](media/result.png)
