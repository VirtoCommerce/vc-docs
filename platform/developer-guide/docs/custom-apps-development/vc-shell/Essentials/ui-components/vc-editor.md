# VcEditor Component

The `VcEditor` component is a rich Markdown editor that allows users to create and edit formatted content with support for image uploads. It's built on top of md-editor-v3 with enhanced features tailored for the VC-Shell framework.

## Storybook

[VcEditor Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vceditor--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vceditor--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcEditor
    v-model="content"
    label="Description"
    placeholder="Start typing here..."
    assetsFolder="uploads"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcEditor } from '@vc-shell/framework';

const content = ref('');
</script>
```

## Props

| Prop             | Type               | Default     | Description                                     |
| ---------------- | ------------------ | ----------- | ----------------------------------------------- |
| `modelValue`     | `string`           | `''`        | Content of the editor                           |
| `label`          | `string`           | `undefined` | Label text for the editor                       |
| `placeholder`    | `string`           | `undefined` | Placeholder text when editor is empty           |
| `required`       | `boolean`          | `false`     | Whether the editor is required                  |
| `disabled`       | `boolean`          | `false`     | Whether the editor is disabled                  |
| `tooltip`        | `string`           | `undefined` | Tooltip text for the editor label               |
| `errorMessage`   | `string`           | `undefined` | Error message to display                        |
| `assetsFolder`   | `string`           | -           | Folder path for uploaded assets (required)      |
| `multilanguage`  | `boolean`          | `false`     | Whether the editor supports multiple languages  |
| `currentLanguage`| `string`           | `undefined` | Current selected language code                  |
| `maxlength`      | `number`           | `undefined` | Maximum number of characters allowed            |
| `toolbar`        | `ToolbarNames[]`   | `undefined` | Custom toolbar configuration                    |

## Events

| Event                | Payload        | Description                          |
| -------------------- | -------------- | ------------------------------------ |
| `update:modelValue`  | `string \| number \| Date \| null \| undefined`       | Emitted when content changes         |

## Slots

| Slot Name | Description                               |
| --------- | ----------------------------------------- |
| `error`   | Custom content for error message display  |

## CSS Variables

The `VcEditor` component relies on the styling provided by the underlying `md-editor-v3` library and the application's global theme. While direct CSS variable overrides for the editor itself are limited, you can influence the appearance in several ways:

```css
:root {
  /* Editor container variables */
  --editor-border-color: var(--secondary-300);        /* Border color for the editor container */
  --editor-border-radius: 4px;                        /* Border radius of the editor container */
  --editor-background-color: var(--additional-50);    /* Background color for the editor */
  
  /* Text and content variables */
  --editor-text-color: var(--neutrals-700);           /* Main text color for editor content */
  --editor-heading-color: var(--neutrals-900);        /* Color for markdown headings */
  --editor-link-color: var(--primary-500);            /* Color for links in the editor */
  --editor-code-color: var(--neutrals-800);           /* Color for inline code elements */
  
  /* Toolbar variables */
  --editor-toolbar-background: var(--neutrals-100);   /* Background color for the editor toolbar */
  --editor-toolbar-button-color: var(--neutrals-600); /* Color for toolbar buttons */
  --editor-toolbar-button-hover: var(--neutrals-700); /* Color for toolbar buttons on hover */
  
  /* Syntax highlighting variables */
  --editor-code-background: var(--neutrals-100);      /* Background color for code blocks */
  --editor-syntax-comment: var(--secondary-600);      /* Color for comments in code blocks */
  --editor-syntax-keyword: var(--primary-700);        /* Color for keywords in code blocks */
  --editor-syntax-string: var(--success-600);         /* Color for strings in code blocks */
  --editor-syntax-number: var(--warning-600);         /* Color for numbers in code blocks */
  --editor-syntax-function: var(--primary-500);       /* Color for functions in code blocks */
}
```

Note: The actual implementation of these variables depends on how the `md-editor-v3` library allows for theming. For detailed customization, you may need to refer to the `md-editor-v3` documentation and create custom CSS overrides or themes.

11. **Character Limits**: When setting `maxlength`, provide visual feedback about the remaining character count to help users manage their content length.

12. **Performance**: For pages with multiple editors, consider lazy-loading editors that aren't immediately visible to improve initial page load performance.

## Examples

### Basic Editor

```vue
<template>
  <VcEditor
    v-model="content"
    label="Description"
    placeholder="Start typing here..."
    assetsFolder="uploads"
  />
  
  <div class="tw-mt-4">
    <p>Content length: {{ content.length }} characters</p>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcEditor } from '@vc-shell/framework';

const content = ref('');
</script>
```

### With Required Field and Error Message

```vue
<template>
  <VcForm @submit.prevent="validateForm">
    <VcEditor
      v-model="content"
      label="Description"
      placeholder="Start typing here..."
      required
      :errorMessage="contentError"
    />
    
    <div class="tw-mt-4">
      <VcButton type="submit">
        Save
      </VcButton>
    </div>
  </VcForm>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcEditor, VcForm, VcButton } from '@vc-shell/framework';

const content = ref('');
const contentError = ref('');

function validateForm() {
  contentError.value = '';
  
  if (!content.value) {
    contentError.value = 'Description is required';
    return;
  }
  
  console.log('Form submitted with content:', content.value);
}
</script>
```

### With Tooltip and Character Limit

```vue
<template>
  <VcEditor
    v-model="content"
    label="Product Description"
    placeholder="Describe your product here..."
    tooltip="The description should be clear and concise"
    :maxlength="500"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcEditor } from '@vc-shell/framework';

const content = ref('');
</script>
```

### Disabled Editor

```vue
<template>
  <VcEditor
    v-model="content"
    label="Read-only Content"
    disabled
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcEditor } from '@vc-shell/framework';

const content = ref('# This is read-only content\n\nThis content cannot be edited by the user.');
</script>
```

### Custom Toolbar

```vue
<template>
  <VcEditor
    v-model="content"
    label="Simple Editor"
    placeholder="Enter basic formatting only..."
    :toolbar="customToolbar"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcEditor } from '@vc-shell/framework';

const content = ref('');
const customToolbar = ['bold', 'italic', 'title', 'link', 'image', 'preview'];
</script>
```

### Multilanguage Support

```vue
<template>
  <VcEditor
    v-model="content"
    label="Localized Description"
    :multilanguage="true"
    :currentLanguage="currentLang"
  />
  
  <div class="tw-mt-4 tw-flex tw-space-x-2">
    <VcButton 
      :selected="currentLang === 'en'"
      @click="currentLang = 'en'"
    >
      English
    </VcButton>
    <VcButton 
      :selected="currentLang === 'fr'"
      @click="currentLang = 'fr'"
    >
      French
    </VcButton>
    <VcButton 
      :selected="currentLang === 'de'"
      @click="currentLang = 'de'"
    >
      German
    </VcButton>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcEditor, VcButton } from '@vc-shell/framework';

const content = ref('');
const currentLang = ref('en');
</script>
```

### Content Preview

```vue
<template>
  <div class="tw-grid tw-grid-cols-2 tw-gap-4">
    <div>
      <h3 class="tw-mb-2 tw-font-semibold">Editor</h3>
      <VcEditor
        v-model="content"
        placeholder="Write content here..."
      />
    </div>
    <div>
      <h3 class="tw-mb-2 tw-font-semibold">Preview</h3>
      <div class="tw-border tw-border-[var(--secondary-300)] tw-rounded-md tw-p-4">
        <div v-html="renderedContent"></div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue';
import { VcEditor } from '@vc-shell/framework';
import { marked } from 'marked';
import DOMPurify from 'dompurify';

const content = ref(`# Hello World\n\nThis is a **markdown** editor with _live preview_.\n\n- List item 1\n- List item 2\n- List item 3`);

const renderedContent = computed(() => {
  return DOMPurify.sanitize(marked(content.value));
});
</script>
```

### In a Product Form

```vue
<template>
  <VcForm @submit.prevent="saveProduct">
    <div class="tw-space-y-4">
      <VcInput
        v-model="product.name"
        label="Product Name"
        required
        :error="!!errors.name"
        :errorMessage="errors.name"
      />
      
      <VcInputCurrency
        v-model:model-value="product.price"
        v-model:option="product.currency"
        label="Price"
        required
        :error="!!errors.price"
        :errorMessage="errors.price"
        :options="currencies"
      />
      
      <VcEditor
        v-model="product.description"
        label="Product Description"
        placeholder="Enter detailed product description..."
        required
        :errorMessage="errors.description"
      />
      
      <div class="tw-mt-6 tw-flex tw-justify-end">
        <VcButton type="button" variant="secondary" class="tw-mr-2">
          Cancel
        </VcButton>
        <VcButton type="submit" variant="primary" :disabled="isSubmitting">
          {{ isSubmitting ? 'Saving...' : 'Save Product' }}
        </VcButton>
      </div>
    </div>
  </VcForm>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue';
import { VcForm, VcInput, VcInputCurrency, VcEditor, VcButton } from '@vc-shell/framework';

const product = reactive({
  name: '',
  price: null as number | null,
  currency: 'USD',
  description: ''
});

const errors = reactive({
  name: '',
  price: '',
  description: ''
});

const isSubmitting = ref(false);

const currencies = [
  { title: 'USD', value: 'USD' },
  { title: 'EUR', value: 'EUR' },
  { title: 'GBP', value: 'GBP' }
];

function saveProduct() {
  // Reset errors
  errors.name = '';
  errors.price = '';
  errors.description = '';
  
  // Validate
  let valid = true;
  
  if (!product.name) {
    errors.name = 'Product name is required';
    valid = false;
  }
  
  if (!product.price) {
    errors.price = 'Price is required';
    valid = false;
  }
  
  if (!product.description) {
    errors.description = 'Description is required';
    valid = false;
  }
  
  if (!valid) return;
  
  // Submit form
  isSubmitting.value = true;
  
  // Simulate API call
  setTimeout(() => {
    console.log('Product saved:', product);
    isSubmitting.value = false;
  }, 1500);
}
</script>
```
