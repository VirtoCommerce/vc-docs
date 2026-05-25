<!-- AUTO-GENERATED FROM vc-shell — DO NOT EDIT MANUALLY -->
<!-- Source: ui/components/atoms/vc-image/vc-image.docs.md -->
<!-- To update: edit the source file in vc-shell, then run yarn docs:sync -->


# VcImage

An image display component with predefined sizes, aspect ratio control, and a placeholder for missing sources. Renders images as CSS backgrounds with automatic HTTPS enforcement.

<div class="vc-storybook-embed" style="--height: 400px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=data-display-vcimage--default&viewMode=story"
    loading="lazy"
    title="data-display-vcimage--default"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/data-display-vcimage--default" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

## When to Use

- Display product thumbnails, profile avatars, or media previews
- Show images with consistent aspect ratios across a layout
- Provide clickable image tiles (e.g., gallery lightbox triggers)
- When NOT to use: for icons or symbolic graphics, use [VcIcon](../misc/vc-icon.md); for full-page hero images, use a standard `<img>` tag

## Basic Usage

```vue
<VcImage src="https://example.com/product.jpg" size="l" />
```

## Key Props

| Prop            | Type                                                            | Default          | Description                                                                                                                                        |
| --------------- | --------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `src`           | `string`                                                        | —                | Image URL; shows a placeholder icon when empty                                                                                                     |
| `size`          | `"auto" \| "xxs" \| "xs" \| "s" \| "m" \| "l" \| "xl" \| "xxl"` | `"auto"`         | Predefined width                                                                                                                                   |
| `aspect`        | `"1x1" \| "16x9" \| "4x3" \| "3x2"`                             | `"1x1"`          | Aspect ratio of the container                                                                                                                      |
| `background`    | `"cover" \| "contain" \| "auto"`                                | `"cover"`        | CSS background-size mode                                                                                                                           |
| `rounded`       | `boolean`                                                       | `false`          | Applies fully rounded corners (circular on 1x1)                                                                                                    |
| `bordered`      | `boolean`                                                       | `false`          | Adds a subtle border                                                                                                                               |
| `clickable`     | `boolean`                                                       | `false`          | Makes the image interactive with cursor and click event                                                                                            |
| `emptyIcon`     | `string`                                                        | `"lucide-image"` | Icon shown when `src` is empty                                                                                                                     |
| `alt`           | `string`                                                        | —                | Accessible alt text                                                                                                                                |
| `thumbnailSize` | `ThumbnailSize`                                                 | —                | Load a thumbnail variant instead of full-size image. Values: `"sm"`, `"md"`, `"lg"`, `"64x64"`, `"128x128"`, `"168x168"`, `"216x216"`, `"348x348"` |

<div class="vc-storybook-embed" style="--height: 300px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=data-display-vcimage--size-variants&viewMode=story"
    loading="lazy"
    title="data-display-vcimage--size-variants"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/data-display-vcimage--size-variants" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

## Size Reference

| Size   | Width          |
| ------ | -------------- |
| `xxs`  | 24px           |
| `xs`   | 32px           |
| `s`    | 48px           |
| `m`    | 64px           |
| `l`    | 96px           |
| `xl`   | 128px          |
| `xxl`  | 145px          |
| `auto` | 100% of parent |

## Common Patterns

### Product Thumbnail in a List

```vue
<VcImage :src="product.primaryImage" size="s" aspect="1x1" bordered :alt="product.name" />
```

### Profile Avatar

```vue
<VcImage :src="user.avatarUrl" size="m" rounded :alt="user.displayName" />
```

### Widescreen Banner

```vue
<VcImage :src="category.bannerUrl" aspect="16x9" background="cover" alt="Category banner" />
```

### Clickable Gallery Image

```vue
<VcImage :src="image.url" size="l" bordered clickable :alt="image.caption" @click="openLightbox(image)" />
```

### Empty State Placeholder

```vue
<VcImage size="xl" empty-icon="lucide-package" alt="" />
```

## Accessibility

- When `src` is present and no `clickable`, the container has `role="img"` with `aria-label` from `alt`
- Clickable images receive `role="button"`, `tabindex="0"`, and keyboard support (Enter/Space)
- Empty placeholder icon is marked `aria-hidden="true"`
- Focus ring appears on `:focus-visible` for clickable images
- HTTP URLs are automatically upgraded to HTTPS when the page is served over HTTPS

!!! tip "Use thumbnailSize for faster load times"
When displaying images in lists or grids, pass a `thumbnailSize` (e.g. `"128x128"`) to request a pre-scaled variant from the platform CDN instead of loading the full-resolution original. This significantly reduces bandwidth and speeds up initial render.

## Related Components

- [VcIcon](../misc/vc-icon.md) — for symbolic icons rather than photographic content
- [VcImageTile](../data-display/vc-image-tile.md) — combines VcImage with overlay actions for gallery use


