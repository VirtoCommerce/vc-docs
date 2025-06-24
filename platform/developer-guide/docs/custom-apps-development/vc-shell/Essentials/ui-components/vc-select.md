# VcSelect Component

The `VcSelect` component is a molecule used throughout the VC-Shell framework for creating customizable dropdown selection fields. It supports single and multiple selections, searchable options, custom styling, and async data loading.

## Storybook

[VcSelect Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vcselect--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vcselect--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcSelect
    v-model="selectedValue"
    :options="options"
    label="Select an option"
    placeholder="Choose from the list"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcSelect } from '@vc-shell/framework';

const selectedValue = ref(null);
const options = [
  { id: 1, title: 'Option 1' },
  { id: 2, title: 'Option 2' },
  { id: 3, title: 'Option 3' }
];
</script>
```

## Props

| Prop            | Type                           | Default     | Description                                           |
| --------------- | ------------------------------ | ----------- | ----------------------------------------------------- |
| `modelValue`    | `any`                          | `undefined` | Value of the select (v-model)                         |
| `options`       | `Array<any> \| Function`       | `[]`        | Options array or async function returning options     |
| `optionValue`   | `string \| Function`           | `'id'`      | Property name or function to get option value         |
| `optionLabel`   | `string \| Function`           | `'title'`   | Property name or function to get option label         |
| `label`         | `string`                       | `undefined` | Label displayed above the select                      |
| `placeholder`   | `string`                       | `undefined` | Placeholder text when no value is selected            |
| `debounce`      | `number`                       | `300`       | Debounce time for search input (in milliseconds)      |
| `clearable`     | `boolean`                      | `false`     | Whether the value can be cleared                      |
| `emitValue`     | `boolean`                      | `true`      | Emit only the value instead of the entire option      |
| `searchable`    | `boolean`                      | `false`     | Enable searching/filtering options                    |
| `multiple`      | `boolean`                      | `false`     | Allow selecting multiple values                       |
| `disabled`      | `boolean`                      | `false`     | Disable the select component                          |
| `required`      | `boolean`                      | `false`     | Mark the select as required (shows asterisk)          |
| `error`         | `boolean`                      | `false`     | Show the select in error state                        |
| `errorMessage`  | `string`                       | `undefined` | Error message to display below the select             |
| `hint`          | `string`                       | `undefined` | Hint text to display below the select                 |
| `tooltip`       | `string`                       | `undefined` | Tooltip text to display next to the label             |
| `prefix`        | `string`                       | `undefined` | Prefix text inside the select field                   |
| `suffix`        | `string`                       | `undefined` | Suffix text inside the select field                   |
| `size`          | `'default' \| 'small'`         | `'default'` | Size of the select field                              |
| `mapOptions`    | `boolean`                      | `true`      | Map labels of model from options array                |
| `loading`       | `boolean`                      | `false`     | Show loading state                                    |
| `outline`       | `boolean`                      | `true`      | Whether to show an outline around the select          |
| `multilanguage` | `boolean`                      | `false`     | Whether the label should show multilanguage icon      |
| `currentLanguage` | `string`                     | `undefined` | Current language code for multilanguage support       |

## Events

| Event               | Payload                        | Description                                           |
| ------------------- | ------------------------------ | ----------------------------------------------------- |
| `update:modelValue` | `any`                         | Emitted when the selected value changes               |
| `click`             | -                              | Emitted when the select is clicked                    |
| `clear`             | -                              | Emitted when the select value is cleared              |
| `search`            | `string`                       | Emitted when the search term changes (if searchable)  |

## Slots

| Slot            | Props                          | Description                                           |
| --------------- | ------------------------------ | ----------------------------------------------------- |
| `control`       | `{ toggleHandler: () => void }` | Custom control element                               |
| `prepend`       | -                              | Content to prepend outside the select field           |
| `prepend-inner` | -                              | Content to prepend inside the select field            |
| `append`        | -                              | Content to append outside the select field            |
| `append-inner`  | -                              | Content to append inside the select field             |
| `option`        | `{ option, index, selected }`  | Custom option rendering in dropdown                   |
| `selected-item` | `{ opt, index }`               | Custom rendering for selected item(s)                 |
| `error`         | -                              | Custom error message rendering                        |
| `hint`          | -                              | Custom hint rendering                                 |
| `no-options`    | -                              | Content shown when no options are available           |

## CSS Variables

The select component uses CSS variables for theming, which can be customized:

```css
:root {
  /* Basic appearance */
  --select-height: 36px;                           /* Default height of select field */
  --select-height-small: 28px;                     /* Height of select field when size="small" */
  --select-border-radius: 4px;                     /* Border radius of the select field */
  --select-border-color: var(--neutrals-300);      /* Border color in normal state */
  --select-text-color: var(--neutrals-800);        /* Text color of selected value */
  --select-padding: 10px;                          /* Horizontal padding inside the select field */
  --select-background-color: var(--additional-50); /* Background color of the select field */
  
  /* Placeholder and icons */
  --select-placeholder-color: var(--neutrals-400); /* Color of placeholder text */
  --select-chevron-color: var(--primary-500);      /* Color of dropdown chevron icon */
  --select-chevron-color-hover: var(--primary-600); /* Color of dropdown chevron icon on hover */
  --select-clear-color: var(--primary-500);        /* Color of clear button */
  --select-clear-color-hover: var(--primary-600);  /* Color of clear button on hover */
  --select-loading-color: var(--info-500);         /* Color of loading spinner */
  
  /* Dropdown and options */
  --select-option-background-color-hover: var(--accent-100);   /* Background of option on hover */
  --select-option-background-color-selected: var(--accent-200); /* Background of selected option */
  --select-multiple-options-background-color: var(--additional-50); /* Background of multiple selected tags */
  --select-multiple-options-border-color: var(--secondary-200); /* Border color of multiple selected tags */
  --select-border-color-input: var(--secondary-200); /* Border color of search input in dropdown */
  --select-search-background-color: var(--additional-50); /* Background color of search field */
  
  /* Focus state */
  --select-border-color-focus: var(--primary-100); /* Border color when select is focused */
  
  /* Disabled state */
  --select-background-color-disabled: var(--neutrals-200); /* Background color when disabled */
  --select-disabled-text-color: var(--neutrals-500);       /* Text color when disabled */
  
  /* Error state */
  --select-border-color-error: var(--danger-500);  /* Border color when in error state */
}
```

## Examples

### Basic Select with Objects

```vue
<template>
  <VcSelect
    v-model="selectedUser"
    :options="users"
    optionValue="id"
    optionLabel="name"
    label="Select User"
    placeholder="Choose a user"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcSelect } from '@vc-shell/framework';

const selectedUser = ref(null);
const users = [
  { id: 1, name: 'John Doe' },
  { id: 2, name: 'Jane Smith' },
  { id: 3, name: 'Robert Johnson' }
];
</script>
```

### Multiple Select

```vue
<template>
  <VcSelect
    v-model="selectedTags"
    :options="tags"
    label="Select Tags"
    placeholder="Choose tags"
    :multiple="true"
    :clearable="true"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcSelect } from '@vc-shell/framework';

const selectedTags = ref([]);
const tags = [
  'JavaScript', 'TypeScript', 'Vue', 'React', 'Angular', 'Node.js'
];
</script>
```

### Searchable Select

```vue
<template>
  <VcSelect
    v-model="selectedProduct"
    :options="products"
    label="Select Product"
    placeholder="Search products"
    :searchable="true"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcSelect } from '@vc-shell/framework';

const selectedProduct = ref(null);
const products = [
  { id: 1, title: 'Laptop' },
  { id: 2, title: 'Smartphone' },
  { id: 3, title: 'Tablet' },
  { id: 4, title: 'Smartwatch' },
  { id: 5, title: 'Headphones' }
];
</script>
```

### Async Options Loading

```vue
<template>
  <VcSelect
    v-model="selectedUser"
    :options="fetchUsers"
    label="Select User"
    placeholder="Search users"
    :searchable="true"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcSelect } from '@vc-shell/framework';

const selectedUser = ref(null);

const fetchUsers = async (keyword = "", skip = 0) => {
  // Simulate API call
  await new Promise(resolve => setTimeout(resolve, 500));
  
  const allUsers = [
    { id: 1, name: 'John Doe' },
    { id: 2, name: 'Jane Smith' },
    { id: 3, name: 'Robert Johnson' },
    { id: 4, name: 'Emily Davis' },
    { id: 5, name: 'Michael Brown' }
  ];
  
  // Filter users based on keyword
  const filteredUsers = keyword 
    ? allUsers.filter(user => user.name.toLowerCase().includes(keyword.toLowerCase()))
    : allUsers;
  
  // Return paginated results
  return {
    results: filteredUsers.slice(skip, skip + 10),
    total: filteredUsers.length
  };
};
</script>
```

### Custom Value and Label Functions

```vue
<template>
  <VcSelect
    v-model="selectedCountry"
    :options="countries"
    :option-value="getOptionValue"
    :option-label="getOptionLabel"
    label="Select Country"
    placeholder="Choose a country"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcSelect } from '@vc-shell/framework';

const selectedCountry = ref(null);
const countries = [
  { code: 'US', name: 'United States' },
  { code: 'CA', name: 'Canada' },
  { code: 'UK', name: 'United Kingdom' },
  { code: 'AU', name: 'Australia' },
  { code: 'JP', name: 'Japan' }
];

const getOptionValue = (option) => option.code;
const getOptionLabel = (option) => `${option.name} (${option.code})`;
</script>
```

### Custom Option Rendering

```vue
<template>
  <VcSelect
    v-model="selectedStatus"
    :options="statuses"
    label="Select Status"
    placeholder="Choose a status"
  >
    <template #option="{ option, selected }">
      <div class="tw-flex tw-items-center tw-gap-2">
        <span 
          class="tw-w-3 tw-h-3 tw-rounded-full" 
          :style="{ backgroundColor: getStatusColor(option.color) }"
        ></span>
        <span>{{ option.label }}</span>
        <VcIcon 
          v-if="selected" 
          icon="material-check" 
          class="tw-ml-auto tw-text-[color:var(--primary-500)]" 
          size="s"
        />
      </div>
    </template>
  </VcSelect>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcSelect, VcIcon } from '@vc-shell/framework';

const selectedStatus = ref(null);
const statuses = [
  { id: 'active', label: 'Active', color: 'green' },
  { id: 'pending', label: 'Pending', color: 'orange' },
  { id: 'inactive', label: 'Inactive', color: 'gray' },
  { id: 'error', label: 'Error', color: 'red' }
];

const getStatusColor = (color) => {
  const colors = {
    green: 'var(--success-500)',
    orange: 'var(--warning-500)',
    gray: 'var(--neutrals-400)',
    red: 'var(--error-500)'
  };
  return colors[color] || 'var(--neutrals-500)';
};
</script>
```

### With Validation

```vue
<template>
  <form @submit.prevent="submitForm">
    <VcSelect
      v-model="selectedCategory"
      :options="categories"
      label="Product Category"
      placeholder="Select a category"
      :error="errors.category"
      :error-message="errorMessages.category"
      required
    />
    
    <VcButton 
      type="submit" 
      class="tw-mt-4"
    >
      Submit
    </VcButton>
  </form>
</template>

<script lang="ts" setup>
import { ref, reactive } from 'vue';
import { VcSelect, VcButton } from '@vc-shell/framework';

const selectedCategory = ref(null);
const categories = [
  { id: 1, title: 'Electronics' },
  { id: 2, title: 'Clothing' },
  { id: 3, title: 'Home & Garden' },
  { id: 4, title: 'Books' },
  { id: 5, title: 'Sports' }
];

const errors = reactive({
  category: false
});

const errorMessages = reactive({
  category: ''
});

function submitForm() {
  // Reset errors
  errors.category = false;
  errorMessages.category = '';
  
  // Validate
  if (!selectedCategory.value) {
    errors.category = true;
    errorMessages.category = 'Please select a category';
    return;
  }
  
  // Form submission logic
  console.log('Form submitted with category:', selectedCategory.value);
}
</script>
```

### With Custom Control

```vue
<template>
  <VcSelect
    v-model="selectedOption"
    :options="options"
    label="Custom Control Select"
  >
    <template #control="{ toggleHandler }">
      <VcButton 
        variant="outlined" 
        class="tw-w-full"
        @click="toggleHandler"
      >
        <template #prepend>
          <VcIcon icon="material-list" />
        </template>
        {{ selectedOption ? getSelectedLabel() : 'Click to select' }}
      </VcButton>
    </template>
  </VcSelect>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue';
import { VcSelect, VcButton, VcIcon } from '@vc-shell/framework';

const selectedOption = ref(null);
const options = [
  { id: 1, title: 'Option 1' },
  { id: 2, title: 'Option 2' },
  { id: 3, title: 'Option 3' }
];

function getSelectedLabel() {
  const selected = options.find(opt => opt.id === selectedOption.value);
  return selected ? selected.title : '';
}
</script>
```
