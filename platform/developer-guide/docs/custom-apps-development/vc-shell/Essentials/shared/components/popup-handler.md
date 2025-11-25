# `usePopup` Composable and Popup System API

The `usePopup` composable is the primary public interface for managing popups and modals within VC-Shell applications. It enables developers to programmatically trigger standard dialogs (confirmation, error, info) and to open custom-built popup components. This system relies on the `VcPopup` component for UI construction of custom popups, and is supported by the underlying `VcPopupHandler` plugin and `VcPopupContainer` component which manage the rendering and lifecycle.

The VC-Shell popup system consists of several key parts:

*  **`usePopup` Composable**: The main API for developers. It provides methods to show pre-styled standard popups and to configure and display custom Vue components as popups.
* **`VcPopup` Component**: The standard UI component used to build the actual interface of your custom popups (e.g., forms, detailed views). You will use `<VcPopup>` within your custom popup components. Refer to the [VcPopup Component Documentation](/platform/developer-guide/latest/custom-apps-development/vc-shell/Essentials/ui-components/vc-popup) for its detailed API.
* **`VcPopupHandler` Plugin**: A Vue plugin automatically installed by the VC-Shell framework. It sets up the global infrastructure for popups, including registering the `VcPopupContainer`.
* **`VcPopupContainer` Component**: A globally available component that acts as the rendering target for all popups managed by `usePopup`. Developers typically do not interact with this component directly.

## Key features

- Centralized popup management via `usePopup`.
- Built-in, pre-styled confirmation, error, and info popups.
- Support for displaying any custom Vue component as a popup.
- Custom popups are best built using the `VcPopup` component for consistency.
- Promise-based API for handling user responses from confirmation dialogs.

## Usage

### Use usePopup composable

The `usePopup` composable provides methods to show different types of popups:

```vue
<template>
  <div>
    <VcButton @click="showConfirmationDialog">Show Confirmation</VcButton>
    <VcButton @click="showErrorDialog">Show Error</VcButton>
    <VcButton @click="showInfoDialog">Show Info</VcButton>
    <VcButton @click="openCustomPopup">Open Custom Popup</VcButton>
  </div>
</template>

<script setup lang="ts">
import { usePopup } from '@vc-shell/framework';
import MyCustomPopupComponent from './MyCustomPopupComponent.vue'; // Assume this exists
import { ref, markRaw } from 'vue';

const { showConfirmation, showError, showInfo, open } = usePopup(); // For standard dialogs

async function showConfirmationDialog() { // Renamed to avoid conflict
  const confirmed = await showConfirmation('Are you sure you want to proceed?');
  if (confirmed) {
    console.log('Action confirmed');
  } else {
    console.log('Action canceled');
  }
}

function showErrorDialog() { // Renamed
  showError('An error occurred while processing your request.');
}

function showInfoDialog() { // Renamed
  showInfo('Your changes have been saved successfully.');
}

// For custom popups
const popupData = ref({ name: 'John Doe', email: 'john@example.com' });

// It's good practice to define the specific popup instance separately if you need its `close` function
const customPopupInstance = usePopup({
  component: MyCustomPopupComponent, // Your custom component, ideally built with VcPopup
  props: {
    data: popupData, // Props for MyCustomPopupComponent
    title: 'Custom Popup Title via Props'
  },
  emits: {
    onSave(data) {
      console.log('Data saved from custom popup:', data);
      customPopupInstance.close(); // Close this specific popup
    },
    onClose() { // Assuming MyCustomPopupComponent emits 'onClose'
      console.log('Custom popup emitted onClose');
    }
  },
  slots: {
    // Example: providing a default slot content as a string
    // default: '<p>This is <em>default slot</em> content from parent.</p>',
    // Example: providing a named slot content using a component (ensure it's imported and markRaw)
    // footerInfo: markRaw(MyFooterInfoComponent) 
  }
});

function openCustomPopup() {
  customPopupInstance.open();
}
</script>
```

### Create and use custom popups

When you need more than standard dialogs, you'll create your own Vue component for the popup's content and UI. **It is highly recommended to use the `VcPopup` component as the main building block within your custom popup component** to ensure consistent styling and behavior (like header, footer, and close button integration).

Refer to the [VcPopup Component Documentation](/platform/developer-guide/latest/custom-apps-development/vc-shell/Essentials/ui-components/vc-popup) for details on how to use `VcPopup` to build your custom popup's structure.

Once your custom popup component (e.g., `MyCustomPopupComponent.vue`) is created (using `VcPopup` internally), you can display it programmatically using `usePopup(options)` as shown in the example above.

#### UsePopupProps interface

```typescript
import { type Component, type Slot as VueSlot, type Ref, type MaybeRef } from 'vue';
import { type ComponentPublicInstanceConstructor, type ComponentEmit } from '@vc-shell/framework'; // Ensure these utility types are correctly exported and path is right

// Assuming RawProps and RawEmits are defined based on ComponentPublicInstanceConstructor
// For documentation clarity:
type RawProps<T extends ComponentPublicInstanceConstructor> = InstanceType<T>['$props'];
type RawEmits<T extends ComponentPublicInstanceConstructor> = ComponentEmit<T>;
type SlotContent = string | Component | VueSlot;

interface UsePopupProps<T extends ComponentPublicInstanceConstructor> {
  component: T;             // The Vue component to render as a popup.
  props?: RawProps<T>;      // Props to pass to the component.
  emits?: RawEmits<T>;      // Event handlers for events emitted by the component.
  slots?: {                 // Slots to render in the component.
    [key: string]: SlotContent; // Slot name -> slot content (HTML string, Component, or Vue Slot function)
  };
}
```

The example for `Form Submission in Custom Popup` already demonstrates a `UserEditPopup.vue` that correctly uses `VcPopup`. This is a good illustration of building a custom popup.

## Declarative usage (embedding `VcPopup` directly)

Besides programmatic control with `usePopup`, you can also embed `VcPopup` directly into your component templates and control its visibility using local state (e.g., a `ref` and `v-if`). This method is suitable when a popup is tightly coupled with a specific component's UI.

```vue
<template>
  <VcButton @click="showMyDeclarativePopup = true">Open My Declarative Popup</VcButton>
  
  <VcPopup 
    v-if="showMyDeclarativePopup" 
    title="My Declarative Form"
    @close="showMyDeclarativePopup = false"
  >
    <template #content>
      <p>This popup's visibility is controlled by `showMyDeclarativePopup`.</p>
      <!-- Add form fields or other content here -->
    </template>
    <template #footer="{ close }"> <!-- VcPopup exposes a close function in its footer slot -->
      <VcButton @click="handleSubmitDeclarative">Submit</VcButton>
      <VcButton variant="outline" @click="close">Cancel</VcButton>
    </template>
  </VcPopup>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcPopup, VcButton } from '@vc-shell/framework'; // Adjust path if necessary

const showMyDeclarativePopup = ref(false);

function handleSubmitDeclarative() {
  console.log('Declarative popup form submitted');
  showMyDeclarativePopup.value = false;
}
</script>
```
This approach doesn't use `usePopup().open()` but relies on `VcPopup`'s own capabilities.

## How it works (underlying mechanism)

The `usePopup` composable works by managing a queue of popups and their lifecycle. When you call `usePopup(options)`, it creates a new instance of the popup component and manages its lifecycle. The `VcPopup` component is used to render the popup content, and the `VcPopupHandler` plugin ensures that the popup is properly registered and managed.
