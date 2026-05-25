<!-- AUTO-GENERATED FROM vc-shell — DO NOT EDIT MANUALLY -->
<!-- Source: ui/components/atoms/vc-widget/vc-widget.docs.md -->
<!-- To update: edit the source file in vc-shell, then run yarn docs:sync -->


# VcWidget

A clickable widget tile with an icon, title, and optional badge counter. Used in blade toolbars and sidebars to trigger blade-level actions or navigation.

<div class="vc-storybook-embed" style="--height: 400px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=data-display-vcwidget--default&viewMode=story"
    loading="lazy"
    title="data-display-vcwidget--default"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/data-display-vcwidget--default" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

## When to Use

- Build widget panels in blade sidebars (e.g., "Orders", "Reviews", "Notifications")
- Show action shortcuts with counts in dashboard layouts
- When NOT to use: primary form actions (use [VcButton](./vc-button.md)); standalone navigation links (use [VcLink](../navigation/vc-link.md))

## Basic Usage

```vue
<template>
  <VcWidget
    icon="lucide-bell"
    title="Notifications"
    :value="unreadCount"
    @click="openNotifications"
  />
</template>

<script setup lang="ts">
import { ref } from "vue";
import { VcWidget } from "@vc-shell/framework";

const unreadCount = ref(5);

function openNotifications() {
  // open notifications blade
}
</script>
```

## Key Props

| Prop         | Type               | Default | Description                                                       |
| ------------ | ------------------ | ------- | ----------------------------------------------------------------- |
| `icon`       | `string`           | --      | Icon name (Lucide format, e.g., `"lucide-save"`)                  |
| `title`      | `string`           | --      | Label text below (or beside) the icon                             |
| `value`      | `string \| number` | --      | Badge count displayed on the icon; numbers above 99 show as "99+" |
| `disabled`   | `boolean`          | `false` | Prevents clicks and applies muted styling                         |
| `isExpanded` | `boolean`          | `false` | Expanded visual state                                             |
| `horizontal` | `boolean`          | `false` | Arranges icon and title side by side instead of stacked           |

## Events

| Event   | Payload | Description                                                   |
| ------- | ------- | ------------------------------------------------------------- |
| `click` | none    | Fired when the widget is clicked (suppressed when `disabled`) |

<div class="vc-storybook-embed" style="--height: 350px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=data-display-vcwidget--sidebar-layout&viewMode=story"
    loading="lazy"
    title="data-display-vcwidget--sidebar-layout"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/data-display-vcwidget--sidebar-layout" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

## Common Patterns

### Sidebar Widget Panel

```vue
<template>
  <div class="tw-flex tw-flex-col tw-gap-2">
    <VcWidget
      v-for="widget in widgets"
      :key="widget.id"
      :icon="widget.icon"
      :title="widget.title"
      :value="widget.count"
      @click="onWidgetClick(widget)"
    />
  </div>
</template>
```

### Horizontal Layout

Use `horizontal` for compact inline widget rows, such as blade header actions.

```vue
<VcWidget icon="lucide-mail" title="Messages" :value="3" horizontal />
```

### Large Badge Count Truncation

Badge values above 99 are automatically displayed as "99+".

```vue
<VcWidget icon="lucide-inbox" title="Inbox" :value="142" />
<!-- Badge shows "99+" -->
```

## CSS Custom Properties

| Variable                     | Default               | Description          |
| ---------------------------- | --------------------- | -------------------- |
| `--widget-bg-color`          | `transparent`         | Background color     |
| `--widget-bg-hover-color`    | `var(--neutrals-50)`  | Background on hover  |
| `--widget-icon-color`        | `var(--neutrals-700)` | Icon color           |
| `--widget-icon-hover-color`  | `var(--primary-600)`  | Icon color on hover  |
| `--widget-title-color`       | `var(--neutrals-600)` | Title text color     |
| `--widget-title-hover-color` | `var(--primary-600)`  | Title color on hover |
| `--widget-border-radius`     | `8px`                 | Corner radius        |
| `--widget-focus-ring-color`  | `var(--primary-300)`  | Focus ring color     |

## Accessibility

- Renders with `role="button"` and `tabindex="0"` for keyboard interaction
- Activates on Enter and Space key presses
- `aria-disabled` set when disabled; `tabindex="-1"` removes from tab order
- `aria-label` set to the `title` value
- Icon is marked `aria-hidden="true"`
- Focus-visible ring for keyboard navigation

## Related Components

- [VcBadge](./vc-badge.md) -- used internally for the count badge overlay
- [VcIcon](./vc-icon.md) -- used internally for the widget icon
- [VcButton](./vc-button.md) -- for standard action buttons


