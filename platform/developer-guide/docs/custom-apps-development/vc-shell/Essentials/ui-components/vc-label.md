# VcLabel Component

The `VcLabel` component is an atom used throughout the VC-Shell framework for displaying form field labels with support for additional features such as required indicators, tooltips, and language indicators for multilingual fields.

## Storybook

[VcLabel Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vclabel--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vclabel--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcLabel>Field Name</VcLabel>
</template>

<script lang="ts" setup>
import { VcLabel } from '@vc-shell/framework';
</script>
```

## Props

| Prop               | Type       | Default           | Description                                        |
| ------------------ | ---------- | ----------------- | -------------------------------------------------- |
| `required`         | `boolean`  | `false`           | Shows required field indicator (asterisk)          |
| `tooltipIcon`      | `string`   | `'material-info'` | Icon to use for the tooltip                        |
| `multilanguage`    | `boolean`  | `false`           | Shows language indicator for multilanguage fields  |
| `currentLanguage`  | `string`   | -                 | Current language code to display                   |
| `error`            | `boolean`  | `false`           | Shows the label in error state                     |

## Slots

| Slot       | Description                                        |
| ---------- | -------------------------------------------------- |
| `default`  | Main content of the label                          |
| `tooltip`  | Content to show in the tooltip                     |

## CSS Variables

The label component uses CSS variables for theming, which can be customized:

```css
:root {
  --label-required-color: var(--danger-500);    /* Color of the required field indicator (asterisk) */
  --label-tooltip-color: var(--info-400);       /* Color of the tooltip icon */
  --label-lang-color: var(--neutrals-500);      /* Color of the language indicator for multilingual fields */
  --label-error-color: var(--danger-500);       /* Color of the label when in error state */
}
```

## Examples

### Basic Label

```vue
<template>
  <VcLabel>Username</VcLabel>
</template>

<script lang="ts" setup>
import { VcLabel } from '@vc-shell/framework';
</script>
```

### Required Field Label

```vue
<template>
  <VcLabel required>Email Address</VcLabel>
</template>

<script lang="ts" setup>
import { VcLabel } from '@vc-shell/framework';
</script>
```

### Label with Tooltip

```vue
<template>
  <VcLabel>
    Password
    <template #tooltip>
      Password must be at least 8 characters long and include at least one number and one special character.
    </template>
  </VcLabel>
</template>

<script lang="ts" setup>
import { VcLabel } from '@vc-shell/framework';
</script>
```

### Label with Custom Tooltip Icon

```vue
<template>
  <VcLabel tooltipIcon="material-help">
    API Key
    <template #tooltip>
      The API key is used to authenticate your requests to the service.
    </template>
  </VcLabel>
</template>

<script lang="ts" setup>
import { VcLabel } from '@vc-shell/framework';
</script>
```

### Error State Label

```vue
<template>
  <VcLabel error>
    Email Address
    <template #tooltip>
      Please provide a valid email address.
    </template>
  </VcLabel>
</template>

<script lang="ts" setup>
import { VcLabel } from '@vc-shell/framework';
</script>
```

### Multilanguage Label

```vue
<template>
  <VcLabel 
    multilanguage 
    currentLanguage="EN"
  >
    Product Description
  </VcLabel>
</template>

<script lang="ts" setup>
import { VcLabel } from '@vc-shell/framework';
</script>
```

### Combined with Form Field

```vue
<template>
  <div class="tw-space-y-2">
    <VcLabel required>
      Full Name
      <template #tooltip>
        Please provide your full legal name as it appears on your ID.
      </template>
    </VcLabel>
    <input
      class="tw-border tw-border-[var(--neutrals-300)] tw-rounded tw-px-3 tw-py-2 tw-w-full"
      placeholder="Enter your full name"
    />
  </div>
</template>

<script lang="ts" setup>
import { VcLabel } from '@vc-shell/framework';
</script>
```

### Group of Form Fields with Labels

```vue
<template>
  <form class="tw-space-y-4">
    <div class="tw-space-y-2">
      <VcLabel required>First Name</VcLabel>
      <input
        class="tw-border tw-border-[var(--neutrals-300)] tw-rounded tw-px-3 tw-py-2 tw-w-full"
        placeholder="Enter first name"
      />
    </div>
    
    <div class="tw-space-y-2">
      <VcLabel required>Last Name</VcLabel>
      <input
        class="tw-border tw-border-[var(--neutrals-300)] tw-rounded tw-px-3 tw-py-2 tw-w-full"
        placeholder="Enter last name"
      />
    </div>
    
    <div class="tw-space-y-2">
      <VcLabel>
        Email
        <template #tooltip>
          We'll never share your email with anyone else.
        </template>
      </VcLabel>
      <input
        type="email"
        class="tw-border tw-border-[var(--neutrals-300)] tw-rounded tw-px-3 tw-py-2 tw-w-full"
        placeholder="Enter email"
      />
    </div>
  </form>
</template>

<script lang="ts" setup>
import { VcLabel } from '@vc-shell/framework';
</script>
```

