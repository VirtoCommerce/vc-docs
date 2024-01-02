# Dynamic Property
Allows to display a dynamic properties controls set.

## Usage

=== "Basic Vue"

    ```html
    <template>
        <vc-dynamic-property
            v-for="item in properties"
            :property="item"
        ></vc-dynamic-property>
    </template>
    ```

=== "Dynamic Views"

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

## Dynamic Properties API

### Props

| Property         | Type                                                         | Description                                                                                                      |
| ---------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `property`       | `T`                                                          | The property type.                                                                                               |
| `modelValue`     | `any`                                                        | The value of the model.                                                                                          |
| `optionsGetter`  | `(property: T, keyword?: string, locale?: string) => Promise<any[]> \| any[]` | A function that retrieves the options for the property.                                                          |
| `required`       | `boolean`                                                    | Indicates if the property is required.                                                                            |
| `multivalue`     | `boolean` \| `undefined`                                     | Indicates if the property supports multiple values.                                                               |
| `multilanguage`  | `boolean` \| `undefined`                                     | Indicates if the property supports multiple languages.                                                           |
| `currentLanguage`| `string` \| `undefined`                                      | The current language for the property.                                                                            |
| `valueType`      | `string`                                                     | The type of the property value.                                                                                  |
| `dictionary`     | `boolean` \| `undefined`                                     | Indicates if the property is a dictionary.                                                                        |
| `name`           | `string`                                                     | The name of the property.                                                                                        |
| `optionsValue`   | `string` \| `undefined`                                      | The property value to use as the option value.                                                                    |
| `optionsLabel`   | `string` \| `undefined`                                      | The property value to use as the option label.                                                                    |
| `displayNames`   | `{ name?: string; languageCode?: string; }[]`                 | An array of display names for the property. Each display name can have a name and a language code.              |
| `rules`          | `{ min?: number; max?: number; regex?: string; }`             | Validation rules for the property.                                                                                |
| `disabled`       | `boolean` \| `undefined`                                     | Indicates if the property is disabled.                                                                            |
| `placeholder`    | `string` \| `undefined`                                      | The placeholder text for the property.                                                                            |


### Emits

| Event | Parameters | Description |
| --- | --- | --- |
| `update:modelValue` | data: { readonly property: T; readonly value: any; readonly dictionary?: any[]; readonly locale?: string } | Emitted when the value of the model changes. |



## Dynamic Views

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
| `property` | `string` | Property name that is used for binding dynamic properties value to blade data.  <br> Supports deep nested properties like `property[1].myProperty`. <br> Additionally, you have the flexibility to bind any function or computed property that returns a value and retrieve changed value as an argument for the function.|
| `exclude` | `string[]` | An array of property names to exclude from the dynamic properties schema. |
| `include` | `string[]` | An array of property names to include in the dynamic properties schema. |
| `disabled` | `{method: string}` | Disabled state for component, could be used to disable dynamic properties based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide dynamic properties based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |

