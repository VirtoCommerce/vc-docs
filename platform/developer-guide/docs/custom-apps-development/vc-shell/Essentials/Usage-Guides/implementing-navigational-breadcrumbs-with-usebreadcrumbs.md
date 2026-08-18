# How-To: Implementing Navigational Breadcrumbs with `useBreadcrumbs`

The `useBreadcrumbs` composable in VC-Shell is designed to simplify the creation and management of breadcrumb navigation trails. This guide will demonstrate how to effectively use `useBreadcrumbs` to enhance navigation within your application, providing users with a clear understanding of their location in the application's hierarchy.

## Prerequisites

-   Understanding of Vue 3 Composition API, including `ref` and `computed`.
-   Familiarity with Vue Router for navigation handling (`useRouter`, `useRoute`).
-   Knowledge of the `useBreadcrumbs` API (see [useBreadcrumbs API Reference](../composables/useBreadcrumbs.md)).
-   Awareness of the `VcBreadcrumbs` UI component for displaying breadcrumbs (see [VcBreadcrumbs Component Documentation](../ui-components/vc-breadcrumbs.md)).

## Core Concept

`useBreadcrumbs` provides a reactive array `breadcrumbs` and methods `push` and `remove` to manage the breadcrumb items. Each breadcrumb item is an object with an `id`, `title`, an optional `icon`, and a `clickHandler`.

-   `push(breadcrumb)`: Adds a breadcrumb. It intelligently avoids duplicates based on `id` or `title`.
-   `remove(ids[])`: Removes breadcrumbs by their unique IDs.
-   `breadcrumbs`: A `ComputedRef<Breadcrumbs[]>` that you can pass to the `VcBreadcrumbs` component.

The `clickHandler` is crucial. It defines what happens when a breadcrumb is clicked. Typically, it involves navigating to a route and should return `true` if subsequent breadcrumbs (those to its right) should be removed from the trail, effectively truncating the path to the clicked item.

```typescript
import { useBreadcrumbs } from '@vc-shell/framework';
import { useRouter } from 'vue-router';

const { breadcrumbs, push, remove } = useBreadcrumbs();
const router = useRouter();

function goToHome() {
  push({
    id: 'home',
    title: 'Home',
    icon: 'home-icon', // Replace with actual icon name or component
    clickHandler: () => {
      router.push({ name: 'HomePage' });
      return true; // Remove any breadcrumbs after 'Home'
    }
  });
}
```

## Implementation Strategies

### 1. Basic Manual Breadcrumb Management

For simple cases or when navigation is not strictly route-based, you can manually push and remove breadcrumbs.

```vue
<!-- MyComponent.vue -->
<template>
  <VcBreadcrumbs :items="breadcrumbs" />
  <!-- ... rest of your component ... -->
  <VcButton @click="navigateToSection('details')">View Details</VcButton>
</template>

<script lang="ts" setup>
import { useBreadcrumbs, VcBreadcrumbs, VcButton } from '@vc-shell/framework';
import { onMounted } from 'vue';

const { breadcrumbs, push, remove } = useBreadcrumbs();

function navigateToSection(sectionId: string, sectionTitle: string) {
  // Potentially remove existing breadcrumbs if this is a top-level navigation
  // remove(['some-old-id']); 

  push({
    id: sectionId,
    title: sectionTitle,
    clickHandler: () => {
      // Logic to show the specific section or navigate
      console.log(`Navigating to ${sectionId}`);
      // If this click should clear subsequent breadcrumbs:
      // 1. Find index of this breadcrumb
      // 2. Remove all breadcrumbs after it
      const currentIndex = breadcrumbs.value.findIndex(b => b.id === sectionId);
      if (currentIndex !== -1 && currentIndex < breadcrumbs.value.length - 1) {
        const idsToRemove = breadcrumbs.value.slice(currentIndex + 1).map(b => b.id);
        remove(idsToRemove);
      }
      return false; // Or true if it should clear subsequent, depends on logic
    }
  });
}

onMounted(() => {
  // Initialize with a base breadcrumb
  push({
    id: 'componentRoot',
    title: 'My Component Base',
    clickHandler: () => { /* Navigate to component base view */ return true; }
  });
});
</script>
```

### 2. Hierarchical Navigation in VcTable with Breadcrumbs

This pattern illustrates how to use `useBreadcrumbs` with `VcTable` for navigating hierarchical data. The core idea is to push new breadcrumbs as the user drills down and use their `clickHandler` to navigate back up, reloading the table data accordingly.

**Conceptual Structure:**

```vue
<!-- AbstractHierarchicalTable.vue -->
<template>
  <div>
    <VcBreadcrumbs :items="breadcrumbs" class="tw-mb-4" />

    <VcTable
      :items="tableItems"
      @item-click="handleTableItemClick"
      :columns="abstractColumns" 
      :loading="isLoading"
      <!-- ... other essential VcTable props ... -->
    >
      <!-- Abstract slot for item rendering -->
      <template #item_name="{ item }">
        {{ item.name }}
        <span v-if="item.isNavigable"> (Click to open)</span>
      </template>
    </VcTable>
  </div>
</template>

<script lang="ts" setup>
import { useBreadcrumbs, VcBreadcrumbs, VcTable, ITableColumns } from '@vc-shell/framework';
import { ref, onMounted } from 'vue';

// Abstract type for data items
interface AbstractDataItem {
  id: string;
  name: string;
  isNavigable: boolean; // Can this item be drilled into?
  // parentId: string | null; // Conceptually needed for data loading
}

const { breadcrumbs, push: pushBc } = useBreadcrumbs();

const isLoading = ref(false);
const tableItems = ref<AbstractDataItem[]>([]); // Items for the current level
const currentLevelId = ref<string | null>(null); // null for root

// Abstract column definition - in reality, this might change per level
const abstractColumns: ITableColumns[] = [{ id: 'name', field: 'name', title: 'Name', type: 'slot', slotName: 'item_name' }];

// --- Abstract Data Loading ---
async function loadDataForLevel(levelId: string | null): Promise<AbstractDataItem[]> {
  isLoading.value = true;
  console.log(`Abstractly fetching data for level: ${levelId || 'root'}`);

  await new Promise(resolve => setTimeout(resolve, 100)); // Simulate delay
  // Example: Returning a generic item if no specific logic
  if (levelId === 'cat1') {
    tableItems.value = [{ id: 'item1_1', name: 'Sub-Item of ' + levelId, isNavigable: false }];
  } else {
    tableItems.value = [{ id: 'cat1', name: 'Top Level Category 1', isNavigable: true }, { id: 'cat2', name: 'Top Level Category 2', isNavigable: true }];
  }
  isLoading.value = false;
  return tableItems.value;
}

// --- Navigation and Breadcrumb Logic ---

// Called when navigating to a specific level (e.g., by a breadcrumb click)
async function navigateToLevel(levelId: string | null, levelName: string) {
  currentLevelId.value = levelId;
  // The breadcrumb's own clickHandler (which calls this function) returning `true` 
  // signals VcBreadcrumbs to remove subsequent breadcrumbs.
  // Here, we just need to ensure the data for this level is loaded.
  await loadDataForLevel(levelId);
}

// Called when an item in the VcTable is clicked to drill down
async function drillDownTo(item: AbstractDataItem) {
  if (!item.isNavigable) return;

  currentLevelId.value = item.id;

  pushBc({
    id: item.id, // Use a unique ID for the breadcrumb, often the item's ID
    title: item.name,
    clickHandler: async () => {
      // When this breadcrumb is clicked, navigate to this item's level
      await navigateToLevel(item.id, item.name);
      return true; // Essential: removes subsequent breadcrumbs
    }
  });

  await loadDataForLevel(item.id); // Load data for the new (child) level
}

function handleTableItemClick(item: AbstractDataItem) {
  if (item.isNavigable) {
    drillDownTo(item);
  }
}

// --- Initial Setup ---
onMounted(async () => {
  // Setup the root/initial breadcrumb
  pushBc({
    id: 'root', // A fixed, unique ID for the base level
    title: 'Home', // Or "All Items", "Categories", etc.
    clickHandler: async () => {
      await navigateToLevel(null, 'Home'); // Navigate to root level
      return true; // Remove any other breadcrumbs
    }
  });
  await loadDataForLevel(null); // Load data for the root level
});

</script>
```

**Core Principles Illustrated:**

1.  **Initial Breadcrumb:** On mount, a root breadcrumb is pushed. Its `clickHandler` navigates to the top level and returns `true` (to clear any other breadcrumbs).
2.  **Drilling Down (`drillDownTo` / `handleTableItemClick`):**
    *   When a navigable item in `VcTable` is clicked, a new breadcrumb is `push`ed.
    *   This new breadcrumb's `id` should be unique (e.g., the item's ID).
    *   Its `clickHandler` is set up to call `navigateToLevel` for its own level and crucially **return `true`**.
    *   Data for the new, deeper level is then loaded into the `VcTable`.
3.  **Navigating Via Breadcrumb Click (`navigateToLevel`):**
    *   The `clickHandler` of any breadcrumb (including the root) calls a function like `navigateToLevel`.
    *   This function reloads the `VcTable` data appropriate for that breadcrumb's level.
    *   Because the `clickHandler` returned `true`, `VcBreadcrumbs` automatically handles removing any breadcrumbs that were to the right of the one clicked.
4.  **Abstract Data Loading (`loadDataForLevel`):** Represents fetching and setting `tableItems.value` based on the current hierarchy level (`levelId`).

This abstract example focuses on the interaction points with `useBreadcrumbs` and `VcTable` for hierarchical navigation, omitting detailed data management or complex UI logic to keep the core concept clear.

### 3. Dynamic Breadcrumbs based on Data (e.g., Product Navigation)

Often, breadcrumb titles need to come from fetched data, like a product name or category name.

```typescript
// Inside a composable like useProductView.ts or a component setup
import { useBreadcrumbs, VcBreadcrumbs } from '@vc-shell/framework';
import { useRouter } from 'vue-router';
import { ref, computed, watch, onMounted } from 'vue';
// Assume: import { fetchProductById, fetchCategoryById } from './apiService';

const { breadcrumbs, push, remove } = useBreadcrumbs();
const router = useRouter();
const currentProduct = ref(null);
const currentCategory = ref(null);

async function loadProductAndSetBreadcrumbs(productId: string) {
  // 0. Clear product-specific breadcrumbs if any
  //    (e.g., remove all after 'Products' breadcrumb)

  // 1. Ensure base breadcrumbs are present (e.g., Home > Products)
  // This part might be handled globally or pushed here if not already present
  if (!breadcrumbs.value.find(b => b.id === 'products')) {
    push({
      id: 'products',
      title: 'All Products',
      clickHandler: () => { router.push('/products'); return true; }
    });
  }
  
  // 2. Fetch product data
  // currentProduct.value = await fetchProductById(productId);
  currentProduct.value = { id: productId, name: `Awesome Gadget ${productId}`, categoryId: 'cat123' }; // Mock

  // 3. (Optional) Fetch category data if product breadcrumb needs category context
  // currentCategory.value = await fetchCategoryById(currentProduct.value.categoryId);
  currentCategory.value = { id: 'cat123', name: 'Electronics' }; // Mock

  // Push category breadcrumb if applicable and not already there
  if (currentCategory.value && !breadcrumbs.value.find(b => b.id === currentCategory.value.id)) {
     push({
      id: currentCategory.value.id,
      // Title can be a ComputedRef if category name might change reactively
      title: computed(() => currentCategory.value?.name || 'Category'), 
      clickHandler: () => { router.push(`/category/${currentCategory.value.id}`); return true; }
    });
  }

  // 4. Push product breadcrumb
  if (currentProduct.value) {
    push({
      id: `product-${currentProduct.value.id}`,
      // Title can be a ComputedRef if product name might change reactively
      title: computed(() => currentProduct.value?.name || 'Product'), 
      clickHandler: () => { router.push(`/product/${currentProduct.value.id}`); return true; }
    });
  }
}

// Example usage: call this when navigating to a product page
// onMounted(() => {
//   const productId = route.params.id;
//   if (productId) loadProductAndSetBreadcrumbs(productId.toString());
// });

// Watch for route changes to update breadcrumbs
// watch(() => route.params.id, (newId) => { /* ... re-evaluate ... */ });
```
This pattern shows how to add breadcrumbs that depend on asynchronous data. The `title` can be a `ComputedRef` to ensure it updates if the underlying data (e.g., `currentProduct.value.name`) changes.

## Best Practices

1.  **Unique IDs**: Ensure every breadcrumb has a truly unique `id`. This is critical for `remove` to work correctly and for `push` to avoid unintended duplicates or replacements.
2.  **Reactive Titles**: If a breadcrumb title depends on data that might change (e.g., an item's name being edited), make the `title` a `ComputedRef<string>`.
3.  **`clickHandler` Logic**: The `clickHandler` should correctly navigate the user AND return `true` if the breadcrumb trail should be truncated at that point. If it returns `false` or nothing, `VcBreadcrumbs` (if used) might not clear subsequent items.
4.  **Clear on `remove()`**: When removing breadcrumbs, be precise with the IDs. Removing the wrong breadcrumbs can confuse users.

By following these strategies and best practices, you can leverage `useBreadcrumbs` to build intuitive and effective navigation aids in your VC-Shell applications.

