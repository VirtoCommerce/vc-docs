# VcInputDropdown Component

The `VcInputDropdown` component is a versatile input component that combines an input field with a dropdown selection. It's ideal for scenarios where users need to both input a value and select a category, unit, or format for that value.

## Storybook

[VcInputDropdown Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vcinputdropdown--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vcinputdropdown--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcInputDropdown
    v-model="inputValue"
    v-model:option="selectedOption"
    :options="options"
    label="Input with Dropdown"
    placeholder="Enter value"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInputDropdown } from '@vc-shell/framework';

const inputValue = ref('100');
const selectedOption = ref('Option 1');
const options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5'];
</script>
```

## Props

| Prop              | Type                                      | Default     | Description                                            |
| ----------------- | ----------------------------------------- | ----------- | ------------------------------------------------------ |
| `modelValue`      | `string \| number \| Date \| null \| undefined` | -          | The value of the input field (v-model binding)         |
| `option`          | `unknown`                                 | -          | Default selected dropdown option (v-model:option binding)   |
| `options`         | `unknown[]`                               | `[]`       | Array of options to display in the dropdown             |
| `optionValue`     | `string \| ((option: unknown) => string)` | `'id'`     | Property or function to extract option value            |
| `optionLabel`     | `string \| ((option: unknown) => string)` | `'title'`  | Property or function to extract option label            |
| `label`           | `string`                                  | -          | Label text for the input                                |
| `placeholder`     | `string`                                  | -          | Placeholder text when no input is entered               |
| `hint`            | `string`                                  | -          | Hint text to display below the input                    |
| `clearable`       | `boolean`                                 | `false`    | Whether the input field can be cleared                  |
| `prefix`          | `string`                                  | -          | Text to display before the input value                  |
| `suffix`          | `string`                                  | -          | Text to display after the input value                   |
| `name`            | `string`                                  | `'Field'`  | HTML name attribute for the input field                 |
| `loading`         | `boolean`                                 | `false`    | Shows a loading indicator                               |
| `debounce`        | `string \| number`                        | `0`        | Debounce time in milliseconds for input changes         |
| `disabled`        | `boolean`                                 | `false`    | Disables the component                                  |
| `autofocus`       | `boolean`                                 | `false`    | Focuses the input field on component mount              |
| `error`           | `boolean`                                 | `false`    | Shows the component in error state                      |
| `errorMessage`    | `string`                                  | -          | Error message to display when in error state            |
| `maxlength`       | `string \| number`                        | -          | Maximum character length for the input field            |
| `tooltip`         | `string`                                  | -          | Tooltip text to show on hover                           |
| `required`        | `boolean`                                 | `false`    | Marks the component as required (shows asterisk)        |
| `searchable`      | `boolean`                                 | `false`    | Enables search functionality in the dropdown            |
| `inputType`       | `string`                                  | `'text'`   | Type of the input field (text, number, email, etc.)     |

## Events

| Event                | Parameters                           | Description                                            |
| -------------------- | ------------------------------------ | ------------------------------------------------------ |
| `update:modelValue`  | `(value: string \| number \| Date \| null \| undefined) => void` | Emitted when the input value changes                   |
| `update:option`      | `(value: unknown) => void`           | Emitted when the selected option changes                |
| `change`             | `(value: unknown) => void`           | Emitted when input value changes                        |
| `blur`               | `(event: Event) => void`             | Emitted when the input loses focus                      |

## Slots

| Slot             | Props                               | Description                                            |
| ---------------- | ----------------------------------- | ------------------------------------------------------ |
| `button`         | `{ toggleHandler: () => void }`     | Custom dropdown toggle button                           |
| `control`        | `{ placeholder, focused, modelValue, emitValue }` | Custom input control                      |
| `append-inner`   | -                                   | Content to append inside the input field                |
| `prepend-inner`  | -                                   | Content to prepend inside the input field               |
| `append`         | -                                   | Content to append outside the input field               |
| `prepend`        | -                                   | Content to prepend outside the input field              |

## CSS Variables

The component uses the following CSS variables for styling:

```css
:root {
  --input-dropdown-toggle-color: var(--primary-500);  /* Color of the dropdown toggle button */
}
```

## Examples

### Basic Dropdown

```vue
<template>
  <VcInputDropdown
    v-model="inputValue"
    v-model:option="selectedUnit"
    :options="unitOptions"
    label="Measurement"
    placeholder="Enter value"
    inputType="number"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInputDropdown } from '@vc-shell/framework';

const inputValue = ref(100);
const selectedUnit = ref('cm');
const unitOptions = ['mm', 'cm', 'm', 'km'];
</script>
```

### With Object Options

```vue
<template>
  <VcInputDropdown
    v-model="price"
    v-model:option="selectedCurrency"
    :options="currencies"
    :option-value="currency => currency.code"
    :option-label="currency => currency.name"
    label="Price"
    placeholder="Enter price"
    inputType="number"
    hint="Enter the price in the selected currency"
    searchable
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInputDropdown } from '@vc-shell/framework';

const price = ref(1000);
const selectedCurrency = ref({ code: 'USD', symbol: '$', name: 'US Dollar' });
const currencies = [
  { code: 'USD', symbol: '$', name: 'US Dollar' },
  { code: 'EUR', symbol: '€', name: 'Euro' },
  { code: 'GBP', symbol: '£', name: 'British Pound' },
  { code: 'JPY', symbol: '¥', name: 'Japanese Yen' },
];
</script>
```

### Custom Dropdown Button

```vue
<template>
  <VcInputDropdown
    v-model="inputValue"
    v-model:option="selectedFormat"
    :options="formatOptions"
    :option-value="opt => opt.id"
    :option-label="opt => opt.label"
    label="Date"
    placeholder="Enter date"
  >
    <template #button="{ toggleHandler }">
      <button
        class="tw-flex tw-items-center tw-px-2 tw-text-primary-500 tw-font-medium"
        @click.stop.prevent="toggleHandler"
      >
        <span>{{ selectedFormat.label }}</span>
        <VcIcon icon="material-keyboard_arrow_down" size="s" class="tw-ml-1" />
      </button>
    </template>
  </VcInputDropdown>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInputDropdown, VcIcon } from '@vc-shell/framework';

const inputValue = ref('31/12/2023');
const selectedFormat = ref({ id: 'DD/MM/YYYY', label: 'Day/Month/Year' });
const formatOptions = [
  { id: 'DD/MM/YYYY', label: 'Day/Month/Year' },
  { id: 'MM/DD/YYYY', label: 'Month/Day/Year' },
  { id: 'YYYY-MM-DD', label: 'ISO Format' },
];
</script>
```

### Custom Input Control

```vue
<template>
  <VcInputDropdown
    v-model="date"
    v-model:option="selectedFormat"
    :options="formatOptions"
    :option-value="opt => opt.id"
    :option-label="opt => opt.label"
    label="Date"
    placeholder="Select date"
  >
    <template #control="{ placeholder }">
      <div class="tw-flex tw-items-center tw-relative tw-w-full">
        <VcButton size="xs" variety="secondary" @click="setToday">Today</VcButton>
        <VcIcon icon="material-calendar_today" class="tw-text-gray-500" size="s" />
        <input
          v-model="date"
          :placeholder="placeholder"
          class="tw-w-full tw-p-2 tw-pl-8 tw-border tw-border-solid tw-border-gray-300 tw-rounded tw-text-sm tw-outline-none"
          @blur="formatDate"
        />
      </div>
    </template>
  </VcInputDropdown>
</template>

<script lang="ts" setup>
import { ref, watch } from 'vue';
import { VcInputDropdown, VcIcon, VcButton } from '@vc-shell/framework';

const date = ref('');
const selectedFormat = ref({ id: 'DD/MM/YYYY', label: 'Day/Month/Year' });
const formatOptions = [
  { id: 'DD/MM/YYYY', label: 'Day/Month/Year' },
  { id: 'MM/DD/YYYY', label: 'Month/Day/Year' },
  { id: 'YYYY-MM-DD', label: 'ISO Format' },
];

const formatDate = () => {
  if (!date.value) return;
  
  const today = new Date();
  const day = String(today.getDate()).padStart(2, '0');
  const month = String(today.getMonth() + 1).padStart(2, '0');
  const year = today.getFullYear();
  
  switch (selectedFormat.value.id) {
    case 'DD/MM/YYYY':
      date.value = `${day}/${month}/${year}`;
      break;
    case 'MM/DD/YYYY':
      date.value = `${month}/${day}/${year}`;
      break;
    case 'YYYY-MM-DD':
      date.value = `${year}-${month}-${day}`;
      break;
  }
};

// Format date when format changes
watch(() => selectedFormat.value, formatDate);

const setToday = () => {
  formatDate();
};
</script>
```
