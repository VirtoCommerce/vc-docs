<!-- AUTO-GENERATED FROM vc-shell — DO NOT EDIT MANUALLY -->
<!-- Source: ui/components/molecules/vc-menu/vc-menu.docs.md -->
<!-- To update: edit the source file in vc-shell, then run yarn docs:sync -->


# VcMenu

Compositional navigation menu component for building sidebar navigation with sections, groups, nested items, badges, and loading skeletons.

<div class="vc-storybook-embed" style="--height: 400px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=navigation-vcmenu--default&viewMode=story"
    loading="lazy"
    title="navigation-vcmenu--default"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/navigation-vcmenu--default" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

## When to Use

- Building the main navigation sidebar in admin applications
- Multi-level navigation with collapsible groups and sections
- When the sidebar needs expanded (full) and collapsed (icon-only) states
- When NOT to use: for contextual dropdown menus, use `VcDropdown` instead

## Basic Usage

```vue
<template>
  <VcMenu :expanded="sidebarExpanded">
    <VcMenuItem
      icon="lucide-home"
      title="Dashboard"
      :active="currentRoute === '/dashboard'"
      @click="navigate('/dashboard')"
    />
    <VcMenuGroup
      group-id="catalog"
      icon="lucide-box"
      title="Catalog"
    >
      <VcMenuItem
        title="Products"
        nested
        @click="navigate('/products')"
      />
      <VcMenuItem
        title="Categories"
        nested
        @click="navigate('/categories')"
      />
    </VcMenuGroup>
    <VcMenuItem
      icon="lucide-settings"
      title="Settings"
      @click="navigate('/settings')"
    />
  </VcMenu>
</template>

<script setup lang="ts">
import { VcMenu, VcMenuItem, VcMenuGroup } from "@vc-shell/framework";
</script>
```

## Key Props

| Prop       | Type      | Default | Description                                               |
| ---------- | --------- | ------- | --------------------------------------------------------- |
| `expanded` | `boolean` | `true`  | Show full menu (titles visible) or collapsed (icons only) |
| `loading`  | `boolean` | `false` | Show skeleton loading placeholders instead of content     |

## Slots

| Slot      | Description                              |
| --------- | ---------------------------------------- |
| `default` | Menu items (`VcMenuItem`, `VcMenuGroup`) |

## Common Patterns

<div class="vc-storybook-embed" style="--height: 400px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=navigation-vcmenu--sections&viewMode=story"
    loading="lazy"
    title="navigation-vcmenu--sections"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/navigation-vcmenu--sections" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

### Section Groups with Nested Items

```vue
<VcMenu :expanded="expanded" :loading="isLoading">
  <VcMenuGroup group-id="activity" title="Activity" variant="section">
    <VcMenuItem icon="lucide-file-text" title="New Orders" @click="navigate('/orders/new')" />
    <VcMenuItem icon="lucide-clock" title="Pending Reviews" @click="navigate('/reviews')" />
  </VcMenuGroup>

  <VcMenuGroup group-id="catalog" title="Catalog" variant="section">
    <VcMenuItem icon="lucide-box" title="Products" @click="navigate('/products')" />
    <VcMenuGroup group-id="orders" icon="lucide-file" title="Orders">
      <VcMenuItem title="Accepted" icon="lucide-check" nested @click="navigate('/accepted')" />
      <VcMenuItem title="Declined" icon="lucide-x" nested @click="navigate('/declined')" />
    </VcMenuGroup>
  </VcMenuGroup>
</VcMenu>
```

### Items with Badges

```vue
<VcMenuItem icon="lucide-shopping-cart" title="New Orders" :badge="{ content: 5, variant: 'primary' }" />
<VcMenuItem icon="lucide-alert-triangle" title="Returns" :badge="{ content: 99, variant: 'danger' }" />
<VcMenuItem icon="lucide-bell" title="Notifications" :badge="{ isDot: true, variant: 'warning' }" />
```

### Collapsed State

<div class="vc-storybook-embed" style="--height: 400px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=navigation-vcmenu--collapsed&viewMode=story"
    loading="lazy"
    title="navigation-vcmenu--collapsed"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/navigation-vcmenu--collapsed" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

When `expanded` is `false`, the menu shows only icons and letter abbreviations. Groups show tooltips on hover. The container width should be reduced (e.g., 64px).

## CSS Variables

| Variable                          | Default              | Description                             |
| --------------------------------- | -------------------- | --------------------------------------- |
| `--vc-menu-gap`                   | `8px`                | Gap between menu items                  |
| `--vc-menu-item-focus-ring-color` | `var(--primary-500)` | Focus ring color on keyboard navigation |

## Accessibility

- `VcMenuItem` renders its interactive row as a native `<button type="button">`, so it is in the tab order and the browser maps Enter/Space to activation. There is no `tabindex` juggling and no `keydown` handler to keep in sync.
- Focus ring on `:focus-visible` only (not on mouse click), colored via `--vc-menu-item-focus-ring-color`
- The active item exposes `aria-current="page"`, so assistive technology announces the current location — `active` drives both the styling and the attribute
- When the menu is collapsed to icons the visible title is hidden, so the button carries `aria-label` with the item title; expanded items rely on their visible text instead and set no `aria-label`
- Icons and letter abbreviations are `aria-hidden="true"` — they are decorative next to the accessible name
- `VcMenuGroup` with `variant="section"` renders a native button that reports `aria-expanded` and points `aria-controls` at the children wrapper it toggles
- Collapsed mode shows tooltips for discoverability (in addition to, not instead of, the accessible name)

## Related Components

- [VcMenuItem](./vc-menu.md) — individual menu item with icon, title, badge
- [VcMenuGroup](./vc-menu.md) — collapsible group container (supports `variant="section"` for top-level sections)
- [VcDropdown](./vc-dropdown.md) — contextual dropdown menus


