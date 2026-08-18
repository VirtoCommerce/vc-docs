# How-To: Preventing Data Loss with `useBeforeUnload`

The `useBeforeUnload` composable is a crucial tool in VC-Shell for enhancing user experience by preventing accidental data loss. When a user has made changes to a form or any other editable content, this composable can trigger a browser confirmation dialog if they attempt to navigate away from the page or close the tab/browser.

This guide will walk you through how to effectively implement `useBeforeUnload` in your Vue components within a VC-Shell application.

## Prerequisites

-   Basic understanding of Vue 3 Composition API.
-   Familiarity with reactive refs (`ref`, `computed`) in Vue.
-   Knowledge of the `useBeforeUnload` composable's basic API (see [useBeforeUnload API Reference](../composables/useBeforeUnload.md)).

## Core Concept

The `useBeforeUnload` composable takes a single argument: a `ComputedRef<boolean>`. This computed ref should return `true` if there are unsaved changes that should prevent the user from leaving without a warning, and `false` otherwise.

```typescript
import { computed } from 'vue';
import { useBeforeUnload } from '@vc-shell/framework';

// someReactiveState represents the data that might have unsaved changes
const someReactiveState = ref({ value: 'initial' });
const originalState = { value: 'initial' };

const hasUnsavedChanges = computed(() => {
  return someReactiveState.value.value !== originalState.value;
});

// Activate the beforeunload listener
useBeforeUnload(hasUnsavedChanges);
```

When `hasUnsavedChanges` is `true`, any attempt to navigate away (e.g., closing tab, browser back button, clicking an external link) will trigger the browser's native "Are you sure you want to leave?" dialog.

## Implementation Steps

### 1. Identify Data Prone to Loss

Determine which data in your component, if modified and not saved, would result in a poor user experience. This is typically form data, editor content, or configuration settings.

### 2. Track Original and Current State

You need a way to compare the current state of the data with its original (or last saved) state.

-   **For simple objects/values**: Store a copy of the initial data.
-   **For complex forms**: Form libraries like VeeValidate often provide a "dirty" or "isModified" state that you can directly use.

### 3. Create a `computed` Property for Unsaved Changes

This `computed` property will be the heart of your `useBeforeUnload` integration. It must accurately reflect whether unsaved changes exist.

```typescript
// In your <script setup lang="ts">

import { ref, computed } from 'vue';
import { useBeforeUnload } from '@vc-shell/framework';

// Example: A simple form
const formData = ref({ name: '', description: '' });
const originalFormData = JSON.parse(JSON.stringify(formData.value)); // Deep copy for initial state

const isFormModified = computed(() => {
  return JSON.stringify(formData.value) !== JSON.stringify(originalFormData);
});

// Example: Using a form library's dirty state (conceptual)
// import { useForm } from 'some-form-library';
// const { isDirty } = useForm();
// const isFormModified = isDirty; // Assuming isDirty is a ComputedRef<boolean>
```
**Note on deep comparison**: `JSON.stringify` is a simple way for deep comparison of objects. For more complex scenarios or performance-critical applications, consider a more robust deep comparison utility or track changes at a more granular level.

### 4. Call `useBeforeUnload`

Pass your `computed` property to `useBeforeUnload`.

```typescript
useBeforeUnload(isFormModified);
```

## Advanced Scenarios

### Integrating with Blade Navigation (`useBladeNavigation`)

`useBeforeUnload` handles browser-level navigation (closing tabs, back/forward). For navigation within VC-Shell's blade system, you need to integrate with `useBladeNavigation` and its `onBeforeClose` hook. This provides a consistent user experience.

```typescript
import { computed } from 'vue';
import { useBeforeUnload, useBladeNavigation, usePopup } from '@vc-shell/framework'; // Assuming VcPopup for confirmation

// ... (formData, originalFormData, isFormModified setup as above) ...

// For browser navigation
useBeforeUnload(isFormModified);

// For blade navigation
const { onBeforeClose } = useBladeNavigation();

const { showConfirmation } = usePopup();

onBeforeClose(async () => {
  if (!isFormModified.value) {
    return true; // Allow closing without confirmation
  }

  // Show a custom VC-Shell confirmation dialog
  const confirmed = await showConfirmation('You have unsaved changes. Are you sure you want to close this blade?');

  return confirmed; // If true, blade closes; if false, it stays open
});
```

This ensures that whether the user tries to close the browser tab OR the blade itself, they are prompted if there are unsaved changes.

### Conditional Activation

You might only want `useBeforeUnload` to be active under certain conditions (e.g., when a user is in "edit mode").

```typescript
const isInEditMode = ref(false);
// ... (formData, originalFormData, isFormModified setup as above) ...

const shouldPreventNavigation = computed(() => {
  return isInEditMode.value && isFormModified.value;
});

useBeforeUnload(shouldPreventNavigation);
```

### Multiple Instances

`useBeforeUnload` can be called multiple times in an application (e.g., in different active blades). The browser will typically show only one `beforeunload` dialog. If any active `useBeforeUnload` instance has its `modified` condition as `true`, the dialog will appear.

## Best Practices

* **Accuracy is Key**: Ensure your `modified` computed property accurately reflects the unsaved changes state. False positives (warning when there's nothing to save) or false negatives (not warning when there are changes) lead to poor UX.
* **Clear Save/Reset Actions**: Provide obvious ways for users to save their work or discard changes. This makes the `useBeforeUnload` prompt a helpful fallback rather than a primary interaction point.
* **Combine with Blade Navigation**: For a seamless experience in VC-Shell apps, always pair `useBeforeUnload` with `useBladeNavigation().onBeforeClose` if your component is within a blade and manages savable state.
* **User Experience**: The `beforeunload` prompt is a native browser dialog and cannot be styled. Its text is also largely standardized by the browser for security reasons. Rely on clear UI in your application to indicate unsaved changes **before** the user attempts to navigate away.


By following this guide, you can effectively use the `useBeforeUnload` composable to protect your users from losing their work, contributing to a more robust and user-friendly VC-Shell application.

