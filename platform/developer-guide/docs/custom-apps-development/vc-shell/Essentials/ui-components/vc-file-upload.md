# VcFileUpload Component

The `VcFileUpload` component provides a flexible interface for uploading files with support for drag-and-drop, file selection dialog, and validation. It's designed for gallery and general file uploads with customizable appearance.

## Storybook

[VcFileUpload Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vcfileupload--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vcfileupload--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcFileUpload
    @upload="handleUpload"
    accept=".jpg, .png, .pdf"
    name="documents"
  />
</template>

<script lang="ts" setup>
import { VcFileUpload } from '@vc-shell/framework';

function handleUpload(files) {
  console.log('Files to upload:', files);
  // Implement your upload logic here
}
</script>
```

## Props

| Prop          | Type                                   | Default                                  | Description                                       |
| ------------- | -------------------------------------- | ---------------------------------------- | ------------------------------------------------- |
| `variant`     | `'gallery' \| 'file-upload'`           | `'gallery'`                              | Layout variant for the upload component           |
| `loading`     | `boolean`                              | `undefined`                              | Show loading state                                |
| `accept`      | `string`                               | `'.jpg, .png, .jpeg, .webp, .heic, .svg'` | Accepted file types in comma-separated string     |
| `multiple`    | `boolean`                              | `undefined`                              | Allow multiple file selection                     |
| `rules`       | `keyof IValidationRules \| IValidationRules` | `undefined`                        | Validation rules (using vee-validate)             |
| `name`        | `string`                               | `'Gallery'`                              | Input field name                                  |
| `icon`        | `string`                               | `'material-cloud_upload'`                | Icon to display in the upload area                |
| `customText`  | `{dragHere: string, browse: string}`   | `undefined`                              | Custom text for drag area and browse button       |

## Events

| Event     | Payload           | Description                                       |
| --------- | ----------------- | ------------------------------------------------- |
| `upload`  | `FileList`        | Emitted when files are ready to be uploaded       |

## Slots

| Slot Name  | Description                                      |
| ---------- | ------------------------------------------------ |
| `error`    | Custom content for error message display         |

## CSS Variables

```css
:root {
  /* Upload area */
  --file-upload-border-color: var(--secondary-200);       /* Border color in normal state */
  --file-upload-border-color-hover: var(--secondary-400); /* Border color when hovered */
  --file-upload-border-color-error: var(--danger-500);    /* Border color when validation error occurs */
  --file-upload-border-radius: 6px;                       /* Border radius of upload area */
  --file-upload-drag-bg: var(--primary-100);              /* Background color when dragging files over the area */
  --file-upload-icon-color: var(--primary-500);           /* Color of the upload icon */
  --file-upload-text-color: var(--neutrals-400);          /* Color of instructional text */
  --file-upload-error-color: var(--danger-500);           /* Color of error message text */
  --file-upload-background-color: var(--primary-50);      /* Default background color of upload area */
}
```

## Examples

### Basic File Upload

```vue
<template>
  <VcFileUpload
    @upload="handleUpload"
    name="documents"
  />
</template>

<script lang="ts" setup>
import { VcFileUpload } from '@vc-shell/framework';

function handleUpload(files) {
  console.log('Files to upload:', files);
  // Process files here
  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    console.log(`File ${i+1}: ${file.name}, Type: ${file.type}, Size: ${file.size} bytes`);
  }
}
</script>
```

### File Upload Variant

```vue
<template>
  <VcFileUpload
    variant="file-upload"
    accept=".pdf, .doc, .docx, .txt"
    :multiple="true"
    @upload="handleDocumentUpload"
  />
  
  <div v-if="files.length" class="tw-mt-4">
    <h3 class="tw-text-lg tw-font-medium">Selected Files:</h3>
    <ul class="tw-list-disc tw-pl-5 tw-mt-2">
      <li v-for="(file, index) in files" :key="index">
        {{ file.name }} ({{ formatFileSize(file.size) }})
      </li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcFileUpload } from '@vc-shell/framework';

const files = ref([]);

function handleDocumentUpload(fileList) {
  files.value = Array.from(fileList);
}

function formatFileSize(bytes) {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}
</script>
```

### Custom Text and Icon

```vue
<template>
  <VcFileUpload
    variant="file-upload"
    icon="material-file_upload"
    :customText="{
      dragHere: 'Drop your files in this area',
      browse: 'Select from your computer'
    }"
    @upload="handleUpload"
  />
</template>

<script lang="ts" setup>
import { VcFileUpload } from '@vc-shell/framework';

function handleUpload(files) {
  console.log('Files to upload:', files);
  // Implement your upload logic here
}
</script>
```

### With Validation Rules

```vue
<template>
  <VcFileUpload
    name="documentUpload"
    :rules="{ required: true }"
    @upload="handleUpload"
  >
    <template #error="{ message }">
      <div class="tw-text-[var(--danger-500)] tw-mt-2">{{ message || 'Please select a file.' }}</div>
    </template>
  </VcFileUpload>
</template>

<script lang="ts" setup>
import { VcFileUpload } from '@vc-shell/framework';

function handleUpload(files) {
  console.log('Files to upload:', files);
  // Implement your upload logic here
}
</script>
```

### Loading State

```vue
<template>
  <VcFileUpload
    variant="file-upload"
    :loading="isUploading"
    @upload="uploadFiles"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcFileUpload } from '@vc-shell/framework';

const isUploading = ref(false);

function uploadFiles(files) {
  isUploading.value = true;
  
  // Simulate upload process
  setTimeout(() => {
    console.log('Files uploaded:', files);
    isUploading.value = false;
  }, 2000);
}
</script>
```
