# VcLink Component

The `VcLink` component is an atom used throughout the VC-Shell framework for displaying clickable links with support for various states such as active and disabled.

## Storybook

[VcLink Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vclink--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vclink--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcLink @click="handleClick">Click me</VcLink>
</template>

<script lang="ts" setup>
import { VcLink } from '@vc-shell/framework';

function handleClick() {
  console.log('Link clicked');
}
</script>
```

## Props

| Prop       | Type        | Default | Description                                     |
| ---------- | ----------- | ------- | ----------------------------------------------- |
| `active`   | `boolean`   | `false` | Sets the link to active state                   |
| `disabled` | `boolean`   | `false` | Disables the link, making it not clickable      |
| `onClick`  | `Function`  | -       | Function to call when the link is clicked       |

## Events

| Event    | Parameters | Description                                            |
| -------- | ---------- | ------------------------------------------------------ |
| `click`  | -          | Emitted when the link is clicked (if not disabled)     |

## Slots

| Slot       | Description                                 |
| ---------- | ------------------------------------------- |
| `default`  | Content of the link                         |

## CSS Variables

The link component uses CSS variables for theming, which can be customized:

```css
:root {
  --link-text-color: var(--primary-500);          /* Default text color for links */
  --link-text-color-hover: var(--primary-400);    /* Text color for links on hover */
  --link-text-color-active: var(--primary-700);   /* Text color for active links */
  --link-text-color-disabled: var(--neutrals-300); /* Text color for disabled links */
}
```

## Examples

### Basic Link

```vue
<template>
  <VcLink @click="handleClick">Click me</VcLink>
</template>

<script lang="ts" setup>
import { VcLink } from '@vc-shell/framework';

function handleClick() {
  console.log('Link clicked');
}
</script>
```

### Active Link

```vue
<template>
  <VcLink :active="true">Active link</VcLink>
</template>

<script lang="ts" setup>
import { VcLink } from '@vc-shell/framework';
</script>
```

### Disabled Link

```vue
<template>
  <VcLink :disabled="true">Disabled link</VcLink>
</template>

<script lang="ts" setup>
import { VcLink } from '@vc-shell/framework';
</script>
```

### Links in Navigation Context

```vue
<template>
  <div class="tw-flex tw-gap-4">
    <VcLink :active="true">Home</VcLink>
    <VcLink>Products</VcLink>
    <VcLink>Services</VcLink>
    <VcLink :disabled="true">Admin</VcLink>
  </div>
</template>

<script lang="ts" setup>
import { VcLink } from '@vc-shell/framework';
</script>
```

### Link with Conditional Active State

```vue
<template>
  <VcLink :active="isCurrentRoute">Current Page</VcLink>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcLink } from '@vc-shell/framework';

const isCurrentRoute = ref(true);
</script>
```

### Link with Icon

```vue
<template>
  <VcLink>
    <div class="tw-flex tw-items-center tw-gap-2">
      <VcIcon icon="material-open-in-new" />
      <span>External Link</span>
    </div>
  </VcLink>
</template>

<script lang="ts" setup>
import { VcLink, VcIcon } from '@vc-shell/framework';
</script>
```

### Using with Router

```vue
<template>
  <VcLink @click="navigateToHome">Go to Home</VcLink>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router';
import { VcLink } from '@vc-shell/framework';

const router = useRouter();

function navigateToHome() {
  router.push('/');
}
</script>
```
