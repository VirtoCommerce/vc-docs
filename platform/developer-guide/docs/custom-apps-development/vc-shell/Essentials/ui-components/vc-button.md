# VcButton Component

The `VcButton` component is a versatile button component that supports various styles, sizes, and states. It's designed to be used as a primary interactive element throughout the application.

## Storybook

[VcButton Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vcbutton--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vcbutton--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcButton>Click Me</VcButton>
</template>

<script lang="ts" setup>
import { VcButton } from '@vc-shell/framework';
</script>
```

## Props

| Prop         | Type                          | Default     | Description                                                     |
| ------------ | ----------------------------- | ----------- | --------------------------------------------------------------- |
| `variant`    | `'primary'` \| `'secondary'`  | `'primary'` | The visual style of the button                                  |
| `icon`       | `String` \| `Component`       | -           | Icon to display within the button                               |
| `iconClass`  | `String`                      | -           | Custom CSS class for the icon                                   |
| `iconSize`   | `String` \| `Number`          | `'s'`       | Size of the icon                                                |
| `disabled`   | `Boolean`                     | `false`     | Whether the button is disabled                                  |
| `size`       | `'xs'` \| `'sm'` \| `'base'`  | `'base'`    | Size of the button                                              |
| `selected`   | `Boolean`                     | `false`     | Whether the button is in a selected state                       |
| `text`       | `Boolean`                     | `false`     | Whether the button should be rendered as text without borders   |
| `small`      | `Boolean`                     | -           | **Deprecated:** Use `size="sm"` instead                         |
| `outline`    | `Boolean`                     | -           | **Deprecated:** Use `variant="secondary"` instead               |
| `raised`     | `Boolean`                     | -           | **Deprecated:** Use custom CSS or variant combinations instead  |

## Events

| Event    | Parameters              | Description                             |
| -------- | ----------------------- | --------------------------------------- |
| `click`  | `(event: Event) => void`| Emitted when the button is clicked      |

## Slots

| Slot        | Description                                      |
| ----------- | ------------------------------------------------ |
| `default`   | Content to display inside the button             |

## CSS Variables

The button component uses CSS variables for theming, which can be customized:

### Primary Variant Variables
```css
--button-primary-background-color: var(--primary-500);       /* Background color of primary button in default state */
--button-primary-background-color-hover: var(--primary-600); /* Background color of primary button on hover state */
--button-primary-background-color-disabled: var(--primary-300); /* Background color of primary button when disabled */
--button-primary-text-color: var(--additional-50);           /* Text color of primary button in default state */
--button-primary-text-color-disabled: var(--additional-50);  /* Text color of primary button when disabled */
--button-primary-border-color: var(--primary-500);           /* Border color of primary button in default state */
--button-primary-border-color-hover: var(--primary-600);     /* Border color of primary button on hover state */
--button-primary-border-color-disabled: var(--primary-300);  /* Border color of primary button when disabled */
```

### Secondary Variant Variables
```css
--button-secondary-background-color: var(--additional-50);   /* Background color of secondary button in default state */
--button-secondary-background-color-hover: var(--primary-100); /* Background color of secondary button on hover state */
--button-secondary-background-color-disabled: var(--additional-50); /* Background color of secondary button when disabled */
--button-secondary-text-color: var(--neutrals-700);          /* Text color of secondary button in default state */
--button-secondary-text-color-disabled: var(--neutrals-400); /* Text color of secondary button when disabled */
--button-secondary-border-color: var(--secondary-300);       /* Border color of secondary button in default state */
--button-secondary-border-color-hover: var(--secondary-400); /* Border color of secondary button on hover state */
--button-secondary-border-color-disabled: var(--secondary-300); /* Border color of secondary button when disabled */
```

### Size and Shape Variables
```css
--button-border-radius: 4px;                /* Border radius of all button variants */
--button-padding-hor: 14px;                 /* Horizontal padding for base size buttons */
--button-padding-vert: 10px;                /* Vertical padding for base size buttons */
--button-padding-hor-small: 12px;           /* Horizontal padding for small size buttons */
--button-padding-vert-small: 8px;           /* Vertical padding for small size buttons */
--button-padding-vert-extra-small: 5px;     /* Vertical padding for extra small size buttons */
--button-padding-hor-extra-small: 12px;     /* Horizontal padding for extra small size buttons */
--button-height: 36px;                      /* Fixed height for base size buttons */
--button-height-small: 28px;                /* Fixed height for small size buttons */
--button-height-extra-small: 22px;          /* Fixed height for extra small size buttons */
```



## Examples

### Primary Button

```vue
<template>
  <VcButton variant="primary">Primary Button</VcButton>
</template>
```

### Secondary Button

```vue
<template>
  <VcButton variant="secondary">Secondary Button</VcButton>
</template>
```

### Button with Icon

```vue
<template>
  <VcButton icon="check">With Icon</VcButton>
</template>
```

### Icon-only Button

```vue
<template>
  <VcButton icon="plus" />
</template>
```

### Different Sizes

```vue
<template>
  <div class="tw-flex tw-space-x-2 tw-items-center">
    <VcButton size="xs">Extra Small</VcButton>
    <VcButton size="sm">Small</VcButton>
    <VcButton size="base">Base</VcButton>
  </div>
</template>
```

### Text Button

```vue
<template>
  <VcButton text>Text Button</VcButton>
</template>
```

### Disabled Button

```vue
<template>
  <VcButton disabled>Disabled Button</VcButton>
</template>
```

### Selected Button

```vue
<template>
  <VcButton selected>Selected Button</VcButton>
</template>
```

### Handling Click Events

```vue
<template>
  <VcButton @click="handleClick">Click Me</VcButton>
</template>

<script lang="ts" setup>
import { VcButton } from '@vc-shell/framework';

function handleClick(event: Event) {
  console.log('Button clicked', event);
  // Handle the click event
}
</script>
```

### Button in a Form

```vue
<template>
  <form @submit.prevent="submitForm">
    <VcInput v-model="name" label="Name" />
    <VcButton type="submit" class="tw-mt-4">Submit</VcButton>
  </form>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcButton, VcInput } from '@vc-shell/framework';

const name = ref('');

function submitForm() {
  console.log('Form submitted with name:', name.value);
  // Handle form submission
}
</script>
```

### Button Group

```vue
<template>
  <div class="button-group">
    <VcButton 
      variant="secondary" 
      :selected="selectedTab === 'tab1'" 
      @click="selectedTab = 'tab1'"
    >
      Tab 1
    </VcButton>
    <VcButton 
      variant="secondary" 
      :selected="selectedTab === 'tab2'" 
      @click="selectedTab = 'tab2'"
    >
      Tab 2
    </VcButton>
    <VcButton 
      variant="secondary" 
      :selected="selectedTab === 'tab3'" 
      @click="selectedTab = 'tab3'"
    >
      Tab 3
    </VcButton>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcButton } from '@vc-shell/framework';

const selectedTab = ref('tab1');
</script>

<style scoped>
.button-group {
  @apply tw-flex tw-border tw-border-[var(--secondary-300)] tw-rounded-[var(--button-border-radius)] tw-overflow-hidden;
}

.button-group .vc-button {
  @apply tw-border-none tw-rounded-none;
}

.button-group .vc-button:not(:last-child) {
  @apply tw-border-r tw-border-r-[var(--secondary-300)];
}
</style>
```