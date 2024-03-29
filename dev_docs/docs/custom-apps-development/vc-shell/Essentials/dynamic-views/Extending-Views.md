# Extending Views

You can significantly improve the interactivity and functionality of your applications by introducing new buttons and controls to your forms, thereby extending the user interface. When dealing with applications that rely on blades built with dynamic views, you can augment these views with fresh UI elements such as fields, forms, lists, and more. The best part is that you can achieve this without the need to make direct modifications to the source code of the application you're extending.

In this guide, we will explore the `Offers` module, and specifically, the `useOffersList` and `useOfferDetails` composables that we are extending.

## Extending Views in Other Applications Using Dynamic Views

Expanding the views of external applications is accomplished through the creation of a new override schema. In this schema, you specify the unique `id` of the `blade` you intend to extend, the path to the element schema, the index, and the value you intend to add or replace.

### Structure of the Override Schema

The override schema is an object that can contain two values: `upsert` and `remove`. Both of these values share a common characteristic, which is the requirement for you to specify the path to the schema `value` and the `id` of the blade you intend to modify.

* The path operates similarly to JSONPath and involves obtaining a value based on a specified path within the object. A basic representation of a path looks like this:

    ```typescript
    const schema = { a: [{ b: { c: 3 } }];

    const path = "a[0].b.c";
    ```

* The Blade ID serves as a unique identifier for the blade and is specified in the schema with the `id` value.

### Understanding Upsert and Removal

When working with the DynamicBladeForm, it's crucial to understand two key operations which provide a robust mechanism for modifying the underlying schema:

* [Upsert.](Extending-Views.md#upsert)
* [Removal.](Extending-Views.md#removal)

#### Upsert

Upsert is an array of objects, and each object can have two possible actions: replace and add. These actions follow the same structure, and the specific action depends on whether you specify the ID of an existing control or if it's a new control.

Upsert adheres to a simplified interface:

```typescript
{
    id: string // Blade ID
    path: string // Path to the desired control in the schema
    index?: number // Position of the element if the schema of the control is an array
    value: // Value to be changed or added
    | {
        id: string // Control ID - new or existing
        ...
    }
    | string | boolean
}
```

The possible interactions with `upsert` are:

* [Adding a new control to the schema.](Extending-Views.md#adding-a-new-control-to-the-schema)
* [Replacing the existing control in the schema.](Extending-Views.md#replacing-an-existing-control-in-the-schema)


##### Adding new control to the schema

To incorporate a new control into the schema using upsert, you need to know the ID of the blade where you intend to add the control and determine how to navigate the path of the control in the base schema. For instance, if you want to add a new input to the `Offer` form, you can find a simplified base schema in the VirtoCommerce/vc-shell repository, located in the `sample` folder, within the 'vc-app' project at this [link](https://github.com/VirtoCommerce/vc-shell/blob/main/sample/vc-app/src/modules/offers/pages/details.ts#L38-L228).

Suppose you wish to add this control to the form with `id: "offersForm,"` nested within the component with `id: "inventoryCard." A simplified schema might look like this:

```typescript
{
 ...
 content: [
     {
         id: "offersForm",
         component: "vc-form",
         children: [
            {
                // some input with index === 0
            },
            {
                id: "inventoryCard",
                component: "vc-card",
                label: "Inventory",
                fields: [
                    {
                        id: "sku",
                        component: "vc-input",
                        label: "SKU",
                        property: "sku",
                        rules: {
                            required: true,
                        },
                    },
                ]
            },
            {
                // some input with index === 2
            },
            ...
         ]
     }
 ]
}
```

The component with `id: "inventoryCard"` represents the `VcCard` component, and all of its content resides within the `fields` array. Let's assume this is where you want to add a new control.

Since the `offersForm` component is within the `content` array of the base schema, and all of its content is nestled within the `children` array, the path would be as follows:

```typescript
const path = "content[0].children[1].fields";
```

Where:

* `content[0]` corresponds to the schema with `id: "offersForm"`
* `children[1]` corresponds to the schema with `id: "inventoryCard"`
* `fields` represents the array of the `inventoryCard` schema

Given that `fields` is an array, you can specify the position for the new element within this array using the 'index' key. If the index is not specified, the new element will be added at the end of the array. In this example, you want to prepend the control, so you opt for index 0.

Since you are adding a new input, the ID of this input should be unique. In this case, let's specify it as `exampleInput.`

The final record for adding a new element would look like this:

```typescript
export const overrides: OverridesSchema = {
upsert: [
    // Adding a new input control that will display data from the 'newField' property
    {
        id: "Offer",
        path: "content[0].children[1].fields",
        index: 0,
        value: {
            id: "exampleInput",
            component: "vc-input",
            label: "New Field",
            property: "newField",
        },
    },
    ...
],
};
```

##### Replacing existing control in the schema

The process of replacing a control in the schema is similar to adding a new one but with some differences:

* You don't need to specify an index.
* The ID of the added control should match the one you want to replace.

For example, in the base schema available at this [link](https://github.com/VirtoCommerce/vc-shell/blob/main/sample/vc-app/src/modules/offers/pages/details.ts#L64), there is a control with `id: "sku."` The final schema to replace this control could look like this:

```typescript
export const overrides: OverridesSchema = {
upsert: [
    // Replacing the SKU input control with a new input control that will display data from the 'newField' property
    {
        id: "Offer",
        path: "content[0].children[1].fields",
        value: {
            id: "sku",
            component: "vc-input",
            label: "New Field",
            property: "newField",
        },
    },
    ...
],
};
```

#### Removal
Removal follows the same schema as upsert, but for removal, you only need to specify the blade ID and the path where you want to delete the element. For example, if you want to remove the element with `id: "sku"` from the base schema, the simplified schema path would look like this:

```typescript


content: [
     {
             id: "offersForm",
             component: "vc-form",
             children: [
                {
                    // some input with index === 0
                },
                {
                    id: "inventoryCard",
                    component: "vc-card",
                    label: "Inventory",
                    fields: [
                        {
                            id: "sku",
                            component: "vc-input",
                            label: "SKU",
                            property: "sku",
                            rules: {
                                required: true,
                            },
                        },
                    ]
                },
                {
                    // some input with index === 2
                },
                ...
             ]
]
```

As seen in the schema, the path to the `sku` input would look like this:

```typescript
const path = "content[0].children[1].fields[0]";
```

Where:

* `content[0]` represents the schema with `id: "offersForm"`
* `children[1]` represents the schema with `id: "inventoryCard"`
* `fields[0]` corresponds to the schema with `id: "sku"`

The final schema for removing the `sku` input would look like this:

```typescript
export const overrides: OverridesSchema = {
upsert: [
    // Removing the SKU input
    {
        id: "Offer",
        path: "content[0].children[1].fields[0]",
    },
    ...
],
};
```