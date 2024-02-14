# Custom component

The custom component allows you to add any component to your Dynamic View blade. It can be a custom Vue component or a third-party component in your custom wrapper.

## Usage

Include the `vc-custom` component in your Vue application:

```typescript
{
    id: "customComponentId",
    component: "vc-custom",
    name: "CustomComponentName"
}
```

!!! note
    Component that you want to use should be globally registered in your application.

## Component creation

The custom component, by default, includes the incoming prop `context`, containing the blade context. This context holds the `item` object, which contains data about the current item displayed in the blade, along with other data useful for the custom component.

The default `Props`:

```typescript
const props = defineProps<{
    context: UseList | UseDetails;
}>();
```

`context` uses `UseList` or `UseDetails` generic types, which are defined in the `@vc-shell/framework` package.

!!! note
    More info about `UseList` generic type can be found [here](../dynamic-views/Dynamic-Blade-List.md#implement-composable-from-uselistfactory) and about `UseDetails` generic type [here](../dynamic-views/Dynamic-Blade-Form.md#implement-composable-from-usedetailsfactory).

## Custom component API

## Dynamic Views

To dynamically integrate the `vc-custom` component into your views, use the schema interface:

```typescript
interface CustomComponentSchema {
    id: string;
    component: "vc-custom";
    name: string;
    visibility?: {
        method: string;
    };
}
```

To incorporate the checkbox into your dynamic applications, define the following properties:

| Property                  | Description                                                                                                                                               |
| ------------------------- |  -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id` {==string==}         | The unique Id for `vc-checkbox` component.                                                                                                                |
| `component` {==string==}  | `vc-checkbox`                                                                                                                                             |
| `name` {==string==} | Name of the component to show as custom component. Should be globally registered in your application.                                                                                                                               |
| `visibility` {=={method: string}==} | Visibility state for component, could be used to hide checkbox based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
