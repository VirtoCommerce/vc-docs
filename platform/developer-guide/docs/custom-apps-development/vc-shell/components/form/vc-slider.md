<!-- AUTO-GENERATED FROM vc-shell — DO NOT EDIT MANUALLY -->
<!-- Source: ui/components/molecules/vc-slider/vc-slider.docs.md -->
<!-- To update: edit the source file in vc-shell, then run yarn docs:sync -->


# VcSlider

A content carousel component built on Swiper.js for displaying slides with optional navigation buttons. Renders any content via the default slot.

<div class="vc-storybook-embed" style="--height: 400px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=form-vcslider--default&viewMode=story"
    loading="lazy"
    title="form-vcslider--default"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/form-vcslider--default" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

## When to Use

- Image carousels (product galleries, banners)
- Horizontally scrollable content cards
- Any list of items that should be browsable one screen at a time
- When NOT to use: vertical scrolling lists (use standard layout), tabbed content (use tabs)

## Basic Usage

```vue
<template>
  <VcSlider
    :slides="products"
    navigation
  >
    <template #default="{ slide }">
      <div class="tw-w-48">
        <img
          :src="slide.imageUrl"
          class="tw-rounded"
        />
        <p>{{ slide.name }}</p>
      </div>
    </template>
  </VcSlider>
</template>

<script setup lang="ts">
import { VcSlider } from "@vc-shell/framework";

const products = [
  { name: "Product A", imageUrl: "/images/a.jpg" },
  { name: "Product B", imageUrl: "/images/b.jpg" },
  { name: "Product C", imageUrl: "/images/c.jpg" },
];
</script>
```

## Key Props

| Prop                 | Type                                     | Default              | Description                                             |
| -------------------- | ---------------------------------------- | -------------------- | ------------------------------------------------------- |
| `slides`             | `Record<string, unknown>[] \| unknown[]` | `[]`                 | Array of slide data objects                             |
| `navigation`         | `boolean`                                | `false`              | Show previous/next navigation buttons                   |
| `slidesPerView`      | `string \| "auto"`                       | `"auto"`             | Number of visible slides at once                        |
| `spaceBetweenSlides` | `number`                                 | `10`                 | Gap between slides in pixels                            |
| `overflow`           | `boolean`                                | `false`              | Allow slides to be visible outside the container bounds |
| `ariaLabel`          | `string`                                 | `"Content carousel"` | Accessible label for the slider region                  |

## Common Patterns

### Fixed Slides Per View

```vue
<VcSlider :slides="items" :slides-per-view="3" navigation :space-between-slides="20">
  <template #default="{ slide }">
    <ProductCard :product="slide" />
  </template>
</VcSlider>
```

### Custom Navigation Buttons

<div class="vc-storybook-embed" style="--height: 400px">
  <iframe
    src="https://vc-shell-storybook.govirto.com/iframe.html?id=form-vcslider--custom-navigation&viewMode=story"
    loading="lazy"
    title="form-vcslider--custom-navigation"
  ></iframe>
  <a href="https://vc-shell-storybook.govirto.com/?path=/story/form-vcslider--custom-navigation" target="_blank" rel="noopener">Open in Storybook ↗</a>
</div>

```vue
<VcSlider :slides="items" navigation>
  <template #default="{ slide }">
    <img :src="slide.url" />
  </template>
  <template #prevBtn>
    <button class="tw-bg-primary-500 tw-text-white tw-p-2 tw-rounded-full">
      <VcIcon icon="lucide-arrow-left" />
    </button>
  </template>
  <template #nextBtn>
    <button class="tw-bg-primary-500 tw-text-white tw-p-2 tw-rounded-full">
      <VcIcon icon="lucide-arrow-right" />
    </button>
  </template>
</VcSlider>
```

### Single Slide View

```vue
<VcSlider :slides="banners" :slides-per-view="1" navigation>
  <template #default="{ slide }">
    <img :src="slide.imageUrl" class="tw-w-full tw-rounded" />
  </template>
</VcSlider>
```

## Slots

| Slot      | Scope       | Description                       |
| --------- | ----------- | --------------------------------- |
| `default` | `{ slide }` | Content for each slide            |
| `prevBtn` | --          | Custom previous navigation button |
| `nextBtn` | --          | Custom next navigation button     |

## Accessibility

- Container has `role="region"` with `aria-label`
- Navigation buttons have `aria-label` ("Previous slide" / "Next slide")
- Navigation icons are `aria-hidden="true"`
- Focus ring on navigation buttons via `:focus-visible`
- Disabled navigation buttons have reduced opacity

## CSS Variables

- `--slider-button-background`, `--slider-button-border` -- navigation button appearance
- `--slider-button-text`, `--slider-button-text-disabled` -- button icon colors
- `--slider-button-border-radius`
- `--slider-focus-ring-color`

## Related Components

- [VcImage](../media/vc-image.md) -- image component often used inside slides

## Skeleton / Loading State

When placed inside a `VcBlade` with `loading=true`, the component automatically renders a skeleton placeholder matching its visual footprint. No additional props or configuration needed.


