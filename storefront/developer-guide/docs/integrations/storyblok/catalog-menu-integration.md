# Overview

In this article, we will integrate `Catalog Menu` with the `Storyblok CMS`. The integration will allow you to create and manage catalog navigation links in the `Storyblok CMS` and display them in the `Virto Commerce Storefront`.

This guide will cover the following topics:

1. **Create of global component**: We will create a new space in `Storyblok` and add `Catalog Menu` to the space.
2. **Fetch Content from Storyblok**: We will fetch catalog navigation links from `Storyblok` and display them in the `Storefront`.

## Setting Up Global Component

To set up a folder in Storyblok, we need to define a content type for the folder. Let's name it `global` as it will hold our global components. We should also ensure that the content type in the global folder cannot be changed, so that we only have entries of that type. Additionally, we should select the default content type option so that `global` is already chosen.

![Create Global Component](../media/create-global-folder.png)

If you don't have a `global` content type - you can create it by clicking on the `New content type` button.

![Create Global Block](../media/create-global-block.png)

After creating the folder, we can proceed to create our first entry within it. When creating the entry, ensure that the content type is set to `global` as we have disabled the ability to change the content type for the folder. You can choose any name for the entry, but make sure it accurately describes the content of the global component to your editors. Since we are creating a `Catalog Menu`, which is actually a `megamenu`, we will name the entry `Megamenu`.

![Create Megamenu](../media/create-megamenu.png)

Next step will be to set-up the actual field in the entry that holds our component, for this we will click on `Define` and adding a new field called `global` of the type `Blocks`.

![Add Global Blocks](../media/add-global-blocks.png)

In next step we will create a new block called `megamenu`.

## Create Catalog Menu Block

First we will navigate to the `Block Library` menu where we will hit `New Block` on the top right corner. You will be prompted with an input field to name the component, we will use `Megamenu`. After confirming the name, we will add a new field called `items` of type `Blocks` and hit `Save`.

![Megamenu Block](../media/megamenu-block.png)

Since components in `Storyblok` have a block structure, we need to create blocks for each menu item and each menu link in the same way. For this, we will create the `Megamenu-item` block and the `Megamenu-link-item` block with the `Nestable block` type.

Example structure of the `Megamenu-item` block:

![Megamenu Item Block](../media/megamenu-item-block.png)

Example structure of the `Megamenu-link-item` block:

![Megamenu Item Link Block](../media/megamenu-item-link-block.png)

After creating all the blocks, we need to link them together to restrict the selection of external blocks that are not related to the `megamenu`. To do this, go to the settings of each block, find the entry with the type `Blocks` in the `General section`, and in the `Edit field` section, select the checkbox `Allow only specific components to be inserted` and choose the component that can be nested in this block. In our example, the nesting should look like this:

```text
Megamenu
    └── Megamenu-item
            └── Megamenu-link-item
```


Example of this configuration for the `Megamenu` block:

![Megamenu Settings](../media/megamenu-settings.png)

After creating all the blocks and configuring their nesting, we can proceed to create the content for our menu.

## Create Catalog Menu Content

After creating the blocks, we can proceed to create the content for our `Catalog Menu`. We will navigate to the `Content` menu and click on the `Megamenu` entry we created earlier. We will then click on the `Add Block` button and select the `Megamenu` block.

![Add Megamenu Block](../media/add-megamenu-block.png)

Next we will add the `Megamenu-item` block and then the `Megamenu-link-item` block. We will then fill in the necessary fields for each block and hit `Save`.

## Fetch Content from Storyblok and Display in Storefront

To fetch content from Storyblok and display it in the Storefront, we will go to the Storefront and edit the `useNavigations` composable. We will change the `fetchCatalogMenu` method to fetch the `Catalog Menu` from `Storyblok`. Specifically, we need to replace the `getMenu` method call with the `useStoryblok` method call and pass the path to our menu.

```typescript title="client-app/core/composables/useNavigations.ts" linenums="1"
export function useNavigations() {
    // ...
      async function fetchCatalogMenu() {
    // ...

    try {
      if (catalog_menu_link_list_name) {

        // Commented out the old method of fetching the catalog menu
        // catalogMenuItems.value = (await getMenu(catalog_menu_link_list_name)).map((item) =>
        //   convertToExtendedMenuLink(item, true),
        // );

        // Get catalog menu from Storyblok
        catalogMenuItems.value = (
          await useStoryblok("global/megamenu", { version: "draft" })
        ).value.content.global.find((x: any) => x.component === "Megamenu").items;

      } else {
        // ...
      }
    }
    // ...
  }
  // ...
}
```

After making the changes, the `Catalog Menu` will now be fetched from `Storyblok` and displayed in the `Storefront`:

![Catalog Menu](../media/catalog-menu.png)

Now you can publish the changes and see the `Catalog Menu` in the `Storefront`.
