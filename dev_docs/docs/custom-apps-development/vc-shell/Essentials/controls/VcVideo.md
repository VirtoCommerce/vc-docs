# Video

The video component displays a YouTube video in an iframe.

## Usage

Include the `vc-video` component in your Vue application, providing theming and enhanced functionality to your video inputs.

![vc-video](../../../media/vc-video.png)

Video is created with `source` property.

=== "Basic Vue"

    Create a basic video as follows:

    ```html
    <template>
        <vc-video :source="https://video-url"></vc-video>
    </template>
    ```

=== "Dynamic Views"

    To start using all the available video properties, specify the `vc-video` component when creating the schema. For example:

    ```typescript
    {
        id: "videoId",
        component: "vc-video",
        property: "videoPropertyWithUrl",
        label: "Video label",
        size: "xl",
    }
    ```

## Video API

API empowers you to create dynamic and interactive video components to customize its appearance and behavior.

## Basic Vue

You can easily incorporate the `vc-video` component into your Vue applications using simple templates. 

### Props

To customize the appearance and behavior of videos, use the following props:

| Property and Type             | Description                       |
| ----------------------------- | --------------------------------- |
| `label` {==string==}          | Label for the video. Also available interpolation `{}` syntax based on current element context. |
| `tooltip` {==string==}        | Tooltip text for the video label. |
| `source` {==string==}         | The source URL of the video.      |
| `size` {=="auto"==}, {=="xs"==}, {=="s"==}, {=="m"==}, {=="l"==}, {=="xl"==}, {=="xxl"==} | Video size. Default: `auto` |

## Dynamic Views

To dynamically integrate the `vc-video` component into your views, use the schema interface:

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

To incorporate the status into your dynamic applications, define the following properties:

| Property and Type                         | Description                                 |
| ----------------------------------------- | ------------------------------------------- |
| `id` {==string==}                         | The unique Id for the `vc-video` component. |
| `component` {==vc-video==}                | Component used in schema.                   |
| `property` {==string==}                   | Property name that is used for binding video url value to blade data.  <br> Supports deep nested properties like `property[1].myProperty`. <br> Additionally, you have the flexibility to bind any function or computed property that returns a value and retrieve changed value as an argument for the function.|
| `label` {==string==}                      | Label for the video. Also available interpolation `{}` syntax based on current element context. |
| `size` {==string==}                       | Video size. Default: `auto` |
| `tooltip` {==string==}                    | Tooltip text for the video label. |
| `visibility` {=={method: string}==}           | Visibility state for component, could be used to hide video based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `update` {=={method: string}==}               | Method to call when the video url value is updated. Method should be defined in the blade `scope`. |

