<!-- AUTO-GENERATED FROM vc-shell — DO NOT EDIT MANUALLY -->
<!-- Source: ui/components/atoms/vc-status/vc-status.docs.md -->
<!-- To update: edit the source file in vc-shell, then run yarn docs:sync -->


# VcStatus

A colored badge that communicates the state of an entity -- such as an order, product, or workflow step -- using semantic color variants.

<div class="vc-storybook-embed" style="--height: 400px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=data-display-vcstatus--default&viewMode=story"
    loading="lazy"
    title="data-display-vcstatus--default"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/data-display-vcstatus--default" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

## When to Use

- Display order or fulfillment status (e.g., "Paid", "Pending", "Cancelled")
- Tag items with severity levels in tables or detail views
- Show a compact dot indicator when label text is not needed
- When NOT to use: boolean on/off state (use [VcStatusIcon](./vc-status-icon.md) instead)

## Basic Usage

```vue
<template>
  <VcStatus variant="success">Published</VcStatus>
</template>

<script setup lang="ts">
import { VcStatus } from "@vc-shell/framework";
</script>
```

## Key Props

| Prop      | Type                                                                                         | Default  | Description                                                                  |
| --------- | -------------------------------------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------- |
| `variant` | `"info" \| "warning" \| "danger" \| "success" \| "light-danger" \| "info-dark" \| "primary"` | `"info"` | Semantic color theme                                                         |
| `extend`  | `boolean`                                                                                    | --       | Extended layout with larger padding, rounded corners, and colored background |
| `dot`     | `boolean`                                                                                    | `false`  | Renders as a small colored circle without text                               |

## Common Patterns

<div class="vc-storybook-embed" style="--height: 450px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=data-display-vcstatus--all-variants&viewMode=story"
    loading="lazy"
    title="data-display-vcstatus--all-variants"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/data-display-vcstatus--all-variants" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

### Status in a Table Cell

```vue
<template>
  <VcStatus :variant="statusVariant(order.status)">
    {{ order.status }}
  </VcStatus>
</template>

<script setup lang="ts">
function statusVariant(status: string) {
  const map: Record<string, string> = {
    Paid: "success",
    Pending: "warning",
    Cancelled: "danger",
    Draft: "info",
  };
  return map[status] ?? "info";
}
</script>
```

### Dot Indicators

Use the `dot` prop for compact status representation alongside text labels.

```vue
<template>
  <div class="tw-flex tw-items-center tw-gap-2">
    <VcStatus
      variant="success"
      dot
    />
    <span>Online</span>
  </div>
</template>
```

### Extended Alert-Style Status

The `extend` prop creates a banner-like status with a colored background, suitable for detail blade headers.

```vue
<template>
  <VcStatus
    variant="danger"
    extend
  >
    <div class="tw-flex tw-items-center">
      <VcIcon
        icon="lucide-triangle-alert"
        size="xl"
        variant="danger"
        class="tw-mr-3"
      />
      <div>
        <h3 class="tw-font-bold">Payment Failed</h3>
        <p>The last transaction was declined. Please update your payment method.</p>
      </div>
    </div>
  </VcStatus>
</template>
```

## CSS Custom Properties

Each variant has its own set of CSS variables following the pattern `--status-{variant}-color`, `--status-{variant}-main-color`, `--status-{variant}-bg-color`. Key shared variables:

| Variable                          | Default               | Description                       |
| --------------------------------- | --------------------- | --------------------------------- |
| `--status-border-radius`          | `9999px`              | Pill shape for standard mode      |
| `--status-border-radius-extended` | `6px`                 | Rounded corners for extended mode |
| `--status-dot-size`               | `10px`                | Diameter of the dot indicator     |
| `--status-text-color`             | `var(--neutrals-700)` | Default label text color          |

## Accessibility

- `role="status"` for screen reader announcements
- In `dot` mode, `aria-label` is set to the variant name so the color meaning is conveyed
- Text content is truncated with `text-overflow: ellipsis` in standard mode; extended mode wraps normally

## Related Components

- [VcStatusIcon](./vc-status-icon.md) -- boolean check/cross icon for active/inactive states
- [VcBadge](../misc/vc-badge.md) -- numeric count badge overlay


