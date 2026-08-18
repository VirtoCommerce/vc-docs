# Grid Components: VcRow & VcCol

The VC-Shell framework provides two foundational layout components for creating flexible grid layouts: `VcRow` and `VcCol`. These components work together to create responsive layouts using CSS Flexbox.

## VcRow Component

The `VcRow` component arranges its children in a horizontal row. It automatically adapts to mobile views by switching to a grid layout.

## Storybook

[VcRow Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vcrow--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vcrow--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

### Basic Usage

```vue
<template>
  <VcRow>
    <div>Item 1</div>
    <div>Item 2</div>
    <div>Item 3</div>
  </VcRow>
</template>

<script lang="ts" setup>
import { VcRow } from '@vc-shell/framework';
</script>
```

### Slots

| Slot      | Description                                        |
| --------- | -------------------------------------------------- |
| `default` | Container for child elements to arrange horizontally |

### CSS Variables and Classes

The row component uses standard CSS classes that can be extended:

```css
.vc-row {
  /* Default flexbox row layout */
  display: flex;
  flex-wrap: nowrap;
  align-items: stretch;
}

/* Responsive behavior for mobile */ 
.vc-app_mobile .vc-row {
  display: grid;
}
```

You can use Tailwind utility classes with the component to further customize it:

```vue
<VcRow class="tw-gap-4">
  <!-- Items with 1rem gap between them -->
</VcRow>
```

## VcCol Component

The `VcCol` component creates a vertical column that can be used within `VcRow` or standalone to create flexible layouts.

## Storybook

[VcCol Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vccol--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vccol--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

### Basic Usage

```vue
<template>
  <VcCol :size="2">
    <div>Content Item 1</div>
    <div>Content Item 2</div>
  </VcCol>
</template>

<script lang="ts" setup>
import { VcCol } from '@vc-shell/framework';
</script>
```

### Props

| Prop     | Type     | Default | Description                                               |
| -------- | -------- | ------- | --------------------------------------------------------- |
| `size`   | `number` | `1`     | Controls the flex-grow value, determining relative width  |

### Slots

| Slot      | Description                                        |
| --------- | -------------------------------------------------- |
| `default` | Container for child elements to arrange vertically |

### CSS Variables and Classes

The column component uses standard CSS classes that can be extended:

```css
.vc-col {
  display: flex;
  flex-direction: column;
  min-width: 0;
  flex-basis: 0;
}
```

## Example: Grid Layout

```vue
<template>
  <div class="tw-p-4">
    <VcRow class="tw-gap-4">
      <VcCol :size="1" class="tw-p-2 tw-bg-[var(--neutrals-100)] tw-rounded">
        <div class="tw-p-2 tw-mb-2">
          <h3 class="tw-font-medium">Column 1</h3>
          <p>Size: 1</p>
        </div>
        <img src="/image1.jpg" class="tw-rounded" />
      </VcCol>
      
      <VcCol :size="2" class="tw-p-2 tw-bg-[var(--neutrals-100)] tw-rounded">
        <div class="tw-p-2 tw-mb-2">
          <h3 class="tw-font-medium">Column 2</h3>
          <p>Size: 2</p>
        </div>
        <img src="/image2.jpg" class="tw-rounded" />
      </VcCol>
      
      <VcCol :size="1" class="tw-p-2 tw-bg-[var(--neutrals-100)] tw-rounded">
        <div class="tw-p-2 tw-mb-2">
          <h3 class="tw-font-medium">Column 3</h3>
          <p>Size: 1</p>
        </div>
        <img src="/image3.jpg" class="tw-rounded" />
      </VcCol>
    </VcRow>
  </div>
</template>

<script lang="ts" setup>
import { VcRow, VcCol } from '@vc-shell/framework';
</script>
```

## Advanced Examples

### Cards in a Row

```vue
<template>
  <VcRow class="tw-gap-4">
    <VcCol v-for="i in 3" :key="i" class="tw-p-4 tw-border tw-border-[var(--neutrals-200)] tw-rounded tw-shadow-sm">
      <h3 class="tw-font-medium tw-mb-2">Card Title {{ i }}</h3>
      <p>This is card content for card {{ i }}.</p>
      <button class="tw-mt-4 tw-px-3 tw-py-1 tw-bg-[var(--primary-500)] tw-text-white tw-rounded">
        Action
      </button>
    </VcCol>
  </VcRow>
</template>

<script lang="ts" setup>
import { VcRow, VcCol } from '@vc-shell/framework';
</script>
```

### Content Layout with Different Column Sizes

```vue
<template>
  <VcRow class="tw-gap-4">
    <!-- Sidebar -->
    <VcCol :size="1" class="tw-p-4 tw-bg-[var(--neutrals-100)] tw-rounded">
      <h3 class="tw-font-medium tw-mb-4">Sidebar</h3>
      <ul class="tw-space-y-2">
        <li class="tw-py-1">Menu Item 1</li>
        <li class="tw-py-1">Menu Item 2</li>
        <li class="tw-py-1">Menu Item 3</li>
        <li class="tw-py-1">Menu Item 4</li>
      </ul>
    </VcCol>
    
    <!-- Main content -->
    <VcCol :size="3" class="tw-p-4 tw-bg-[var(--neutrals-50)] tw-rounded">
      <h2 class="tw-text-xl tw-font-bold tw-mb-4">Main Content</h2>
      <p class="tw-mb-4">This is the main content area that takes up more space with a size of 3.</p>
      
      <VcRow class="tw-gap-2 tw-mb-4">
        <VcCol v-for="i in 3" :key="i" class="tw-p-2 tw-bg-white tw-shadow-sm tw-rounded">
          <h4 class="tw-font-medium">Sub-Item {{ i }}</h4>
          <p class="tw-text-sm">Description for sub-item {{ i }}.</p>
        </VcCol>
      </VcRow>
      
      <p>Additional content can go here.</p>
    </VcCol>
  </VcRow>
</template>

<script lang="ts" setup>
import { VcRow, VcCol } from '@vc-shell/framework';
</script>
```

### Creating Equal-Width Columns

```vue
<template>
  <VcRow class="tw-gap-2">
    <VcCol v-for="i in 4" :key="i" :size="1" class="tw-p-3 tw-text-center tw-bg-[var(--neutrals-100)] tw-rounded">
      Column {{ i }}
    </VcCol>
  </VcRow>
</template>

<script lang="ts" setup>
import { VcRow, VcCol } from '@vc-shell/framework';
</script>
```

### Mobile Responsive Layout

```vue
<template>
  <div>
    <!-- This layout will automatically switch to grid on mobile devices -->
    <VcRow class="tw-gap-4">
      <VcCol :size="1" class="tw-p-4 tw-bg-[var(--neutrals-100)] tw-rounded">
        <h3>Section 1</h3>
        <p>This content will stack vertically on mobile.</p>
      </VcCol>
      
      <VcCol :size="1" class="tw-p-4 tw-bg-[var(--neutrals-100)] tw-rounded">
        <h3>Section 2</h3>
        <p>This content will stack vertically on mobile.</p>
      </VcCol>
      
      <VcCol :size="1" class="tw-p-4 tw-bg-[var(--neutrals-100)] tw-rounded">
        <h3>Section 3</h3>
        <p>This content will stack vertically on mobile.</p>
      </VcCol>
    </VcRow>
  </div>
</template>

<script lang="ts" setup>
import { VcRow, VcCol } from '@vc-shell/framework';
</script>
```
