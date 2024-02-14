# Rating

Rating is a control that can display a rating with various representations.

## Usage

Include the `vc-rating` component in your Vue application:

![vc-rating](../../../media/vc-rating.png)

=== "Basic Vue"

    Create a basic rating as follows:

    ```html
    <template>
        <vc-rating :modelValue="ratingProperty"></vc-rating>
    </template>
    ```

=== "Dynamic Views"

    To start using all the available rating properties, specify the `vc-rating` component when creating the schema. For example:

    ```typescript
    {
        id: "ratingId",
        component: "vc-rating",
        property: "ratingProperty",
    }
    ```

## Rating API

API empowers you to create dynamic and interactive rating components to customize its appearance and behavior.

## Basic Vue

You can easily incorporate the `vc-rating` component into your Vue applications using simple templates.

### Props

To customize the appearance and behavior of rating component, use the following props:

| Property and Type                  | Description                                           |
| ---------------------------------- |  ---------------------------------------------------- |
| `modelValue` {==number==}| The value of the component.                           |
| `label` {==string==}               | The label of the component.                           |
| `tooltip` {==string==}             | The tooltip text to display when hovering over the component. |
| `placeholder` {==string==} | Placeholder text to show when no `modelValue` provided |
| `max` {==number==} | Maximum quantity of rating stars. Default: `5` |
| `variant` {==stars\|star-and-text\|text ==} | Representation variant. Default: `stars` |

### Slots

To enhance the content of the `vc-rating` component, use the slot system:

| Name      | Description                                      |
| --------- | -------------------------------------------------|
| `details` | Slot to show any text or component when the `star-and-text` variant is chosen.                      |

## Dynamic Views

To dynamically integrate the `vc-rating` component into your views, use the schema interface:

```typescript
interface RatingSchema {
    id: string;
    component: "vc-rating";
    label?: string;
    tooltip?: string;
    placeholder?: string;
    property: string;
    max?: number;
    type?: "text" | "stars" | "star-and-text";
    update?: {
        method: string
    };
    visibility?: {
        method: string;
    };
    horizontalSeparator?: boolean;
}
```

To incorporate the rating into your dynamic applications, define the following properties:

| Property                  | Description                                                                                                                                               |
| ------------------------- |  -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id` {==string==}         | The unique Id for `vc-rating` component.                                                                                                                |
| `component` {==string==}  | `vc-rating`                                                                                                                                             |
| `label` {==string==}      | Rating component label that is displayed above the rating. Also available interpolation `{}` syntax based on current element context. You can specify the localization key for the `label`. Under the hood, [vue-i18n](https://kazupon.github.io/vue-i18n/) is used.                      |
| `tooltip` {==string==}    | Rating tooltip that is displayed when hovering over the rating label tooltip icon. You can specify the localization key for the `tooltip`. Under the hood, [vue-i18n](https://kazupon.github.io/vue-i18n/) is used.                                                                   |
| `placeholder` {==string==}   | Placeholder text to show when no `modelValue` provided |
| `property` {==string==}   | Property name that is used for binding rating value to blade data. <br> Supports deep nested properties like `property[1].myProperty`. <br> Additionally, you have the flexibility to bind computed property that returns a value. Computed property should be defined in the blade `scope`.                                                               |
| `max` {==number==} | Maximum quantity of rating stars. Default: `5` |
| `type` {==text\|stars\|star-and-text==} | Representation variant. Default: `stars` |
| `update` {=={method: string}==} | Update method that is called when rating value is changed. It gets changed value, schema property name and field internal context as arguments. Method should be defined in the blade `scope`.                                        |
| `visibility` {=={method: string}==} | Visibility state for component, could be used to hide rating based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `horizontalSeparator` {==boolean==}       | Adds a horizontal separator line after the component. |
