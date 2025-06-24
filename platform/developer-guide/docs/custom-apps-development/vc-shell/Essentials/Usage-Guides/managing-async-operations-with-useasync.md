# Effectively Managing Asynchronous Operations with `useAsync`

Asynchronous operations, such as API calls, data fetching, or complex computations, are a fundamental part of modern web applications. The `useAsync` composable in VC-Shell provides a structured and simplified way to handle these operations, primarily by managing loading states around your asynchronous logic and helping to write cleaner code.

## Prerequisites

-   Solid understanding of JavaScript Promises and `async/await` syntax.
-   Familiarity with Vue 3 Composition API.
-   Basic knowledge of the `useAsync` composable (see [useAsync API Reference](../composables/useAsync.md)).

## Core Concept

The `useAsync` composable wraps an asynchronous function you provide (referred to as `innerAction`). It returns an object containing:

1.  `action`: A new function. When you call this `action` function (optionally with a payload), it executes your `innerAction`.
2.  `loading`: A reactive boolean `Ref` (`Readonly<Ref<boolean>>`) that automatically becomes `true` just before your `innerAction` starts and `false` once it completes (either successfully or with an error).

**Important**: `useAsync` itself **does not handle error catching or data assignment** from your `innerAction`. Your `innerAction` is responsible for its own `try...catch` blocks, updating relevant reactive state (like `ref`s for data or error messages), and managing the outcome of the promise. `useAsync` will log errors from `innerAction` to the console and re-throw them, allowing the calling code to also act upon them if needed.

`useAsync` is generic, allowing you to specify types for the `payload` of your `innerAction` and the `Result` it might return.

```typescript
// Generic signature:
// useAsync<Payload = void, Result = void>(innerAction: (payload?: Payload, ...rest: any[]) => Promise<Result>)

// Example: innerAction updates refs directly, no specific payload or return type beyond Promise<void>
const { action, loading } = useAsync<void, void>(async () => {
  // ... perform async task, update refs, handle errors ...
});

// Example: innerAction takes a payload and returns a specific result type
const { action, loading } = useAsync<MyPayload, MyResult>(async (payload: MyPayload): Promise<MyResult> => {
  // ... use payload, perform async task, update refs, handle errors, return result ...
});
```

## Examples

Let's explore common use cases for `useAsync`.

### 1. Basic Data Fetching

This example demonstrates fetching data, updating reactive state, and handling errors within the `innerAction`. The `loading` state is used to provide UI feedback.

```vue
<template>
  <div>
    <VcButton @click="fetchAndSetItems" :disabled="isLoadingItems">
      {{ isLoadingItems ? 'Loading Items...' : 'Refresh Items' }}
    </VcButton>

    <VcLoading v-if="isLoadingItems" class="tw-mt-2" />

    <div v-if="!isLoadingItems && items.length" class="item-list tw-mt-2">
      <div v-for="item in items" :key="item.id" class="item">
        <h4>{{ item.name }}</h4>
      </div>
    </div>
    <VcAlert v-if="itemError" color="danger" title="Error Loading Items" class="tw-mt-2">
      {{ itemError }}
    </VcAlert>
    <p v-if="!isLoadingItems && !items.length && !itemError && attemptedLoad">
      No items found.
    </p>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { useAsync, VcButton, VcLoading, VcAlert, notification } from '@vc-shell/framework'; // Assuming useNotifications is desired

interface Item {
  id: string;
  name: string;
}

const items = ref<Item[]>([]);
const itemError = ref<string | null>(null);
const attemptedLoad = ref(false); // To know if a load was tried, for 'No items found' message

// Define the asynchronous operation for useAsync
const { action: fetchAndSetItems, loading: isLoadingItems } = useAsync<void, void>(async () => {
  itemError.value = null;
  attemptedLoad.value = true;
  try {
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 1000));
    // Example: const response = await fetch('/api/items');
    // if (!response.ok) throw new Error(`API Error: ${response.status}`);
    // const data = await response.json();

    const mockData: Item[] = [{ id: '1', name: 'Sample Item 1' }, { id: '2', name: 'Sample Item 2' }];
    items.value = mockData;

    if (mockData.length) {
      notification.success('Successfully fetched items.');
    }
  } catch (err: any) {
    console.error('Fetch Items Error:', err);
    items.value = []; // Clear items on error
    itemError.value = err.message || 'Could not fetch items.';
    notification.error(itemError.value);
    throw err; // Re-thrown by useAsync implicitly after it logs it
  }
});

// Optional: Load on component mount
// import { onMounted } from 'vue';
// onMounted(fetchAndSetItems);
</script>

<style scoped>
.item-list { margin-top: 1rem; }
.item { border: 1px solid #eee; padding: 0.5rem; margin-bottom: 0.5rem; }
</style>
```

**Key points from this example:**

- `useAsync<void, void>`: Used when `innerAction` doesn't take a specific payload and its primary job is to cause side effects (like updating refs) rather than returning a specific value to the caller of `action`.
- `isLoadingItems`: Directly used from `useAsync` to disable the button and show a loading indicator.
- Error Handling: `try...catch` is *inside* `innerAction`. `itemError` ref is updated for UI display. `useNotifications` is used for global feedback. The error is then re-thrown.
- Data Assignment: `items.value` is updated directly within `innerAction`.

### 2. Action with Payload and Typed Result

This example demonstrates passing a payload to the `action` function, using TypeScript generics for `Payload` and `Result` types, and handling the `Promise<Result>` returned by `action`.

```vue
<template>
  <div>
    <VcInput v-model="entityIdToFetch" placeholder="Enter Entity ID (e.g., 42 or 'fail')" />
    <VcButton @click="handleLoadEntity" :disabled="isLoadingEntity" class="tw-ml-2">
      {{ isLoadingEntity ? 'Loading...' : 'Load Entity' }}
    </VcButton>

    <VcLoading v-if="isLoadingEntity" class="tw-mt-2" />
    
    <div v-if="entityData" class="entity-details tw-mt-2">
      <p>ID: {{ entityData.id }}</p>
      <p>Value: {{ entityData.value }}</p>
    </div>

    <VcAlert v-if="entityFetchError" color="danger" title="Fetch Error" class="tw-mt-2">
      {{ entityFetchError }}
    </VcAlert>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { useAsync, VcButton, VcLoading, VcAlert, VcInput, notification } from '@vc-shell/framework';

interface Entity {
  id: string;
  value: string;
}

interface FetchEntityPayload {
  id: string;
}

const entityIdToFetch = ref('42');
const entityData = ref<Entity | null>(null);
const entityFetchError = ref<string | null>(null);

// innerAction takes a FetchEntityPayload and is expected to return a Promise<Entity>
const { action: loadEntityAction, loading: isLoadingEntity } = useAsync<FetchEntityPayload, Entity>(
  async (payload: FetchEntityPayload): Promise<Entity> => {
    entityFetchError.value = null; // Clear previous errors
    entityData.value = null;       // Clear previous data
    try {
      await new Promise(resolve => setTimeout(resolve, 1200)); // Simulate API delay

      if (!payload || !payload.id) {
        throw new Error('Entity ID is required for fetching.');
      }
      if (payload.id === 'fail') {
        throw new Error('Simulated server error: Entity cannot be fetched.');
      }

      // Simulate a successful API response
      const fetchedEntity: Entity = { id: payload.id, value: `Details for entity ${payload.id}` };
      // Note: We could assign to entityData.value here, or rely on the return value as shown below.
      notification.info(`Data for entity ${fetchedEntity.id} loaded.`);
      return fetchedEntity;
    } catch (err: any) {
      entityFetchError.value = err.message || 'An unknown error occurred.';
      notification.error(entityFetchError.value);
      throw err; // Re-throw for useAsync to log and for the caller of `action` to catch
    }
  }
);

// Wrapper function to call the action and handle its promise
async function handleLoadEntity() {
  try {
    // The result of innerAction is available here if needed
    const result = await loadEntityAction({ id: entityIdToFetch.value });
    entityData.value = result; // Assign the successfully fetched data
    // entityFetchError.value is already cleared within innerAction's try block
  } catch (error) {
    // Error is already handled for UI display (entityFetchError ref) within innerAction's catch block.
    // useAsync also logs it. This catch block is for any additional logic if the *caller* needs to react to the error.
    console.log('handleLoadEntity caught an error (primarily for flow control or further specific handling):', error);
    entityData.value = null; // Ensure data is cleared on error at this level too
  }
}
</script>
```

**Key points from this example:**

- `useAsync<FetchEntityPayload, Entity>`: Specifies that `innerAction` expects a `FetchEntityPayload` and will return a `Promise<Entity>`.
- Payload: The `id` is passed to `loadEntityAction` when called.
- Returned Promise: `loadEntityAction` returns a `Promise<Entity>`. The `handleLoadEntity` function awaits this promise and can use its resolved value (`result`).
- Error Propagation: If `innerAction` throws an error, `loadEntityAction`'s promise rejects. The `catch` block in `handleLoadEntity` can then react to this, even though `innerAction` already updated UI error refs.
- Typed Result: The `result` obtained from `await loadEntityAction(...)` is correctly typed as `Entity`.

## Key Benefits of Using `useAsync`

-   **Simplified Loading State Management**: Automatically handles the `loading` ref, reducing boilerplate.
-   **Encourages Cleaner Code**: Helps separate the triggering of async logic from its execution details.
-   **Improved Readability**: Makes the purpose of async calls and their loading states more explicit.
-   **Consistency**: Promotes a uniform way to handle async tasks with loading states across the application.

## Best Practices

1.  **Robust Error Handling in `innerAction`**: Always implement `try...catch` blocks *within the `innerAction`* passed to `useAsync`. Update UI-specific error refs and use notifications from within this `catch` block. `useAsync` will re-throw the error, so your calling code can also react if needed.
2.  **Clear User Feedback**: Utilize the `loading` state for visual cues (spinners, disabled buttons, `VcLoading`). Inform users about outcomes (success/failure) via refs, `VcAlert`, `useNotifications`, etc.
3.  **Explicit Typing with Generics**: Use TypeScript generics (`useAsync<PayloadType, ResultType>`) for payloads and return types. This greatly improves type safety and code clarity.
4.  **Focused `innerAction`**: Each `innerAction` should ideally represent a single, logical asynchronous operation.
5.  **Composability**: Encapsulate `useAsync` calls within feature-specific composables (e.g., `useEntityLoader`, `useProductList`) to keep UI components clean.
6.  **Return Value of `innerAction`**: `innerAction` can either directly update reactive `ref`s (common for `Promise<void>` returns) or return a value (e.g., `Promise<MyData>`), which then becomes the resolved value of the promise returned by `action`. Choose the pattern that best fits clarity and reusability.
7.  **Aggregating Loading States**: For scenarios with multiple independent async operations where a combined loading state is desired, consider using the `useLoading` composable. It can take multiple `loading` refs (from `useAsync` or other sources) and provide a single reactive boolean indicating if any of them are true.

## Related API Reference

-   For detailed information on `useAsync` parameters and return values, see the [useAsync API Reference](../composables/useAsync.md)
