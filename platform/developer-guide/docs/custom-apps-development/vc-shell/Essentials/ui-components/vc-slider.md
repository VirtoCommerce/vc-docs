# VcSlider Component

The `VcSlider` component is a versatile carousel/slider that displays content in a horizontal scrollable container. It's based on the Swiper.js library and provides a simple way to create carousels with customizable slides, navigation, and layout options.

## Storybook

[VcSlider Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vcslider--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vcslider--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcSlider
    :slides="slides"
    slidesPerView="2"
    :spaceBetweenSlides="10"
    :navigation="true"
  >
    <template #default="{slide}">
      <VcImage :src="slide.imageUrl" class="tw-rounded-md" />
      <div class="tw-mt-2 tw-font-medium">{{ slide.title }}</div>
      <div class="tw-text-sm tw-text-[var(--neutrals-500)]">{{ slide.description }}</div>
    </template>
  </VcSlider>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcSlider, VcImage } from '@vc-shell/framework';

const slides = [
  { title: 'Slide 1', description: 'Description 1', imageUrl: 'https://picsum.photos/400/300?random=1' },
  { title: 'Slide 2', description: 'Description 2', imageUrl: 'https://picsum.photos/400/300?random=2' },
  { title: 'Slide 3', description: 'Description 3', imageUrl: 'https://picsum.photos/400/300?random=3' },
  { title: 'Slide 4', description: 'Description 4', imageUrl: 'https://picsum.photos/400/300?random=4' },
];
</script>
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `slides` | `Record<string, unknown>[] \| unknown[]` | `[]` | Array of objects representing slides to display |
| `navigation` | `boolean` | `undefined` | Enables/disables navigation buttons for the slider |
| `overflow` | `boolean` | `undefined` | Allows slides to be visible outside the container |
| `slidesPerView` | `string \| 'auto'` | `'auto'` | Number of slides visible simultaneously |
| `spaceBetweenSlides` | `number` | `10` | Space between slides in pixels |

## Slots

| Slot | Props | Description |
|------|-------|-------------|
| `default` | `{ slide: Object }` | Content for each slide |
| `prevBtn` | - | Custom previous button content |
| `nextBtn` | - | Custom next button content |

## CSS Variables

The slider component uses CSS variables for theming, which can be customized:

```css
:root {
  --slider-button-background: var(--additional-50);  /* Background color for navigation buttons */
  --slider-button-border: var(--neutrals-300);       /* Border color for navigation buttons */
  --slider-button-text: var(--primary-500);          /* Icon/text color for enabled navigation buttons */
  --slider-button-text-disabled: var(--neutrals-400); /* Icon/text color for disabled navigation buttons */
}
```

## Examples

### Standard Slider with Two Visible Slides

```vue
<template>
  <VcSlider
    :slides="products"
    slidesPerView="2"
    :spaceBetweenSlides="10"
    :navigation="true"
    class="tw-w-full"
  >
    <template #default="{slide}">
      <VcImage :src="slide.imageUrl" class="tw-rounded-md" />
      <div class="tw-mt-2 tw-font-medium">{{ slide.name }}</div>
      <div class="tw-text-sm tw-text-[var(--neutrals-500)]">{{ slide.price }}</div>
    </template>
  </VcSlider>
</template>

<script lang="ts" setup>
import { VcSlider, VcImage } from '@vc-shell/framework';

const products = [
  { name: 'Product A', price: '$19.99', imageUrl: 'https://picsum.photos/400/300?random=1' },
  { name: 'Product B', price: '$24.99', imageUrl: 'https://picsum.photos/400/300?random=2' },
  { name: 'Product C', price: '$34.99', imageUrl: 'https://picsum.photos/400/300?random=3' },
  { name: 'Product D', price: '$44.99', imageUrl: 'https://picsum.photos/400/300?random=4' },
];
</script>
```

### Auto-width Slides with Overflow

```vue
<template>
  <VcSlider
    :slides="categories"
    slidesPerView="auto"
    :overflow="true"
    :spaceBetweenSlides="15"
    :navigation="true"
    class="tw-w-full"
  >
    <template #default="{slide}">
      <div class="tw-w-48">
        <VcImage :src="slide.imageUrl" class="tw-rounded-md" />
        <div class="tw-mt-2 tw-font-medium tw-text-center">{{ slide.name }}</div>
      </div>
    </template>
  </VcSlider>
</template>

<script lang="ts" setup>
import { VcSlider, VcImage } from '@vc-shell/framework';

const categories = [
  { name: 'Electronics', imageUrl: 'https://picsum.photos/400/300?random=1' },
  { name: 'Clothing', imageUrl: 'https://picsum.photos/400/300?random=2' },
  { name: 'Home & Garden', imageUrl: 'https://picsum.photos/400/300?random=3' },
  { name: 'Toys', imageUrl: 'https://picsum.photos/400/300?random=4' },
  { name: 'Sports', imageUrl: 'https://picsum.photos/400/300?random=5' },
];
</script>
```

### Single Slide with Full Width

```vue
<template>
  <VcSlider
    :slides="banners"
    slidesPerView="1"
    :navigation="true"
    class="tw-w-full"
  >
    <template #default="{slide}">
      <div class="tw-relative">
        <VcImage :src="slide.imageUrl" class="tw-rounded-md tw-w-full" />
        <div class="tw-absolute tw-bottom-0 tw-left-0 tw-w-full tw-p-4 tw-bg-black tw-bg-opacity-50 tw-text-white">
          <div class="tw-text-xl tw-font-bold">{{ slide.title }}</div>
          <div class="tw-mt-1">{{ slide.description }}</div>
        </div>
      </div>
    </template>
  </VcSlider>
</template>

<script lang="ts" setup>
import { VcSlider, VcImage } from '@vc-shell/framework';

const banners = [
  { 
    title: 'Summer Sale', 
    description: 'Up to 50% off on selected items', 
    imageUrl: 'https://picsum.photos/1200/400?random=1'
  },
  { 
    title: 'New Collection', 
    description: 'Check out our latest arrivals', 
    imageUrl: 'https://picsum.photos/1200/400?random=2'
  },
  { 
    title: 'Free Shipping', 
    description: 'On orders over $50', 
    imageUrl: 'https://picsum.photos/1200/400?random=3'
  },
];
</script>
```

### Custom Navigation Buttons

```vue
<template>
  <VcSlider
    :slides="items"
    slidesPerView="2"
    :navigation="true"
    class="tw-w-full"
  >
    <template #default="{slide}">
      <VcImage :src="slide.imageUrl" class="tw-rounded-md" />
      <div class="tw-mt-2 tw-font-medium">{{ slide.title }}</div>
    </template>
    
    <template #prevBtn>
      <button class="tw-bg-[var(--primary-500)] tw-text-white tw-p-2 tw-rounded-full">
        <VcIcon icon="material-arrow_back" size="s" />
      </button>
    </template>
    
    <template #nextBtn>
      <button class="tw-bg-[var(--primary-500)] tw-text-white tw-p-2 tw-rounded-full">
        <VcIcon icon="material-arrow_forward" size="s" />
      </button>
    </template>
  </VcSlider>
</template>

<script lang="ts" setup>
import { VcSlider, VcImage, VcIcon } from '@vc-shell/framework';

const items = [
  { title: 'Item 1', imageUrl: 'https://picsum.photos/400/300?random=1' },
  { title: 'Item 2', imageUrl: 'https://picsum.photos/400/300?random=2' },
  { title: 'Item 3', imageUrl: 'https://picsum.photos/400/300?random=3' },
  { title: 'Item 4', imageUrl: 'https://picsum.photos/400/300?random=4' },
];
</script>
```

### Product Cards Carousel

```vue
<template>
  <div class="tw-p-4">
    <h2 class="tw-text-2xl tw-font-bold tw-mb-4">Featured Products</h2>
    
    <VcSlider
      :slides="products"
      slidesPerView="auto"
      :spaceBetweenSlides="20"
      :navigation="true"
      class="tw-w-full"
    >
      <template #default="{slide}">
        <div class="tw-w-64 tw-border tw-border-[var(--neutrals-200)] tw-rounded-lg tw-overflow-hidden">
          <VcImage :src="slide.imageUrl" class="tw-w-full tw-h-48 tw-object-cover" />
          <div class="tw-p-4">
            <div class="tw-font-medium tw-text-lg">{{ slide.name }}</div>
            <div class="tw-flex tw-justify-between tw-items-center tw-mt-2">
              <div class="tw-font-bold tw-text-[var(--primary-700)]">{{ slide.price }}</div>
              <VcRating :model-value="slide.rating" :max="5" variant="stars" />
            </div>
            <VcButton variant="primary" size="small" class="tw-mt-3 tw-w-full">
              Add to Cart
            </VcButton>
          </div>
        </div>
      </template>
    </VcSlider>
  </div>
</template>

<script lang="ts" setup>
import { VcSlider, VcImage, VcButton, VcRating } from '@vc-shell/framework';

const products = [
  { name: 'Wireless Headphones', price: '$89.99', rating: 4.5, imageUrl: 'https://picsum.photos/400/300?random=1' },
  { name: 'Smart Watch', price: '$199.99', rating: 4.2, imageUrl: 'https://picsum.photos/400/300?random=2' },
  { name: 'Bluetooth Speaker', price: '$49.99', rating: 3.8, imageUrl: 'https://picsum.photos/400/300?random=3' },
  { name: 'Laptop Stand', price: '$29.99', rating: 4.7, imageUrl: 'https://picsum.photos/400/300?random=4' },
  { name: 'Wireless Charger', price: '$39.99', rating: 4.0, imageUrl: 'https://picsum.photos/400/300?random=5' },
];
</script>
```

### Responsive Testimonials Slider

```vue
<template>
  <div class="tw-bg-[var(--neutrals-100)] tw-p-6 tw-rounded-lg">
    <h2 class="tw-text-2xl tw-font-bold tw-mb-4 tw-text-center">What Our Customers Say</h2>
    
    <VcSlider
      :slides="testimonials"
      :slidesPerView="isMobile ? '1' : '3'"
      :spaceBetweenSlides="24"
      :navigation="true"
      class="tw-w-full"
    >
      <template #default="{slide}">
        <div class="tw-bg-white tw-p-5 tw-rounded-lg tw-shadow-sm tw-h-full">
          <div class="tw-flex tw-items-center tw-mb-4">
            <div class="tw-w-12 tw-h-12 tw-rounded-full tw-overflow-hidden tw-mr-3">
              <VcImage :src="slide.avatar" class="tw-w-full tw-h-full tw-object-cover" />
            </div>
            <div>
              <div class="tw-font-medium">{{ slide.name }}</div>
              <VcRating :model-value="slide.rating" :max="5" variant="stars" />
            </div>
          </div>
          <p class="tw-text-[var(--neutrals-700)]">{{ slide.comment }}</p>
        </div>
      </template>
    </VcSlider>
  </div>
</template>

<script lang="ts" setup>
import { inject, Ref } from 'vue';
import { VcSlider, VcImage, VcRating } from '@vc-shell/framework';

const isMobile = inject('isMobile') as Ref<boolean>;

const testimonials = [
  {
    name: 'John Smith',
    rating: 5,
    comment: 'Excellent product quality and fast shipping. Would definitely order again!',
    avatar: 'https://randomuser.me/api/portraits/men/1.jpg'
  },
  {
    name: 'Emily Johnson',
    rating: 4,
    comment: 'Great customer service and the product exceeded my expectations.',
    avatar: 'https://randomuser.me/api/portraits/women/2.jpg'
  },
  {
    name: 'Michael Brown',
    rating: 5,
    comment: 'I've been a customer for years and have never been disappointed.',
    avatar: 'https://randomuser.me/api/portraits/men/3.jpg'
  },
  {
    name: 'Sarah Wilson',
    rating: 4,
    comment: 'The quality is top-notch and delivery was faster than expected.',
    avatar: 'https://randomuser.me/api/portraits/women/4.jpg'
  },
];
</script>
```
