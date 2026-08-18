# VcInput Component

The `VcInput` component is a versatile form control for various types of input fields including text, numbers, passwords, dates, and more. It provides a consistent UI with numerous customization options and styling variants.

## Storybook

[VcInput Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vcinput--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vcinput--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcInput v-model="inputValue" label="Full Name" placeholder="Enter your full name" />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInput } from '@vc-shell/framework';

const inputValue = ref('');
</script>
```

## Props

| Prop                 | Type                                                | Default     | Description                                                 |
| -------------------- | --------------------------------------------------- | ----------- | ----------------------------------------------------------- |
| `modelValue`         | `string \| number \| Date \| null \| undefined`     | -           | Value of the input, can be bound using v-model              |
| `label`              | `string`                                            | -           | Label text shown above the input                             |
| `placeholder`        | `string`                                            | -           | Placeholder text shown when input is empty                   |
| `type`               | `string`                                            | `'text'`    | Type of input (`'text'`, `'password'`, `'email'`, `'tel'`, `'number'`, `'integer'`, `'url'`, `'time'`, `'date'`, `'datetime-local'`) |
| `step`               | `string`                                            | `'1'`       | Step value for number inputs                                |
| `hint`               | `string`                                            | -           | Help text shown below the input                              |
| `clearable`          | `boolean`                                           | `false`     | Whether to show a clear button when input has a value        |
| `prefix`             | `string`                                            | -           | Text to display before the input value                       |
| `suffix`             | `string`                                            | -           | Text to display after the input value                        |
| `name`               | `string`                                            | `'Field'`   | Name attribute for the input element                         |
| `loading`            | `boolean`                                           | `false`     | Shows a loading spinner inside the input                     |
| `debounce`           | `string \| number`                                  | -           | Debounce time in milliseconds for the input event            |
| `disabled`           | `boolean`                                           | `false`     | Disables the input                                           |
| `autofocus`          | `boolean`                                           | `false`     | Automatically focuses the input on render                    |
| `error`              | `boolean`                                           | `false`     | Indicates an error state for the input                       |
| `errorMessage`       | `string`                                            | -           | Error message shown when error is true                       |
| `maxlength`          | `string \| number`                                  | `'1024'`    | Maximum character length for the input                       |
| `tooltip`            | `string`                                            | -           | Tooltip text shown next to the label                         |
| `required`           | `boolean`                                           | `false`     | Adds a required indicator to the label                       |
| `multilanguage`      | `boolean`                                           | `false`     | Indicates if the field supports multiple languages           |
| `currentLanguage`    | `string`                                            | -           | Current selected language for multilanguage inputs           |
| `datePickerOptions`  | `VueDatePickerProps`                                | -           | Options for date picker when type is date or datetime        |
| `size`               | `'default' \| 'small'`                              | `'default'` | Size of the input                                            |

## Events

| Event                | Parameters                                           | Description                                      |
| -------------------- | ---------------------------------------------------- | ------------------------------------------------ |
| `update:modelValue`  | `(value: string \| number \| Date \| null \| undefined) => void` | Emitted when input value changes           |
| `blur`               | `(event: Event) => void`                             | Emitted when input loses focus                    |
| `focus`              | `() => void`                                         | Emitted when input receives focus                 |

## Slots

| Slot             | Props                                             | Description                                      |
| ---------------- | ------------------------------------------------- | ------------------------------------------------ |
| `control`        | `{ editable, focused, modelValue, emitValue, placeholder }` | Custom input control                              |
| `prepend`        | `{ focus: () => void }`                           | Content to prepend outside the input              |
| `prepend-inner`  | `{ focus: () => void }`                           | Content to prepend inside the input               |
| `append-inner`   | `{ focus: () => void }`                           | Content to append inside the input                |
| `append`         | `{ focus: () => void }`                           | Content to append outside the input               |
| `error`          | -                                                 | Custom error message content                      |
| `hint`           | -                                                 | Custom hint content                               |

## CSS Variables

The input component uses CSS variables for theming, which can be customized:

```css
:root {
  --input-height: 36px;                        /* Default height of input field */
  --input-height-small: 30px;                  /* Height of input field when size="small" */
  --input-border-radius: 4px;                  /* Border radius of the input field */
  --input-border-color: var(--neutrals-300);   /* Border color in normal state */
  --input-padding: 10px;                       /* Horizontal padding inside the input field */
  
  --input-background-color: var(--additional-50); /* Background color of the input field */
  --input-placeholder-color: var(--neutrals-400); /* Color of placeholder text */
  --input-clear-color: var(--primary-500);        /* Color of the clear button */
  --input-clear-color-hover: var(--primary-600);  /* Color of the clear button on hover */
  --input-text-color: var(--neutrals-800);        /* Color of input text */
  
  /* Disabled state */
  --input-disabled-text-color: var(--neutrals-500); /* Text color when input is disabled */
  --input-disabled-bg-color: var(--neutrals-200);   /* Background color when input is disabled */
  
  /* Error state */
  --input-text-color-error: var(--danger-500);    /* Text color when in error state */
  --input-border-color-error: var(--danger-500);  /* Border color when in error state */
  
  /* Focus state */
  --input-border-color-focus: var(--primary-100); /* Outline color when input is focused */
}
```

## Examples

### Basic Text Input

```vue
<template>
  <VcInput 
    v-model="username" 
    label="Username" 
    placeholder="Enter username" 
    hint="Choose a unique username"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInput } from '@vc-shell/framework';

const username = ref('');
</script>
```

### Password Input with Visibility Toggle

```vue
<template>
  <VcInput 
    v-model="password" 
    type="password" 
    label="Password" 
    placeholder="Enter password"
    :required="true"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInput } from '@vc-shell/framework';

const password = ref('');
</script>
```

### Number Input

```vue
<template>
  <VcInput 
    v-model="quantity" 
    type="number" 
    label="Quantity" 
    placeholder="Enter quantity" 
    min="1"
    step="1"
    hint="Minimum order is 1 unit"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInput } from '@vc-shell/framework';

const quantity = ref(1);
</script>
```

### Input with Prefix and Suffix

```vue
<template>
  <VcInput 
    v-model="price" 
    type="number" 
    label="Price" 
    placeholder="0.00"
    prefix="$"
    suffix="USD"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInput } from '@vc-shell/framework';

const price = ref(null);
</script>
```

### Input with Error State

```vue
<template>
  <VcInput 
    v-model="email" 
    type="email" 
    label="Email" 
    placeholder="Enter your email"
    :error="!!emailError"
    :errorMessage="emailError"
    @blur="validateEmail"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInput } from '@vc-shell/framework';

const email = ref('');
const emailError = ref('');

function validateEmail() {
  const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
  
  if (!email.value) {
    emailError.value = 'Email is required';
  } else if (!emailRegex.test(email.value)) {
    emailError.value = 'Please enter a valid email address';
  } else {
    emailError.value = '';
  }
}
</script>
```

### Date Input

```vue
<template>
  <VcInput 
    v-model="birthdate" 
    type="date" 
    label="Birth Date" 
    placeholder="Select date"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInput } from '@vc-shell/framework';

const birthdate = ref(null);
</script>
```

### Datetime Input

```vue
<template>
  <VcInput 
    v-model="appointmentTime" 
    type="datetime-local" 
    label="Appointment Time" 
    placeholder="Select date and time"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInput } from '@vc-shell/framework';

const appointmentTime = ref(null);
</script>
```

### Input with Clearable Option

```vue
<template>
  <VcInput 
    v-model="search" 
    label="Search" 
    placeholder="Enter search term"
    clearable
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInput } from '@vc-shell/framework';

const search = ref('');
</script>
```

### Input with Prepend and Append Slots

```vue
<template>
  <VcInput 
    v-model="searchTerm" 
    label="Search" 
    placeholder="Enter search term"
  >
    <template #prepend>
      <div class="tw-bg-[var(--neutrals-300)] tw-px-3 tw-flex tw-items-center tw-rounded-l-[var(--input-border-radius)]">
        <VcIcon icon="search" />
      </div>
    </template>
    <template #append>
      <VcButton>Search</VcButton>
    </template>
  </VcInput>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInput, VcIcon, VcButton } from '@vc-shell/framework';

const searchTerm = ref('');
</script>
```

### Small Size Input

```vue
<template>
  <VcInput 
    v-model="tag" 
    label="Tag" 
    placeholder="Enter tag name"
    size="small"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInput } from '@vc-shell/framework';

const tag = ref('');
</script>
```

### Input with Debounce

```vue
<template>
  <VcInput 
    v-model="searchQuery" 
    label="Search" 
    placeholder="Start typing to search..."
    :debounce="500"
    @update:modelValue="performSearch"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInput } from '@vc-shell/framework';

const searchQuery = ref('');
const searchResults = ref([]);

function performSearch(query) {
  console.log(`Searching for: ${query}`);
  // API call or search logic here after debounce
}
</script>
```

### Input with Character Counter

```vue
<template>
  <VcInput 
    v-model="message" 
    label="Message" 
    placeholder="Type your message..."
    :maxlength="50"
  >
    <template #append-inner>
      <div class="tw-text-xs tw-text-gray-500">
        {{ message.length }}/50
      </div>
    </template>
  </VcInput>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInput } from '@vc-shell/framework';

const message = ref('');
</script>
```

### Custom Control Slot

```vue
<template>
  <VcInput 
    v-model="customValue" 
    label="Custom Input"
  >
    <template #control="{ modelValue, emitValue, placeholder }">
      <div class="tw-w-full tw-h-full tw-flex tw-items-center">
        <input
          :value="modelValue"
          @input="(e) => emitValue(e.target.value)"
          :placeholder="placeholder"
          class="tw-w-full tw-h-full tw-outline-none tw-border-none tw-px-2 tw-bg-gray-100 tw-rounded"
        />
      </div>
    </template>
  </VcInput>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcInput } from '@vc-shell/framework';

const customValue = ref('');
</script>
```

## Special Type Features

### Integer Type

The `integer` type is a special input type that only allows whole numbers:

```vue
<template>
  <VcInput 
    v-model="quantity" 
    type="integer" 
    label="Quantity" 
    placeholder="Enter a whole number"
  />
</template>
```

### Date and Datetime Types

The `date` and `datetime-local` types use the Vue Datepicker component with integrated formatting based on the user's locale:

```vue
<template>
  <VcInput 
    v-model="eventDate" 
    type="datetime-local" 
    label="Event Date & Time" 
    :datePickerOptions="{
      disabledDates: [new Date(2023, 0, 1)],
      yearRange: [2023, 2025]
    }"
  />
</template>
```

The `datePickerOptions` prop accepts all options from the [@vuepic/vue-datepicker](https://vue3datepicker.com/) component.

