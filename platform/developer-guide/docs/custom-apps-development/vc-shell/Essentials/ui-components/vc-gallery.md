# VcGallery

VcGallery is a versatile component for displaying, managing, and interacting with collections of images or other assets. It provides functionality for viewing, uploading, editing, deleting, and reordering images with an intuitive user interface.

## Storybook

[VcGallery Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/organisms-vcgallery--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=organisms-vcgallery--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcGallery
    :images="productImages"
    label="Product Images"
    :required="true"
    @upload="handleUpload"
    @edit="handleEdit"
    @remove="handleRemove"
    @sort="handleSort"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcGallery, ICommonAsset } from '@vc-shell/framework';

const productImages = ref<ICommonAsset[]>([
  {
    id: '1',
    name: 'product-image-1.jpg',
    url: '/assets/images/product-1.jpg',
    sortOrder: 0
  },
  {
    id: '2',
    name: 'product-image-2.jpg',
    url: '/assets/images/product-2.jpg',
    sortOrder: 1
  }
]);

function handleUpload(files: FileList, startingSortOrder?: number) {
  // Handle file upload logic
  console.log('Files to upload:', files);
  console.log('Starting sort order:', startingSortOrder);
}

function handleEdit(image: ICommonAsset) {
  // Handle image edit logic
  console.log('Image to edit:', image);
}

function handleRemove(image: ICommonAsset) {
  // Handle image removal logic
  console.log('Image to remove:', image);
}

function handleSort(sortedImages: ICommonAsset[]) {
  // Handle images reordering
  productImages.value = sortedImages;
}
</script>
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `images` | `ICommonAsset[]` | `[]` | Array of images to display in the gallery |
| `disabled` | `boolean` | `false` | Disables all interactions with the gallery |
| `required` | `boolean` | `false` | Indicates if the field is required |
| `label` | `string` | — | Label text for the gallery |
| `tooltip` | `string` | — | Tooltip text for the label |
| `uploadIcon` | `string` | `'material-cloud_upload'` | Icon for the upload button |
| `multiple` | `boolean` | `false` | Allows multiple file selection during upload |
| `variant` | `'gallery' \| 'file-upload'` | `'gallery'` | Visual variant of the component |
| `itemActions` | `{ preview: boolean, edit: boolean, remove: boolean }` | `{ preview: true, edit: true, remove: true }` | Controls which actions are available for each image |
| `hideAfterUpload` | `boolean` | `false` | Hides the upload button after files are uploaded |
| `rules` | `IValidationRules \| keyof IValidationRules` | — | Validation rules for uploaded files |
| `name` | `string` | `'Gallery'` | Name of the gallery (used for identification) |
| `loading` | `boolean` | `false` | Shows loading state during operations |
| `customText` | `{ dragHere: string, browse: string }` | — | Custom text for the upload area |

## Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `upload` | `(files: FileList, startingSortOrder?: number)` | Emitted when files are selected for upload |
| `sort` | `(sorted: ICommonAsset[])` | Emitted when images are reordered |
| `edit` | `(image: ICommonAsset)` | Emitted when an image edit action is triggered |
| `remove` | `(image: ICommonAsset)` | Emitted when an image removal action is triggered |

## CSS Variables

The VcGallery component and its internal components use CSS variables for styling:

```css
:root {
  /* Main gallery component */
  --gallery-reorder-color: var(--primary-500);            /* Color of the line indicator when reordering images */
  
  /* Gallery item component */
  --gallery-item-border-color: var(--secondary-200);      /* Border color for gallery item thumbnails */
  --gallery-item-overlay-bg-color: var(--primary-100);    /* Background color for the overlay when hovering over an item */
  --gallery-item-move-icon-color: var(--secondary-300);   /* Color of the drag handle icon for reordering */
  --gallery-item-button-icon-color: var(--primary-500);   /* Color of action button icons (preview, edit, delete) */
  
  /* Gallery preview component */
  --gallery-preview-btn-bg-color: var(--secondary-50);    /* Background color for navigation buttons in preview mode */
  --gallery-preview-btn-icon-color: var(--secondary-400); /* Color of navigation button icons in preview mode */
  --gallery-preview-btn-shadow-color: var(--neutrals-950); /* Base color for button shadows in preview mode */
  --gallery-preview-btn-shadow: 0 0 20px rgba(var(--gallery-preview-btn-shadow-color), 0.15); /* Shadow for buttons on hover in preview mode */
  --gallery-preview-overlay-color: var(--primary-400);    /* Color of the active thumbnail indicator in preview mode */
}
```

## ICommonAsset Interface

The gallery uses the `ICommonAsset` interface for image objects:

```typescript
interface ICommonAsset {
  id?: string;              // Unique identifier
  name?: string;            // File name
  url?: string;             // URL to the image
  sortOrder?: number;       // Order position
  title?: string;           // Display title
  relativeUrl?: string;     // Relative URL path
  description?: string;     // Image description
  modifiedDate?: Date;      // Last modified date
  altText?: string;         // Alternative text
  typeId?: string;          // Type identifier
  size?: number;            // File size in bytes
  readableSize?: string;    // Human-readable size
  createdDate?: Date;       // Creation date
  [key: string]: any;       // Additional properties
}
```

## Drag and Drop Reordering

VcGallery supports drag-and-drop reordering of images, allowing users to visually arrange images in the desired order:

```vue
<template>
  <VcGallery
    :images="productImages"
    label="Product Images"
    @sort="handleSort"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcGallery, ICommonAsset } from '@vc-shell/framework';

const productImages = ref<ICommonAsset[]>([
  { id: '1', name: 'image1.jpg', url: '/images/1.jpg', sortOrder: 0 },
  { id: '2', name: 'image2.jpg', url: '/images/2.jpg', sortOrder: 1 },
  { id: '3', name: 'image3.jpg', url: '/images/3.jpg', sortOrder: 2 }
]);

function handleSort(sortedImages: ICommonAsset[]) {
  productImages.value = sortedImages;
}
</script>
```

## Image Preview

The gallery provides a built-in preview mode that allows users to view images in full-screen:

```vue
<template>
  <VcGallery
    :images="productImages"
    :itemActions="{ preview: true, edit: false, remove: false }"
  />
</template>
```

## Customizing Actions

You can customize which actions are available for each image in the gallery:

```vue
<template>
  <VcGallery
    :images="productImages"
    :itemActions="{
      preview: true,  // Allow image preview
      edit: true,     // Allow image editing
      remove: false   // Disable image removal
    }"
  />
</template>
```

## File Upload Variants

VcGallery supports different visual styles for the upload area:

```vue
<template>
  <!-- Gallery style (default) -->
  <VcGallery
    :images="productImages"
    variant="gallery"
  />
  
  <!-- File upload style -->
  <VcGallery
    :images="productImages"
    variant="file-upload"
  />
</template>
```

## Custom Upload Icon

You can customize the icon displayed in the upload area:

```vue
<template>
  <VcGallery
    :images="productImages"
    uploadIcon="material-file_upload"
  />
</template>
```

## Integration with useAssets Composable

VcGallery is designed to work seamlessly with the `useAssets` composable for handling file operations:

```vue
<template>
  <VcGallery
    :images="productImages"
    :loading="loading"
    @upload="handleUpload"
    @edit="handleEdit"
    @remove="handleRemove"
    @sort="handleSort"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcGallery, useAssets } from '@vc-shell/framework';

const productImages = ref([]);
const { upload, edit, remove, loading } = useAssets();

async function handleUpload(files, startingSortOrder) {
  const uploadedImages = await upload(files, 'products/images', startingSortOrder);
  productImages.value = [...productImages.value, ...uploadedImages];
}

function handleEdit(image) {
  const updatedImages = edit([image], productImages.value);
  productImages.value = updatedImages;
}

function handleRemove(image) {
  const remainingImages = remove([image], productImages.value);
  productImages.value = remainingImages;
}

function handleSort(sortedImages) {
  productImages.value = sortedImages;
}
</script>
```

## Custom Text for Upload Area

You can customize text in the upload area:

```vue
<template>
  <VcGallery
    :images="productImages"
    :customText="{
      dragHere: 'Drop your files here',
      browse: 'Select files'
    }"
  />
</template>
```


