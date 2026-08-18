# How-To: Working with Blade Navigation in VC-Shell

This guide provides practical steps and examples for effectively using the blade navigation system in VC-Shell, primarily through the `useBladeNavigation` composable and `VcBlade` component.

## Prerequisites

-   Familiarity with Vue 3 Composition API.
-   Understanding of the `VcBladeNavigation` component and `useBladeNavigation` composable API. (Refer to the [VcBladeNavigation API Documentation](/platform/developer-guide/latest/custom-apps-development/vc-shell/Essentials/shared/components/blade-navigation)).
-   Basic knowledge of Vue Router.
-   Your blade/page components should be correctly configured with necessary static properties (like `name`, `url`, `isWorkspace`, etc.) and included in your module's `createAppModule` definition for automatic registration by the VC-Shell modularity system. Refer to the [Modularity Plugin documentation](/platform/developer-guide/latest/custom-apps-development/vc-shell/Essentials/plugins/modularity) for details on how to define and register pages.
-   The `VcBladeNavigation` component is part of the core `vc-app.vue` and does not require manual setup in your layout.

## 1. Basic Blade Creation and Opening

Blades are standard Vue components. For them to integrate with the navigation system and have a consistent look and feel, it's recommended to use the `VcBlade` component as their root. Blades interact with the VC-Shell navigation system by receiving a standard set of properties (like `param`, `options`, `expanded`, `closable`) and by emitting a standard set of events (like `close:blade`, `parent:call`).

### a. Create a Simple Blade Component

```vue
// src/components/blades/MyDetailsBlade.vue
<template>
  <VcBlade title="My Details">
    <p>This is MyDetailsBlade.</p>
    <p v-if="param">Received parameter: {{ param }}</p>
    <p v-if="options && options.message">Received options: {{ options.message }}</p>
    <VcButton @click="openAnother">Open Another Blade</VcButton>
  </VcBlade>
</template>

<script setup lang="ts">
import { useBladeNavigation } from '@vc-shell/framework';
import AnotherBlade from './AnotherBlade.vue';

export interface Props {
  expanded: boolean;
  closable: boolean;
  param?: string;
  options?: { message?: string };
}

// Props passed by the navigation system
defineProps<Props>();

defineOptions({
  name: 'MyDetailsBlade',
  url: '/my-details',
});

const { openBlade } = useBladeNavigation();

function openAnother() {
  openBlade({
    blade: AnotherBlade,
    options: { cameFrom: 'MyDetailsBlade' },
  });
}
</script>
```

```vue
// src/components/blades/AnotherBlade.vue
<template>
  <VcBlade title="Another Blade">
    <p>This is AnotherBlade.</p>
    <p v-if="options && options.cameFrom">Opened from: {{ options.cameFrom }}</p>Ф
  </VcBlade>
</template>

<script setup lang="ts">
export interface Props {
  expanded: boolean;
  closable: boolean;
  param?: string;
  options?: { cameFrom?: string };
}

defineOptions({
  name: 'AnotherBlade',
});

defineProps<Props>();
</script>
```

### b. Opening the Blade

From any other component (e.g., a list view, a dashboard widget):

```vue
// src/components/MyList.vue
<template>
  <VcButton @click="showDetails('item-123')">View Item 123</VcButton>
</template>

<script setup lang="ts">
import { useBladeNavigation } from '@vc-shell/framework';

const { openBlade } = useBladeNavigation();

function showDetails(itemId: string) {
  openBlade({
    blade: { name: 'MyDetailsBlade' },
    param: itemId,
    options: { message: 'Hello from MyList!' },
    onOpen: () => console.log(`MyDetailsBlade for ${itemId} opened.`),
    onClose: () => console.log(`MyDetailsBlade for ${itemId} closed.`),
  });
}
</script>
```

**Key Points:**

-   `openBlade` takes an object with `blade` (component definition **or its registered name**), optional `param`, `options`, and lifecycle hooks.
-   Blades receive `param` and `options` as props.
-   Ensure the blade name used (e.g., 'MyDetailsBlade') matches how it was registered by the `createAppModule` (typically the `name` property of the component itself).

## 2. Workspaces

Workspaces are special blades that typically represent a main section of your application. Opening a workspace usually closes all other open blades and becomes the new root of the blade stack.

### a. Defining a Workspace Blade

A workspace blade is a regular blade component. It's designated as a workspace by setting its static `isWorkspace: true` property, which is then used by `createAppModule` during registration, or it can be opened as a workspace dynamically.

```vue
// src/components/workspaces/SettingsWorkspace.vue
<template>
  <VcBlade title="Application Settings" :closable="false">
    <p>Configure your application here.</p>
    {/* ... settings form ... */}
  </VcBlade>
</template>

<script setup lang="ts">
import { VcBlade } from '@vc-shell/framework/ui';
// Workspaces are typically not closable by the standard close button.

defineOptions({
  url: '/settings',
  isWorkspace: true,
});
</script>
```

### b. Opening a Workspace

```vue
// src/components/layout/AppMenu.vue
<script setup lang="ts">
import { useBladeNavigation } from '@vc-shell/framework';
// Assuming SettingsWorkspace is registered via createAppModule under the name 'SettingsWorkspace'
// and potentially marked with isWorkspace: true in its definition.
// import SettingsWorkspace from '../workspaces/SettingsWorkspace.vue';

const { openBlade } = useBladeNavigation();

function goToSettings() {
  openBlade({
    blade: { name: 'SettingsWorkspace' },
    // Workspaces usually don't take params/options directly on open,
    // but rely on their own internal state or services.
  }, true);
}
</script>
```

## 3. Preventing Blade Closure (Handling Unsaved Changes)

The `onBeforeClose` hook allows you to intercept the close event, for example, to ask the user for confirmation if there are unsaved changes.

```vue
// src/components/blades/EditorBlade.vue
<template>
  <VcBlade title="Content Editor" :toolbar-items="toolbarItems">
    <textarea v-model="content" @input="markDirty"></textarea>
    <p v-if="isDirty">You have unsaved changes!</p>
  </VcBlade>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { VcBlade, VcButton } from '@vc-shell/framework/ui';
import { useBladeNavigation, usePopup } from '@vc-shell/framework'; // Assuming usePopup is available

export interface Emits {
  (event: "parent:call", args: IParentCallArgs): void;
  (event: "close:blade"): void;
  (event: "collapse:blade"): void;
  (event: "expand:blade"): void;
}
const emit = defineEmits<Emits>();

const { onBeforeClose, closeBlade, currentBladeNavigationData } = useBladeNavigation();
const { showConfirmation } = usePopup(); // Your app's confirmation dialog service

const content = ref('');
const isDirty = ref(false);

const toolbarItems = [
  {
    id: 'close',
    title: 'Close',
    icon: 'close',
    onClick: closeSelf,
  },
  {
    id: 'save',
    title: 'Save',
    icon: 'save',
    onClick: save,
  },
];

function markDirty() {
  isDirty.value = true;
}

async function save() {
  // ... save logic ...
  console.log('Content saved:', content.value);
  isDirty.value = false;
  // Optionally close after save:
  // if (currentBladeNavigationData.value) {
  //   closeBlade(currentBladeNavigationData.value.idx);
  // }
}

// This hook is registered for the current blade instance
onBeforeClose(async () => {
  if (isDirty.value) {
    const userConfirmed = await showConfirmation(
      'Unsaved Changes',
      'You have unsaved changes. Are you sure you want to close without saving?'
    );
    // If user clicks "Cancel" (userConfirmed is false), we prevent closing by returning true.
    // If user clicks "OK" (userConfirmed is true), we allow closing by returning false.
    return !userConfirmed;
  }
  return false; // Allow closing if not dirty
});

// Example of blade closing itself
function closeSelf() {
    // A blade can request its own closure by emitting 'close:blade'
    // Or, if it knows its index (less common for self-closure)
    // if (currentBladeNavigationData.value) {
    //    closeBlade(currentBladeNavigationData.value.idx);
    // }
    // VcBlade itself might handle this when its own close button is clicked,
    // but for a custom button, you might emit or call closeBlade.
    emit('close:blade');
}
</script>
```
**Important**: `onBeforeClose` should return `false` (or a Promise resolving to `false`) to allow closing, and `true` (or a Promise resolving to `true`) to prevent it.

## 4. Parent-Child Communication

Child blades can call methods exposed by their parent blade.

### a. Parent Blade Exposing a Method

```vue
// src/components/blades/ParentWithActionsBlade.vue
<template>
  <VcBlade :title="`Parent Blade - Counter: ${counter}`">
    <VcButton @click="openChildToUpdate">Open Child Editor</VcButton>
  </VcBlade>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { VcBlade, VcButton } from '@vc-shell/framework/ui';
import { useBladeNavigation } from '@vc-shell/framework/shared';
import ChildEditorBlade from './ChildEditorBlade.vue';

const { openBlade } = useBladeNavigation();
const counter = ref(0);

function openChildToUpdate() {
  openBlade({ blade: ChildEditorBlade });
}

// Expose a method for the child to call
defineExpose({
  updateParentCounter(amount: number) {
    counter.value += amount;
    console.log(`Parent counter updated by ${amount}, new value: ${counter.value}`);
    return { success: true, newValue: counter.value };
  }
});
</script>
```

### b. Child Blade Calling Parent's Method

```vue
// src/components/blades/ChildEditorBlade.vue
<template>
  <VcBlade title="Child Editor">
    <VcButton @click="incrementParent(5)">Increment Parent Counter by 5</VcButton>
  </VcBlade>
</template>

<script setup lang="ts">
import type { IParentCallArgs } from '@vc-shell/framework';

// Define the standard events a blade can emit
export interface Emits {
  (event: "parent:call", args: IParentCallArgs): void;
  (event: "close:blade"): void;
  (event: "collapse:blade"): void;
  (event: "expand:blade"): void;
}

const emit = defineEmits<Emits>();

function incrementParent(value: number) {
  // Use the typed emit function from defineEmits
  emit('parent:call', {
    method: 'updateParentCounter', // Must match the method name exposed by the parent
    args: value,
    callback: (result: any) => {
      if (result && result.success) {
        console.log('Parent method call successful. New parent counter:', result.newValue);
      } else {
        console.warn('Parent method call failed or returned unexpected result.', result);
      }
    }
  });
}

// Example of how another standard event might be emitted:
// function requestClose() {
//   emit('close:blade');
// }
</script>
```

## 5. Working with URL Query Parameters

You can manage URL query parameters that are automatically scoped to the current active workspace.

```vue
// src/components/workspaces/ProductListWorkspace.vue
<template>
  <VcBlade title="Products">
      <input type="text" v-model="filters.searchTerm" placeholder="Search..." @input="updateQuery" />
      <select v-model="filters.category" @change="updateQuery">
        <option :value="null">All Categories</option>
        <option value="electronics">Electronics</option>
        <option value="books">Books</option>
      </select>
      <!-- ... display products based on filters ... -->
      <p>Current search: {{ filters.searchTerm }}, category: {{ filters.category }}</p>
  </VcBlade>
</template>

<script setup lang="ts">
import { reactive, onMounted, watch } from 'vue';
import { useBladeNavigation } from '@vc-shell/framework';

const { setNavigationQuery, getNavigationQuery } = useBladeNavigation();

const filters = reactive({
  searchTerm: '',
  category: null as string | null,
});

// Load initial filters from URL query on mount
onMounted(() => {
  const query = getNavigationQuery();
  if (query) {
    filters.searchTerm = String(query.searchTerm || '');
    filters.category = query.category ? String(query.category) : null;
  }
  fetchProducts();
});

function fetchProducts() {
  console.log('Fetching products with filters:', filters);
  // ... actual data fetching logic ...
}

function updateQuery() {
  const queryToSet: Record<string, string | number | null> = {};
  if (filters.searchTerm) queryToSet.searchTerm = filters.searchTerm;
  if (filters.category) queryToSet.category = filters.category;
  setNavigationQuery(queryToSet);
}

// Watch for filter changes to refetch data
// setNavigationQuery will update the URL, which might also trigger route watchers if any.
watch(filters, () => {
  // The URL is already updated by setNavigationQuery called by @input/@change.
  // Here, just fetch data.
  fetchProducts();
}, { deep: true });

</script>
```
The URL might look like: `/#/your-workspace-route?productlistworkspace_searchTerm=books&productlistworkspace_category=fiction`

## 6. Deep Linking and URL Structure

-   **Blade URLs**: Routable blades (workspaces or regular blades that can be linked directly) should have a `url` property defined in their static options when registered (e.g., `url: '/settings'`).
-   **Automatic URL Updates**: As you open and close blades, `useBladeNavigation` updates the browser's URL to reflect the current stack.
-   **URL Parsing**: On page load or direct navigation to a URL, the `routeResolver` (part of `useBladeNavigation`) parses the URL segments:
    -   It identifies a base parameter if your application uses one (e.g., tenant ID).
    -   It then looks for a workspace segment, followed by child blade segments and parameters.
    -   Example: `/#/main/products/edit/123` might map to:
        -   `main`: Base parameter.
        -   `products`: `ProductsWorkspace.url`.
        -   `edit`: `ProductEditBlade.url`.
        -   `123`: `param` for `ProductEditBlade`.
-   Ensure your blade components are registered with `useBladeRegistry` if you want them to be resolvable from URL segments by name or their defined `url`.

## 7. Closing Blades

-   **From within a blade**: A blade can request its own closure by emitting `close:blade`. The `VcBlade` component often provides a close button that does this.
    ```vue
    // Inside a blade's method
    // emit('close:blade');
    ```
-   **Programmatically**: Use `closeBlade(index)` from `useBladeNavigation`.
    ```typescript
    const { closeBlade, blades } = useBladeNavigation();

    // Close the last blade
    if (blades.value.length > 0) {
      closeBlade(blades.value.length - 1);
    }

    // Close all blades starting from the second blade (index 1)
    // This leaves the workspace (index 0) open.
    // closeBlade(1);
    ```
-   The `index` refers to the blade's position in the `blades` array. `0` is the workspace.
-   `onBeforeClose` hooks will be respected. `closeBlade` returns a Promise resolving to `true` if closing was prevented, `false` otherwise.


This How-To guide should cover the main practical aspects of using the blade navigation system. Refer to the [VcBladeNavigation API Documentation](/platform/developer-guide/latest/custom-apps-development/vc-shell/Essentials/shared/components/blade-navigation) for detailed API information and the [Modularity Plugin Documentation](/platform/developer-guide/latest/custom-apps-development/vc-shell/Essentials/plugins/modularity) for how pages/blades are registered. 
