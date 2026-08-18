# VcImage Component

The `VcImage` component is a versatile atom for displaying images throughout the VC-Shell framework. It provides consistent presentation of images with support for various aspect ratios, sizes, and styling options such as rounded corners and borders.

## Storybook

[VcImage Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vcimage--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vcimage--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcImage src="https://example.com/image.jpg" size="m" />
</template>

<script lang="ts" setup>
import { VcImage } from '@vc-shell/framework';
</script>
```

## Props

| Prop          | Type                                            | Default           | Description                                                     |
| ------------- | ----------------------------------------------- | ----------------- | --------------------------------------------------------------- |
| `src`         | `string`                                        | `undefined`       | Source URL of the image                                         |
| `aspect`      | `'1x1' \| '16x9' \| '4x3' \| '3x2'`             | `'1x1'`           | The aspect ratio of the image container                         |
| `size`        | `'auto' \| 'xxs' \| 'xs' \| 's' \| 'm' \| 'l' \| 'xl' \| 'xxl'` | `'auto'` | Predefined size of the image                                   |
| `background`  | `'cover' \| 'contain' \| 'auto'`                | `'cover'`         | Background image sizing method                                  |
| `rounded`     | `boolean`                                       | `false`           | Whether to display the image with rounded corners               |
| `bordered`    | `boolean`                                       | `false`           | Whether to display a border around the image                    |
| `clickable`   | `boolean`                                       | `false`           | Whether the image can be clicked, emitting a click event        |
| `emptyIcon`   | `string`                                        | `'material-image'`| The icon to display when no src is provided                     |

## Events

| Event         | Parameters | Description                                                     |
| ------------- | ---------- | --------------------------------------------------------------- |
| `click`       | -          | Emitted when clicking on an image with `clickable` set to true  |

## CSS Variables

The image component uses CSS variables for theming, which can be customized:

```css
:root {
  --image-size-xxs: 24px;             /* Extra-extra-small image size */
  --image-size-xs: 32px;              /* Extra-small image size */
  --image-size-s: 48px;               /* Small image size */
  --image-size-m: 64px;               /* Medium image size (default) */
  --image-size-l: 96px;               /* Large image size */
  --image-size-xl: 128px;             /* Extra-large image size */
  --image-size-xxl: 145px;            /* Extra-extra-large image size */

  --image-border-radius: 3px;         /* Border radius when bordered prop is true */
  --image-border-color: var(--neutrals-200); /* Border color when bordered prop is true */
  --image-empty-icon-color: var(--secondary-500); /* Color of the placeholder icon when no image is present */
}
```

## Examples

### Default Image

```vue
<template>
  <div class="tw-w-48">
    <VcImage src="https://example.com/image.jpg" />
  </div>
</template>
```

### Widescreen Image

```vue
<template>
  <div class="tw-w-64">
    <VcImage 
      src="https://example.com/landscape.jpg" 
      aspect="16x9" 
    />
  </div>
</template>
```

### Profile Image

```vue
<template>
  <VcImage 
    src="https://example.com/profile.jpg" 
    size="xl" 
    rounded 
  />
</template>
```

### Thumbnails with Borders

```vue
<template>
  <div class="tw-flex tw-gap-2">
    <VcImage 
      v-for="i in 3" 
      :key="i" 
      :src="`https://example.com/image${i}.jpg`" 
      size="s" 
      bordered 
    />
  </div>
</template>
```

### Clickable Image Gallery

```vue
<template>
  <div class="tw-grid tw-grid-cols-3 tw-gap-2">
    <VcImage 
      v-for="(image, index) in images" 
      :key="index" 
      :src="image.src" 
      clickable 
      bordered 
      @click="openImage(image)" 
    />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcImage } from '@vc-shell/framework';

const images = ref([
  { id: 1, src: 'https://example.com/image1.jpg', title: 'Image 1' },
  { id: 2, src: 'https://example.com/image2.jpg', title: 'Image 2' },
  { id: 3, src: 'https://example.com/image3.jpg', title: 'Image 3' },
  { id: 4, src: 'https://example.com/image4.jpg', title: 'Image 4' },
  { id: 5, src: 'https://example.com/image5.jpg', title: 'Image 5' },
  { id: 6, src: 'https://example.com/image6.jpg', title: 'Image 6' },
]);

function openImage(image) {
  console.log('Opening image:', image.title);
  // Implement your image viewing logic here
}
</script>
```

### Image with Contain Sizing

```vue
<template>
  <div class="tw-w-64 tw-h-48 tw-bg-[var(--neutrals-100)]">
    <VcImage 
      src="https://example.com/image.jpg" 
      background="contain" 
      aspect="16x9" 
    />
  </div>
</template>
```

### Placeholder for Missing Image

```vue
<template>
  <VcImage 
    size="l" 
    bordered 
    emptyIcon="material-broken_image" 
  />
</template>
```

### Image with Different Sizes

```vue
<template>
  <div class="tw-flex tw-items-end tw-gap-2">
    <div v-for="size in sizes" :key="size">
      <p class="tw-text-center tw-text-xs tw-mb-1">{{ size }}</p>
      <VcImage 
        src="https://example.com/image.jpg" 
        :size="size" 
        bordered 
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { VcImage } from '@vc-shell/framework';

const sizes = ['xxs', 'xs', 's', 'm', 'l', 'xl', 'xxl'];
</script>
```

### CSS Escaping for URLs

The component properly escapes URLs to prevent CSS injection:

```js
// In the computed property
`background: url(${CSS.escape(secureUrl)}) center / ${props.background} no-repeat`
```

