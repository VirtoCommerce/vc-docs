# VcRating Component

The `VcRating` component displays a rating visualization with different display variants. It's perfect for showing product ratings, reviews, or any other context where a numerical rating needs to be displayed in an intuitive way.

## Storybook

[VcRating Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vcrating--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vcrating--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcRating
    v-model="rating"
    :max="5"
    variant="stars"
    label="Product Rating"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcRating } from '@vc-shell/framework';

const rating = ref(4);
</script>
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `modelValue` | `number` | `undefined` | Current rating value (use with v-model) |
| `max` | `number` | `5` | Maximum rating value |
| `variant` | `'stars' \| 'star-and-text' \| 'text'` | `'stars'` | Rating display variant |
| `label` | `string` | `undefined` | Label for the rating component |
| `placeholder` | `string` | `undefined` | Placeholder text when no rating is available |
| `tooltip` | `string` | `undefined` | Additional tooltip information |

## Events

| Event | Payload | Description |
|-------|---------|-------------|
| `update:modelValue` | `number` | Emitted when the rating value changes |

## Slots

| Slot | Props | Description |
|------|-------|-------------|
| `details` | - | Additional content to display after the rating value |

## CSS Variables

```css
:root {
  --rating-placeholder-color: var(--neutrals-400);    /* Color of the placeholder text when no rating */
  --rating-special-color: var(--warning-500);         /* Color of the rating stars */
  --rating-special-color-hover: var(--warning-600);   /* Color of the rating stars on hover */
  --rating-special-color-disabled: var(--warning-200); /* Color of the rating stars when disabled */
}
```

## Examples

### Stars Variant

```vue
<template>
  <VcRating
    v-model="rating"
    :max="5"
    variant="stars"
    label="Product Rating"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcRating } from '@vc-shell/framework';

const rating = ref(4);
</script>
```

### Star and Text Variant

```vue
<template>
  <VcRating
    v-model="rating"
    :max="5"
    variant="star-and-text"
    label="Product Rating"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcRating } from '@vc-shell/framework';

const rating = ref(3);
</script>
```

### Text Only Variant

```vue
<template>
  <VcRating
    v-model="rating"
    :max="5"
    variant="text"
    label="Text Rating"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcRating } from '@vc-shell/framework';

const rating = ref(5);
</script>
```

### With Tooltip

```vue
<template>
  <VcRating
    v-model="rating"
    :max="5"
    variant="stars"
    label="Rating with Tooltip"
    tooltip="This shows the product's average customer rating"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcRating } from '@vc-shell/framework';

const rating = ref(4);
</script>
```

### No Rating (Placeholder)

```vue
<template>
  <VcRating
    v-model="rating"
    :max="5"
    variant="stars"
    label="No Rating Available"
    placeholder="Not rated yet"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcRating } from '@vc-shell/framework';

const rating = ref(0);
</script>
```

### Custom Maximum Value

```vue
<template>
  <VcRating
    v-model="rating"
    :max="10"
    variant="star-and-text"
    label="10-Star Rating"
  />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcRating } from '@vc-shell/framework';

const rating = ref(8);
</script>
```

### With Custom Details Slot

```vue
<template>
  <VcRating
    v-model="rating"
    :max="5"
    variant="star-and-text"
    label="Product Rating"
  >
    <template #details>
      <span class="tw-ml-2 tw-text-sm tw-text-[var(--neutrals-500)]">
        (Based on {{ reviewCount }} reviews)
      </span>
    </template>
  </VcRating>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcRating } from '@vc-shell/framework';

const rating = ref(4);
const reviewCount = 42;
</script>
```

### Multiple Rating Display

```vue
<template>
  <div class="tw-space-y-4">
    <div v-for="(product, index) in products" :key="index" class="tw-p-4 tw-border tw-rounded">
      <h3 class="tw-text-lg tw-font-medium">{{ product.name }}</h3>
      <p class="tw-text-sm tw-mb-2 tw-text-[var(--neutrals-500)]">{{ product.description }}</p>
      
      <VcRating
        :model-value="product.rating"
        :max="5"
        variant="star-and-text"
      >
        <template #details>
          <span class="tw-ml-2 tw-text-sm tw-text-[var(--neutrals-500)]">
            ({{ product.reviewCount }} reviews)
          </span>
        </template>
      </VcRating>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { VcRating } from '@vc-shell/framework';

const products = [
  {
    name: 'Wireless Headphones',
    description: 'Noise-cancelling headphones with 30-hour battery life',
    rating: 4.5,
    reviewCount: 128
  },
  {
    name: 'Smartphone Stand',
    description: 'Adjustable aluminum stand for phones and tablets',
    rating: 3.7,
    reviewCount: 42
  },
  {
    name: 'USB-C Hub',
    description: '7-in-1 USB-C hub with HDMI, USB 3.0, and card readers',
    rating: 4.2,
    reviewCount: 89
  }
];
</script>
```

### Interactive Rating

```vue
<template>
  <div class="tw-space-y-4">
    <h3>Leave Your Rating</h3>
    
    <VcRating
      v-model="userRating"
      :max="5"
      variant="stars"
      label="Your Rating"
    />
    
    <VcTextarea
      v-model="reviewText"
      label="Your Review"
      placeholder="Write your review here..."
      rows="3"
    />
    
    <VcButton variant="primary" @click="submitReview">
      Submit Review
    </VcButton>
    
    <div v-if="submitted" class="tw-p-4 tw-bg-[var(--success-100)] tw-rounded">
      Thank you for your review! You rated this product {{ userRating }}/5 stars.
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcRating, VcTextarea, VcButton } from '@vc-shell/framework';

const userRating = ref(0);
const reviewText = ref('');
const submitted = ref(false);

const submitReview = () => {
  if (userRating.value > 0) {
    submitted.value = true;
    // Here you would typically send the review to your backend
    console.log('Review submitted:', { rating: userRating.value, text: reviewText.value });
  }
};
</script>
```
