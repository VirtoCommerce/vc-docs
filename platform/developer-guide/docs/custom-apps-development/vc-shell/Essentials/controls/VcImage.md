# Image

The image component displays a single image.

## Storybook

Explore the `vc-image` component in the [VC Shell Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vcimage--docs).

Dynamic Views examples are also available in the [VC Shell Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/dynamicviews-atoms-vcimage--docs) for a better understanding of the component usage.

## Usage

Include the `vc-image` component in your Vue application, providing theming and enhanced functionality to your image inputs.

Image is created with `src` property.

=== "Basic Vue"

    Create a basic image as follows:

    ```html
    <template>
        <vc-image :src="https://image-url"></vc-image>
    </template>
    ```

=== "Dynamic Views"

    To start using all the available image properties, specify the `vc-image` component when creating the schema. For example:

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

## Image API

API empowers you to create dynamic and interactive image components to customize its appearance and behavior.

## Basic Vue

You can easily incorporate the `vc-image` component into your Vue applications using simple templates.

### Props

To customize the appearance and behavior of images, use the following props:

| Property      | Type                                              | Description                                                       |
| --------------|------------------------------------------------   | ----------------------------------------------------------------- |
| `aspect`      | `"1x1"`, `"16x9"`, `"4x3"`, `"3x2"`               | Image aspect ratio. Default: `"1x1"`                              |
| `rounded`     | `boolean`                                         | Whether the image is rounded or not.                              |
| `bordered`    | `boolean`                                         | Whether the image is bordered or not.                             |
| `clickable`   | `boolean`                                         | Whether the image has preview on click or not. Default: `false`   |
| `src`         | `string`                                          | The source URL of the image.                                      |
| `size`        | `"auto"`, `"xs"`, `"s"`, `"m"`, `"l"`, `"xl"`, `"xxl"` | Image size. Default: `auto`                                   |
| `background`  | `"cover"`, `"contain"`, `"auto"`                  | Size of the element's background image. Accepts auto, cover, contain CSS background-size value. Default: `cover` |

### Emits

To interact with the `vc-image` component, use the emitted events. The `click` event, triggered when the button is clicked, allows you to implement dynamic behaviors and responses within your application:

| Name      | Parameters        | ReturnType | Description                                                     |
| --------- | ----------------- | ---------- | --------------------------------------------------------------- |
| `click`   | `void`            | `void`     | Emitted when the image is clicked.                              |

## Dynamic Views

To dynamically integrate the `vc-image` component into your views, use the schema interface:

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
    horizontalSeparator?: boolean;
}
```

To incorporate the image into your dynamic applications, define the following properties:

| Property      | Type                                  | Description |
| --------------|---------------------------------------| ----------- |
| `id`          | `string`                              | The unique Id for the `vc-image` component. |
| `component`   | `vc-image`                            | Component utilized in the schema. |
| `property`    | `string`                              | Name of the property used for binding the image URL value to blade data. Supports deep nested properties, such as `property[1].myProperty`. <br> Additionally, you have the flexibility to bind computed property that returns a value. Computed property should be defined in the blade `scope`. |
| `aspect`      | `string`                              | Image aspect ratio. Default: `1x1`. |
| `background`  | `string`                              | Size of the element's background image. Accepts CSS background-size values like auto, cover, or contain. Default: `cover`. |
| `size`        | `string`                              | Image size. Default: `auto`. |
| `rounded`     | `boolean`                             | Specification of whether the image should have rounded corners. |
| `bordered`    | `boolean`                             | Specification of whether the image should have a border. |
| `clickable`   | `boolean`                             | Specification of whether the image has a preview on click. Default: `false`. |
| `visibility`  | `{method: string}`                    | Definition of the visibility state for the component, allowing you to hide the image based on certain conditions. The method or variable should be defined in the blade `scope` and return a boolean value. |
| `update`      | `{method: string}`                    | Specification of the method to call when the image URL value is updated. It gets changed value, schema property name and field internal context as arguments. The method should be defined in the blade `scope`. |
| `horizontalSeparator` | `boolean`                     | Adds a horizontal separator line after the component. |

