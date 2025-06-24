# How-To: Managing Loading States with `useLoading`

The `useLoading` composable provides an elegant solution for combining multiple loading states in VC-Shell applications. This guide demonstrates how to effectively manage complex loading scenarios where multiple asynchronous operations need to be tracked simultaneously.

## Prerequisites

- Understanding of Vue 3 Composition API, including `ref` and `computed`.
- Familiarity with the `useLoading` composable (see [useLoading API Reference](../composables/useLoading.md)).
- Basic knowledge of the `useAsync` composable for asynchronous operations.
- Understanding of reactive state management in Vue applications.

## Core Concept

The `useLoading` composable takes multiple boolean reactive references and returns a computed property that indicates whether any of those states are currently `true`. This pattern is essential for:

- **Unified Loading Indicators**: Show a single loading state while multiple operations are in progress
- **UI State Management**: Disable forms or buttons during any ongoing operation
- **User Experience**: Provide clear feedback when multiple background tasks are running
- **Performance Optimization**: Avoid redundant API calls while operations are pending

```typescript
import { useLoading } from '@vc-shell/framework';

const isLoading = useLoading(loadingState1, loadingState2, loadingState3);
// isLoading.value will be true if ANY of the individual states are true
```

## Implementation Strategies

### 1. Basic Data Loading Coordination

Coordinate multiple data fetching operations for a complete page load:

```vue
<!-- DashboardPage.vue -->
<template>
  <div class="dashboard-page">
    <VcLoading v-if="isLoadingData" overlay />
    
    <div v-else class="dashboard-content">
      <div class="stats-section">
        <StatsWidget :data="statsData" />
      </div>
      
      <div class="charts-section">
        <SalesChart :data="salesData" />
        <OrdersChart :data="ordersData" />
      </div>
      
      <div class="tables-section">
        <RecentOrders :orders="recentOrders" />
        <TopProducts :products="topProducts" />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { useAsync, useLoading, VcLoading } from '@vc-shell/framework';

// Individual data states
const statsData = ref(null);
const salesData = ref([]);
const ordersData = ref([]);
const recentOrders = ref([]);
const topProducts = ref([]);

// Create async operations for each data source
const { loading: loadingStats, action: fetchStats } = useAsync(async () => {
  const response = await api.getStats();
  statsData.value = response;
});

const { loading: loadingSales, action: fetchSales } = useAsync(async () => {
  const response = await api.getSalesData();
  salesData.value = response;
});

const { loading: loadingOrders, action: fetchOrdersData } = useAsync(async () => {
  const response = await api.getOrdersData();
  ordersData.value = response;
});

const { loading: loadingRecentOrders, action: fetchRecentOrders } = useAsync(async () => {
  const response = await api.getRecentOrders();
  recentOrders.value = response;
});

const { loading: loadingTopProducts, action: fetchTopProducts } = useAsync(async () => {
  const response = await api.getTopProducts();
  topProducts.value = response;
});

// Combine all loading states
const isLoadingData = useLoading(
  loadingStats,
  loadingSales,
  loadingOrders,
  loadingRecentOrders,
  loadingTopProducts
);

onMounted(async () => {
  // Start all data fetching operations
  await Promise.all([
    fetchStats(),
    fetchSales(),
    fetchOrdersData(),
    fetchRecentOrders(),
    fetchTopProducts()
  ]);
});
</script>
```

### 2. Form Operations with Multiple Actions

Manage loading states for forms with multiple possible actions:

```vue
<!-- ProductForm.vue -->
<template>
  <form @submit.prevent="handleSubmit">
    <div class="form-fields">
      <VcInput 
        v-model="product.name" 
        label="Product Name" 
        :disabled="isAnyOperationRunning"
      />
      <VcInput 
        v-model="product.price" 
        label="Price" 
        type="number"
        :disabled="isAnyOperationRunning"
      />
      <VcTextarea 
        v-model="product.description" 
        label="Description"
        :disabled="isAnyOperationRunning"
      />
    </div>
    
    <div class="form-actions">
      <VcButton 
        type="submit" 
        :loading="isSaving"
        :disabled="isAnyOperationRunning"
      >
        Save Product
      </VcButton>
      
      <VcButton 
        variant="outline"
        :loading="isValidating"
        :disabled="isAnyOperationRunning"
        @click="validateProduct"
      >
        Validate
      </VcButton>
      
      <VcButton 
        variant="outline"
        :loading="isPublishing"
        :disabled="isAnyOperationRunning"
        @click="publishProduct"
      >
        Save & Publish
      </VcButton>
      
      <VcButton 
        variant="danger"
        :loading="isDeleting"
        :disabled="isAnyOperationRunning"
        @click="deleteProduct"
      >
        Delete
      </VcButton>
    </div>
    
    <div v-if="isAnyOperationRunning" class="operation-status">
      <VcLoading size="sm" />
      <span>Processing...</span>
    </div>
  </form>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue';
import { useAsync, useLoading, VcButton, VcInput, VcTextarea, VcLoading } from '@vc-shell/framework';

interface Props {
  productId?: string;
}

const props = defineProps<Props>();

const product = ref({
  name: '',
  price: 0,
  description: ''
});

// Individual operation states
const { loading: isSaving, action: saveProduct } = useAsync(async () => {
  await api.saveProduct(product.value);
  notification.success('Product saved successfully');
});

const { loading: isValidating, action: validateProduct } = useAsync(async () => {
  const errors = await api.validateProduct(product.value);
  if (errors.length === 0) {
    notification.success('Product validation passed');
  } else {
    notification.error('Product validation failed');
  }
});

const { loading: isPublishing, action: publishProduct } = useAsync(async () => {
  await api.saveProduct(product.value);
  await api.publishProduct(product.value.id);
  notification.success('Product saved and published');
});

const { loading: isDeleting, action: deleteProduct } = useAsync(async () => {
  await api.deleteProduct(props.productId);
  notification.success('Product deleted');
  router.push('/products');
});

// Combine all operation states
const isAnyOperationRunning = useLoading(
  isSaving,
  isValidating,
  isPublishing,
  isDeleting
);

function handleSubmit() {
  saveProduct();
}
</script>
```

### 3. Hierarchical Loading States

Create different loading contexts for different parts of your application:

```vue
<!-- ProductManagement.vue -->
<template>
  <div class="product-management">
    <!-- Header with global actions -->
    <div class="header">
      <h1>Product Management</h1>
      <VcButton 
        :loading="isImporting"
        :disabled="isAnyGlobalOperation"
        @click="importProducts"
      >
        Import Products
      </VcButton>
      <VcButton 
        :loading="isExporting"
        :disabled="isAnyGlobalOperation"
        @click="exportProducts"
      >
        Export Products
      </VcButton>
    </div>
    
    <!-- Search and filters -->
    <div class="filters" :class="{ 'tw-opacity-50': isLoadingData }">
      <VcInput 
        v-model="searchQuery" 
        placeholder="Search products..."
        :disabled="isLoadingData"
        @input="searchProducts"
      />
      <VcSelect 
        v-model="selectedCategory"
        :options="categories"
        :disabled="isLoadingData"
        @change="filterProducts"
      />
    </div>
    
    <!-- Product list -->
    <div class="product-list">
      <VcLoading v-if="isLoadingData" />
      
      <VcTable 
        v-else
        :items="products"
        :loading="isBulkOperating"
        @bulk-action="handleBulkAction"
      >
        <template #actions="{ item }">
          <VcButton 
            size="sm"
            :loading="isUpdatingProduct(item.id)"
            :disabled="isAnyProductOperation"
            @click="updateProduct(item)"
          >
            Update
          </VcButton>
          <VcButton 
            size="sm"
            variant="danger"
            :loading="isDeletingProduct(item.id)"
            :disabled="isAnyProductOperation"
            @click="deleteProduct(item.id)"
          >
            Delete
          </VcButton>
        </template>
      </VcTable>
    </div>
    
    <!-- Global loading overlay for major operations -->
    <VcLoading v-if="isAnyGlobalOperation" overlay />
  </div>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue';
import { useAsync, useLoading } from '@vc-shell/framework';

const searchQuery = ref('');
const selectedCategory = ref('');
const products = ref([]);
const categories = ref([]);

// Data loading operations
const { loading: loadingProducts, action: fetchProducts } = useAsync(async () => {
  const response = await api.getProducts({ search: searchQuery.value, category: selectedCategory.value });
  products.value = response;
});

const { loading: loadingCategories, action: fetchCategories } = useAsync(async () => {
  const response = await api.getCategories();
  categories.value = response;
});

// Global operations
const { loading: isImporting, action: importProducts } = useAsync(async () => {
  await api.importProducts();
  await fetchProducts(); // Refresh data
});

const { loading: isExporting, action: exportProducts } = useAsync(async () => {
  await api.exportProducts();
});

// Product-specific operations
const { loading: isBulkOperating, action: handleBulkAction } = useAsync(async (action, items) => {
  await api.bulkAction(action, items);
  await fetchProducts(); // Refresh data
});

const updatingProducts = ref(new Set());
const deletingProducts = ref(new Set());

// Individual product operations
async function updateProduct(product) {
  updatingProducts.value.add(product.id);
  try {
    await api.updateProduct(product);
    await fetchProducts();
  } finally {
    updatingProducts.value.delete(product.id);
  }
}

async function deleteProduct(productId) {
  deletingProducts.value.add(productId);
  try {
    await api.deleteProduct(productId);
    await fetchProducts();
  } finally {
    deletingProducts.value.delete(productId);
  }
}

// Computed loading states for different contexts
const isLoadingData = useLoading(loadingProducts, loadingCategories);
const isAnyGlobalOperation = useLoading(isImporting, isExporting);
const isAnyProductOperation = computed(() => 
  isBulkOperating.value || updatingProducts.value.size > 0 || deletingProducts.value.size > 0
);

// Helper functions for individual product states
const isUpdatingProduct = (productId) => updatingProducts.value.has(productId);
const isDeletingProduct = (productId) => deletingProducts.value.has(productId);

// Search and filter functions
const { loading: isSearching, action: searchProducts } = useAsync(async () => {
  await fetchProducts();
});

const { loading: isFiltering, action: filterProducts } = useAsync(async () => {
  await fetchProducts();
});
</script>
```

### 4. API Client Integration

Combine `useLoading` with API clients for comprehensive state management:

```typescript
// useProductOperations.ts
import { useApiClient, useAsync, useLoading } from '@vc-shell/framework';
import { ProductsClient } from '@your-api-package';

export function useProductOperations() {
  const { getApiClient } = useApiClient(ProductsClient);

  // Individual operations
  const { loading: isCreating, action: createProduct } = useAsync(async (productData) => {
    const client = await getApiClient();
    return await client.createProduct(productData);
  });

  const { loading: isUpdating, action: updateProduct } = useAsync(async (product) => {
    const client = await getApiClient();
    return await client.updateProduct(product);
  });

  const { loading: isDeleting, action: deleteProduct } = useAsync(async (productId) => {
    const client = await getApiClient();
    return await client.deleteProduct(productId);
  });

  const { loading: isValidating, action: validateProduct } = useAsync(async (product) => {
    const client = await getApiClient();
    return await client.validateProduct(product);
  });

  const { loading: isPublishing, action: publishProduct } = useAsync(async (productId) => {
    const client = await getApiClient();
    return await client.publishProduct(productId);
  });

  // Combined loading states for different contexts
  const isMutating = useLoading(isCreating, isUpdating, isDeleting);
  const isProcessing = useLoading(isValidating, isPublishing);
  const isAnyOperation = useLoading(isCreating, isUpdating, isDeleting, isValidating, isPublishing);

  return {
    // Individual operations
    createProduct,
    updateProduct,
    deleteProduct,
    validateProduct,
    publishProduct,
    
    // Individual loading states
    isCreating,
    isUpdating,
    isDeleting,
    isValidating,
    isPublishing,
    
    // Combined loading states
    isMutating,
    isProcessing,
    isAnyOperation
  };
}
```

### 5. Complex Workflow Management

Handle multi-step workflows with dependent operations:

```typescript
// useProductWorkflow.ts
import { useAsync, useLoading } from '@vc-shell/framework';

export function useProductWorkflow() {
  // Step 1: Validation
  const { loading: isValidating, action: validateProduct } = useAsync(async (product) => {
    const errors = await api.validateProduct(product);
    if (errors.length > 0) {
      throw new Error('Validation failed');
    }
    return true;
  });

  // Step 2: Save draft
  const { loading: isSavingDraft, action: saveDraft } = useAsync(async (product) => {
    return await api.saveProductDraft(product);
  });

  // Step 3: Upload images
  const { loading: isUploadingImages, action: uploadImages } = useAsync(async (productId, images) => {
    return await api.uploadProductImages(productId, images);
  });

  // Step 4: Final publication
  const { loading: isPublishing, action: publishProduct } = useAsync(async (productId) => {
    return await api.publishProduct(productId);
  });

  // Combined states for different workflow phases
  const isPreparingProduct = useLoading(isValidating, isSavingDraft);
  const isFinalizingProduct = useLoading(isUploadingImages, isPublishing);
  const isWorkflowRunning = useLoading(isValidating, isSavingDraft, isUploadingImages, isPublishing);

  // Complete workflow function
  const { loading: isRunningWorkflow, action: runCompleteWorkflow } = useAsync(async (product, images) => {
    // Step 1: Validate
    await validateProduct(product);
    
    // Step 2: Save draft
    const savedProduct = await saveDraft(product);
    
    // Step 3: Upload images
    if (images && images.length > 0) {
      await uploadImages(savedProduct.id, images);
    }
    
    // Step 4: Publish
    await publishProduct(savedProduct.id);
    
    return savedProduct;
  });

  return {
    // Individual steps
    validateProduct,
    saveDraft,
    uploadImages,
    publishProduct,
    
    // Complete workflow
    runCompleteWorkflow,
    
    // Loading states
    isValidating,
    isSavingDraft,
    isUploadingImages,
    isPublishing,
    isRunningWorkflow,
    
    // Combined states
    isPreparingProduct,
    isFinalizingProduct,
    isWorkflowRunning
  };
}
```

## Best Practices

1. **Logical Grouping**: Group related loading states together based on their UI impact and user context.

2. **Granular Control**: Create multiple combined loading states for different parts of your UI rather than one global state.

3. **User Experience**: Use loading states to provide appropriate feedback and disable relevant UI elements.

4. **Performance**: Avoid unnecessary re-renders by being selective about which loading states to combine.

5. **Error Handling**: Remember that loading states don't handle errors - combine with proper error handling patterns.

6. **Accessibility**: Ensure loading states are properly announced to screen readers and provide meaningful feedback.

7. **Testing**: Test loading state combinations to ensure they behave correctly in all scenarios.

## Integration with Other Composables

### With useAsync
```typescript
// Perfect combination for managing async operations
const { loading: loadingData, action: fetchData } = useAsync(async () => {
  // Async operation
});

const { loading: savingData, action: saveData } = useAsync(async (data) => {
  // Save operation
});

const isAnyOperation = useLoading(loadingData, savingData);
```

### With API Clients
```typescript
// Combine with useApiClient for comprehensive state management
const { getApiClient } = useApiClient(MyApiClient);
const { loading: isLoading, action: performOperation } = useAsync(async () => {
  const client = await getApiClient();
  return await client.someOperation();
});
```

By following these patterns and best practices, you can create sophisticated loading state management that provides excellent user experience while maintaining clean and maintainable code.
