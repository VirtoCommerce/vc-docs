# VcMultivalue Component

The `VcMultivalue` component is a versatile input that allows users to select or enter multiple values. It supports both dropdown selection from predefined options and manual text entry, making it perfect for tags, multi-select, and other use cases that require collecting multiple values.

## Storybook

[VcMultivalue Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vcmultivalue--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vcmultivalue--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcMultivalue
    v-model="selectedValues"
    label="Categories"
    placeholder="Select categories"
    :options="options"
    option-value="id"
    option-label="title"
    multivalue
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcMultivalue } from '@vc-shell/framework';

const selectedValues = ref([]);
const options = [
  { id: '1', title: 'Electronics' },
  { id: '2', title: 'Clothing' },
  { id: '3', title: 'Home & Garden' },
  { id: '4', title: 'Books' },
  { id: '5', title: 'Toys' }
];
</script>
```

## Props

| Prop             | Type                           | Default     | Description                                     |
| ---------------- | ------------------------------ | ----------- | ----------------------------------------------- |
| `modelValue`     | `any[]`                        | `[]`        | Array of selected values                        |
| `placeholder`    | `string`                       | `undefined` | Placeholder text for the input field            |
| `type`           | `'text'` \| `'number'` \| `'integer'` | `'text'`  | Input type for manual entry                |
| `label`          | `string`                       | `undefined` | Label text for the field                        |
| `tooltip`        | `string`                       | `undefined` | Tooltip text for additional information         |
| `name`           | `string`                       | `'Field'`   | Name attribute for the field                    |
| `hint`           | `string`                       | `undefined` | Helper text displayed below the field           |
| `options`        | `any[]`                        | `[]`        | Available options for selection                 |
| `optionValue`    | `string`                       | `'id'`      | Property name to use as the option value        |
| `optionLabel`    | `string`                       | `'title'`   | Property name to use as the option label        |
| `multivalue`     | `boolean`                      | `false`     | Enables multiple value selection mode           |
| `error`          | `boolean`                      | `false`     | Indicates an error state                        |
| `errorMessage`   | `string`                       | `undefined` | Error message to display                        |
| `required`       | `boolean`                      | `false`     | Makes the field required                        |
| `disabled`       | `boolean`                      | `false`     | Disables the field                              |
| `loading`        | `boolean`                      | `false`     | Shows a loading indicator                       |
| `multilanguage`  | `boolean`                      | `false`     | Enable multilanguage support for the label      |
| `currentLanguage`| `string`                       | `undefined` | Current language code for multilanguage support |

## Events

| Event                | Payload        | Description                                     |
| -------------------- | -------------- | ----------------------------------------------- |
| `update:model-value` | `any[]`        | Emitted when selected values change             |
| `close`              | -              | Emitted when the dropdown is closed             |
| `search`             | `string`       | Emitted when searching in the dropdown          |

## Slots

| Slot               | Props                               | Description                               |
| ------------------ | ----------------------------------- | ----------------------------------------- |
| `option`           | `{ item }`                          | Custom template for dropdown options      |
| `selected-item`    | `{ value, item, remove }`          | Custom template for selected values       |
| `error`            | -                                   | Custom error message content              |
| `hint`             | -                                   | Custom hint content                       |

## CSS Variables

```css
:root {
  /* Base styles */
  --multivalue-height: 36px;                            /* Height of the multivalue field */
  --multivalue-border-radius: 4px;                      /* Border radius of the input field */
  --multivalue-border-color: var(--neutrals-300);       /* Border color in normal state */
  --multivalue-border-color-error: var(--danger-100);   /* Border color in error state */
  --multivalue-background-color: var(--additional-50);  /* Background color of the multivalue field */
  --multivalue-placeholder-color: var(--neutrals-400);  /* Color of placeholder text */
  --multivalue-text-color: var(--neutrals-800);         /* Color of input text */
  --multivalue-padding: 10px;                           /* Internal padding of the field */
  
  /* Dropdown & Select styles */
  --multivalue-select-border-radius: 4px;                /* Border radius of dropdown */
  --multivalue-select-border-color: var(--neutrals-200); /* Border color of dropdown */
  --multivalue-select-border-color-error: var(--danger-500); /* Border color of dropdown in error state */
  --multivalue-select-background-color: var(--additional-50); /* Background color of dropdown */
  --multivalue-select-placeholder-color: var(--neutrals-400); /* Color of placeholder text in dropdown */
  --multivalue-select-chevron-color: var(--primary-500);      /* Color of dropdown arrow icon */
  --multivalue-select-chevron-color-hover: var(--primary-600); /* Color of dropdown arrow icon on hover */
  
  /* Item styles */
  --multivalue-search-border-color: var(--secondary-200);      /* Border color of search field in dropdown */
  --multivalue-item-hover-background-color: var(--accent-100); /* Background color of dropdown item on hover */
  --multivalue-hint-color: var(--danger-500);                  /* Color of hint/error text */
  --multivalue-field-value-background-color: var(--additional-50); /* Background color of selected value tags */
  --multivalue-field-value-border-color: var(--secondary-200);     /* Border color of selected value tags */
  --multivalue-clear-icon-color: var(--primary-500);          /* Color of clear icon in selected value tags */
  
  /* Disabled state */
  --multivalue-select-background-color-disabled: var(--neutrals-50); /* Background color when disabled */
  --multivalue-disabled-text-color: var(--neutrals-500);             /* Text color when disabled */
  --multivalue-disabled-background-color: var(--neutrals-200);       /* Background color when disabled */
}
```

## Examples

### Basic Multiple Selection

```vue
<template>
  <VcMultivalue
    v-model="selectedValues"
    label="Categories"
    placeholder="Select categories"
    :options="categories"
    option-value="id"
    option-label="name"
    multivalue
  />
  
  <div class="tw-mt-4">
    <p>Selected categories: {{ selectedValues.length }}</p>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcMultivalue } from '@vc-shell/framework';

const selectedValues = ref([]);
const categories = [
  { id: '1', name: 'Electronics' },
  { id: '2', name: 'Clothing' },
  { id: '3', name: 'Home & Garden' },
  { id: '4', name: 'Books' },
  { id: '5', name: 'Toys' }
];
</script>
```

### Manual Text Entry Mode

```vue
<template>
  <VcMultivalue
    v-model="tags"
    label="Tags"
    placeholder="Add tags (press Enter after each tag)"
    hint="Enter keywords that describe your product"
    :multivalue="false"
  />
  
  <div class="tw-mt-4 tw-flex tw-flex-wrap tw-gap-1">
    <div 
      v-for="(tag, index) in tags" 
      :key="index"
      class="tw-px-2 tw-py-1 tw-bg-[var(--primary-100)] tw-text-[var(--primary-800)] tw-rounded"
    >
      {{ tag }}
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcMultivalue } from '@vc-shell/framework';

const tags = ref([]);
</script>
```

### With Validation

```vue
<template>
  <VcForm @submit.prevent="validateForm">
    <VcMultivalue
      v-model="selectedItems"
      label="Required Field"
      placeholder="Select at least one item"
      :options="items"
      option-value="id"
      option-label="name"
      multivalue
      required
      :error="hasError"
      :errorMessage="errorMessage"
    />
    
    <div class="tw-mt-4">
      <VcButton type="submit">
        Validate
      </VcButton>
    </div>
  </VcForm>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcMultivalue, VcForm, VcButton } from '@vc-shell/framework';

const selectedItems = ref([]);
const hasError = ref(false);
const errorMessage = ref('');

const items = [
  { id: '1', name: 'Item 1' },
  { id: '2', name: 'Item 2' },
  { id: '3', name: 'Item 3' },
  { id: '4', name: 'Item 4' },
  { id: '5', name: 'Item 5' }
];

function validateForm() {
  if (selectedItems.value.length === 0) {
    hasError.value = true;
    errorMessage.value = 'Please select at least one item';
  } else {
    hasError.value = false;
    errorMessage.value = '';
    console.log('Form is valid!', selectedItems.value);
  }
}
</script>
```

### Custom Item Templates

```vue
<template>
  <VcMultivalue
    v-model="selectedUsers"
    label="Assign Users"
    placeholder="Select users to assign"
    :options="users"
    option-value="id"
    option-label="name"
    multivalue
  >
    <template #option="{ item }">
      <div class="tw-flex tw-items-center">
        <div 
          class="tw-w-6 tw-h-6 tw-rounded-full tw-flex tw-items-center tw-justify-center tw-bg-[var(--primary-100)] tw-text-[var(--primary-800)] tw-mr-2"
        >
          {{ item.name.charAt(0) }}
        </div>
        <div>
          <div class="tw-font-medium">{{ item.name }}</div>
          <div class="tw-text-xs tw-text-[var(--neutrals-500)]">{{ item.email }}</div>
        </div>
      </div>
    </template>
    
    <template #selected-item="{ item, remove }">
      <div class="tw-flex tw-items-center">
        <div 
          class="tw-w-5 tw-h-5 tw-rounded-full tw-flex tw-items-center tw-justify-center tw-bg-[var(--primary-100)] tw-text-[var(--primary-800)] tw-mr-1"
        >
          {{ item.name.charAt(0) }}
        </div>
        <span class="tw-mr-1">{{ item.name }}</span>
        <VcIcon
          icon="material-close"
          size="xs"
          class="tw-cursor-pointer"
          @click="remove"
        />
      </div>
    </template>
  </VcMultivalue>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcMultivalue, VcIcon } from '@vc-shell/framework';

const selectedUsers = ref([]);
const users = [
  { id: '1', name: 'John Doe', email: 'john.doe@example.com' },
  { id: '2', name: 'Jane Smith', email: 'jane.smith@example.com' },
  { id: '3', name: 'Michael Brown', email: 'michael.brown@example.com' },
  { id: '4', name: 'Sarah Johnson', email: 'sarah.johnson@example.com' },
  { id: '5', name: 'David Williams', email: 'david.williams@example.com' }
];
</script>
```

### Numeric Values

```vue
<template>
  <VcMultivalue
    v-model="quantities"
    label="Quantities"
    placeholder="Add quantities (press Enter after each value)"
    type="number"
    :multivalue="false"
    hint="Enter numeric values only"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcMultivalue } from '@vc-shell/framework';

const quantities = ref([]);
</script>
```

### Loading State

```vue
<template>
  <VcMultivalue
    v-model="selectedCategories"
    label="Categories"
    placeholder="Loading categories..."
    :options="categories"
    option-value="id"
    option-label="name"
    multivalue
    :loading="isLoading"
  />
  
  <div class="tw-mt-4">
    <VcButton @click="loadCategories">
      {{ isLoading ? 'Loading...' : 'Reload Categories' }}
    </VcButton>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcMultivalue, VcButton } from '@vc-shell/framework';

const selectedCategories = ref([]);
const categories = ref([]);
const isLoading = ref(true);

// Simulate API call
function loadCategories() {
  isLoading.value = true;
  categories.value = [];
  
  setTimeout(() => {
    categories.value = [
      { id: '1', name: 'Electronics' },
      { id: '2', name: 'Clothing' },
      { id: '3', name: 'Home & Garden' },
      { id: '4', name: 'Books' },
      { id: '5', name: 'Toys' }
    ];
    isLoading.value = false;
  }, 1500);
}

// Load categories on mount
loadCategories();
</script>
```

### Product Form with Tags

```vue
<template>
  <VcForm @submit.prevent="saveProduct">
    <div class="tw-space-y-4">
      <VcInput
        v-model="product.name"
        label="Product Name"
        required
      />
      
      <VcMultivalue
        v-model="product.categories"
        label="Categories"
        placeholder="Select product categories"
        :options="categories"
        option-value="id"
        option-label="name"
        multivalue
        required
      />
      
      <VcMultivalue
        v-model="product.tags"
        label="Tags"
        placeholder="Add search tags (press Enter after each tag)"
        :multivalue="false"
        hint="Add keywords to help customers find your product"
      />
      
      <div class="tw-mt-6 tw-flex tw-justify-end">
        <VcButton type="submit" variant="primary">
          Save Product
        </VcButton>
      </div>
    </div>
  </VcForm>
</template>

<script lang="ts" setup>
import { reactive } from 'vue';
import { VcMultivalue, VcForm, VcInput, VcButton } from '@vc-shell/framework';

const product = reactive({
  name: '',
  categories: [],
  tags: []
});

const categories = [
  { id: '1', name: 'Electronics' },
  { id: '2', name: 'Clothing' },
  { id: '3', name: 'Home & Garden' },
  { id: '4', name: 'Books' },
  { id: '5', name: 'Toys' }
];

function saveProduct() {
  console.log('Product saved:', product);
  // Implement API call to save product
}
</script>
```

