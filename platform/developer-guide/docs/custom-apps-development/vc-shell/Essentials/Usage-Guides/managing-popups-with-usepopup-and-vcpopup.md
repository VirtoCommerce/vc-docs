# How-To: Managing Popups with `usePopup` and `VcPopup`

This guide provides practical examples of how to effectively manage and display popups in your VC-Shell application using the `usePopup` composable for programmatic control and the `VcPopup` component for building custom popup user interfaces.

## Prerequisites

-   Understanding of Vue 3 Composition API (`ref`, `computed`, `defineProps`, `defineEmits`).
-   Familiarity with the [`usePopup` Composable API Reference](../../Essentials/shared/components/popup-handler.md).
-   Familiarity with the [`VcPopup` Component API Reference](../../Essentials/ui-components/vc-popup.md).
-   Basic knowledge of Vue's dynamic components and slots.

## Core Concepts

VC-Shell offers two main ways to work with popups:

1.  **Programmatic Control with `usePopup`**: Ideal for triggering popups from business logic, showing standard confirmation/error/info dialogs, or displaying custom popup components dynamically.
2.  **Declarative UI with `VcPopup`**: Suitable for embedding popups directly within a component's template, where the popup's lifecycle is tightly coupled with its parent.

Often, these are combined: you build a custom popup UI using `VcPopup` and then manage its presentation programmatically with `usePopup`.

## 1. Using Standard Dialogs via `usePopup`

The `usePopup` composable provides convenient methods for common dialog types.

```vue
<script setup lang="ts">
import { usePopup } from '@vc-shell/framework';
import { VcButton } from '@vc-shell/framework'; // For example buttons

const { showConfirmation, showError, showInfo } = usePopup();

async function confirmAction() {
  const confirmed = await showConfirmation('Are you sure you want to save these changes?');
  if (confirmed) {
    // Perform save action
    showInfo('Changes saved successfully!');
  } else {
    showError('Save operation was cancelled.');
  }
}
</script>

<template>
  <VcButton @click="confirmAction">Save Changes</VcButton>
</template>
```

## 2. Creating a Custom Popup Component with `VcPopup`

For custom content and interactions, create a new Vue component using `VcPopup` as its base.

**Example: `UserDetailsPopup.vue`**

```vue
<!-- UserDetailsPopup.vue -->
<template>
  <VcPopup
    :title="props.isEditMode ? 'Edit User' : 'View User'"
    :modal-width="'tw-max-w-lg'" 
    @close="emit('closeRequested')"
  >
    <template #content>
      <form @submit.prevent="handleFormSubmit" class="tw-space-y-4">
        <div>
          <label>Name:</label>
          <VcInput v-model="editableUser.name" :disabled="!props.isEditMode" />
        </div>
        <div>
          <label>Email:</label>
          <VcInput v-model="editableUser.email" type="email" :disabled="!props.isEditMode" />
        </div>
        <slot name="additionalFields"></slot> <!-- For extra fields from parent -->
      </form>
    </template>
    <template #footer>
      <div class="tw-flex tw-justify-end tw-gap-3">
        <VcButton variant="outline" @click="emit('closeRequested')">Cancel</VcButton>
        <VcButton v-if="props.isEditMode" @click="handleFormSubmit">Save</VcButton>
      </div>
    </template>
  </VcPopup>
</template>

<script setup lang="ts">
import { reactive, defineProps, defineEmits, watchEffect } from 'vue';
import { VcPopup, VcInput, VcButton } from '@vc-shell/framework'; // Adjust paths

interface UserData {
  id: string;
  name: string;
  email: string;
}

const props = defineProps<{
  userData: UserData;
  isEditMode: boolean;
}>();

const emit = defineEmits<{
  (e: 'closeRequested'): void;
  (e: 'saveUser', data: UserData): void;
}>();

const editableUser = reactive<UserData>({ ...props.userData });

watchEffect(() => {
  // Keep local state in sync if prop changes
  Object.assign(editableUser, props.userData);
});

function handleFormSubmit() {
  if (props.isEditMode) {
    emit('saveUser', { ...editableUser });
  }
}
</script>
```

## 3. Programmatically Opening and Managing Custom Popups

Use `usePopup(options)` to show your custom popup component (`UserDetailsPopup.vue` in this case).

```vue
<script setup lang="ts">
import { ref } from 'vue';
import { usePopup, VcButton } from '@vc-shell/framework';
import UserDetailsPopup from './UserDetailsPopup.vue'; // Your custom component

const currentUser = ref({ id: 'user1', name: 'Alice Wonderland', email: 'alice@example.com' });
const isEditingUser = ref(false);

// Configure the popup instance
const userPopup = usePopup({
  component: UserDetailsPopup,
  props: { // These are props for UserDetailsPopup.vue
    userData: currentUser,      // Pass reactive data
    isEditMode: isEditingUser,  // Pass reactive data
  },
  emits: { // These handle events emitted by UserDetailsPopup.vue
    closeRequested: () => {
      console.log('UserDetailsPopup closed by user or internally.');
      userPopup.close(); // Explicitly close the programmatically opened popup
    },
    saveUser: (updatedData) => {
      console.log('User data to save:', updatedData);
      // currentUser.value = { ...updatedData }; // Update local data
      // await apiSaveUser(updatedData); // Call API
      userPopup.close(); // Close after saving
    },
  },
  slots: {
    // Example of providing content for the 'additionalFields' slot in UserDetailsPopup
    additionalFields: '<p class="tw-text-sm tw-text-gray-500">This is an admin-only field injected from parent.</p>'
  }
});

function showUserPopup(editMode: boolean) {
  isEditingUser.value = editMode;
  // Props for UserDetailsPopup are already reactive, so they will update.
  // If you needed to change the component or non-reactive props, you might re-configure usePopup.
  userPopup.open();
}

</script>

<template>
  <VcButton @click="showUserPopup(false)">View User</VcButton>
  <VcButton @click="showUserPopup(true)" class="tw-ml-2">Edit User</VcButton>
</template>
```

**Key Points for Programmatic Custom Popups:**

*   **`component`**: Pass the imported Vue component itself.
*   **`props`**: Pass data to your custom popup. If you pass Vue `ref`s or `reactive` objects, the popup will update if these sources change while it's open (though `usePopup` itself doesn't automatically re-render if its initial `options` object changes deeply; for significant option changes, you might need a new `usePopup` instance or careful management of reactive props).
*   **`emits`**: Define handlers for events emitted by your custom popup component.
*   **`slots`**: You can provide content for named slots within your custom popup. This can be an HTML string, another Vue component (use `markRaw` from Vue), or a Vue `Slot` function.
*   **Closing**: The `close()` method returned by `usePopup(options)` is specific to that popup instance. It's often called within your event handlers (e.g., after saving or on a custom close event).

## 4. Declarative Usage of `VcPopup`

For popups tightly coupled with a parent component's UI and state, direct template usage is simpler.

```vue
<template>
  <VcButton @click="isHelpPopupVisible = true">Show Help</VcButton>

  <VcPopup
    v-if="isHelpPopupVisible"
    title="Help & Information"
    @close="isHelpPopupVisible = false"
  >
    <template #content>
      <p>This section provides help for the current page.</p>
      <ul>
        <li>Feature A: How to use...</li>
        <li>Feature B: Common issues...</li>
      </ul>
    </template>
    <template #footer="{ close }">
      <VcButton @click="close">Got it!</VcButton>
    </template>
  </VcPopup>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { VcPopup, VcButton } from '@vc-shell/framework'; // Adjust path

const isHelpPopupVisible = ref(false);
</script>
```
Here, `usePopup` is not directly involved in showing/hiding. `VcPopup` handles its own presentation based on `v-if` and emits a `close` event.

## Best Practices

*   **Build Custom Popups with `VcPopup`**: When creating your own popup components (like `UserDetailsPopup.vue`), always use `<VcPopup>` as the root or main structural element. This ensures they integrate well with the framework's styling, accessibility, and basic behaviors (like title, close button in header, footer structure).
*   **Choose the Right Method**: Use programmatic `usePopup` for dialogs triggered from logic, shared popups, or when needing to pass complex/dynamic data. Use declarative `VcPopup` for simpler, component-specific popups.
*   **Props and Events**: Clearly define `props` and `emits` for your custom popup components for good encapsulation.
*   **Closing Popups**: Programmatically opened popups should be closed via the `close` method returned by their `usePopup(options)` instance. Declarative popups are typically closed by setting their `v-if` condition to false, often triggered by the `VcPopup`'s own `@close` event or a button in its footer slot.
*   **State Management**: For complex forms within popups, consider using VeeValidate or Vue's built-in reactivity for managing form state locally within your custom popup component.
*   **Error Handling**: Implement error handling within your popup logic (e.g., for API calls made from a popup form) and use `showError` from `usePopup` if needed.

By combining `usePopup` for managing popup instances and `VcPopup` for building their UIs, you can create a flexible and consistent modal experience in your VC-Shell application. Refer to the respective API documentations for more detailed options. 
