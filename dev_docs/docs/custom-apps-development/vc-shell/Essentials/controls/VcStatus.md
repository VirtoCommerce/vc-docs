# Status

The status component is used to display a status badge with customizable view and icon as well as its size, title, and badge content text.

## Usage

Include the `vc-status` component in your Vue application, providing theming and enhanced functionality to your status inputs.

![vc-status](../../../media/status-basic.png)

=== "Basic Vue"

    Create a basic status as follows:

    ```html
    <template>
        <vc-status variant="danger" :outline="false">Status text</vc-status>
    </template>
    ```

=== "Dynamic Views"

    To start using all the available status properties, specify the `vc-status` component when creating the schema. For example:

    ```typescript
    {
        id: "statusId",
        component: "vc-status",
        variant: "danger",
        content: {
            method: "statusText",
        },
    }
    ```

## Status API

API empowers you to create dynamic and interactive status components to customize its appearance and behavior.

## Basic Vue

You can easily incorporate the `vc-status` component into your Vue applications using simple templates. 

### Props

To customize the appearance and behavior of statuses, use the following props:

| Property and Type                                                                             | Description                                                |
| ----------------------------------------------------------------------------------------------| ---------------------------------------------------------- |
| `variant` {=="info"==}, {=="warning"==}, {=="danger"==}, {=="success"==}, {=="light-danger"==}| Status variant.                                            |
| `outline` {==boolean==}                                                                       | Whether the status is outlined or not.                     |
| `extend` {==boolean==}                                                                        | Whether the status is extendable or not.                   |

### Slots

To enhance the content of the `vc-status` component, use the slot system:

| Name      | Description                                                     |
| --------- | --------------------------------------------------------------- |
| `default` | Status content slot.                                            |


## Dynamic Views

To dynamically integrate the `vc-status` component into your views, use the schema interface:

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

To incorporate the status into your dynamic applications, define the following properties:

| Property                              | Description                                                           |
| ------------------------------------- | --------------------------------------------------------------------  |
| `id` {==string==}                     | The unique Id for the `vc-status` component.                          |
| `component` {==vc-status==}           | Component used in schema.                                             |
| `variant` {==string==}                | Status variant.                                                       |
| `icon` {==string==}                   | Icon to show in status badge. Uses [AwesomeIcons](https://fontawesome.com/) package  |
| `iconVariant` {==string==}            | Icon variant.                                                         |
| `iconSize` {==string==}               | Icon size.                                                            |
| `title` {==string==}                  | Status title.                                                         |
| `outline` {==boolean==}               | Whether the status is outlined or not.                                |
| `extend` {==boolean==}                | Whether the status is extendable or not.                              |
| `content` {=={method: string}==}      | Method to call to get status content. Method should be defined in the blade `scope` and should return string value. |
| `visibility` {=={method: string}==}   | Visibility state for component, could be used to hide status based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |