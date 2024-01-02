# Video
Displays a YouTube video in iframe.

## Usage
![vc-video](./../../../../media/controls/atoms/vc-video/vc-video.png)

Video is created with `source` property.

=== "Basic Vue"


    ```html
    <template>
        <vc-video :source="https://video-url"></vc-video>
    </template>
    ```

=== "Dynamic Views"

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

## Video API

## Basic Vue

### Props

| Property | Type | Description |
| --- | --- | --- |
| `label` | `string` | Label for the video. Also available interpolation `{}` syntax based on current element context. |
| `tooltip` | `string` | Tooltip text for the video label. |
| `source` | `string` | The source URL of the video. |
| `size` | `"auto" \| "xs" \| "s" \| "m" \| "l" \| "xl" \| "xxl"` | Video size. Default: `auto` |

## Dynamic Views

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
| `property` | `string` | Property name that is used for binding video url value to blade data.  <br> Supports deep nested properties like `property[1].myProperty`. <br> Additionally, you have the flexibility to bind any function or computed property that returns a value and retrieve changed value as an argument for the function.|
| `label` | `string` | Label for the video. Also available interpolation `{}` syntax based on current element context. |
| `size` | `string` | Video size. Default: `auto` |
| `tooltip` | `string` | Tooltip text for the video label. |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide video based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `update` | `{method: string}` | Method to call when the video url value is updated. Method should be defined in the blade `scope`. |


