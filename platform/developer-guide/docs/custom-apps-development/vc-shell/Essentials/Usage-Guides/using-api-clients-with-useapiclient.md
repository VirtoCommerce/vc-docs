# How-To: Using API Clients with `useApiClient`

The `useApiClient` composable provides a standardized way to access authenticated API clients in VC-Shell applications. This guide demonstrates how to effectively use API clients for data fetching, CRUD operations, and integration with other composables.

## Prerequisites

- Understanding of Vue 3 Composition API, including `async/await` and reactive state.
- Familiarity with the `useApiClient` composable (see [useApiClient API Reference](../composables/useApiClient.md)).
- Basic knowledge of TypeScript interfaces and API client classes.
- Understanding of VC-Shell's composable patterns and data management.

## Core Concept

`useApiClient` creates authenticated API client instances that handle:

- **Authentication**: Automatic token management for API requests
- **Base URL Configuration**: Proper endpoint resolution
- **Type Safety**: Full TypeScript support for API operations
- **Consistent Interface**: Standardized way to access different API services

The composable takes an API client class and returns a factory function that provides authenticated instances.

```typescript
import { useApiClient } from '@vc-shell/framework';
import { VcmpSellerCatalogClient } from '@your-api-package';

const { getApiClient } = useApiClient(VcmpSellerCatalogClient);

// Get authenticated client instance
const client = await getApiClient();
const result = await client.searchProducts(query);
```

## Implementation Patterns

### 1. Basic API Client Setup

The most common pattern is to set up API clients at the module level:

```typescript
// Module-level API client setup
import { useApiClient } from '@vc-shell/framework';
import { 
  VcmpSellerCatalogClient,
  VcmpPublicationRequestClient,
  StateMachineClient 
} from '@your-api-package';

// Create API client factories
const { getApiClient } = useApiClient(VcmpSellerCatalogClient);
const { getApiClient: getRequestApiClient } = useApiClient(VcmpPublicationRequestClient);
const { getApiClient: getStateMachineApiClient } = useApiClient(StateMachineClient);
```

### 2. API Client in Data Loading

Use API clients for loading and fetching data in composables:

```typescript
// Loading data with API client
async function loadProductDetails(productId: string) {
  const client = await getApiClient();
  const product = await client.getProductById(productId);
  return product;
}

// Search with query parameters
async function searchProducts(query: ISearchProductsQuery) {
  const client = await getApiClient();
  const searchQuery = new SearchProductsQuery(query);
  return await client.searchProducts(searchQuery);
}
```

### 3. CRUD Operations Pattern

Implement create, read, update, delete operations using API clients:

```typescript
// CRUD operations with API clients
const productOperations = {
  // Create
  async create(productData: ProductDetails) {
    const client = await getApiClient();
    const command = new CreateNewProductCommand({
      sellerId: await getSellerId(),
      productDetails: productData
    });
    return await client.createNewProduct(command);
  },

  // Read
  async getById(id: string) {
    const client = await getApiClient();
    return await client.getProductById(id);
  },

  // Update
  async update(product: IProductDetails) {
    const client = await getApiClient();
    const command = new UpdateProductDetailsCommand({
      sellerId: await getSellerId(),
      sellerProductId: product.id,
      productDetails: new ProductDetails(product)
    });
    return await client.updateProductDetails(command);
  },

  // Delete
  async remove(productIds: string[]) {
    const client = await getApiClient();
    return await client.deleteProducts(productIds);
  }
};
```

### 4. Multiple API Clients in One Composable

Use multiple API clients when working with different services:

```typescript
// Multiple API clients for different operations
export function useProductManagement() {
  const { getApiClient } = useApiClient(VcmpSellerCatalogClient);
  const { getApiClient: getRequestApiClient } = useApiClient(VcmpPublicationRequestClient);
  const { getApiClient: getStateMachineApiClient } = useApiClient(StateMachineClient);

  async function saveAndSubmitForApproval(product: IProductDetails) {
    // Save product using catalog client
    const catalogClient = await getApiClient();
    const savedProduct = await catalogClient.updateProductDetails(command);

    // Submit for approval using request client
    const requestClient = await getRequestApiClient();
    const requestCommand = new CreateSmPublicationRequestCommand({
      sellerId: await getSellerId(),
      productId: savedProduct.id
    });
    await requestClient.createNewPublicationRequest(requestCommand);

    return savedProduct;
  }
}
```

### 5. API Client with Search and Pagination

Handle search operations with pagination using API clients:

```typescript
// Search with pagination
export function useProductSearch() {
  const { getApiClient } = useApiClient(VcmpSellerCatalogClient);
  
  async function searchWithPagination(searchParams: {
    keyword?: string;
    skip?: number;
    take?: number;
    sort?: string;
  }) {
    const client = await getApiClient();
    const query = new SearchProductsQuery({
      sellerId: await getSellerId(),
      ...searchParams
    });
    
    return await client.searchProducts(query);
  }

  async function searchCategories(keyword?: string, skip = 0, ids?: string[]) {
    const client = await getApiClient();
    return await client.searchCategories(
      new SearchCategoriesQuery({
        sellerId: await getSellerId(),
        objectIds: ids,
        keyword,
        skip,
        take: 20
      })
    );
  }
}
```

### 6. API Client with Validation

Use API clients for data validation operations:

```typescript
// Validation using API client
export function useProductValidation() {
  const { getApiClient } = useApiClient(VcmpSellerCatalogClient);

  async function validateProduct(product: ISellerProduct) {
    const client = await getApiClient();
    const query = new ValidateProductQuery({
      sellerProduct: new SellerProduct(product)
    });
    
    try {
      return await client.validateProduct(query);
    } catch (error) {
      console.error('Validation failed:', error);
      throw error;
    }
  }

  async function validateGtin(gtin: string, productId?: string) {
    const product = { gtin, id: productId } as ISellerProduct;
    const errors = await validateProduct(product);
    return errors.filter(error => 
      error.propertyName?.toLowerCase() === 'gtin'
    );
  }
}
```

## Integration with Other Composables

### With useAsync

Combine `useApiClient` with `useAsync` for loading state management:

```typescript
import { useAsync, useApiClient } from '@vc-shell/framework';

export function useProductLoader() {
  const { getApiClient } = useApiClient(VcmpSellerCatalogClient);

  const { action: loadProduct, loading } = useAsync(async (productId: string) => {
    const client = await getApiClient();
    return await client.getProductById(productId);
  });

  return {
    loadProduct,
    loading
  };
}
```

## Error Handling

Always implement proper error handling when using API clients:

```typescript
// Error handling pattern
export function useProductOperations() {
  const { getApiClient } = useApiClient(VcmpSellerCatalogClient);

  async function safeApiCall<T>(operation: () => Promise<T>): Promise<T | null> {
    try {
      return await operation();
    } catch (error) {
      console.error('API operation failed:', error);
      
      // Handle specific error types
      if (error.status === 404) {
        console.warn('Resource not found');
      } else if (error.status === 403) {
        console.warn('Access denied');
      }
      
      throw error; // Re-throw for caller to handle
    }
  }

  async function loadProductSafely(id: string) {
    return safeApiCall(async () => {
      const client = await getApiClient();
      return await client.getProductById(id);
    });
  }
}
```

## Best Practices

* **Consistent Naming**: Use descriptive names for API client factories.

* **Error Handling**: Always wrap API calls in try-catch blocks and provide meaningful error messages.

* **Type Safety**: Use proper TypeScript interfaces and command classes for API operations.

* **Reusability**: Create reusable functions for common API operations within your composables.

* **Authentication**: Let `useApiClient` handle authentication automatically - don't manually manage tokens.

* **Resource Cleanup**: API clients are automatically managed, no manual cleanup required.

By following these patterns and best practices, you can effectively use `useApiClient` to build robust and maintainable API integrations in your VC-Shell applications.
