# Select
Select is used to choose an item from a collection of options.
Supports connecting a method for loading options directly from the server with automatic loading of items when scrolling.

## Usage

![vc-select](./../../../../media/controls/molecules/vc-select/vc-select.png)

=== "Basic Vue"

    ```html
    <template>
        <vc-select
            label="Country"
            :property="selectProperty"
            :placeholder="Select placeholder"
            :options="fetchMethod"
            optionValue="value"
            optionLabel="label"
        ></vc-select>
    </template>
    ```

=== "Dynamic Views"

    To start using all the available select properties, specify the `vc-select` component when creating the schema.

    Base usage looks like this:

    ```typescript
    {
        id: "selectId",
        component: "vc-select",
        label: "Country",
        property: "selectProperty",
        placeholder: "Select placeholder",
        optionsMethod: "fetchMethod",
        optionValue: "value",
        optionLabel: "label",
    }
    ```

    where `optionProperty` is object array containing select options, `optionValue` is the name of the property that contains the value of the option, `optionLabel` is the name of the property that contains the label of the option.

## Select API

## Basic Vue

### Props

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of select |
| `modelValue` | `any` | Model of the component; Must be Array if using 'multiple' prop; Use this property with a listener for 'update:modelValue' event OR use v-model directive |
| `mapOptions` | `boolean` | Try to map labels of model from 'options' Array; If you are using emit-value you will probably need to use map-options to display the label text in the select field rather than the value; Default value: true |
| `error` | `boolean` | Does field have validation errors? |
| `errorMessage` | `string` | Validation error message (gets displayed only if 'error' is set to 'true') |
| `label` | `string` | Select label |
| `hint` | `string` | Select description (hint) text below input component |
| `prefix` | `string` | Prefix |
| `suffix` | `string` | Suffix |
| `loading` | `boolean` | Signals the user a process is in progress by displaying a spinner |
| `clearable` | `boolean` | Appends clearable icon when a value is set; When clicked, model becomes null |
| `disabled` | `boolean` | Put component in disabled mode |
| `multiple` | `boolean` | Allow multiple selection; Model must be Array |
| `options` | `((keyword?: string, skip?: number, ids?: string[]) => Promise<P>) \| T[]` | Available options that the user can select from. Default value: [] |
| `optionValue` | `OptionProp<Option>` | Property of option which holds the 'value' Default value: id |
| `optionLabel` | `OptionProp<Option>` | Property of option which holds the 'label' Default value: title |
| `emitValue` | `boolean` | Update model with the value of the selected option instead of the whole option |
| `debounce` | `number \| string` | Debounce the search input update with an amount of milliseconds Default value: 500 |
| `placeholder` | `string` | Input placeholder text |
| `tooltip` | `string` | Input tooltip information |
| `required` | `boolean` | Input required state |
| `searchable` | `boolean` | Input search activation |
| `multilanguage` | `boolean` | Multilanguage support |
| `currentLanguage` | `string` | Current language |

### Slots

| Name           | Parameters                                  | Description                                                                                     |
| -------------- | ------------------------------------------- |----------------------------------------------------------------------------------------------- |
| `control`        | scope: { toggleHandler: () => void }               | Custom select control                                                                           |
| `prepend-inner`  | void                                        | Prepend inner field                                                                             |
| `append-inner`   | void                                        | Append to inner field                                                                           |
| `prepend`        | void                                        | Prepend outer field                                                                             |
| `append`         | void                                        | Append outer field                                                                              |
| `no-option`      | void                                        | What should the menu display after filtering options and none are left to be displayed         |
| `error`          | void                                        | Slot for errors                                                                                 |
| `hint`           | void                                        | Slot for hint text                                                                              |
| `selected-item`  | scope: { index: number; opt: Option; selected: boolean; removeAtIndex: (index: number) => void }        | Override default selection slot                                                                 |
| `option`         | scope: { index: number; opt: Option; selected: boolean; toggleOption: (opt: any) => void }        | Override default selection slot                                                                 |
| `no-options`     | void                                       | Slot for when there are no options available                                                    |

### Emits

| Event | Parameters | Description |
| --- | --- | --- |
| `update:modelValue` | `inputValue: MaybeArray<string \| Option> \| null` | Emitted when the component needs to change the model; Is also used by v-model |
| `search` | `inputValue: string` | Emitted when user wants to filter a value |
| `close` | - | Emitted when the select options list is hidden |


## Dynamic Views

Schema interface for select looks like this:

```typescript
interface SelectSchema {
    id: string;
    component: "vc-select";
    label?: string;
    property: string;
    rules?: IValidationRules;
    placeholder?: string;
    tooltip?: string;
    optionsMethod: string;
    optionValue?: string;
    optionLabel?: string;
    searchable?: boolean;
    clearable?: boolean;
    emitValue?: boolean;
    customTemplate?: {
        component: string;
    };
    disabled?: {
        method: string;
    };
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
| `id` | `string` | Unique identifier for the `vc-select` component. |
| `component` | `vc-select` | Component used in schema. |
| `label` | `string` | Label for the select. Also available interpolation `{}` syntax based on current element context. |
| `property` | `string` | Property name that is used for binding select value to blade data.  <br> Supports deep nested properties like `property[1].myProperty`. <br> Additionally, you have the flexibility to bind any function or computed property that returns a value and retrieve changed value as an argument for the function.|
| `rules` | `IValidationRules` | Validation rules for the select. Uses [VeeValidate](https://vee-validate.logaretm.com/v4/) validation rules. |
| `placeholder` | `string` | Placeholder text for the select.  |
| `tooltip` | `string` | Tooltip text for the select label. |
| `optionsMethod` | `string` | Method to call to get select options. Method should be defined in the blade `scope`. |
| `optionValue` | `string` | Property that holds the value of the option. Default: `id` |
| `optionLabel` | `string` | Property that holds the label of the option. Default: `title` |
| `searchable` | `boolean` | Whether the select is searchable. |
| `clearable` | `boolean` | Whether the select has a clear button. |
| `emitValue` | `boolean` | Update model with the value of the selected option instead of the whole option. If true - emits only selected value, if false - emits whole selected object. |
| `customTemplate` | `{component: string}` | Custom template for select options. Component should be registered globally. |
| `disabled` | `{method: string}` | Disabled state for component, could be used to disable select based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `visibility` | `{method: string}` | Visibility state for component, could be used to hide select based on some conditions. Method or variable should be defined in the blade `scope` and should return a boolean value. |
| `update` | `{method: string}` | Method to call when the select value is updated. Method should be defined in the blade `scope`. |
