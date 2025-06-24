# VcBreadcrumbs Component

The `VcBreadcrumbs` component is a molecule used throughout the VC-Shell framework for displaying navigation hierarchy. It provides an adaptive and interactive way for users to understand their location within the application and navigate backwards through the hierarchy.

## Storybook

[VcBreadcrumbs Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vcbreadcrumbs--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vcbreadcrumbs--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcBreadcrumbs :items="breadcrumbItems" />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcBreadcrumbs } from '@vc-shell/framework';

const breadcrumbItems = ref([
  { id: 'home', title: 'Home', icon: 'material-home' },
  { id: 'products', title: 'Products' },
  { id: 'electronics', title: 'Electronics' }
]);
</script>
```

## Props

| Prop        | Type            | Default     | Description                                   |
| ----------- | --------------- | ----------- | --------------------------------------------- |
| `items`     | `Breadcrumbs[]` | `[]`        | Array of breadcrumb items to display          |
| `variant`   | `string`        | `'default'` | Visual style variant ('default' or 'light')   |
| `separated` | `boolean`       | `false`     | Whether to show separators between items      |

## Events

| Event       | Payload   | Description                                      |
| ----------- | --------- | ------------------------------------------------ |
| -           | -         | Clicks on breadcrumb items are handled via the `clickHandler` property within each item of the `items` array. See the `Breadcrumbs` interface below. |

## Slots

| Slot      | Props                                   | Description                                |
| --------- | --------------------------------------- | ------------------------------------------ |
| `trigger` | `{ click: () => void, isActive: boolean }` | Custom content for the dropdown trigger button |

## Breadcrumbs Interface

The items passed to the breadcrumbs component should follow this interface:

```typescript
interface Breadcrumbs {
  id?: string;                           // Unique identifier for the breadcrumb
  title?: string;                        // Display text
  icon?: string;                         // Optional icon (material icon name)
  clickHandler?: (id?: string) => void;  // Optional click handler function. Receives the item's ID.
}
```

## CSS Variables

The breadcrumbs component uses CSS variables for theming, which can be customized:

```css
:root {
  /* VcBreadcrumbs component variables */
  --separator-color: var(--neutrals-400);               /* Color of the separator between breadcrumb items */
  --breadcrumbs-item-border-color: var(--secondary-300); /* Border color for breadcrumb items */
  --breadcrumbs-item-border-color-hover: var(--secondary-400); /* Border color for breadcrumb items on hover */
  --breadcrumbs-expand-button-color: var(--neutrals-500); /* Color for the expand/collapse button */
  --breadcrumbs-expand-button-color-hover: var(--neutrals-600); /* Color for the expand/collapse button on hover */
  
  /* VcBreadcrumbsItem internal component variables */
  --breadcrumbs-item-text-color: var(--secondary-300);  /* Text color for breadcrumb items */
  --breadcrumbs-item-text-color-hover: var(--neutrals-500); /* Text color for breadcrumb items on hover */
  --breadcrumbs-item-color: var(--neutrals-400);        /* Overall color for breadcrumb items */
  --breadcrumbs-item-color-current: var(--primary-500); /* Color for the current/active breadcrumb item */
  --breadcrumbs-item-icon-color: var(--secondary-300);  /* Color for icons in breadcrumb items */
}
```

## Examples

### Basic Breadcrumbs

```vue
<template>
  <VcBreadcrumbs :items="breadcrumbItems" />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcBreadcrumbs } from '@vc-shell/framework';

const breadcrumbItems = ref([
  { id: 'home', title: 'Home', icon: 'material-home' },
  { id: 'products', title: 'Products' },
  { id: 'electronics', title: 'Electronics' }
]);
</script>
```

### Breadcrumbs with Click Handlers

```vue
<template>
  <VcBreadcrumbs :items="breadcrumbItems" />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcBreadcrumbs } from '@vc-shell/framework';

const breadcrumbItems = ref([
  { 
    id: 'home', 
    title: 'Home', 
    icon: 'material-home',
    clickHandler: () => navigateToHome()
  },
  { 
    id: 'products', 
    title: 'Products',
    clickHandler: () => navigateToProducts()
  },
  { 
    id: 'electronics', 
    title: 'Electronics' 
  }
]);

function navigateToHome() {
  console.log('Navigating to home');
  // Navigation logic here
}

function navigateToProducts() {
  console.log('Navigating to products');
  // Navigation logic here
}
</script>
```

### Breadcrumbs with Separators

```vue
<template>
  <VcBreadcrumbs :items="breadcrumbItems" :separated="true" />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcBreadcrumbs } from '@vc-shell/framework';

const breadcrumbItems = ref([
  { id: 'home', title: 'Home', icon: 'material-home' },
  { id: 'products', title: 'Products' },
  { id: 'electronics', title: 'Electronics' },
  { id: 'laptops', title: 'Laptops' }
]);
</script>
```

### Light Variant

```vue
<template>
  <VcBreadcrumbs :items="breadcrumbItems" variant="light" />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcBreadcrumbs } from '@vc-shell/framework';

const breadcrumbItems = ref([
  { id: 'home', title: 'Home', icon: 'material-home' },
  { id: 'products', title: 'Products' },
  { id: 'electronics', title: 'Electronics' }
]);
</script>
```

### Custom Dropdown Trigger

```vue
<template>
  <VcBreadcrumbs :items="breadcrumbItems">
    <template #trigger="{ click, isActive }">
      <VcButton 
        :variant="isActive ? 'primary' : 'outlined'"
        size="s"
        @click="click"
      >
        <template #prepend>
          <VcIcon icon="material-more_horiz" />
        </template>
        More
      </VcButton>
    </template>
  </VcBreadcrumbs>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcBreadcrumbs, VcButton, VcIcon } from '@vc-shell/framework';

const breadcrumbItems = ref([
  { id: 'home', title: 'Home', icon: 'material-home' },
  { id: 'products', title: 'Products' },
  { id: 'electronics', title: 'Electronics' },
  { id: 'computers', title: 'Computers' },
  { id: 'laptops', title: 'Laptops' }
]);
</script>
```

### Integration with useBreadcrumbs Composable

```vue
<template>
  <VcBreadcrumbs :items="breadcrumbs" />
  
  <div class="tw-mt-8">
    <VcButton @click="navigateToNewPage">
      Navigate to New Page
    </VcButton>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcBreadcrumbs, VcButton, useBreadcrumbs } from '@vc-shell/framework';

const { breadcrumbs, push, remove, clear } = useBreadcrumbs();

// Example navigation function
function navigateToNewPage() {
  // Add a new breadcrumb
  push({
    id: 'new-page',
    title: 'New Page',
    clickHandler: (id) => {
      console.log(`Navigating back from ${id}`);
      return true; // Return true to update breadcrumbs
    }
  });
  
  // Simulate navigation
  console.log('Navigating to new page');
}

// Initialize with a home breadcrumb
onMounted(() => {
  clear(); // Clear any existing breadcrumbs
  push({
    id: 'home',
    title: 'Home',
    icon: 'material-home',
    clickHandler: () => {
      console.log('Navigating to home');
      return true;
    }
  });
});
</script>
```

### Dynamic Breadcrumbs Based on Route

```vue
<template>
  <VcBreadcrumbs :items="breadcrumbs" />
</template>

<script lang="ts" setup>
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import { VcBreadcrumbs } from '@vc-shell/framework';

const route = useRoute();
const breadcrumbs = ref([]);

// Function to update breadcrumbs based on current route
function updateBreadcrumbs() {
  const newBreadcrumbs = [
    {
      id: 'home',
      title: 'Home',
      icon: 'material-home',
      clickHandler: () => navigateTo('/')
    }
  ];
  
  if (route.path.includes('/products')) {
    newBreadcrumbs.push({
      id: 'products',
      title: 'Products',
      clickHandler: () => navigateTo('/products')
    });
    
    if (route.params.category) {
      newBreadcrumbs.push({
        id: `category-${route.params.category}`,
        title: getCategoryName(route.params.category),
        clickHandler: () => navigateTo(`/products/${route.params.category}`)
      });
      
      if (route.params.product) {
        newBreadcrumbs.push({
          id: `product-${route.params.product}`,
          title: getProductName(route.params.product)
        });
      }
    }
  }
  
  breadcrumbs.value = newBreadcrumbs;
}

// Helper functions
function navigateTo(path) {
  // Navigation logic
  console.log(`Navigating to ${path}`);
}

function getCategoryName(categoryId) {
  // Logic to get category name from ID
  return categoryId.toString().charAt(0).toUpperCase() + categoryId.toString().slice(1);
}

function getProductName(productId) {
  // Logic to get product name from ID
  return `Product ${productId}`;
}

// Watch for route changes
watch(() => route.path, updateBreadcrumbs, { immediate: true });
</script>
```
