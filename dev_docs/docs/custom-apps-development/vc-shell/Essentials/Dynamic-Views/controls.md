# Overview

Dynamic views allow you to use built-in components within VC Shell to create new views using a new style of description - schemas. Dynamic views under the hood leverage standard components from the VC Shell UI kit but in a slightly modified wrapper. In most cases, all the input data passed to the component when creating the schema use the same names as the component parameters. For the convenience of schema creation, each available component has its new interface.

This guide will explain which components are available for use in dynamic views and what capabilities they offer.

In this guide, we'll use the example of the `vc-app` project schemas, which is located in the `sample/vc-app/src/modules/offers/pages` folder.

[![The source code of sample project](../../../media/source_code.png)](https://github.com/VirtoCommerce/vc-shell/tree/main/sample/vc-app)

## Available Controls

### Button
Based on the `vc-button` component, allows you to add buttons to dynamic views. Could be used to trigger actions separately or in cooperation with other components. Has disabled and visibility state settings. Also has customizable size, icon, icon size, text, method called on click.

#### Usage
To start using all the available button properties, specify the `vc-button` component when creating the schema.

Base usage looks like this:

```typescript
{
    id: "buttonId",
    component: "vc-button",
    method: "buttonClick",
    content: "Button text",
}
```

#### API
Shema interface for button looks like this:

```typescript
interface ButtonSchema {
    id: string;
    component: "vc-button";
    content: string;
    small?: boolean;
    icon?: string;
    iconSize?: "xs" | "s" | "m" | "l" | "xl" | "xxl" | "xxxl";
    text?: boolean;
    method?: string;
    disabled?: {
        method: string;
    };
    visibility?: {
        method: string;
    };
}
```

| Property       | Type              | Description                                                     |
| -------------- | ----------------- | --------------------------------------------------------------- |
| `id`           | `string`          | Unique identifier for `vc-button` component.                    |
| `component`    | `vc-button`       | Component used in schema.                                      |
| `content`      | `string`          | Button inner text.                                              |
| `small`        | `boolean`         | Makes button small sized.                                      |
| `icon`         | `string`          | Button icon. Uses [AwesomeIcons](https://fontawesome.com/) package         |
| `iconSize`     | `string`          | Size of the button icon.                                       |
| `text`         | `string`          | Button as text without overlay.                                |
| `method`       | `string`          | Method to be called when the button is clicked. Method should be defined in the blade `scope`. |
| `disabled`     | `{method: string}` | Disabled state for component, could be used to disable button based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `visibility`   | `{method: string}` | Visibility state for component, could be used to hide button based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |


### Card
Based on the `vc-card` component, allows you to create a card that can contain other components of any depth.
The component has visibility state settings. Accepts an array of component schemas in the fields that will be displayed inside the card. Also has a customizable action button displayed in the top right corner of the card.

#### Usage
To start using all the available card properties, specify the `vc-card` component when creating the schema.

Base usage looks like this:

```typescript
{
    id: "cardId",
    component: "vc-card",
    label: "Card label",
    fields: [
        // other components schemas
    ],
}
```

As card has the ability of deep nesting, you can add other cards or controls to it and create complex UI interfaces.

#### API
Schema interface for card looks like this:

```typescript
interface CardSchema {
    id: string;
    component: "vc-card";
    label: string;
    fields: ControlSchema[];
    action?: ButtonSchema & {
        method: string;
    };
    collapsible?: boolean;
    visibility?: {
        method: string;
    };
}
```

| Property       | Type                                  | Description                                                     |
| -------------- | ------------------------------------- | --------------------------------------------------------------- |
| `id`           | `string`                              | Unique identifier for `vc-card` component.                     |
| `component`    | `vc-card`                             | Component used in schema.                                      |
| `label`        | `string`                              | Card label that is displayed in the header. Also available interpolation `{}` syntax based on current element context.                    |
| `fields`       | `ControlSchema[]`                    | Array of schemas for components that will be displayed inside the card. |
| `action`       | `ButtonSchema & {method: string}`    | Action button that is displayed in the top right corner of the card. Could be used to trigger some actions. |
| `collapsible`  | `boolean`                             | Makes the card collapsible.                                     |
| `visibility`   | `{method: string}`                   | Visibility state for the component, could be used to hide the card based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |


#### Example
Card example with action button and fieldset component containing several inputs from `vc-app` project:

=== "Screenshot"

    ![Card example](../../../media/vc-card.png)

=== "Code"

    ```typescript title="vc-app-extend/src/modules/offers/pages/details.ts" linenums="1"
    {
        id: "pricingCard",
            component: "vc-card",
            label: "Pricing",
            action: {
                id: "addPrice",
                component: "vc-button",
                content: "Add price",
                small: true,
                method: "addPrice",
            },
            fields: [
                {
                id: "pricesFieldset",
                component: "vc-fieldset",
                property: "prices",
                columns: 3,
                remove: {
                    method: "removePrice",
                },
                fields: [
                    {
                        id: "listPrice",
                        component: "vc-input-currency",
                        label: "List price",
                        property: "listPrice",
                        placeholder: "Set list price",
                        optionProperty: "currency",
                        optionValue: "value",
                        optionLabel: "title",
                        rules: {
                            required: true,
                            min_value: 0,
                        },
                    },
                    {
                        id: "salePrice",
                        component: "vc-input-currency",
                        label: "Sales price",
                        property: "salePrice",
                        placeholder: "Set product sales price",
                        optionProperty: "currency",
                        optionValue: "value",
                        optionLabel: "title",
                    },
                    {
                        id: "minQuantity",
                        component: "vc-input",
                        label: "Minimum quantity",
                        property: "minQuantity",
                        placeholder: "Enter product minimal quantity in order",
                        clearable: true,
                        rules: {
                            required: true,
                            min_value: 0,
                        },
                        variant: "number",
                    },
                ],
                },
            ],
    }
    ```

### Checkbox
Based on the `vc-checkbox` component, allows you to create a checkbox that can be checked or unchecked. The component has disabled and visibility state settings. Also has customizable label, content, and many other settings.

#### Usage
To start using all the available checkbox properties, specify the `vc-checkbox` component when creating the schema.

Base usage looks like this:

```typescript
{
    id: "checkboxId",
    component: "vc-checkbox",
    label: "Checkbox label",
    property: "checkboxProperty",
    content: "Checkbox text content",
}
```

#### API
Schema interface for checkbox looks like this:

```typescript
interface CheckboxSchema {
    id: string;
    component: "vc-checkbox";
    trueValue?: boolean;
    falseValue?: boolean;
    label?: string;
    rules?: IValidationRules;
    tooltip?: string;
    property: string;
    content?: string;
    update?: {
        method: string
    };
    disabled?: {
        method: string;
    };
    visibility?: {
        method: string;
    };
}
```



| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique identifier for `vc-checkbox` component. |
| `component` | `string` | `vc-checkbox` |
| `trueValue` | `boolean` | Set value for checked state. |
| `falseValue` | `boolean` | Set value for unchecked state. |
| `label` | `string` | Checkbox label that is displayed above the checkbox. Also available interpolation `{}` syntax based on current element context. |
| `rules` | `IValidationRules` | Checkbox validation rules. Could be used to validate checkbox value. Uses [VeeValidate](https://vee-validate.logaretm.com/v4/) validation rules. |
| `tooltip` | `string` | Checkbox tooltip that is displayed when hovering over the checkbox label tooltip icon. |
| `property` | `string` | Property name that is used for binding checkbox value to blade data. |
| `content` | `string` | Text content that is displayed on the right side of the checkbox. |
| `update` | `{method: string}` | Update method that is called when checkbox value is changed. Method should be defined in the blade `scope`. |
| `disabled` | `{method: string}` | Disabled state for component, could be used to disable checkbox based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide checkbox based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |

### Dynamic Property
Based on the `vc-dynamic-property` component, allows you to display a dynamic properties controls. Has disabled and visibility state settings. Also has customizable label, placeholder, tooltip, and many other settings.

#### Usage
To start using all the available dynamic property properties, specify the `vc-dynamic-properties` component when creating the schema.

Base usage looks like this:

```typescript
{
    id: "dynamicPropertyId",
    component: "vc-dynamic-properties",
    property: "dynamicPropertyProperty",
    exclude: ["propertyToExclude"],
    include: ["propertyToInclude"],
}
```

#### API
Schema interface for dynamic property looks like this:

```typescript
interface DynamicPropertiesSchema {
    id: string;
    component: "vc-dynamic-properties";
    property: string;
    exclude?: string[];
    include?: string[];
    disabled?: {
        method: string;
    };
    visibility?: {
        method: string;
    };
}
```

| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique identifier for `vc-dynamic-properties` component. |
| `component` | `vc-dynamic-properties` | Component used in schema. |
| `property` | `string` | Property name that is used for binding dynamic properties value to blade data. |
| `exclude` | `string[]` | An array of property names to exclude from the dynamic properties schema. |
| `include` | `string[]` | An array of property names to include in the dynamic properties schema. |
| `disabled` | `{method: string}` | Disabled state for component, could be used to disable dynamic properties based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide dynamic properties based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |


### Editor
Based on the `vc-editor` component, allows you to display a Rich Text Editor, based on Vue-wrapped [Quill](https://vueup.github.io/vue-quill/). The component has disabled and visibility state settings. Also has customizable label, placeholder, tooltip, and many other settings.

#### Usage
To start using all the available editor properties, specify the `vc-editor` component when creating the schema.

Base usage looks like this:

```typescript
{
    id: "editorId",
    component: "vc-editor",
    label: "Editor label",
    property: "editorProperty",
    placeholder: "Editor placeholder",
}
```

#### API
Schema interface for editor looks like this:

```typescript
interface EditorSchema {
    id: string;
    component: "vc-editor";
    label?: string;
    property: string;
    rules?: IValidationRules;
    placeholder?: string;
    tooltip?: string;
    multilanguage?: boolean;
    disabled?: {
        method: string;
    };
    visibility?: {
        method: string;
    };
    update?: {
        method: string;
    };
}
```

| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique identifier for the `vc-editor` component. |
| `component` | `vc-editor` | Component used in schema. |
| `label` | `string` | Label for the editor. Also available interpolation `{}` syntax based on current element context. |
| `property` | `string` | Property name that is used for binding editor value to blade data. |
| `rules` | `IValidationRules` | Validation rules for the editor. Uses [VeeValidate](https://vee-validate.logaretm.com/v4/) validation rules. |
| `placeholder` | `string` | Placeholder text for the editor.  |
| `tooltip` | `string` | Tooltip text for the editor label. |
| `multilanguage` | `boolean` | Whether the editor supports multiple languages. |
| `disabled` | `{method: string}` | Disabled state for component, could be used to disable editor based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide editor based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `update` | `{method: string}` | Method to call when the editor value is updated. Method should be defined in the blade `scope`. |

### Fieldset
Fieldset allows displaying sets of any available controls of any nested depth. It allows arranging elements in a grid with a customizable number of columns and aspect ratio that allows to control columns width, the ability to build a grid with multiple rows based on an array of data bound to the fieldset using the `property` option.
Also has visibility state settings and ability to remove elements from the fieldset.

#### Usage
To start using all the available fieldset properties, specify the `vc-fieldset` component when creating the schema.

Base usage looks like this:

```typescript
{
    id: "fieldsetId",
    component: "vc-fieldset",
    fields: [
        // other components schemas
    ],
}
```

As fieldset has the ability of deep nesting, you can add other fieldsets or controls to it and create complex UI interfaces.

#### API
Schema interface for fieldset looks like this:

```typescript
interface FieldsetSchema {
    id: string;
    component: "vc-fieldset";
    fields: ControlSchema[];
    columns?: number;
    property?: string;
    aspectRatio?: number[];
    remove?: {
        method: string;
    };
    visibility?: {
        method: string;
    };
}
```

| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique identifier for the fieldset. |
| `component` | `vc-fieldset` | Component used in schema. |
| `fields` | `ControlSchema[]` | Array of control schemas to be displayed in the fieldset. |
| `columns` | `number` | Number of columns to display the fields in. |
| `property` | `string` | Property name that is used for binding fieldset value to blade data. |
| `aspectRatio` | `number[]` | Array of numbers that define the aspect ratio of each column. Uses CSS flex-grow property. <br> Example: set to [1, 1] to make all columns equal width |
| `remove` | `{method: string}` | Method to call to remove field from the fieldset. When set - activates remove button. Used for property-based fieldsets. Method should be defined in the blade `scope`. |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide fieldset based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |


#### Guide
Fieldset allows you to create different display options for controls. For example, you can create a fieldset with two columns, each of which will have two inputs. To do this, you need to create a fieldset with two inputs and specify the value `2` in the `columns` parameter. You can also specify the `aspectRatio` parameter and set the aspect ratio of the column width. For example, if you specify `[1, 1]`, the columns will be the same width. If you specify `[1, 2]`, the second column will be twice as wide as the first.

Let's look at a few examples of use cases.

1) A regular fieldset with two fields in one column:

```typescript
{
        id: "fieldsetId",
        component: "vc-fieldset",
        fields: [
            {
                id: "input1",
                component: "vc-input",
                label: "Input 1",
                property: "input1",
            },
            {
                id: "input2",
                component: "vc-input",
                label: "Input 2",
                property: "input2",
            },
        ],
}
```

2) If we specify, for example, the number of columns as 2, then we will get a Fieldset with two fields in two columns:

```typescript
{
        id: "fieldsetId",
        component: "vc-fieldset",
        columns: 2,
        fields: [
            {
                id: "input1",
                component: "vc-input",
                label: "Input 1",
                property: "input1",
            },
            {
                id: "input2",
                component: "vc-input",
                label: "Input 2",
                property: "input2",
            },
        ],
}
```

3) If we have an array of data from which we want to build a fieldset, we can use the `property` parameter. In this case, each element of the array will be displayed in a separate fieldset. Also, if we want to add a delete button, we can specify a method that will be called when the delete button is clicked. In this method, we can remove an element from the data array that we specified in the `property` parameter.

```typescript
{
        id: "fieldsetId",
        component: "vc-fieldset",
        property: "fieldsetProperty",
        remove: {
            method: "removeFieldsetElement",
        },
        fields: [
            {
                id: "input1",
                component: "vc-input",
                label: "Input 1",
                property: "input1",
            },
            {
                id: "input2",
                component: "vc-input",
                label: "Input 2",
                property: "input2",
            },
        ],
}
```

If we want each field to have a label that is not manually set, but obtained when building from an array, we can use **interpolation**.
For example, if we want each field to have a label that we get from an object in the array, we can specify the following in the label parameter: `label: "{label}"`. In this case, when building the fieldset, each field will be set a label that will be obtained from the data array.

Let's consider this on the example of a small data array located in `fieldsetProperty`:

```typescript
[
    {
        label: "Label 1",
        value: "Input 1",
    },
    {
        label: "Label 2",
        value: "Input 2",
    }
]
```

Then, if we specify the following fieldset:

```typescript
{
    id: "fieldsetId",
    component: "vc-fieldset",
    property: "fieldsetProperty",
    fields: [
        {
            id: "input1",
            component: "vc-input",
            label: "{label}",
            property: "value",
        },
    ],
}
```

Then, when building the fieldset, each field will be set a label that will be obtained from the data array.

4) Also, we can specify the number of columns and `aspectRatio` for the fieldset, which will be displayed inside the fieldset. In this case, we will get a fieldset with two columns, each of which will have a fieldset with two fields and second fieldset will be twice as wide as the first.

```typescript
{
        id: "fieldsetId",
        component: "vc-fieldset",
        columns: 2,
        aspectRatio: [1, 2],
        fields: [
            {
                id: "fieldsetId",
                component: "vc-fieldset",
                fields: [
                    {
                        id: "input1",
                        component: "vc-input",
                        label: "Input 1",
                        property: "input1",
                    },
                    {
                        id: "input2",
                        component: "vc-input",
                        label: "Input 2",
                        property: "input2",
                    },
                ],
            },
            {
                id: "fieldsetId",
                component: "vc-fieldset",
                fields: [
                    {
                        id: "input1",
                        component: "vc-input",
                        label: "Input 1",
                        property: "input1",
                    },
                    {
                        id: "input2",
                        component: "vc-input",
                        label: "Input 2",
                        property: "input2",
                    },
                ],
            },
        ],
}
```



### Gallery
Based on the `vc-gallery` component, allows you to display a gallery of images. The component has disabled and visibility state settings. Also has customizable upload folder, label, tooltip, and many other settings.

#### Usage
To start using all the available gallery properties, specify the `vc-gallery` component when creating the schema.

Base usage looks like this:

```typescript
{
    id: "galleryId",
    component: "vc-gallery",
    uploadFolder: "folderForFilesUpload"
}
```

#### API
Schema interface for gallery looks like this:

```typescript
interface GallerySchema {
    id: string;
    component: "vc-gallery";
    uploadFolder: string;
    label?: string;
    property: string;
    rules?: IValidationRules;
    tooltip?: string;
    disabled?: {
        method: string;
    };
    visibility?: {
        method: string;
    };
    update?: {
        method: string;
    };
}
```

| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique identifier for the `vc-gallery` component. |
| `component` | `vc-gallery` | Component used in schema. |
| `uploadFolder` | `string` | Folder name for files upload. |
| `label` | `string` | Label for the gallery. Also available interpolation `{}` syntax based on current element context. |
| `property` | `string` | Property name that is used for binding gallery value to blade data. |
| `rules` | `IValidationRules` | Validation rules for the gallery. Uses [VeeValidate](https://vee-validate.logaretm.com/v4/) validation rules. |
| `tooltip` | `string` | Tooltip text for the gallery label. |
| `disabled` | `{method: string}` | Disabled state for component, could be used to disable gallery based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide gallery based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `update` | `{method: string}` | Method to call when the gallery value is updated. Method should be defined in the blade `scope`. |


#### Guide
Gallery allows you to upload files to the specified folder. To do this, you need to specify the `uploadFolder` parameter. The folder name must be specified in the `upload` section of the blade.

To enable file uploads, you should also specify the `assetsHandler` within the composable blade's scope, which uses the gallery. The `assetsHandler` requires the passing of a composing blade responsible for image processing.

In the vc-shell/framework, there exists a generic interface, `AssetsHandler`, which accepts a class type of the asset, for instance, `Image`.

A basic example of a composable for image processing can be found in the `vc-app` sample folder in VirtoCommerce/vc-shell repository: [useAssets](https://github.com/VirtoCommerce/vc-shell/blob/main/sample/vc-app/src/modules/common/composables/useAssets/index.ts). Since dynamic views default to using this composable interface, it's essential to adhere to this specific writing style.

Here's an example of connecting a ready-to-use composable for image processing from the `vc-app` project:

```typescript title="vc-app/src/modules/offers/pages/details.ts" linenums="1"
import { Image } from "@vc-app/api";

const scope = ref<OfferDetailsScope>({
    ...,
    assetsHandler: {
      images: useAssets(Image),
    },
    ...,
})
```

### Input Currency
Based on the `vc-input-currency` component, allows you to display an input with a currency selector. The component has disabled and visibility state settings. Also has customizable label, placeholder, tooltip, and many other settings.

#### Usage
To start using all the available input currency properties, specify the `vc-input-currency` component when creating the schema.

Base usage looks like this:

```typescript
{
    id: "inputCurrencyId",
    component: "vc-input-currency",
    label: "Input currency label",
    property: "inputCurrencyProperty",
    placeholder: "Input currency placeholder",
    optionProperty: "currency",
    optionValue: "value",
    optionLabel: "title",
}
```

where `optionProperty` is object array containing currency data, `optionValue` is the name of the property that contains the value of the currency, `optionLabel` is the name of the property that contains the label of the currency.

Currency array example:

```typescript
[
    {
        value: "USD",
        title: "US Dollar",
    }
]
```

#### API

Schema interface for input currency looks like this:

```typescript
interface InputCurrencySchema {
    id: string;
    component: "vc-input-currency";
    label?: string;
    property: string;
    rules?: IValidationRules;
    placeholder?: string;
    tooltip?: string;
    optionProperty: string;
    optionValue?: string;
    optionLabel?: string;
    disabled?: {
        method: string;
    };
    visibility?: {
        method: string;
    };
    update?: {
        method: string;
    };
}
```

| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique identifier for the `vc-input-currency` component. |
| `component` | `vc-input-currency` | Component used in schema. |
| `label` | `string` | Label for the input currency. Also available interpolation `{}` syntax based on current element context. |
| `property` | `string` | Property name that is used for binding input currency value to blade data. |
| `rules` | `IValidationRules` | Validation rules for the input currency. Uses [VeeValidate](https://vee-validate.logaretm.com/v4/) validation rules. |
| `placeholder` | `string` | Placeholder text for the input currency.  |
| `tooltip` | `string` | Tooltip text for the input currency label. |
| `optionProperty` | `string` | Property that holds available currency options. |
| `optionValue` | `string` | Property that holds the value of the currency. Default: `id` |
| `optionLabel` | `string` | Property that holds the label of the currency. Default: `title` |
| `disabled` | `{method: string}` | Disabled state for component, could be used to disable input currency based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide input currency based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `update` | `{method: string}` | Method to call when the input currency value is updated. Method should be defined in the blade `scope`. |

### Input
Based on the `vc-input` component, allows you to display an input. The component has disabled and visibility state settings. Also has customizable label, placeholder, tooltip, and many other settings.
Also component has customizable slots to show any other component like Button - `append`, `appendInner`, `prepend`, `prependInner`.

#### Usage
To start using all the available input properties, specify the `vc-input` component when creating the schema.

Base usage looks like this:

```typescript
{
    id: "inputId",
    component: "vc-input",
    label: "Input label",
    property: "inputProperty",
    placeholder: "Input placeholder",
}
```

#### API
Schema interface for input looks like this:

```typescript
interface InputSchema {
    id: string;
    component: "vc-input";
    label?: string;
    property: string;
    rules?: IValidationRules;
    placeholder?: string;
    tooltip?: string;
    clearable?: boolean;
    variant?: "number" | "text" | "password" | "email" | "tel" | "url" | "time" | "date" | "datetime-local";
    disabled?: {
        method: string;
    };
    visibility?: {
        method: string;
    };
    update?: {
        method: string;
    };
    prepend?: ControlSchema;
    prependInner?: ControlSchema;
    append?: ControlSchema;
    appendInner?: ControlSchema;
}
```

| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique identifier for the `vc-input` component. |
| `component` | `vc-input` | Component used in schema. |
| `label` | `string` | Label for the input. Also available interpolation `{}` syntax based on current element context. |
| `property` | `string` | Property name that is used for binding input value to blade data. |
| `rules` | `IValidationRules` | Validation rules for the input. Uses [VeeValidate](https://vee-validate.logaretm.com/v4/) validation rules. |
| `placeholder` | `string` | Placeholder text for the input.  |
| `tooltip` | `string` | Tooltip text for the input label. |
| `clearable` | `boolean` | Whether the input has a clear button. |
| `variant` | `string` | Input variant. |
| `disabled` | `{method: string}` | Disabled state for component, could be used to disable input based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide input based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `update` | `{method: string}` | Method to call when the input value is updated. Method should be defined in the blade `scope`. |
| `prepend` | `ControlSchema` | Schema of component to be displayed before the input. |
| `prependInner` | `ControlSchema` | Schema of component to be displayed inside the input before the value. |
| `append` | `ControlSchema` | Schema of component to be displayed after the input. |
| `appendInner` | `ControlSchema` | Schema of component to be displayed inside the input after the value. |


### Select
Based on the `vc-select` component, allows you to display a select. The component has disabled and visibility state settings, customizable template for displayed items. Also has customizable label, placeholder, tooltip, and many other settings.
Supports connecting a method for loading options directly from the server with automatic loading of items when scrolling.

#### Usage
To start using all the available select properties, specify the `vc-select` component when creating the schema.

Base usage looks like this:

```typescript
{
    id: "selectId",
    component: "vc-select",
    label: "Select label",
    property: "selectProperty",
    placeholder: "Select placeholder",
    optionProperty: "optionProperty",
    optionValue: "optionValue",
    optionLabel: "optionLabel",
}
```

where `optionProperty` is object array containing select options, `optionValue` is the name of the property that contains the value of the option, `optionLabel` is the name of the property that contains the label of the option.

#### API
Schema interface for select looks like this:

```typescript
interface SelectSchema {
    id: string;
    component: "vc-select";
    label?: string;
    property: string;
    rules?: IValidationRules;
    placeholder?: string;
    tooltip?: string;
    optionsMethod: string;
    optionValue?: string;
    optionLabel?: string;
    searchable?: boolean;
    clearable?: boolean;
    emitValue?: boolean;
    customTemplate?: {
        component: string;
    };
    disabled?: {
        method: string;
    };
    visibility?: {
        method: string;
    };
    update?: {
        method: string;
    };
}
```

| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique identifier for the `vc-select` component. |
| `component` | `vc-select` | Component used in schema. |
| `label` | `string` | Label for the select. Also available interpolation `{}` syntax based on current element context. |
| `property` | `string` | Property name that is used for binding select value to blade data. |
| `rules` | `IValidationRules` | Validation rules for the select. Uses [VeeValidate](https://vee-validate.logaretm.com/v4/) validation rules. |
| `placeholder` | `string` | Placeholder text for the select.  |
| `tooltip` | `string` | Tooltip text for the select label. |
| `optionsMethod` | `string` | Method to call to get select options. Method should be defined in the blade `scope`. |
| `optionValue` | `string` | Property that holds the value of the option. Default: `id` |
| `optionLabel` | `string` | Property that holds the label of the option. Default: `title` |
| `searchable` | `boolean` | Whether the select is searchable. |
| `clearable` | `boolean` | Whether the select has a clear button. |
| `emitValue` | `boolean` | Update model with the value of the selected option instead of the whole option. If true - emits only selected value, if false - emits whole selected object. |
| `customTemplate` | `{component: string}` | Custom template for select options. Component should be registered globally. |
| `disabled` | `{method: string}` | Disabled state for component, could be used to disable select based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide select based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `update` | `{method: string}` | Method to call when the select value is updated. Method should be defined in the blade `scope`. |


#### Guide
Select allows you to display a list of options. To do this, you need to specify the `optionsMethod` parameter. The method should return an array of objects.

This method should follow the following signature:

```typescript
async function fetchSelectOptions(keyword?: string, skip = 0, ids?: string[]) {
    return await optionsFetchMethod({
        objectIds: ids,
        keyword,
        skip,
        take: 20 // Number of items to load per request
        })
    );
  }
```

To specify what you want to display you should use `optionLabel` as label property and `optionValue` as selected value property.
For example, if you have option like this:

    ```typescript
    {
        id: "optionId",
        title: "Option title",
    }
    ```

Then you should specify `optionLabel: "title"` and `optionValue: "id"`. What is under `optionValue` will be written in the `property` of the select.

### Status
Based on the `vc-status` component, allows you to display a status. The component has visibility state settings. Used to show the status badge with customizable view, icon and its size, title and badge content text.

#### Usage
To start using all the available status properties, specify the `vc-status` component when creating the schema.

Base usage looks like this:

```typescript
{
    id: "statusId",
    component: "vc-status",
    variant: "success",
    icon: "fas fa-check",
    iconVariant: "success",
    iconSize: "xxl",
    title: "Status title",
    content: {
        method: "statusText",
    },
}
```

#### API
Schema interface for status looks like this:

```typescript
interface StatusSchema {
    id: string;
    component: "vc-status";
    variant: "info" | "warning" | "danger" | "success" | "light-danger";
    icon?: string;
    iconVariant?: "warning" | "danger" | "success";
    iconSize?: "xs" | "s" | "m" | "l" | "xl" | "xxl" | "xxxl";
    title?: string;
    outline?: boolean;
    extend?: boolean;
    content?: {
        method: string;
    };
    visibility?: {
        method: string;
    };
}
```

| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique identifier for the `vc-status` component. |
| `component` | `vc-status` | Component used in schema. |
| `variant` | `string` | Status variant. |
| `icon` | `string` | Icon to show in status badge. Uses [AwesomeIcons](https://fontawesome.com/) package  |
| `iconVariant` | `string` | Icon variant. |
| `iconSize` | `string` | Icon size. |
| `title` | `string` | Status title. |
| `outline` | `boolean` | Whether the status is outlined or not. |
| `extend` | `boolean` | Whether the status is extendable or not. |
| `content` | `{method: string}` | Method to call to get status content. Method should be defined in the blade `scope` and should return string value. |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide status based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |

### Data field
Based on the `vc-field` component, allows you to display a data field. The component has visibility state settings. Used to show simple string data with label.
Could be used to display text, date, date-ago and links. Also has ability to copy displayed value.

#### Usage
To start using all the available data field properties, specify the `vc-field` component when creating the schema.

Base usage looks like this:

```typescript
{
    id: "fieldId",
    component: "vc-field",
    label: "Field label",
    property: "fieldProperty",
    type: "text",
    copyable: true
}
```

#### API
Schema interface for data field looks like this:

```typescript
interface FieldSchema {
    id: string;
    component: "vc-field";
    label?: string;
    tooltip?: string;
    property: string;
    variant: "text" | "date" | "date-ago" | "link";
    copyable?: boolean;
    visibility?: {
        method: string;
    };
}
```

| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique identifier for the `vc-field` component. |
| `component` | `vc-field` | Component used in schema. |
| `label` | `string` | Label for the field. Also available interpolation `{}` syntax based on current element context. |
| `tooltip` | `string` | Tooltip text for the field label. |
| `property` | `string` | Property name that is used for binding field value to blade data. |
| `variant` | `string` | Field variant. Default: `text` |
| `copyable` | `boolean` | Whether the field is copyable or not. |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide field based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |


### Image
Based on the `vc-image` component, allows you to display an image. The component has visibility state settings. Also has customizable size options, aspect ratio, and many other settings.

#### Usage
To start using all the available image properties, specify the `vc-image` component when creating the schema.

Base usage looks like this:

```typescript
{
    id: "imageId",
    component: "vc-image",
    property: "imagePropertyWithUrl",
    size: "xl",
    background: "contain",
    bordered: true
}
```

#### API

Schema interface for image looks like this:

```typescript
interface ImageSchema {
    id: string;
    component: "vc-image";
    property: string;
    aspect?: "1x1" | "16x9" | "4x3" | "3x2";
    background?: "auto" | "cover" | "contain";
    size?: "auto" | "xs" | "s" | "m" | "l" | "xl" | "xxl";
    rounded?: boolean;
    bordered?: boolean;
    clickable?: boolean;
    visibility?: {
        method: string;
    };
    update?: {
        method: string;
    };
}
```

| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique identifier for the `vc-image` component. |
| `component` | `vc-image` | Component used in schema. |
| `property` | `string` | Property name that is used for binding image url value to blade data. |
| `aspect` | `string` | Image aspect ratio. Default: `1x1`|
| `background` | `string` | Size of the element's background image. Accepts auto, cover, contain CSS background-size value. Default: `cover` |
| `size` | `string` | Image size. Default: `auto` |
| `rounded` | `boolean` | Whether the image is rounded or not. |
| `bordered` | `boolean` | Whether the image is bordered or not. |
| `clickable` | `boolean` | Whether the image has preview on click or not. Default: `false` |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide image based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `update` | `{method: string}` | Method to call when the image url value is updated. Method should be defined in the blade `scope`. |

### Video
Based on the `vc-video` component, allows you to display a YouTube video in iframe. The component has visibility state settings. Also has customizable size options, and many other settings.

#### Usage
To start using all the available video properties, specify the `vc-video` component when creating the schema.

Base usage looks like this:

```typescript
{
    id: "videoId",
    component: "vc-video",
    property: "videoPropertyWithUrl",
    label: "Video label",
    size: "xl",
}
```

#### API

Schema interface for video looks like this:

```typescript
interface VideoSchema {
    id: string;
    component: "vc-video";
    property: string;
    label?: string;
    size?: "auto" | "xs" | "s" | "m" | "l" | "xl" | "xxl";
    tooltip?: string;
    visibility?: {
        method: string;
    };
    update?: {
        method: string;
    };
}
```

| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique identifier for the `vc-video` component. |
| `component` | `vc-video` | Component used in schema. |
| `property` | `string` | Property name that is used for binding video url value to blade data. |
| `label` | `string` | Label for the video. Also available interpolation `{}` syntax based on current element context. |
| `size` | `string` | Video size. Default: `auto` |
| `tooltip` | `string` | Tooltip text for the video label. |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide video based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `update` | `{method: string}` | Method to call when the video url value is updated. Method should be defined in the blade `scope`. |


