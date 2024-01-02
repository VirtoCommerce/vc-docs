# Image
Displays a single image.

## Usage
Image is created with `src` property.

=== "Basic Vue"

    ```html
    <template>
        <vc-image :src="https://image-url"></vc-image>
    </template>
    ```

=== "Dynamic Views"

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

## Image API

## Basic Vue

### Props

| Property | Type | Description |
| --- | --- | --- |
| `aspect` | `"1x1" \| "16x9" \| "4x3" \| "3x2"` | Image aspect ratio. Default: `1x1` |
| `rounded` | `boolean` | Whether the image is rounded or not. |
| `bordered` | `boolean` | Whether the image is bordered or not. |
| `clickable` | `boolean` | Whether the image has preview on click or not. Default: `false` |
| `src` | `string` | The source URL of the image. |
| `size` | `"auto" \| "xs" \| "s" \| "m" \| "l" \| "xl" \| "xxl"` | Image size. Default: `auto` |
| `background` | `"cover" \| "contain" \| "auto"` | Size of the element's background image. Accepts auto, cover, contain CSS background-size value. Default: `cover` |

### Emits

| Name      | Parameters        | ReturnType | Description                                                     |
| --------- | ----------------- | ---------- | --------------------------------------------------------------- |
| `click` | `void` | `void` | Emitted when the image is clicked.                |

## Dynamic Views

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
| `property` | `string` | Property name that is used for binding image url value to blade data.  <br> Supports deep nested properties like `property[1].myProperty`. <br> Additionally, you have the flexibility to bind any function or computed property that returns a value and retrieve changed value as an argument for the function.|
| `aspect` | `string` | Image aspect ratio. Default: `1x1`|
| `background` | `string` | Size of the element's background image. Accepts auto, cover, contain CSS background-size value. Default: `cover` |
| `size` | `string` | Image size. Default: `auto` |
| `rounded` | `boolean` | Whether the image is rounded or not. |
| `bordered` | `boolean` | Whether the image is bordered or not. |
| `clickable` | `boolean` | Whether the image has preview on click or not. Default: `false` |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide image based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `update` | `{method: string}` | Method to call when the image url value is updated. Method should be defined in the blade `scope`. |
