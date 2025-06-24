# VcTextarea Component

The `VcTextarea` component is a molecule used throughout the VC-Shell framework for creating multiline text input fields. It provides a responsive and customizable textarea with support for labels, validation, error states, and more.

## Storybook

[VcTextarea Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vctextarea--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vctextarea--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcTextarea
    v-model="description"
    label="Description"
    placeholder="Enter your description here..."
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcTextarea } from '@vc-shell/framework';

const description = ref('');
</script>
```

## Props

| Prop              | Type       | Default     | Description                                            |
| ----------------- | ---------- | ----------- | ------------------------------------------------------ |
| `modelValue`      | `string`   | `undefined` | Value of the textarea (v-model)                        |
| `label`           | `string`   | `undefined` | Label displayed above the textarea                     |
| `placeholder`     | `string`   | `undefined` | Placeholder text when textarea is empty                |
| `required`        | `boolean`  | `false`     | Whether the field is required                          |
| `disabled`        | `boolean`  | `false`     | Whether the textarea is disabled                       |
| `error`           | `boolean`  | `false`     | Whether to show the textarea in error state            |
| `errorMessage`    | `string`   | `undefined` | Error message to display below the textarea            |
| `tooltip`         | `string`   | `undefined` | Tooltip text for additional information                |
| `name`            | `string`   | `'Field'`   | Name attribute for the textarea element                |
| `maxlength`       | `string`   | `'1024'`    | Maximum number of characters                           |
| `multilanguage`   | `boolean`  | `false`     | Whether the label should show multilanguage icon       |
| `currentLanguage` | `string`   | `undefined` | Current language code for multilanguage support        |

## Events

| Event              | Payload  | Description                                       |
| ------------------ | -------- | ------------------------------------------------- |
| `update:modelValue` | `string` | Emitted when the textarea's value changes        |

## Slots

| Slot      | Description                                            |
| --------- | ------------------------------------------------------ |
| `error`   | Custom content for error message display               |

## CSS Variables

The textarea component uses CSS variables for theming, which can be customized:

```css
:root {
  --textarea-height: 120px;                    /* Minimum height of the textarea */
  --textarea-border-color: var(--neutrals-300); /* Border color in normal state */
  --textarea-text-color: var(--neutrals-800);  /* Text color in the textarea */
  --textarea-border-radius: 4px;               /* Border radius of the textarea */
  --textarea-background-color: var(--additional-50); /* Background color of the textarea */
  --textarea-placeholder-color: var(--neutrals-400); /* Placeholder text color */
  
  /* Error state */
  --textarea-text-color-error: var(--danger-500); /* Text color in error state */
  --textarea-border-color-error: var(--danger-500); /* Border color in error state */
  
  /* Focus state */
  --textarea-border-color-focus: var(--primary-100); /* Border/outline color when focused */
  
  /* Disabled state */
  --textarea-disabled-background-color: var(--neutrals-200); /* Background when disabled */
  --textarea-disabled-text-color: var(--neutrals-500); /* Text color when disabled */
}
```

## Examples

### Basic Textarea

```vue
<template>
  <VcTextarea
    v-model="notes"
    placeholder="Enter your notes here..."
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcTextarea } from '@vc-shell/framework';

const notes = ref('');
</script>
```

### Textarea with Label

```vue
<template>
  <VcTextarea
    v-model="description"
    label="Product Description"
    placeholder="Describe your product..."
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcTextarea } from '@vc-shell/framework';

const description = ref('');
</script>
```

### Required Textarea

```vue
<template>
  <VcTextarea
    v-model="feedback"
    label="Feedback"
    placeholder="Please provide your feedback..."
    required
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcTextarea } from '@vc-shell/framework';

const feedback = ref('');
</script>
```

### Textarea with Character Limit

```vue
<template>
  <VcTextarea
    v-model="summary"
    label="Summary"
    placeholder="Briefly describe the issue..."
    maxlength="500"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcTextarea } from '@vc-shell/framework';

const summary = ref('');
</script>
```

### Disabled Textarea

```vue
<template>
  <VcTextarea
    v-model="readOnlyData"
    label="System Information"
    disabled
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcTextarea } from '@vc-shell/framework';

const readOnlyData = ref('This is read-only system information that cannot be modified.');
</script>
```

### Textarea with Error State

```vue
<template>
  <VcTextarea
    v-model="userInput"
    label="Comments"
    :error="hasError"
    :errorMessage="errorMessage"
    @update:modelValue="validateInput"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcTextarea } from '@vc-shell/framework';

const userInput = ref('');
const hasError = ref(false);
const errorMessage = ref('');

function validateInput(value: string) {
  if (value.length < 10) {
    hasError.value = true;
    errorMessage.value = 'Comments must be at least 10 characters long';
  } else {
    hasError.value = false;
    errorMessage.value = '';
  }
}
</script>
```

### Textarea with Tooltip

```vue
<template>
  <VcTextarea
    v-model="metaDescription"
    label="Meta Description"
    tooltip="This text will appear in search engine results. Keep it concise and descriptive."
    placeholder="Enter a meta description for SEO..."
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcTextarea } from '@vc-shell/framework';

const metaDescription = ref('');
</script>
```

### Textarea with Custom Error Display

```vue
<template>
  <VcTextarea
    v-model="biography"
    label="Biography"
    :error="validationError"
  >
    <template #error>
      <div class="tw-flex tw-items-center tw-mt-1 tw-text-[color:var(--error-500)]">
        <VcIcon icon="material-warning" size="s" class="tw-mr-1" />
        <span>Your biography should be between 50 and 500 characters</span>
      </div>
    </template>
  </VcTextarea>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue';
import { VcTextarea, VcIcon } from '@vc-shell/framework';

const biography = ref('');
const validationError = computed(() => {
  const length = biography.value.length;
  return length > 0 && (length < 50 || length > 500);
});
</script>
```

### Form with Multiple Textareas

```vue
<template>
  <form @submit.prevent="submitForm" class="tw-space-y-4">
    <VcTextarea
      v-model="formData.shortDescription"
      label="Short Description"
      placeholder="Provide a brief overview..."
      required
      :error="errors.shortDescription"
      :errorMessage="errorMessages.shortDescription"
    />
    
    <VcTextarea
      v-model="formData.detailedDescription"
      label="Detailed Description"
      placeholder="Provide comprehensive details..."
      :error="errors.detailedDescription"
      :errorMessage="errorMessages.detailedDescription"
    />
    
    <VcTextarea
      v-model="formData.technicalNotes"
      label="Technical Notes"
      placeholder="Add any technical details..."
      :error="errors.technicalNotes"
      :errorMessage="errorMessages.technicalNotes"
    />
    
    <VcButton type="submit">Submit</VcButton>
  </form>
</template>

<script lang="ts" setup>
import { ref, reactive } from 'vue';
import { VcTextarea, VcButton } from '@vc-shell/framework';

const formData = reactive({
  shortDescription: '',
  detailedDescription: '',
  technicalNotes: ''
});

const errors = reactive({
  shortDescription: false,
  detailedDescription: false,
  technicalNotes: false
});

const errorMessages = reactive({
  shortDescription: '',
  detailedDescription: '',
  technicalNotes: ''
});

function submitForm() {
  // Reset all errors
  errors.shortDescription = false;
  errors.detailedDescription = false;
  errors.technicalNotes = false;
  
  // Validate short description
  if (!formData.shortDescription) {
    errors.shortDescription = true;
    errorMessages.shortDescription = 'Short description is required';
  } else if (formData.shortDescription.length < 10) {
    errors.shortDescription = true;
    errorMessages.shortDescription = 'Short description must be at least 10 characters';
  }
  
  // Validate detailed description (optional but with min length if provided)
  if (formData.detailedDescription && formData.detailedDescription.length < 50) {
    errors.detailedDescription = true;
    errorMessages.detailedDescription = 'Detailed description must be at least 50 characters';
  }
  
  // Check if form is valid
  if (!errors.shortDescription && !errors.detailedDescription && !errors.technicalNotes) {
    console.log('Form submitted:', formData);
    // Process form submission
  }
}
</script>
```
