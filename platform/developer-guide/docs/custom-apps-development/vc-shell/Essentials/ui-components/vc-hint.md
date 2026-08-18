# VcHint Component

The `VcHint` component is a simple atom used to display supplementary information or guidance text throughout the VC-Shell framework. It provides consistent styling for secondary text that guides users with additional context, instructions, or notes.

## Storybook

[VcHint Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vchint--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vchint--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcHint>This is a helpful hint for the user.</VcHint>
</template>

<script lang="ts" setup>
import { VcHint } from '@vc-shell/framework';
</script>
```

## Slots

| Slot      | Description                                          |
| --------- | ---------------------------------------------------- |
| `default` | Content to display inside the hint                   |

## CSS Variables

The hint component uses CSS variables for theming, which can be customized:

```css
:root {
  --hint-color: var(--neutrals-500);    /* Text color for hint content */
  --hint-font-size: 12px;               /* Font size for hint text */
}
```



## Examples

### Basic Hint

```vue
<template>
  <VcHint>This field is optional.</VcHint>
</template>

<script lang="ts" setup>
import { VcHint } from '@vc-shell/framework';
</script>
```

### Hint with Rich Text Content

```vue
<template>
  <VcHint>
    This field is optional. Learn more in our
    <a href="#" class="tw-text-[var(--primary-500)] tw-underline">documentation</a>.
  </VcHint>
</template>

<script lang="ts" setup>
import { VcHint } from '@vc-shell/framework';
</script>
```

### Multiple Hints for Requirements

```vue
<template>
  <div>
    <div class="tw-font-medium tw-mb-1">Password requirements:</div>
    <VcHint>• Must be at least 8 characters long</VcHint>
    <VcHint>• Must include at least one number</VcHint>
    <VcHint>• Must include at least one special character</VcHint>
  </div>
</template>

<script lang="ts" setup>
import { VcHint } from '@vc-shell/framework';
</script>
```

### File Upload Instructions

```vue
<template>
  <div>
    <div class="tw-font-medium tw-mb-1">File upload:</div>
    <VcHint>Maximum file size: 5MB</VcHint>
    <VcHint>Supported formats: JPG, PNG, PDF</VcHint>
  </div>
</template>

<script lang="ts" setup>
import { VcHint } from '@vc-shell/framework';
</script>
```

### Hint with Warning

```vue
<template>
  <VcHint class="tw-flex tw-items-center">
    <span class="tw-text-[var(--warning-500)] tw-mr-1">⚠️</span>
    This action cannot be undone.
  </VcHint>
</template>

<script lang="ts" setup>
import { VcHint } from '@vc-shell/framework';
</script>
```

### Customized Hint

```vue
<template>
  <VcHint class="tw-italic tw-text-[var(--info-500)]">
    Pro tip: You can use keyboard shortcuts for faster navigation.
  </VcHint>
</template>

<script lang="ts" setup>
import { VcHint } from '@vc-shell/framework';
</script>
```

