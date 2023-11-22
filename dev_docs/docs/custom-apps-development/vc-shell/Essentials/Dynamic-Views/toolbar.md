# Overview
The toolbar allows you to create buttons with additional actions upon clicking, such as saving or deleting data. Each toolbar button has customizable visibility, disabled status, icon, text, and a customizable method that will be invoked when the button is clicked.

## Toolbar schema creation
To create toolbar schema you should pass `toolbar` property to the view schema object.

Lets take a look at minified schema of the view:

```typescript
import { DynamicDetailsSchema } from "@vc-shell/framework";

const schema: DynamicDetailsSchema = {
  settings: {
    // ...
    toolbar: [
      {
        id: "createItem",
        title: "Create New Item",
        icon: "fas fa-plus",
        method: "create",
      },
    ],
  },
};
```

This schema will create toolbar with one button with `createItem` id, `Create New Item` title, `fas fa-plus` icon and `create` method.

But this button will not be visible until you add `create` method to the `toolbarOverrides` object in the view composable `scope`. Lets take a look how to do it in next section.

## Creating toolbar methods and properties

So, if you have toolbar schema like this:

```typescript
toolbar: [{
    id: "createItem",
    title: "Create New Item",
    icon: "fas fa-plus",
    method: "create",
}],
```

you should add `create` method to your `toolbarOverrides` object:

```typescript
const useList = (args: // ...): UseList => {
    const scope = ref<ListScope>({
        // ...
        toolbarOverrides: {
            create: () => {
                // your custom logic here
            },
        },
    });
}
```

or you can create object with `visible` and `disabled` properties and also `clickHandler` method:

```typescript
const useList = (args: // ...): UseList => {
    const scope = ref<ListScope>({
        // ...
        toolbarOverrides: {
            create: {
                clickHandler() {
                    // your custom logic here
                },
                visible: true,
                disabled: false,
            }
        }
    });
}
```

`visible` and `disabled` properties can be boolean, function or even computed property that returns boolean value.

`clickHandler` method also has argument with provided `bladeContext` object.

!!! note
    More about `bladeContext` object you can find in [DynamicBladeList Blade Context](./views/DynamicBladeList.md#dynamicbladelist-blade-context) and  [DynamicBladeForm Blade Context](./views/DynamicBladeForm.md#dynamicbladeform-blade-context) section.

## Toolbar default methods
Every view has default toolbar methods that can be used in toolbar schema and also could be overridden in `toolbarOverrides` object.

You can find more information about default methods in [DynamicBladeForm Toolbar Defaults](../default-methods.md) or [DynamicBladeForm Toolbar Defaults](../default-methods.md) sections.

## Overriding default toolbar methods and properties
As every view has default toolbar methods and properties, you can override them in `toolbarOverrides` object like adding new one.

For example, if you have default toolbar schema with it's method and disabled state, you can override only method or only disabled state or both of them. And also you can add visibility property, if default toolbar button doesn't have it.
