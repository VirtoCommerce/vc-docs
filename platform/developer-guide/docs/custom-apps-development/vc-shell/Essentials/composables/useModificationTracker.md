# How-To: Tracking Data Changes with `useModificationTracker`

The `useModificationTracker` composable is a powerful utility in VC-Shell for detecting changes in reactive data, such as objects or arrays. It is especially useful in forms and detail-editing screens to determine if a user has modified any data, which can then be used to enable/disable UI elements like a "Save" button.

## Prerequisites

-   Strong understanding of Vue 3 Composition API, particularly `ref`, `computed`, and `watch`.
-   Familiarity with deep cloning and deep equality concepts (this composable uses `lodash-es`'s `cloneDeep` and `isEqual`).

## Core Concept

`useModificationTracker` takes an initial value (or a `Ref` to it) and creates two internal copies:
1.  **`pristineValue`**: A "clean" version representing the original, unmodified state.
2.  **`currentValue`**: A reactive `Ref` that you bind to your UI components (e.g., form inputs).

It then returns:
-   `currentValue`: The reactive `Ref<T>` you should use for `v-model` or other bindings.
-   `isModified`: A `DeepReadonly<Ref<boolean>>` that becomes `true` if `currentValue` is no longer deeply equal to `pristineValue`.
-   `resetModificationState`: A function to reset the tracker. It makes the current state the new "pristine" state.

This is invaluable for scenarios where you only want to allow saving when actual changes have occurred, preventing unnecessary API calls.

## API Reference: `useModificationTracker`

### Function Signature
```typescript
function useModificationTracker<T>(initialValueProp: T | Ref<T>): UseModificationTrackerReturn<T>
```

### Parameters
-   `initialValueProp`: The initial data to be tracked. It can be a simple value, an object, an array, or a `Ref` to any of these.

### Return Value (`UseModificationTrackerReturn<T>`)
An object containing:
-   `currentValue: Ref<T>`: A reactive reference to the current tracked value. You should bind your inputs to this ref.
-   `isModified: DeepReadonly<Ref<boolean>>`: A read-only ref that is `true` if `currentValue` has been modified compared to its original state.
-   `resetModificationState(newBaselineValue?: T | Ref<T>)`: A function to reset the modification state.
    -   If called with no arguments, it sets the current value of `currentValue` as the new "pristine" state, making `isModified` become `false`.
    -   If a `newBaselineValue` is provided, it sets that new value as the "pristine" state *and* resets `currentValue` to match it. This is useful after successfully saving data.

## Implementation Example

This example demonstrates using `useModificationTracker` within a product details blade to control the "Save" button.

```vue
<template>
  <VcBlade :toolbar-items="bladeToolbar">
    <div class="p-5">
      <!-- Bind inputs to `currentValue` -->
      <VcInput label="Product Name" v-model="currentValue.name" />
      <VcInput label="SKU" v-model="currentValue.sku" />
    </div>
  </VcBlade>
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue';
import { useModificationTracker, VcInput, VcBlade } from '@vc-shell/framework';
import type { IBladeToolbarItem } from '@vc-shell/framework';

interface Product {
  id: string;
  name: string;
  sku: string;
}

const productData = ref<Product | null>(null);

// useModificationTracker initialized with the ref
const { currentValue, isModified, resetModificationState } = useModificationTracker(productData);

// Blade toolbar configuration
const bladeToolbar = computed<IBladeToolbarItem[]>(() => [
  {
    id: 'save',
    title: 'Save',
    icon: 'material-save',
    // The Save button is only enabled when the data has been modified
    disabled: !isModified.value,
    onClick: handleSave,
  },
]);

async function handleSave() {
  if (!productData.value) return;

  console.log('Saving data...', currentValue.value);
  // Assume saveData is an API call
  // await apiService.saveProduct(currentValue.value);

  // After a successful save, reset the modification state.
  // This makes the newly saved data the "pristine" state.
  resetModificationState();

  // Alternatively, if the API returns the saved object, you can pass it:
  // const savedProduct = await apiService.saveProduct(currentValue.value);
  // resetModificationState(savedProduct); // Resets both pristine and current value
}

// Simulate loading initial data
onMounted(async () => {
  // await new Promise(resolve => setTimeout(resolve, 500));
  productData.value = { id: 'p123', name: 'Original Name', sku: 'SKU-ORIGINAL' };

  // No need to call resetModificationState here because useModificationTracker
  // automatically updates its internal state when the source ref (productData) changes.
});
</script>
```

### Handling Asynchronously Loaded Data

A key feature of `useModificationTracker` is its ability to handle initial data that is loaded asynchronously. If you pass a `Ref` as the `initialValueProp`, the composable will watch this source `Ref`. When the source `Ref` is updated (e.g., after an API call completes), `useModificationTracker` automatically updates its internal "pristine" value.

Crucially, it will only update `currentValue` if `isModified` is `false`. This prevents overwriting changes a user might have already made while the data was loading in the background.

## Best Practices

1.  **Bind to `currentValue`**: Always use the `currentValue` returned from the composable for your `v-model` bindings, not the original source `Ref`.
2.  **Reset After Save**: After successfully saving data, always call `resetModificationState()` to mark the new state as "pristine". This correctly disables the "Save" button until further changes are made.
3.  **Combine with Validation**: In forms, you'll often combine `isModified` with a form validation state (e.g., `isFormValid`) to control UI elements: `disabled: !isModified.value || !isFormValid.value`.
4.  **Use for Complex Objects**: `useModificationTracker` is most valuable for objects and arrays where a simple comparison (`===`) is not enough to detect changes. It performs a deep equality check.

By leveraging `useModificationTracker`, you can create more intuitive user interfaces that clearly indicate data state and prevent redundant operations, leading to a better user experience and cleaner code.

## Related Resources
-   [Usage Guide: Implementing Form Validation in Blades](./../Usage-Guides/implementing-form-validation-in-blades.md)
