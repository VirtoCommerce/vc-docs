# VcWidget Component

The `VcWidget` component is an atom used throughout the VC-Shell framework for creating clickable widgets with an icon, title, and optional badge. It's commonly used in dashboards, sidebars, and navigation elements.

## Storybook

[VcWidget Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vcwidget--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vcwidget--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcWidget 
    icon="material-save" 
    title="Saved" 
    :value="12" 
    @click="handleWidgetClick" 
  />
</template>

<script lang="ts" setup>
import { VcWidget } from '@vc-shell/framework';

function handleWidgetClick() {
  console.log('Widget clicked');
}
</script>
```

## Props

| Prop         | Type                | Default     | Description                                       |
| ------------ | ------------------- | ----------- | ------------------------------------------------- |
| `icon`       | `string`            | `undefined` | Icon to display in the widget                     |
| `title`      | `string`            | `undefined` | Title text displayed below the icon               |
| `value`      | `string \| number`  | `undefined` | Value to display as a badge count (truncated at 99+) |
| `disabled`   | `boolean`           | `false`     | Whether the widget is disabled                    |
| `isExpanded` | `boolean`           | `false`     | Whether the widget is expanded                    |
| `horizontal` | `boolean`           | `false`     | Whether to arrange the widget horizontally        |

## Events

| Event    | Payload | Description                                           |
| -------- | ------- | ----------------------------------------------------- |
| `click`  | -       | Emitted when the widget is clicked (if not disabled)  |

## CSS Variables

The widget component uses CSS variables for theming, which can be customized:

```css
:root {
  --widget-bg-color: transparent;                /* Background color for the widget */
  --widget-bg-hover-color: transparent;          /* Background color when hovering over the widget */
  --widget-icon-color: var(--neutrals-700);      /* Default color for the widget icon */
  --widget-icon-hover-color: var(--primary-600); /* Icon color when hovering over the widget */
  --widget-icon-disabled-color: var(--neutrals-400); /* Icon color when the widget is disabled */
  --widget-title-color: var(--neutrals-600);     /* Default color for the widget title */
  --widget-title-hover-color: var(--primary-600); /* Title color when hovering over the widget */
  --widget-title-disabled-color: var(--neutrals-400); /* Title color when the widget is disabled */
}
```

## Examples

### Basic Widget

```vue
<template>
  <VcWidget 
    icon="material-save" 
    title="Saved" 
    :value="12" 
    @click="handleWidgetClick" 
  />
</template>

<script lang="ts" setup>
import { VcWidget } from '@vc-shell/framework';

function handleWidgetClick() {
  console.log('Widget clicked');
}
</script>
```

### Horizontal Widget

```vue
<template>
  <VcWidget 
    icon="material-home" 
    title="Dashboard" 
    :horizontal="true" 
    @click="handleWidgetClick" 
  />
</template>

<script lang="ts" setup>
import { VcWidget } from '@vc-shell/framework';

function handleWidgetClick() {
  console.log('Widget clicked');
}
</script>
```

### Disabled Widget

```vue
<template>
  <VcWidget 
    icon="material-lock" 
    title="Locked" 
    :disabled="true" 
  />
</template>

<script lang="ts" setup>
import { VcWidget } from '@vc-shell/framework';
</script>
```

### Widget with Large Badge Count

```vue
<template>
  <VcWidget 
    icon="material-notifications" 
    title="Notifications" 
    :value="120" 
    @click="handleWidgetClick" 
  />
</template>

<script lang="ts" setup>
import { VcWidget } from '@vc-shell/framework';

function handleWidgetClick() {
  console.log('Widget clicked');
}
</script>
```

### Expanded Widget

```vue
<template>
  <VcWidget 
    icon="material-menu" 
    title="Menu" 
    :isExpanded="true" 
    @click="handleWidgetClick" 
  />
</template>

<script lang="ts" setup>
import { VcWidget } from '@vc-shell/framework';

function handleWidgetClick() {
  console.log('Widget clicked');
}
</script>
```

### Multiple Widgets in a Group

```vue
<template>
  <div class="tw-flex tw-gap-4 tw-p-4 tw-bg-[color:var(--neutrals-100)] tw-rounded">
    <VcWidget 
      v-for="widget in widgets" 
      :key="widget.id"
      :icon="widget.icon" 
      :title="widget.title" 
      :value="widget.value" 
      :disabled="widget.disabled"
      @click="() => handleWidgetClick(widget)" 
    />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcWidget } from '@vc-shell/framework';

const widgets = ref([
  { id: 1, icon: 'material-dashboard', title: 'Dashboard', value: null, disabled: false },
  { id: 2, icon: 'material-shopping_cart', title: 'Orders', value: 5, disabled: false },
  { id: 3, icon: 'material-inventory', title: 'Products', value: null, disabled: false },
  { id: 4, icon: 'material-people', title: 'Customers', value: 18, disabled: false },
  { id: 5, icon: 'material-settings', title: 'Settings', value: null, disabled: true }
]);

function handleWidgetClick(widget) {
  console.log(`Widget clicked: ${widget.title}`);
}
</script>
```

### Widget Navigation Menu

```vue
<template>
  <div class="tw-flex tw-flex-col tw-gap-2 tw-p-2 tw-bg-[color:var(--neutrals-100)] tw-w-24">
    <VcWidget 
      v-for="item in navItems" 
      :key="item.id"
      :icon="item.icon" 
      :title="item.title" 
      :value="item.count" 
      :isExpanded="activeItem === item.id"
      @click="() => setActiveItem(item.id)" 
    />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcWidget } from '@vc-shell/framework';

const activeItem = ref(1);

const navItems = [
  { id: 1, icon: 'material-home', title: 'Home', count: null },
  { id: 2, icon: 'material-inbox', title: 'Inbox', count: 12 },
  { id: 3, icon: 'material-favorite', title: 'Favorites', count: 5 },
  { id: 4, icon: 'material-folder', title: 'Files', count: null },
  { id: 5, icon: 'material-settings', title: 'Settings', count: null }
];

function setActiveItem(id) {
  activeItem.value = id;
}
</script>
```

### Interactive Widget Dashboard

```vue
<template>
  <div>
    <h3 class="tw-text-lg tw-font-medium tw-mb-4">Dashboard</h3>
    
    <div class="tw-grid tw-grid-cols-2 md:tw-grid-cols-4 tw-gap-4">
      <div 
        v-for="widget in dashboardWidgets" 
        :key="widget.id"
        class="tw-bg-white tw-p-4 tw-rounded-lg tw-shadow-sm tw-border tw-border-[color:var(--neutrals-200)] tw-text-center"
      >
        <VcWidget 
          :icon="widget.icon" 
          :title="widget.title" 
          :value="widget.value" 
          :disabled="widget.disabled"
          @click="() => handleWidgetClick(widget)" 
        />
        
        <div class="tw-mt-4 tw-text-2xl tw-font-semibold">
          {{ widget.displayValue }}
        </div>
        
        <div class="tw-mt-2 tw-text-xs tw-text-[color:var(--neutrals-500)]">
          {{ widget.description }}
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcWidget } from '@vc-shell/framework';

const dashboardWidgets = ref([
  { 
    id: 1, 
    icon: 'material-shopping_cart', 
    title: 'Orders', 
    value: 15,
    disabled: false,
    displayValue: '1,234',
    description: 'Total orders this month'
  },
  { 
    id: 2, 
    icon: 'material-attach_money', 
    title: 'Revenue', 
    value: null,
    disabled: false,
    displayValue: '$45,678',
    description: 'Total revenue this month'
  },
  { 
    id: 3, 
    icon: 'material-people', 
    title: 'Customers', 
    value: 8,
    disabled: false,
    displayValue: '892',
    description: 'Registered customers'
  },
  { 
    id: 4, 
    icon: 'material-inventory', 
    title: 'Products', 
    value: null,
    disabled: false,
    displayValue: '156',
    description: 'Available products'
  }
]);

function handleWidgetClick(widget) {
  console.log(`Widget clicked: ${widget.title}`);
}
</script>
```
