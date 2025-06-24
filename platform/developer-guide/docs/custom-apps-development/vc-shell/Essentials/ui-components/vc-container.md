# VcContainer Component

The `VcContainer` component is a versatile scrollable container atom that provides a consistent UI for handling scrollable content throughout the VC-Shell framework. It offers features like customizable scrolling behavior, pull-to-refresh functionality, and visual indicators for scrollable content.

## Storybook

[VcContainer Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vccontainer--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vccontainer--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <div class="tw-h-64 tw-w-full tw-border tw-rounded">
    <VcContainer :shadow="true">
      <p>This is scrollable content inside a container.</p>
      <p>The container will automatically handle overflow and scrolling.</p>
      <!-- More content -->
    </VcContainer>
  </div>
</template>

<script lang="ts" setup>
import { VcContainer } from '@vc-shell/framework';
</script>
```

## Props

| Prop        | Type      | Default  | Description                                           |
| ----------- | --------- | -------- | ----------------------------------------------------- |
| `shadow`    | `boolean` | `false`  | Whether to show shadows when content is scrollable    |
| `noPadding` | `boolean` | `false`  | Removes default padding from the container            |
| `usePtr`    | `boolean` | `false`  | Enables pull-to-refresh functionality for mobile      |

## Events

| Event        | Parameters    | Description                                     |
| ------------ | ------------- | ----------------------------------------------- |
| `scroll:ptr` | -             | Emitted when pull-to-refresh action is triggered |
| `scroll`     | `Event`       | Emitted when container is scrolled              |

## Exposed Methods

| Method       | Parameters    | Description                                     |
| ------------ | ------------- | ----------------------------------------------- |
| `scrollTop`  | -             | Scroll to the top of the container              |
| `component`  | -             | Reference to the inner container element        |

## CSS Variables

The container component uses CSS variables for theming, which can be customized:

```css
:root {
  --container-overscroll-icon-color: var(--secondary-600); /* Color of the pull-to-refresh indicator icon */
  --container-text-color: var(--neutrals-400);             /* Color of text within the container */
  --container-padding: 16px;                               /* Default internal padding for container content */
  --container-transition-duration: 0.3s;                   /* Duration of transition animations (like shadows) */
  --container-transition-ease: ease-out;                   /* Easing function for transitions */
  --container-shadow-color: var(--additional-950);         /* Base color for container shadows */
  --container-shadow-opacity: 0.1;                         /* Opacity of container shadows */
  --container-shadow: 0 3px 2px rgba(var(--container-shadow-color), var(--container-shadow-opacity)) inset; /* Shadow effect when content is scrollable */
}
```

## Examples

### Basic Container

```vue
<template>
  <div class="tw-h-64 tw-w-full tw-border tw-rounded">
    <VcContainer>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
      <p>Vivamus pellentesque tortor id lacus viverra, ut mollis libero auctor.</p>
      <p>Curabitur viverra, justo eu convallis pulvinar, dui nisi luctus quam.</p>
      <!-- Additional content -->
    </VcContainer>
  </div>
</template>

<script lang="ts" setup>
import { VcContainer } from '@vc-shell/framework';
</script>
```

### Container with Shadow

```vue
<template>
  <div class="tw-h-64 tw-w-full tw-border tw-rounded">
    <VcContainer :shadow="true">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
      <p>Vivamus pellentesque tortor id lacus viverra, ut mollis libero auctor.</p>
      <p>Curabitur viverra, justo eu convallis pulvinar, dui nisi luctus quam.</p>
      <!-- Additional content -->
    </VcContainer>
  </div>
</template>

<script lang="ts" setup>
import { VcContainer } from '@vc-shell/framework';
</script>
```

### Container without Padding

```vue
<template>
  <div class="tw-h-64 tw-w-full tw-border tw-rounded">
    <VcContainer :noPadding="true">
      <div class="tw-bg-[var(--neutrals-100)] tw-p-4">
        <h3 class="tw-mt-0">Edge-to-edge content</h3>
        <p>This content has no padding from the container, allowing it to extend all the way to the edges.</p>
      </div>
      <div class="tw-p-4">
        <p>Content can define its own padding as needed.</p>
      </div>
      <div class="tw-bg-[var(--neutrals-200)] tw-p-4">
        <p>Another section with a different background.</p>
      </div>
    </VcContainer>
  </div>
</template>

<script lang="ts" setup>
import { VcContainer } from '@vc-shell/framework';
</script>
```

### Container with Pull-to-Refresh

```vue
<template>
  <div class="tw-h-64 tw-w-full tw-border tw-rounded">
    <VcContainer 
      :usePtr="true" 
      :shadow="true"
      @scroll:ptr="refreshData"
    >
      <div class="tw-text-center tw-text-[var(--neutrals-600)] tw-py-4">
        ↓ Pull down to refresh (on mobile devices) ↓
      </div>
      <div v-for="(item, index) in items" :key="index" class="tw-p-2 tw-border-b tw-border-[var(--neutrals-200)]">
        {{ item }}
      </div>
    </VcContainer>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcContainer } from '@vc-shell/framework';

const items = ref(['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']);

function refreshData() {
  // Simulate data refresh
  setTimeout(() => {
    items.value = ['Refreshed Item 1', 'Refreshed Item 2', 'Refreshed Item 3',
      'Refreshed Item 4', 'Refreshed Item 5'];
  }, 1000);
}
</script>
```

### Content Panel

```vue
<template>
  <div class="tw-flex tw-flex-col tw-h-full tw-border tw-rounded">
    <div class="tw-bg-[var(--neutrals-100)] tw-p-4 tw-border-b tw-border-[var(--neutrals-200)]">
      <h2 class="tw-m-0 tw-text-xl">Content Panel</h2>
    </div>
    <VcContainer :shadow="true">
      <h3>Section heading</h3>
      <p>VcContainer is often used to create scrollable panels within a larger layout.</p>
      
      <div class="tw-bg-[var(--neutrals-100)] tw-border tw-border-[var(--neutrals-300)] tw-rounded tw-p-3 tw-my-4">
        <p class="tw-m-0"><strong>Note:</strong> This component handles overflow automatically.</p>
      </div>
      
      <h3>Another section</h3>
      <p>You can include various types of content including:</p>
      <ul class="tw-pl-5">
        <li>Lists like this one</li>
        <li>Images and other media</li>
        <li>Forms and interactive elements</li>
      </ul>
      
      <h3>Additional content</h3>
      <p>Add as much content as needed, and the container will handle scrolling.</p>
    </VcContainer>
  </div>
</template>

<script lang="ts" setup>
import { VcContainer } from '@vc-shell/framework';
</script>
```

### Accessing the Container

```vue
<template>
  <div class="tw-h-64 tw-w-full tw-border tw-rounded">
    <VcContainer ref="containerRef">
      <p v-for="n in 20" :key="n">
        Paragraph {{ n }}
      </p>
    </VcContainer>
    <button @click="scrollToTop" class="tw-mt-2 tw-px-4 tw-py-2 tw-bg-[var(--primary-500)] tw-text-white tw-rounded">
      Scroll to Top
    </button>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcContainer } from '@vc-shell/framework';

const containerRef = ref<InstanceType<typeof VcContainer>>();

function scrollToTop() {
  containerRef.value?.scrollTop();
}
</script>
```
