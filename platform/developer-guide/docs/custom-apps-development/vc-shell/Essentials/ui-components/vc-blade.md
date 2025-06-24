# VcBlade

VcBlade is a container component that implements the blade pattern for UI organization. Blades are panels that slide in from the right side of the screen and can be stacked to create a navigation hierarchy. They are ideal for displaying details, forms, and related content while maintaining context.

## Basic Usage

```vue
<template>
  <VcBlade
    title="Product Details"
    icon="material-shopping-cart"
    width="40%"
    :closable="true"
    :toolbar-items="toolbarItems"
    @close="handleClose"
    @expand="handleExpand"
    @collapse="handleCollapse"
  >
    <!-- Blade content here -->
    <div class="tw-p-4">
      Content of the blade goes here
    </div>
  </VcBlade>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcBlade, IBladeToolbar } from '@vc-shell/framework';

const toolbarItems = ref<IBladeToolbar[]>([
  { 
    id: 'refresh', 
    icon: 'material-refresh', 
    title: 'Refresh',
    clickHandler: () => refreshData()
  },
  { 
    id: 'add', 
    icon: 'material-add', 
    title: 'Add New',
    clickHandler: () => addNewItem()
  }
]);

function refreshData() {
  // Handle refresh action
}

function addNewItem() {
  // Handle add new item action
}

function handleClose() {
  // Handle blade close
}

function handleExpand() {
  // Handle blade expand
}

function handleCollapse() {
  // Handle blade collapse
}
</script>
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `icon` | `string` | - | Icon displayed in the blade header |
| `title` | `string` | - | Title displayed in the blade header |
| `subtitle` | `string` | - | Subtitle displayed in the blade header |
| `width` | `number \| string` | `"30%"` | Width of the blade (can be in pixels or percentage) |
| `expanded` | `boolean` | `false` | Whether the blade is expanded to full width. If not provided, defaults to `false`. |
| `closable` | `boolean` | `true` | Whether the blade can be closed by the user |
| `toolbarItems` | `IBladeToolbar[]` | `[]` | Array of toolbar items to display |
| `modified` | `boolean` | `undefined` | Indicates whether there are unsaved changes in the blade content. Defaults to `undefined`. |

## Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `close` | - | Emitted when the close button is clicked |
| `expand` | - | Emitted when the expand button is clicked |
| `collapse` | - | Emitted when the collapse button is clicked |

## Slots

| Slot Name | Description |
|-----------|-------------|
| `default` | The main content of the blade |
| `actions` | Custom actions to display in the blade header |
| `backButton` | Custom back button for mobile view |
| `widgets` | **Deprecated**. Use `useWidgets()` composable instead. Slot for blade widgets. |

## Toolbar Items

The `toolbarItems` prop accepts an array of `IBladeToolbar` objects with the following properties:

```ts
interface IBladeToolbar {
  id: string;
  title: string | Ref<string>;
  icon: string;
  clickHandler?: () => void;
  disabled?: boolean | Ref<boolean>;
  isVisible?: boolean | Ref<boolean>;
}
```

## CSS Variables

The blade component uses CSS variables for theming, which can be customized:

```css
:root {
  --blade-background-color: var(--additional-50);   /* Background color of the blade */
  --blade-color-error: var(--danger-500);           /* Color for error notifications in the blade */
  --blade-color-unsaved-changes: var(--secondary-600); /* Background color for unsaved changes notification */

  --blade-border-color: var(--neutrals-200);        /* Border color for the blade */
  --blade-icon-color: var(--secondary-400);         /* Default icon color in the blade */
  --blade-icon-hover-color: var(--secondary-500);   /* Icon color on hover */

  --blade-widgets-width: 50px;                      /* Width of the widgets sidebar when collapsed */
  --blade-widgets-width-expanded: 120px;            /* Width of the widgets sidebar when expanded */

  --blade-shadow-color: var(--primary-700);         /* Color base for the blade shadow */
  --blade-shadow: 2px 2px 8px rgb(from var(--blade-shadow-color) r g b / 14%); /* Shadow effect for the blade */

  --blade-text-color: var(--additional-50);         /* Text color for blade notifications */

  --blade-widgets-bg-color: var(--neutrals-100);    /* Background color of the widgets area */
  --blade-widgets-more-color: var(--neutrals-600);  /* Color for "more" indicator in widgets area */
}
```

## Integration with Blade Navigation

VcBlade is designed to work with the VC-Shell blade navigation system. When used with the `useBladeNavigation` composable, it provides a powerful way to navigate between different views:

```vue
<script lang="ts" setup>
import { VcBlade, useBladeNavigation } from '@vc-shell/framework';
import ProductEditForm from './ProductEditForm.vue';

const { openBlade } = useBladeNavigation();

function openEditView(productId) {
  openBlade({
    blade: ProductEditForm,
    param: productId,
    onClose() {
      // Handle close event
    }
  });
}
</script>
```

## Mobile Support

VcBlade automatically adapts to mobile screens. On mobile devices:

- Blades take up the full width of the screen
- A back button can be shown (provided through the `backButton` slot)
- Navigation is simplified with a more app-like experience

## Examples

### Basic Blade with Toolbar

```vue
<template>
  <VcBlade
    title="Products"
    width="50%"
    :toolbar-items="toolbarItems"
    @close="$emit('close')"
  >
    <VcTable
      :columns="columns"
      :items="products"
      @item-click="onProductClick"
    />
  </VcBlade>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcBlade, VcTable, IBladeToolbar, useBladeNavigation } from '@vc-shell/framework';
import ProductDetails from './ProductDetails.vue';

const { openBlade } = useBladeNavigation();

const toolbarItems = ref<IBladeToolbar[]>([
  { 
    id: 'refresh', 
    icon: 'material-refresh', 
    title: 'Refresh', 
    clickHandler: () => loadProducts()
  },
  { 
    id: 'add', 
    icon: 'material-add', 
    title: 'Add Product', 
    clickHandler: () => addProduct()
  }
]);

const columns = ref([
  { id: 'name', title: 'Name', sortable: true },
  { id: 'sku', title: 'SKU', sortable: true },
  { id: 'price', title: 'Price', sortable: true }
]);

const products = ref([
  { id: '1', name: 'Product A', sku: 'SKU001', price: 29.99 },
  { id: '2', name: 'Product B', sku: 'SKU002', price: 49.99 },
  { id: '3', name: 'Product C', sku: 'SKU003', price: 19.99 }
]);

function onProductClick(product) {
  openBlade({
    blade: ProductDetails,
    param: product.id
  });
}

function loadProducts() {
  // Reload products
}

function addProduct() {
  openBlade({
    blade: ProductDetails,
    options: { isNew: true }
  });
}
</script>
```

### Blade with Error Message

```vue
<template>
  <VcBlade
    title="Product Details"
    width="40%"
    :modified="hasChanges"
    @close="confirmClose"
  >
    <div v-if="error" class="tw-text-red-500 tw-p-4">
      {{ error }}
    </div>
    
    <VcForm 
      v-if="product" 
      :model="product"
      @update:model="hasChanges = true"
    >
      <!-- Form fields -->
    </VcForm>
  </VcBlade>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcBlade, VcForm, usePopup } from '@vc-shell/framework';

const product = ref(null);
const error = ref('');
const hasChanges = ref(false);
const { showConfirmation } = usePopup();

async function loadProduct(id) {
  try {
    // Load product
  } catch (err) {
    error.value = 'Failed to load product: ' + err.message;
  }
}

async function confirmClose() {
  if (hasChanges.value) {
    const confirmed = await showConfirmation('You have unsaved changes. Are you sure you want to close?');
    if (confirmed) {
      closeForm();
    }
  } else {
    closeForm();
  }
}

function closeForm() {
  // Close logic
}
</script>
```

### Blade with Custom Actions

```vue
<template>
  <VcBlade
    title="Image Preview"
    width="60%"
    :closable="true"
  >
    <template #actions>
      <VcButton 
        variant="icon" 
        icon="material-download" 
        @click="downloadImage"
      />
      <VcButton 
        variant="icon" 
        icon="material-share" 
        @click="shareImage"
      />
    </template>
    
    <div class="tw-p-4">
      <VcImage :src="imageUrl" aspect="16x9" />
    </div>
  </VcBlade>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcBlade, VcButton, VcImage } from '@vc-shell/framework';

const imageUrl = ref('https://example.com/image.jpg');

function downloadImage() {
  // Download logic
}

function shareImage() {
  // Share logic
}
</script>
```
