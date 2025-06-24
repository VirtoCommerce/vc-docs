# VcSkeleton Component

The `VcSkeleton` component is an atom used throughout the VC-Shell framework for displaying loading placeholders for content. It improves user experience by showing preliminary placeholders where content is loading, reducing perceived loading times.

## Storybook

[VcSkeleton Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vcskeleton--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vcskeleton--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcSkeleton :rows="3" animated />
</template>

<script lang="ts" setup>
import { VcSkeleton } from '@vc-shell/framework';
</script>
```

## Props

| Prop       | Type      | Default | Description                                  |
| ---------- | --------- | ------- | -------------------------------------------- |
| `rows`     | `number`  | `1`     | Number of skeleton rows to display           |
| `animated` | `boolean` | `false` | Enables pulse animation on skeleton elements |



## Examples

### Basic Skeleton

```vue
<template>
  <VcSkeleton />
</template>

<script lang="ts" setup>
import { VcSkeleton } from '@vc-shell/framework';
</script>
```

### Animated Skeleton

```vue
<template>
  <VcSkeleton animated />
</template>

<script lang="ts" setup>
import { VcSkeleton } from '@vc-shell/framework';
</script>
```

### Multiple Rows

```vue
<template>
  <VcSkeleton :rows="5" animated />
</template>

<script lang="ts" setup>
import { VcSkeleton } from '@vc-shell/framework';
</script>
```

### Card Loading Skeleton

```vue
<template>
  <div class="tw-border tw-rounded-lg tw-overflow-hidden tw-shadow-sm">
    <!-- Image placeholder -->
    <div class="tw-h-[200px] tw-bg-[color:var(--neutrals-200)]"></div>
    <div class="tw-p-4">
      <!-- Title placeholder -->
      <div class="tw-h-5 tw-bg-[color:var(--neutrals-200)] tw-rounded tw-w-3/5 tw-mb-2"></div>
      <!-- Content placeholder -->
      <VcSkeleton :rows="3" animated />
      <!-- Buttons placeholder -->
      <div class="tw-flex tw-gap-2 tw-mt-4">
        <div class="tw-h-8 tw-w-20 tw-bg-[color:var(--neutrals-200)] tw-rounded-md"></div>
        <div class="tw-h-8 tw-w-20 tw-bg-[color:var(--neutrals-200)] tw-rounded-md"></div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { VcSkeleton } from '@vc-shell/framework';
</script>
```

### User List Loading Skeleton

```vue
<template>
  <div class="tw-space-y-4">
    <div v-for="i in 3" :key="i" class="tw-flex tw-gap-4 tw-items-center">
      <!-- Avatar placeholder -->
      <div class="tw-w-12 tw-h-12 tw-bg-[color:var(--neutrals-200)] tw-rounded-full"></div>
      <div class="tw-flex-1">
        <!-- Username placeholder -->
        <div class="tw-h-4 tw-bg-[color:var(--neutrals-200)] tw-rounded tw-w-2/5 tw-mb-2"></div>
        <!-- Description placeholder -->
        <VcSkeleton :rows="1" animated />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { VcSkeleton } from '@vc-shell/framework';
</script>
```

### Product Grid Loading Skeleton

```vue
<template>
  <div class="tw-grid tw-grid-cols-1 md:tw-grid-cols-3 tw-gap-6">
    <div v-for="i in 6" :key="i" class="tw-border tw-rounded-lg tw-overflow-hidden tw-p-4">
      <!-- Product image placeholder -->
      <div class="tw-h-40 tw-bg-[color:var(--neutrals-200)] tw-rounded-md tw-mb-4"></div>
      <!-- Product title placeholder -->
      <div class="tw-h-5 tw-bg-[color:var(--neutrals-200)] tw-rounded tw-w-4/5 tw-mb-2"></div>
      <!-- Product description placeholder -->
      <VcSkeleton :rows="2" animated />
      <!-- Price placeholder -->
      <div class="tw-h-6 tw-bg-[color:var(--neutrals-200)] tw-rounded tw-w-1/4 tw-mt-3"></div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { VcSkeleton } from '@vc-shell/framework';
</script>
```

### Form Loading Skeleton

```vue
<template>
  <div class="tw-space-y-6 tw-max-w-lg">
    <div v-for="i in 4" :key="i" class="tw-space-y-2">
      <!-- Field label placeholder -->
      <div class="tw-h-4 tw-bg-[color:var(--neutrals-200)] tw-rounded tw-w-1/4"></div>
      <!-- Field input placeholder -->
      <div class="tw-h-10 tw-bg-[color:var(--neutrals-200)] tw-rounded tw-w-full"></div>
    </div>
    <!-- Submit button placeholder -->
    <div class="tw-h-10 tw-bg-[color:var(--neutrals-200)] tw-rounded tw-w-1/3 tw-mt-4"></div>
  </div>
</template>

<script lang="ts" setup>
import { VcSkeleton } from '@vc-shell/framework';
</script>
```

### Table Loading Skeleton

```vue
<template>
  <div class="tw-border tw-rounded-lg tw-overflow-hidden">
    <!-- Table header -->
    <div class="tw-flex tw-p-3 tw-bg-[color:var(--neutrals-100)]">
      <div class="tw-w-1/4 tw-h-6 tw-bg-[color:var(--neutrals-200)] tw-rounded tw-mr-2"></div>
      <div class="tw-w-1/4 tw-h-6 tw-bg-[color:var(--neutrals-200)] tw-rounded tw-mr-2"></div>
      <div class="tw-w-1/4 tw-h-6 tw-bg-[color:var(--neutrals-200)] tw-rounded tw-mr-2"></div>
      <div class="tw-w-1/4 tw-h-6 tw-bg-[color:var(--neutrals-200)] tw-rounded"></div>
    </div>
    
    <!-- Table rows -->
    <div v-for="i in 5" :key="i" class="tw-flex tw-p-3 tw-border-t">
      <div class="tw-w-1/4 tw-mr-2"><VcSkeleton animated /></div>
      <div class="tw-w-1/4 tw-mr-2"><VcSkeleton animated /></div>
      <div class="tw-w-1/4 tw-mr-2"><VcSkeleton animated /></div>
      <div class="tw-w-1/4"><VcSkeleton animated /></div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { VcSkeleton } from '@vc-shell/framework';
</script>
```
