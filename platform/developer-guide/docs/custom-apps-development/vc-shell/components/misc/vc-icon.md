<!-- AUTO-GENERATED FROM vc-shell — DO NOT EDIT MANUALLY -->
<!-- Source: ui/components/atoms/vc-icon/vc-icon.docs.md -->
<!-- To update: edit the source file in vc-shell, then run yarn docs:sync -->


# VcIcon

A unified icon component that renders icons from multiple libraries. Lucide Icons (`lucide-` prefix) are the standard; legacy libraries (FontAwesome, Bootstrap, Material) are deprecated.

<div class="vc-storybook-embed" style="--height: 400px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=layout-vcicon--basic&viewMode=story"
    loading="lazy"
    title="layout-vcicon--basic"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/layout-vcicon--basic" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

## When to Use

- Display icons in buttons, menus, toolbars, and status indicators
- Indicate status with color variants (success, warning, danger)
- Render custom Vue icon components inline
- When NOT to use: for decorative images or product photos, use [VcImage](../media/vc-image.md)

## Basic Usage

```vue
<VcIcon icon="lucide-home" size="m" />
```

## Key Props

| Prop           | Type                                                   | Default           | Description                                                                                                                                            |
| -------------- | ------------------------------------------------------ | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `icon`         | `string \| Component`                                  | `"lucide-square"` | Icon identifier or Vue component                                                                                                                       |
| `size`         | `"xs" \| "s" \| "m" \| "l" \| "xl" \| "xxl" \| "xxxl"` | `"m"`             | Predefined size                                                                                                                                        |
| `variant`      | `"warning" \| "danger" \| "success"`                   | —                 | Semantic color variant                                                                                                                                 |
| `customSize`   | `number`                                               | —                 | Custom size in pixels (overrides `size`)                                                                                                               |
| `ariaLabel`    | `string`                                               | —                 | Accessible label for meaningful icons                                                                                                                  |
| `basePath`     | `string`                                               | `"/assets/icons"` | Base path for SVG sprite icons                                                                                                                         |
| `useContainer` | `boolean`                                              | `false`           | Deprecated. Wraps the icon in a fixed-size container; removed in a future version (logs a dev warning). Remove it — icons render correctly without it. |

<div class="vc-storybook-embed" style="--height: 300px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=layout-vcicon--all-sizes&viewMode=story"
    loading="lazy"
    title="layout-vcicon--all-sizes"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/layout-vcicon--all-sizes" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

## Size Reference

| Size   | Pixels |
| ------ | ------ |
| `xs`   | 12px   |
| `s`    | 14px   |
| `m`    | 18px   |
| `l`    | 20px   |
| `xl`   | 22px   |
| `xxl`  | 30px   |
| `xxxl` | 64px   |

<div class="vc-storybook-embed" style="--height: 200px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=layout-vcicon--all-variants&viewMode=story"
    loading="lazy"
    title="layout-vcicon--all-variants"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/layout-vcicon--all-variants" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

## Icon Prefix Guide

| Prefix            | Library                | Status                 |
| ----------------- | ---------------------- | ---------------------- |
| `lucide-`         | Lucide Icons           | Standard (recommended) |
| `fa-` / `fas fa-` | Font Awesome           | Deprecated             |
| `bi-`             | Bootstrap Icons        | Deprecated             |
| `material-`       | Material Symbols       | Deprecated             |
| `svg:`            | SVG sprite file        | Supported              |
| _(Component)_     | Vue component instance | Supported              |

## Common Patterns

### Status Indicator

```vue
<div class="tw-flex tw-items-center tw-gap-2">
  <VcIcon icon="lucide-circle-check" variant="success" size="l" />
  <span>In Stock</span>
</div>
```

### Icon Inside a Button

```vue
<VcButton variant="primary" icon="lucide-plus">Add Item</VcButton>
```

### Custom Pixel Size

```vue
<VcIcon icon="lucide-shield" :custom-size="48" />
```

### Meaningful Icon with Accessible Label

```vue
<VcIcon icon="lucide-triangle-alert" variant="warning" size="l" aria-label="Warning: low stock" />
```

### Custom Vue Component as Icon

```vue
<script setup lang="ts">
import { VcIcon } from "@vc-shell/framework";
import MyCustomIcon from "./MyCustomIcon.vue";
</script>

<template>
  <VcIcon
    :icon="MyCustomIcon"
    size="l"
  />
</template>
```

## Accessibility

- Decorative icons (default) render with `aria-hidden="true"`
- When `ariaLabel` is provided, the icon receives `role="img"` and `aria-label` instead
- Always provide `ariaLabel` for icons that convey meaning not available in surrounding text
- Icon color inherits from `currentColor` by default, ensuring it follows parent text color

## Related Components

- [VcButton](./vc-button.md) — uses VcIcon internally for button icons
- [VcImage](../media/vc-image.md) — for photos and larger imagery
- [VcBanner](../feedback/vc-banner.md) — uses VcIcon for the leading alert icon


