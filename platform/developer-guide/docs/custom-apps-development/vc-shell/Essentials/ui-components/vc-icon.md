# VcIcon Component

The `VcIcon` component is a versatile icon component that supports multiple icon libraries including Material Symbols, Bootstrap Icons, Lucide Icons, Font Awesome, and custom SVG icons.

## Storybook

[VcIcon Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vcicon--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vcicon--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <!-- Material Icon -->
  <VcIcon icon="material-home" />
  
  <!-- Bootstrap Icon -->
  <VcIcon icon="bi-house" />
  
  <!-- Lucide Icon -->
  <VcIcon icon="lucide-home" />
  
  <!-- Font Awesome Icon -->
  <VcIcon icon="fas fa-home" />
  
  <!-- Custom SVG Icon -->
  <VcIcon icon="svg:/assets/icons/home.svg" />
</template>

<script lang="ts" setup>
import { VcIcon } from '@vc-shell/framework';
</script>
```

## Props

| Prop          | Type                 | Default | Description                                                           |
| ------------- | -------------------- | ------- | --------------------------------------------------------------------- |
| `icon`        | `String\|Component`  | `"fas fa-square-full"` | The icon to display (string identifier or component)    |
| `size`        | `String`             | `"m"`   | Predefined size: "xs", "s", "m", "l", "xl", "xxl", "xxxl"            |
| `variant`     | `String`             | -       | Color variant: "warning", "danger", "success"                         |
| `useContainer`| `Boolean`            | `true`  | Whether to wrap the icon in a container for consistent spacing        |
| `customSize`  | `Number`             | -       | Custom size in pixels (overrides `size` prop)                         |
| `basePath`    | `String`             | `"/assets/icons"` | Base path for SVG icons (only for SVG icons)                |

## CSS Variables

The component uses CSS variables for consistent sizing and colors:

```css
:root {
  /* Icon sizes */
  --icon-size-xs: 12px;          /* Extra small icon size */
  --icon-size-s: 14px;           /* Small icon size */
  --icon-size-m: 18px;           /* Medium icon size (default) */
  --icon-size-l: 20px;           /* Large icon size */
  --icon-size-xl: 22px;          /* Extra large icon size */
  --icon-size-xxl: 30px;         /* Double extra large icon size */
  --icon-size-xxxl: 64px;        /* Triple extra large icon size */
  
  /* Variant colors */
  --icon-color-success: var(--success-500);  /* Success variant color (green) */
  --icon-color-danger: var(--danger-500);    /* Danger variant color (red) */
  --icon-color-warning: var(--warning-500);  /* Warning variant color (yellow) */
}
```

## Icon Sources

The `VcIcon` component automatically detects the icon library based on prefix:

### Material Symbols

```vue
<VcIcon icon="material-home" />
```

### Bootstrap Icons

```vue
<VcIcon icon="bi-house" />
```

### Lucide Icons

```vue
<VcIcon icon="lucide-home" />
```

### Font Awesome

```vue
<VcIcon icon="fas fa-home" />
```

### SVG Icons

```vue
<VcIcon icon="svg:/assets/icons/home.svg" />
```

### Custom Component

```vue
<template>
  <VcIcon :icon="HomeIcon" />
</template>

<script lang="ts" setup>
import { HomeIcon } from 'lucide-vue-next';
import { VcIcon } from '@vc-shell/framework';
</script>
```

## Sizing

The component provides predefined sizes that are consistent across all icon types:

```vue
<template>
  <VcIcon icon="material-home" size="xs" /> <!-- 12px -->
  <VcIcon icon="material-home" size="s" />  <!-- 14px -->
  <VcIcon icon="material-home" size="m" />  <!-- 18px (default) -->
  <VcIcon icon="material-home" size="l" />  <!-- 20px -->
  <VcIcon icon="material-home" size="xl" /> <!-- 22px -->
  <VcIcon icon="material-home" size="xxl" /> <!-- 30px -->
  <VcIcon icon="material-home" size="xxxl" /> <!-- 64px -->
  
  <!-- Custom size (in pixels) -->
  <VcIcon icon="material-home" :customSize="42" />
</template>
```

## Color Variants

Use the `variant` prop to apply predefined colors:

```vue
<template>
  <VcIcon icon="material-check_circle" variant="success" /> <!-- Success (green) -->
  <VcIcon icon="material-warning" variant="warning" /> <!-- Warning (yellow) -->
  <VcIcon icon="material-error" variant="danger" /> <!-- Danger (red) -->
</template>
```

## Using Container

By default, icons are wrapped in a container for consistent spacing. You can disable this with the `useContainer` prop:

```vue
<template>
  <!-- With container (default) -->
  <VcIcon icon="material-home" />
  
  <!-- Without container -->
  <VcIcon icon="material-home" :useContainer="false" />
</template>
```

## Styling Icons with CSS

The `VcIcon` component supports inheriting size from CSS styles:

```vue
<template>
  <!-- Setting size through parent element -->
  <div class="tw-text-2xl">
    <VcIcon icon="fas fa-star" />
  </div>

  <!-- Direct styling -->
  <VcIcon 
    icon="bi-heart" 
    class="tw-text-[40px] tw-text-[var(--danger-500)]"
  />
</template>
```

### Size Priority

The icon size is determined in the following order of priority:

1. `customSize` prop (highest priority)
2. External CSS styles (font-size applied to the icon)
3. Preset size via the `size` prop (lowest priority)

## SVG Icons

You can use SVG icons with the `svg:` prefix:

```vue
<template>
  <!-- Using path relative to basePath -->
  <VcIcon icon="svg:menu.svg" />
  
  <!-- Using absolute path -->
  <VcIcon icon="svg:/assets/icons/cart.svg" />
  
  <!-- With custom base path -->
  <VcIcon icon="svg:star.svg" basePath="/custom/icons/path" />
</template>
```

## Example: Integration with Buttons

```vue
<template>
  <VcButton>
    <VcIcon icon="material-save" class="tw-mr-2" />
    Save
  </VcButton>
</template>
```

## Example: Icon Button

```vue
<template>
  <button 
    class="tw-inline-flex tw-items-center tw-justify-center tw-p-2 tw-rounded-full tw-bg-[var(--primary-500)] tw-text-white"
    @click="handleClick"
  >
    <VcIcon 
      icon="material-add" 
      size="l" 
      :useContainer="false"
    />
  </button>
</template>

<script lang="ts" setup>
import { VcIcon } from '@vc-shell/framework';

function handleClick() {
  // Handle click event
}
</script>
```

## Example: Navigation with Icons

```vue
<template>
  <nav class="tw-flex tw-space-x-4">
    <a 
      v-for="item in navItems" 
      :key="item.path" 
      :href="item.path" 
      class="tw-flex tw-items-center tw-p-2 tw-text-[var(--neutrals-700)] hover:tw-text-[var(--primary-600)]"
    >
      <VcIcon :icon="item.icon" class="tw-mr-2" />
      {{ item.title }}
    </a>
  </nav>
</template>

<script lang="ts" setup>
import { VcIcon } from '@vc-shell/framework';

const navItems = [
  { title: 'Home', path: '/', icon: 'material-home' },
  { title: 'Search', path: '/search', icon: 'material-search' },
  { title: 'Settings', path: '/settings', icon: 'material-settings' },
  { title: 'Profile', path: '/profile', icon: 'material-person' },
];
</script>
```

