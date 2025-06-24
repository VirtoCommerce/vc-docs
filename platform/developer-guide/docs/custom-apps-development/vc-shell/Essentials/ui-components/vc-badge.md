# VcBadge Component

The `VcBadge` component is used to display short pieces of information such as notification counts, status indicators, or labels. It's typically displayed as a small circle or pill with text or as a dot.

## Storybook

[VcBadge Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vcbadge--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vcbadge--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcBadge content="5">
    <VcIcon icon="bell" />
  </VcBadge>
</template>

<script lang="ts" setup>
import { VcBadge, VcIcon } from '@vc-shell/framework';
</script>
```

## Props

| Prop              | Type                                                             | Default    | Description                                                   |
| ----------------- | ---------------------------------------------------------------- | ---------- | ------------------------------------------------------------- |
| `content`         | `String` \| `Number`                                             | -          | Content to display inside the badge                           |
| `variant`         | `'primary'` \| `'success'` \| `'warning'` \| `'danger'` \| `'info'` \| `'secondary'` | `'primary'` | The color variant of the badge                                |
| `size`            | `'s'` \| `'m'`                                                   | `'m'`      | Size of the badge                                             |
| `isDot`           | `Boolean`                                                         | `false`    | Whether to display the badge as a dot without text            |
| `active`          | `Boolean`                                                         | `false`    | Whether the badge is in an active state                       |
| `disabled`        | `Boolean`                                                         | `false`    | Whether the badge is disabled                                 |
| `clickable`       | `Boolean`                                                         | `false`    | Whether the badge is clickable                                |
| `customPosition`  | `Boolean`                                                         | `false`    | Whether to use custom positioning for the badge               |
| `top`             | `String`                                                          | -          | Custom top position when `customPosition` is `true`           |
| `right`           | `String`                                                          | -          | Custom right position when `customPosition` is `true`         |

## Events

| Event     | Parameters                | Description                             |
| --------- | ------------------------- | --------------------------------------- |
| `click`   | -                         | Emitted when a clickable badge is clicked |

## Slots

| Slot        | Description                                      |
| ----------- | ------------------------------------------------ |
| `default`   | Content that the badge will be attached to       |

## CSS Variables

The badge component uses CSS variables for theming, which can be customized:

```css
:root {
  /* Default state colors */
  --badge-background-color: var(--accent-500);        /* Default background color for badges */
  --badge-text-color: var(--additional-50);           /* Default text color for badges */
  --badge-border-color: var(--additional-50);         /* Default border color for badges */

  /* Hover state colors */
  --badge-background-color-hover: var(--neutrals-200);  /* Background color when hovering over clickable badges */
  --badge-text-color-hover: var(--neutrals-800);        /* Text color when hovering over clickable badges */
  --badge-border-color-hover: var(--primary-300);       /* Border color when hovering over clickable badges */

  /* Active state colors */
  --badge-background-color-active: var(--neutrals-200);  /* Background color for active badges */
  --badge-text-color-active: var(--neutrals-800);        /* Text color for active badges */
  --badge-border-color-active: var(--primary-300);       /* Border color for active badges */

  /* Disabled state colors */
  --badge-background-color-disabled: var(--neutrals-300);  /* Background color for disabled badges */
  --badge-text-color-disabled: var(--neutrals-500);        /* Text color for disabled badges */
  --badge-border-color-disabled: var(--primary-200);       /* Border color for disabled badges */

  /* Variant background colors */
  --badge-background-color-primary: var(--primary-500);    /* Background color for primary variant */
  --badge-background-color-secondary: var(--secondary-500); /* Background color for secondary variant */
  --badge-background-color-success: var(--success-500);    /* Background color for success variant */
  --badge-background-color-warning: var(--warning-500);    /* Background color for warning variant */
  --badge-background-color-danger: var(--danger-500);      /* Background color for danger variant */
  --badge-background-color-info: var(--info-500);          /* Background color for info variant */

  /* Size dimensions */
  --badge-size-small: 17px;                        /* Height and minimum width of small badges */
  --badge-size-medium: 20px;                       /* Height and minimum width of medium badges */

  /* Positioning offset values */
  --badge-distance-top-small: -8px;                /* Top offset for small badges */
  --badge-distance-right-small: -10px;             /* Right offset for small badges */
  --badge-distance-top-medium: -8px;               /* Top offset for medium badges */
  --badge-distance-right-medium: -10px;            /* Right offset for medium badges */

  /* Visual properties */
  --badge-border-radius: 9999px;                   /* Border radius for badges (full rounded) */
  --badge-dot-size-small: 8px;                     /* Size of small dot badge */
  --badge-dot-size-medium: 10px;                   /* Size of medium dot badge */
}
```

## Examples

### Basic Badge

```vue
<template>
  <VcBadge content="5">
    <VcIcon icon="bell" size="1.5rem" />
  </VcBadge>
</template>
```

### Badge Variants

```vue
<template>
  <div class="tw-flex tw-space-x-6">
    <VcBadge content="1" variant="primary">
      <VcIcon icon="inbox" />
    </VcBadge>
    <VcBadge content="2" variant="secondary">
      <VcIcon icon="inbox" />
    </VcBadge>
    <VcBadge content="3" variant="success">
      <VcIcon icon="inbox" />
    </VcBadge>
    <VcBadge content="4" variant="warning">
      <VcIcon icon="inbox" />
    </VcBadge>
    <VcBadge content="5" variant="danger">
      <VcIcon icon="inbox" />
    </VcBadge>
    <VcBadge content="6" variant="info">
      <VcIcon icon="inbox" />
    </VcBadge>
  </div>
</template>
```

### Dot Badge

```vue
<template>
  <div class="tw-flex tw-space-x-6">
    <VcBadge isDot variant="primary">
      <VcIcon icon="bell" />
    </VcBadge>
    <VcBadge isDot variant="success">
      <VcIcon icon="check-circle" />
    </VcBadge>
    <VcBadge isDot variant="warning">
      <VcIcon icon="alert-triangle" />
    </VcBadge>
    <VcBadge isDot variant="danger">
      <VcIcon icon="x-circle" />
    </VcBadge>
  </div>
</template>
```

### Different Sizes

```vue
<template>
  <div class="tw-flex tw-space-x-6 tw-items-center">
    <VcBadge content="99+" size="s">
      <VcIcon icon="inbox" />
    </VcBadge>
    <VcBadge content="99+" size="m">
      <VcIcon icon="inbox" size="1.5rem" />
    </VcBadge>
  </div>
</template>
```

### Clickable Badge

```vue
<template>
  <VcBadge content="5" clickable @click="handleClick">
    <VcIcon icon="bell" />
  </VcBadge>
</template>

<script lang="ts" setup>
import { VcBadge, VcIcon } from '@vc-shell/framework';

function handleClick() {
  console.log('Badge clicked');
  // Handle the click event
}
</script>
```

### Custom Positioning

```vue
<template>
  <VcBadge content="New" customPosition top="-5px" right="-15px">
    <VcButton>Feature</VcButton>
  </VcBadge>
</template>
```

### Active Badge

```vue
<template>
  <VcBadge content="3" active>
    <VcIcon icon="message-circle" />
  </VcBadge>
</template>
```

### Disabled Badge

```vue
<template>
  <VcBadge content="Unavailable" disabled>
    <VcIcon icon="x-circle" />
  </VcBadge>
</template>
```

### Badge with Long Text

```vue
<template>
  <VcBadge content="999+">
    <VcIcon icon="bell" />
  </VcBadge>
</template>
```

### Badge on Custom Elements

```vue
<template>
  <VcBadge content="3" variant="danger">
    <div class="tw-p-4 tw-bg-[var(--neutrals-100)] tw-rounded">
      <h3 class="tw-text-base tw-font-semibold">Notifications</h3>
      <p class="tw-text-sm">You have unread messages</p>
    </div>
  </VcBadge>
</template>
```

### Badge in Navigation

```vue
<template>
  <nav class="tw-flex tw-space-x-6">
    <div v-for="item in navItems" :key="item.id" class="tw-relative">
      <VcBadge 
        v-if="item.count && item.count > 0" 
        :content="item.count > 99 ? '99+' : item.count" 
        :variant="item.badgeVariant || 'primary'"
      >
        <a href="#" class="tw-flex tw-items-center tw-px-4 tw-py-2">
          <VcIcon :icon="item.icon" class="tw-mr-2" />
          {{ item.title }}
        </a>
      </VcBadge>
      <a 
        v-else 
        href="#" 
        class="tw-flex tw-items-center tw-px-4 tw-py-2"
      >
        <VcIcon :icon="item.icon" class="tw-mr-2" />
        {{ item.title }}
      </a>
    </div>
  </nav>
</template>

<script lang="ts" setup>
import { VcBadge, VcIcon } from '@vc-shell/framework';

const navItems = [
  { id: 1, title: 'Home', icon: 'home', count: 0 },
  { id: 2, title: 'Messages', icon: 'message-circle', count: 5, badgeVariant: 'primary' },
  { id: 3, title: 'Notifications', icon: 'bell', count: 12, badgeVariant: 'danger' },
  { id: 4, title: 'Settings', icon: 'settings', count: 0 },
];
</script>
```
