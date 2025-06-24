# useLoading Composable

The `useLoading` composable provides a simple yet powerful way to track and combine multiple loading states in Vue applications. This utility is particularly useful when you need to monitor several asynchronous operations and determine if any of them are in progress.

The `useLoading` composable accepts multiple boolean reactive references (Refs) representing individual loading states and returns a computed property that indicates whether any of those states are currently `true`. This pattern is commonly used to show loading indicators while waiting for multiple API calls or asynchronous operations to complete.

## API Reference

### Parameters

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `...args` | `Readonly<Ref<boolean>>[]` | A list of boolean reactive references representing individual loading states |

### Return value

| Type | Description |
| ---- | ----------- |
| `ComputedRef<boolean>` | A computed boolean that is `true` if any of the passed loading states are `true`, otherwise `false` |

## Usage

```typescript
import { ref } from 'vue';
import { useLoading } from '@vc-shell/framework';

// Create individual loading states
const isLoadingData = ref(false);
const isSubmitting = ref(false);

// Combine loading states
const isLoading = useLoading(isLoadingData, isSubmitting);

// Now isLoading.value will be true if either isLoadingData OR isSubmitting is true
```

### With useAsync composable

```typescript
import { useAsync, useLoading } from '@vc-shell/framework';

const { loading: loadingUsers, action: fetchUsers } = useAsync(async () => {
  return await api.getUsers();
});

const { loading: loadingRoles, action: fetchRoles } = useAsync(async () => {
  return await api.getRoles();
});

// Combine loading states
const isLoading = useLoading(loadingUsers, loadingRoles);
```

## Interface

The `useLoading` composable is also exported with a `HasLoading` interface that can be used for type definitions:

```typescript
export interface HasLoading {
  loading: Readonly<Ref<boolean>>;
}

// Example usage in a function that accepts components with loading states
function setupComponent(component: HasLoading) {
  // Now TypeScript knows that component has a loading property
  watch(component.loading, (isLoading) => {
    console.log(`Loading state changed: ${isLoading}`);
  });
}
```

## Key features

- **Multiple state combination**: Combines any number of boolean reactive references into a single computed state
- **Reactive updates**: Automatically updates when any of the input loading states change
- **Type safety**: Fully typed with TypeScript for reliable development experience
- **Performance optimized**: Uses Vue's computed properties for efficient reactivity
- **Framework integration**: Works seamlessly with `useAsync` and other VC-Shell composables

## Important notes

- The composable returns `true` if **any** of the input loading states are `true`
- All input parameters must be `Readonly<Ref<boolean>>` (reactive boolean references)
- The returned computed property is read-only and updates automatically
- Commonly used with `useAsync` composable for managing multiple asynchronous operations
- Ideal for coordinating UI states across multiple concurrent operations

## Related resources

- [Managing loading states guide](../Usage-Guides/managing-loading-states-with-useloading.md) - Comprehensive guide with practical examples
- [useAsync composable](./useAsync.md) - For handling asynchronous operations with built-in loading states
