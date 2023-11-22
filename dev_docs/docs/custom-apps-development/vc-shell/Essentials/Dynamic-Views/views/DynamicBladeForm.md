# Overview

This type of view allows you to create blades containing a form. Here is a list of features for this view:
1) Built-in validation
2) Ability to create complex UI forms
3) Customizable component in the blade header
4) Ability to connect widgets

## Creating a composable for DynamicBladeForm
To create a composable for `DynamicBladeForm`, you need to use the built-in composable factory function named `useDetailsFactory`. This factory returns a composable method that provides you with all the necessary methods and properties to work with the form.

### useDetailsFactory API
The `useDetailsFactory` function return an object with the following properly typed properties:

| Property | Type | Description |
| --- | --- | --- |
| `item` | `Ref<Item | undefined>` | The current loaded details item. |
| `loading` | `Ref<boolean>` | Indicates whether the data is loading. |
| `validationState` | `ComputedRef<IValidationState<Item>>` | Validation state and methods of the form. <br> More information about [validationState](#validationState) section |
| `load` | `AsyncAction<ItemId>` | The method used to load the details item. |
| `saveChanges` | `AsyncAction<Item>` | The method used to create or save the details item. |
| `remove` | `AsyncAction<ItemId>` | The method used to remove the details item. |

This function accepts an object with callback methods `load`, `saveChanges`, `remove`, which you should implement. The `load` method is used for loading the details item. The `saveChanges` method is used for creating or saving the details item. The `remove` method is used for removing the details item.

!!! note
    The `load`, `saveChanges` and `remove` methods must return a promise.

### Composable Anatomy

#### Implementing composable from `useDetailsFactory`

Let's create a file named `useDetails.ts` in the `composables` folder of your module and add the following code:

```typescript
import { useDetailsFactory, UseDetails } from "@vc-shell/framework";

const useDetails = (): UseDetails => {
    const factory = useDetailsFactory({
        load: async ([ id ]) => {
            // return your load method here
        },
        saveChanges: async (details) => {
            // return your saveChanges method here
        },
        remove: async ({ id }) => {
            // return your remove method here
        }
    });

    const { load, saveChanges, remove, loading, item, validationState, query } = factory();

    return {
        load,
        saveChanges,
        remove,
        loading,
        item,
        query,
        validationState
    };
}
```

To implement the `load`, `saveChanges` and `remove` methods, you need to use `useApiClient` composable from `@vc-shell/framework` package. This composable returns a `getApiClient` method, that provides you with an  instance of the API client class, which you can use to make requests to your API.

Let's look at an example of using the `useApiClient` method with `useDetailsFactory` in the `useDetails` composable:

```typescript
import { useApiClient } from "@vc-shell/framework";
import { SomeClient } from "@your-api-package";

const { getApiClient } = useApiClient(SomeClient);

const useDetails = (): UseDetails => {
    const factory = useDetailsFactory({
        load: async ({ id }) => {
            return (await getApiClient()).someSearchFn(id);
        },
        saveChanges: async (details) => {
            return details.id ? (await getApiClient()).someSaveFn(details) : (await getApiClient()).someCreateFn(details);
        },
        remove: async ({ id }) => {
            return (await getApiClient()).someRemoveFn(id);
        }
    });
}
```

!!!note
    As you can see, this callback methods has arguments.
    - The `load` method gets an `id`, that is passed to blade as a `param` prop.
    - The `saveChanges` method gets a `details` object, that contains the current details item.
    - The `remove` method gets an `id`, that is passed to blade as a `param` prop.


With the use of `useDetailsFactory`, you get a ready-to-use composable, which already has all the necessary methods and properties to work with the form. All you need to do is just to implement the `load`, `remove` and `saveChanges` methods. Also you can add your own logic, methods and properties to the composable, as in other composable functions.

Since the `useDetailsFactory` method is generic, you can provide your own types for your loaded `item`. Lets look at an example based on Offers module from `vc-app`:

```typescript
useDetailsFactory<IOffer>(
    // ...
)
```

`UseDetails` interface is also a generic type that accepts your `item` and `scope` types:

```typescript
UseDetails<IOffer, OfferDetailsScope>
```

!!! note
    More information about `scope` can be found in the [Blade Scope](#blade-scope) section.

This allows you to get proper typing of your composable and data.

#### Access to Blade Component Props and Events
All composables created for dynamic views have incoming parameters by default, which are passed from the dynamic views component:

1. `props` - the `props` object of the dynamic views component, which includes all blade parameters.
2. `emit` - the `emit` object of the dynamic views component, which includes all blade events that it can emit.
3. `mounted` - a reactive value that returns `true` if the dynamic views component has been mounted, otherwise `false`.

To obtain types, you also need to import `DynamicBladeForm`. It looks like this:

```typescript
import { Ref } from "vue";
import { DynamicBladeForm } from "@vc-shell/framework";

const useDetails = (args: {
    props: InstanceType<typeof DynamicBladeForm>["$props"];
    emit: InstanceType<typeof DynamicBladeForm>["$emit"];
    mounted: Ref<boolean>;
}) => {
    // your composable code here
}
```

Thanks to this, you always have access to all incoming blade parameters and can use events `emit` directly from your composable.

#### Blade Scope
Each composable created for dynamic views can have a special variable - `scope`, which can contain all additional methods, computed values, reactive variables, toolbar overrides that you want to use in your blade.

To use `scope`, you need to return it from your composable:

```typescript
const useDetails = (args: // ...): UseList => {
    const scope = ref<DetailsScope>({
        // your scope here
    });

    return {
        // ...,
        scope: computed(() => scope.value),
    }
}
```

Also, you need to create an interface, for example, `DetailsScope`, which should extend from the `DetailsBaseBladeScope` interface to provide type-check for the `scope` and should include all additional methods, computed values, reactive variables, toolbar overrides that you want to use in your blade:

```typescript
import { DetailsBaseBladeScope } from "@vc-shell/framework";

interface DetailsScope extends DetailsBaseBladeScope {
    // scope types here
}
```

#### `toolbarOverrides` object

When you define toolbar object in schema, you probably want to add some custom actions to it or change its visibility or disabled state. To do this, you can use `toolbarOverrides` object in your `scope`:

```typescript
const useDetails = (args: // ...): UseList => {
    const scope = ref<DetailsScope>({
        // ...
        toolbarOverrides: {
            // your toolbar overrides here
        },
    });
}
```

!!! note
    More information about toolbar creation can be found in the [Toolbar schema creation](./../toolbar.md#toolbar-schema-creation) section.

#### Default toolbar buttons

`DynamicBladeForm` has a built-in toolbar buttons, which you can use. All this toolbar button objects has methods, visibility and disabled state already implemented, so you just need to add in in your view schema. Also you can override this methods in `toolbarOverrides` object by its names.

This method names are: `saveChanges`, `remove`.

!!! note
    More information about toolbar overriding can be found in the [Overriding default toolbar methods and properties](./../toolbar.md#overriding-default-toolbar-methods-and-properties) section.

### `validationState` API
The `validationState` property is a computed property presented by the `IValidationState` interface:

```typescript
interface IValidationState<Item> {
  valid: boolean;
  dirty: boolean;
  disabled: boolean;
  modified: boolean;
  validated: boolean;
  cachedValue: Item | undefined;
  setFieldError: FormContext["setFieldError"];
  setErrors: FormContext["setErrors"];
  resetModified: (data: MaybeRef<Item>, updateInitial?: MaybeRef<boolean>) => void;
  validate: FormContext["validate"];
}
```

| Property | Type | Description |
| --- | --- | --- |
| `valid` | `boolean` | Indicates whether the form is valid. |
| `dirty` | `boolean` | Indicates whether the form is dirty. |
| `disabled` | `boolean` | Indicates whether the form is disabled. |
| `modified` | `boolean` | Indicates whether the form is modified. |
| `validated` | `boolean` | Indicates whether the form is validated. |
| `cachedValue` | `Item` | The cached value of the form. |
| `setFieldError` | `FormContext["setFieldError"]` | The Vee-Validate method used to set the field error. More info could be found in [Vee-Validate](https://vee-validate.logaretm.com/v4/api/form#default) docs. |
| `setErrors` | `FormContext["setErrors"]` | The Vee-Validate method used to set the errors.  More info could be found in [Vee-Validate](https://vee-validate.logaretm.com/v4/api/form#default) docs. |
| `resetModified` | `(data: MaybeRef<Item>, updateInitial?: MaybeRef<boolean>) => void` | The method used to reset the modified state and, if needed, override the initial `item` value. |
| `validate` | `FormContext["validate"]` | The Vee-Validate method used to validate the form.  More info could be found in [Vee-Validate](https://vee-validate.logaretm.com/v4/api/form#default) docs. |

## DynamicBladeForm Blade Context
`DynamicBladeForm` blade context is an object that contains all methods and properties, returned from composable and settings from view schema.

## DynamicBladeForm API
This view is implemented using the `DynamicDetailsSchema` interface, which includes `settings` and `content`:

```typescript
interface DynamicDetailsSchema {
    settings: SettingsDetails;
    content: [FormContentSchema, WidgetsSchema?];
}
```

| Property | Type | Description |
| --- | --- | --- |
| `settings` | `SettingsDetails` | The settings of the view.  |
| `content` | `[FormContentSchema, WidgetsSchema?]` | The content of the view. |

### SettingsDetails
`SettingsDetails` is an extension of `SettingsBase` with additional settings for `DynamicBladeForm`:

```typescript
interface SettingsDetails extends SettingsBase {
    component: "DynamicBladeForm";
    status?: {
        component: string;
    };
}
```

!!! note
    More information about `SettingsBase` can be found in the [Schema Settings API](./schema-settings.md) section.

`Status` option allows you to specify a custom component in the blade header. The component must be registered globally. More information about creating custom components can be found in the [Creating custom templates](./../custom-templates.md) documentation section.


### FormContentSchema
`FormContentSchema` is an interface that contains settings for the form:

```typescript
interface FormContentSchema {
  id: string;
  component: "vc-form";
  children: ControlSchema[];
}
```
Where `ControlSchema` is an interface that represents array of form controls. More information about each control can be found in the [controls](../controls.md) documentation section.

### WidgetsSchema
`WidgetsSchema` is an interface that contains settings for widgets:

```typescript
interface WidgetsSchema {
  id: "string";
  component: "vc-widgets";
  children: string[];
}
```

`children` property is an array of widget component names. Widget components must be registered globally. More information about creating widgets can be found in the [Creating widgets](./../widgets.md) documentation section.
