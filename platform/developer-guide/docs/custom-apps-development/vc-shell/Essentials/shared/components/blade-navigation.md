# VcBladeNavigation Component and `useBladeNavigation` Composable

The `VcBladeNavigation` component, in conjunction with the `useBladeNavigation` composable, forms the heart of VC-Shell's blade-based navigation system. This system enables a hierarchical UI where screens (blades) open side-by-side, creating a traceable navigation path.

Blade navigation allows multiple UI levels to be displayed simultaneously. Each blade represents a discrete functionality and can open other blades. This is ideal for complex interfaces requiring drill-down capabilities while maintaining context. The `VcBladeNavigation` component is the main container that orchestrates the display of blades, while the `useBladeNavigation` composable provides the API for programmatic control over navigation, blade lifecycle, and state.

## Key Features

-   **Multi-level blade navigation**: Displays blades side-by-side.
-   **Programmatic control**: Full control via `useBladeNavigation` composable (opening, closing, state management).
-   **Automatic breadcrumb generation**: Integrates with `useBreadcrumbs` for navigation context.
-   **Blade state management**: Manages the stack of open blades.
-   **Responsive design**: Adapts blade display for different screen sizes.
-   **Deep linking & URL-driven navigation**: Opens blades based on URL paths and updates URLs during navigation.
-   **Blade lifecycle hooks**: Provides `onOpen`, `onClose`, and `onBeforeClose` for state management.
-   **Parent-child blade communication**: Facilitates interaction between parent and child blades.
-   **Workspace concept**: Supports primary "workspace" blades.
-   **Permissions integration**: Works with `usePermissions` for access control.
-   **Analytics integration**: Tracks page views using `useAppInsights`.
-   **Error isolation**: Each blade is wrapped in an `ErrorInterceptor`.
-   **Automatic blade registration and resolution**: Blades (pages) are automatically registered by the VC-Shell modularity system (`createAppModule`). `useBladeNavigation` then resolves these registered blades by name or URL for display.
-   **Navigation query parameters**: Allows setting and getting URL query parameters for the current workspace.

## `VcBladeNavigation` component API

The `VcBladeNavigation` component is the main container for the blade system. **It is already integrated into the core `vc-app.vue` component, so developers do not need to manually add it to their application layouts.** It works by rendering the blades managed by the `useBladeNavigation` composable and reacting to Vue Router changes. Developers generally don't need to pass any props directly to `VcBladeNavigation` or interact with its slots or events, as its behavior is primarily controlled through `useBladeNavigation` and the router.

## Blade component API (for components used as blades)

For `useBladeNavigation` to effectively manage blades, especially for features like opening by name or resolving from URLs, blades first need to be made known to the system. This is typically achieved by registering them globally using the `useBladeRegistry()` composable. During this registration process, or when opening a blade, you define its key characteristics.

When you create a Vue component to function as a blade, it adheres to a standard interface provided by the VC-Shell navigation system. This interface includes a set of props automatically passed to your component and a standard set of events your component can emit to communicate with the navigation system or parent blades. Key static properties like `url` (essential for routable blades and defined during registration with `useBladeRegistry`) and `isWorkspace` (which can be set during registration or specified when calling `openBlade({ blade }, true)`) are crucial for its behavior within the navigation system.

When you create a Vue component to function as a blade (often referred to as a "Page" component in VC-Shell), its integration with the navigation system is largely handled by the modularity plugin (`createAppModule`). You define the component and its characteristics (like `name`, `url`, `isWorkspace`, `permissions`, `menuItem`, etc.) as static properties or as part of its definition that `createAppModule` consumes. The modularity system then registers these pages, making them available to `useBladeNavigation`.

Your blade component interacts with the navigation system by:

*  Receiving a standard set of **props** (see below) passed by the system (e.g., `param`, `options`) or managed by it (`expanded`, `closable`, `navigation`).
*  Emitting a standard set of **events** (see below) to communicate intentions like closing or calling parent methods.

Key static properties for your page/blade component, which are typically defined directly on the component object or its options and used by `createAppModule` during registration, include:

-   `name` (string): A unique name for the blade component. If not provided for routable blades, it's often derived from the `url`. This name is used when opening blades programmatically via `openBlade({ blade: { name: 'MyBladeName' } })`.
-   `url` (string, optional): If the blade should be routable via a URL, this defines its path segment (e.g., `'/details'`). `createAppModule` uses this to set up Vue Router routes.
-   `isWorkspace` (boolean, optional): Set to `true` if this blade should function as a top-level workspace. This can also be specified dynamically when calling `openBlade(args, true)`.
-   `permissions` (string[] | string, optional): Permissions required to access this blade. Checked by `useBladeNavigation` before opening.
-   `menuItem` (object, optional): Configuration if this blade should appear in the main application menu. See `createAppModule` and `useMenuService` for details.
-   Other custom static properties can also be defined as needed by your application or extensions.

### Standard props (passed to your blade component by system)

The navigation system will provide the following props to your blade component. While `param` and `options` are for data you pass during `openBlade`, `expanded`, `closable`, and `navigation` are managed or injected by the system.

| Prop         | Type                        | Description                                              |
| :----------- | :---------------------------| :--------------------------------------------------------------------------------------------------------------------- |
| `expanded`   | `boolean`                   | (System-managed) Indicates if the blade is currently in its expanded state (typically the last visible blade on larger screens or the only visible one on mobile). |
| `closable`   | `boolean`                   | (System-managed) Indicates if the blade should offer a close control. Usually true for non-workspace blades.                                             |
| `param`      | `string`                    | (Optional, passed via `openBlade`) A string parameter passed when the blade was opened (e.g., an ID for an entity).                                     |
| `options`    | `Record<string, any>`       | (Optional, passed via `openBlade`) An object containing custom data/options passed when the blade was opened.                                      |
| `navigation` | `object`                    | (System-injected) Contains internal navigation state for the blade like `idx`, `isVisible`, `instance` reference, and lifecycle hooks (`onOpen`, `onClose`, `onBeforeClose`). Your component interacts with these hooks via `useBladeNavigation` or by defining them in the `openBlade` call. |

You should define these props in your blade component using `defineProps` as needed (typically `param` and `options` if your blade logic uses them). `expanded` and `closable` can also be part of your props definition if you need to react to their state directly, though they are often implicitly handled by UI components like `VcBlade`.

### Standard events (emitted by your blade component)

Your blade component can emit the following standard events to interact with the navigation system or its parent blade. You should define these events using `defineEmits` if your blade needs to trigger these actions.

| Event           | Payload                                              | Description                                                                                                     |
| :-------------- | :--------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| `close:blade`   | -                                                    | Emitted by the blade to request its own closure. The `VcBlade` component often handles this via its own close button. |
| `expand:blade`  | -                                                    | Emitted by the blade if it has custom logic to request expansion (less common, typically system-handled).      |
| `collapse:blade`| -                                                    | Emitted by the blade if it has custom logic to request collapse (less common, typically system-handled).       |
| `parent:call`   | `IParentCallArgs { method, args?, callback? }`       | Emitted to call an exposed method on the immediate parent blade. See `IParentCallArgs` in `useBladeNavigation`. |

### Exposed methods (`defineExpose`)

Your blade component can expose methods using `defineExpose`. These methods can then be called by child blades using the `parent:call` event and `useBladeNavigation().onParentCall` mechanism.

```typescript
// Inside your blade component's <script setup>
defineExpose({
  refreshData(filters) {
    // ... logic to refresh data ...
    return { status: 'ok' };
  }
});
```

## `useBladeNavigation()` composable API

This is the primary API for interacting with the blade navigation system programmatically.

### Return value

An object with the following properties and methods:

#### Properties

| Property                     | Type                                                            | Description                                                                                                   |
| :--------------------------- | :-------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| `blades`                     | `ComputedRef<BladeVNode[]>`                                     | A read-only array of all currently managed blade VNodes in the navigation stack.                                |
| `activeWorkspace`            | `ComputedRef<BladeVNode | undefined>`                           | A read-only reference to the current workspace blade VNode, if one is active. The workspace is always at `idx: 0`. |
| `currentBladeNavigationData` | `ComputedRef<BladeVNode['props']['navigation'] \| undefined>` | A read-only reference to the `navigation` object of the current blade instance where the composable is called. Provides access to `idx`, `isVisible`, lifecycle hooks, etc., for the *current* blade context. |

#### Methods

| Method                 | Signature                                                                                                 | Description                                                        |
| :--------------------- | :-------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------|
| `openBlade`            | `<Blade extends Component>(args: IBladeEvent<Blade>, isWorkspace?: boolean) => Promise<void | NavigationFailure>` | Opens a new blade or a workspace. The `args` object (`IBladeEvent`) includes: `blade` (component constructor or its **registered name**), `param?` (string), `options?` (object), `onOpen?` (hook), `onClose?` (hook), `onBeforeClose?` (hook), `replaceCurrentBlade?: boolean`. If `isWorkspace` is true, the blade opens as a new workspace, replacing any existing ones. |
| `closeBlade`           | `(index: number) => Promise<boolean>`                                                                     | Closes blades from the given `index` onwards. Returns `true` if closure was prevented by an `onBeforeClose` hook, `false` otherwise.                                                                                                                                                             |
| `goToRoot`             | `() => RouteLocationRaw`                                                                                  | Returns a `RouteLocationRaw` object pointing to the defined root/main route of the application. Useful for resetting navigation.                                                                                                                                                                    |
| `onParentCall`         | `(args: IParentCallArgs, currentBladeIndex?: number) => void`                               | Handles the `parent:call` event emitted by
child blades. This allows a blade to define handlers for methods called by its children. The recommended way for child blades to call parent methods is to emit the `parent:call` event, which is then handled by this listener. `currentBladeIndex` specifies which blade is listening for the call, ensuring the correct parent responds. |
| `onBeforeClose`        | `(cb: () => Promise<boolean | undefined>) => void`                                                         | Registers a callback function to be executed before the *current* blade (where this is called) closes. The callback should return `false` to allow closing, or `true` (or a Promise resolving to `true`) to prevent it.                                                                        |
| `resolveBladeByName`   | `(name: string) => BladeInstanceConstructor \| undefined`                                                  | Resolves a blade component constructor by its **name (as registered by the modularity system via `createAppModule`)**.                                                                                                                                                                                                             |
| `routeResolver`        | `(to: RouteLocationNormalized) => Promise<RouteLocationRaw \| undefined> \| RouteLocationRaw \| undefined`     | (Advanced) The main function used by the Vue Router navigation guard to parse incoming URLs and orchestrate the opening of workspaces and blades based on their **registered `url` properties**.                                                                                                                                              |
| `setNavigationQuery`   | `(query: Record<string, string \| number>) => void`                                                        | Sets URL query parameters for the current active workspace. Parameters are prefixed with the workspace name (e.g., `workspacename_param=value`).                                                                                                                                                 |
| `getNavigationQuery`   | `() => Record<string, string \| number> \| undefined`                                                       | Retrieves URL query parameters scoped to the current active workspace, removing the prefix.                                                                                                                                                                                                      |
| `setBladeError`   | `(bladeIdx: number, error: unknown) => void`                                                       | Sets an error state for a specific blade at the given index. This is useful for displaying an error boundary or a custom error message within the blade.                                                                                                                                                                                                      |
| `clearBladeError`   | `(bladeIdx: number) => void`                                                       | Clears the error state for the blade at the given index.                                                                                                                                                                                                     |

### `IBladeEvent<Blade>` interface

When calling `openBlade`, the `args` parameter is of type `IBladeEvent`:

```typescript
interface IBladeEvent<T extends Component = Component> {
  blade: BladeInstanceConstructor<T> | { name: string } | undefined; // Component definition or its registered name
  options?: Record<string, any>;    // Custom data for the blade
  param?: string;                   // URL parameter for the blade
  onOpen?: () => void;              // Hook called after blade is opened and mounted
  onClose?: () => void;             // Hook called after blade is closed and unmounted
  onBeforeClose?: () => Promise<boolean | undefined>; // Hook called before blade closes. Return false to allow, true to prevent.
  replaceCurrentBlade?: boolean;    // If true, the current blade will be marked as not visible before opening the new one.
}
```

### `IParentCallArgs` interface

Used with `onParentCall` and the `parent:call` event:

```typescript
interface IParentCallArgs {
  method: keyof CoreBladeExposed; // Name of the method exposed by the parent
  args?: unknown;                 // Arguments to pass to the parent's method
  callback?: (result: unknown) => void; // Optional callback to receive the result from the parent's method
}
```

## Usage examples

### Open standard blade

```vue
// Inside a component (e.g., a list view blade)
<script setup lang="ts">
import { useBladeNavigation } from '@vc-shell/framework/shared';
import ProductDetailsBlade from './ProductDetailsBlade.vue'; // Your blade component, assumed to be registered via createAppModule

const { openBlade } = useBladeNavigation();

function viewProduct(productId: string) {
  openBlade({
    blade: { name: 'ProductDetailsBlade' }, // Name under which ProductDetailsBlade was registered (e.g., its component name)
    param: productId,
    options: { someOption: 'value' },
    onOpen: () => console.log('Product Details blade opened!'),
    onClose: () => console.log('Product Details blade closed.'),
  });
}
</script>
```

### Open blade as workspace

Workspaces are typically top-level blades that replace the entire current blade stack.

```vue
// Inside a main menu or dashboard component
<script setup lang="ts">
import { useBladeNavigation } from '@vc-shell/framework/shared';
// import SettingsWorkspace from './SettingsWorkspace.vue'; // Component definition

const { openBlade } = useBladeNavigation();

function openSettings() {
  openBlade({
    blade: { name: 'SettingsWorkspace' }, // Name under which SettingsWorkspace was registered
  }, true); // Second argument `true` signifies it's a workspace
}
</script>
```

### Prevent blade closure (unsaved changes)

```vue
// Inside ProductEditorBlade.vue
<script setup lang="ts">
import { ref } from 'vue';
import { useBladeNavigation, usePopup } from '@vc-shell/framework/shared'; // Assuming usePopup exists

const { onBeforeClose } = useBladeNavigation();
const { showConfirmation } = usePopup(); // Your confirmation dialog composable

const hasUnsavedChanges = ref(false);
// ... logic to set hasUnsavedChanges to true when form is dirty

onBeforeClose(async () => {
  if (hasUnsavedChanges.value) {
    const confirmed = await showConfirmation(
      'You have unsaved changes. Are you sure you want to close?'
    );
    return !confirmed; // Return `true` to PREVENT closing if user cancels (confirmed = false)
                       // Return `false` to ALLOW closing if user confirms (confirmed = true)
  }
  return false; // No unsaved changes, allow closing
});
</script>
```

### Parent-child blade communication

```vue
// ParentBlade.vue
<script setup lang="ts">
import { useBladeNavigation } from '@vc-shell/framework/shared';
import ChildBladeWithData from './ChildBladeWithData.vue';

const { openBlade } = useBladeNavigation();

function openChild() {
  openBlade({ blade: ChildBladeWithData });
}

defineExpose({
  refreshParentData(newData: any) {
    console.log('Parent got data from child:', newData);
    // ... update parent's data ...
    return { status: 'Refreshed in parent' };
  }
});
</script>

// ChildBladeWithData.vue
<script setup lang="ts">
import { getCurrentInstance } from 'vue';

export interface Emits {
  (event: "parent:call", args: IParentCallArgs): void;
  (event: "close:blade"): void;
  (event: "collapse:blade"): void;
  (event: "expand:blade"): void;
}

const emit = defineEmits<Emits>();

function sendDataToParent() {
  const dataToSend = { id: 1, value: 'Updated Value' };
  emit('parent:call', {
    method: 'refreshParentData',
    args: dataToSend,
    callback: (result: any) => {
      console.log('Parent call result:', result);
    }
  });
}
</script>
<template>
  <VcBlade title="Child Blade">
    <VcButton @click="sendDataToParent">Send Data & Refresh Parent</VcButton>
  </VcBlade>
</template>
```

### Work with navigation query parameters

```vue
// Inside a Workspace Blade (e.g., ProductListWorkspace.vue)
<script setup lang="ts">
import { ref, watch, onMounted } from 'vue';
import { useBladeNavigation } from '@vc-shell/framework/shared';

const { setNavigationQuery, getNavigationQuery } = useBladeNavigation();

const filters = ref({
  searchTerm: '',
  category: null,
});

// Load initial query params
onMounted(() => {
  const query = getNavigationQuery();
  if (query) {
    filters.value.searchTerm = query.searchTerm || '';
    filters.value.category = query.category || null;
    // Note: Ensure 'category' in query matches `filters.value.category` type if it's not string.
  }
});

// Watch for filter changes and update URL
watch(filters, (newFilters) => {
  setNavigationQuery(newFilters);
  // ... also refetch data based on newFilters ...
}, { deep: true });
</script>
```

## Deep linking and URL structure

The blade navigation system relies on the Vue Router and constructs URLs that reflect the current blade stack.

- A base URL segment might be present (e.g., a tenant ID or a main route parameter).
- The first significant path segment after the base usually represents the **workspace blade's URL**.
- Subsequent segments can represent child **blade URLs** and their **parameters**.
- Example: `/#/tenant-id/products/details/123`
    - `tenant-id`: Base parameter (if applicable, e.g., from `sellerId` in the route).
    - `products`: URL for the `ProductsWorkspace`.
    - `details`: URL for the `ProductDetailsBlade`.
    - `123`: Parameter for `ProductDetailsBlade`.

The `routeResolver` function in `useBladeNavigation` is responsible for parsing these URLs on initial load or direct navigation and reconstructing the blade stack. Page components define their `url` property (e.g., `url: '/details'`) as a static property, which `createAppModule` uses to configure routing.

### Vue router setup

To enable deep linking and URL-driven blade navigation, you need to configure a catch-all route in your Vue Router setup. This route will pass the navigation handling to `routeResolver`.

```typescript
// Example from apps/vendor-portal/src/router/routes.ts
// Ensure your main layout component (which includes <VcBladeNavigation />) is correctly specified.

import { useBladeNavigation } from '@vc-shell/framework/shared'; // Adjust path as needed
// import MainLayout from '@/layouts/MainLayout.vue'; // Example: your main layout component

// Example of a sellerId regex, adapt as needed or omit if not used
// const sellerIdRegex = '[^/]+';

export const routes = [
  // ... other routes ...
  {
    // If you have a dynamic prefix like sellerId:
    // path: `/:sellerId(${sellerIdRegex})?/:pathMatch(.*)*`,

    // If you don't have a dynamic prefix or it's handled differently:
    path: `/:pathMatch(.*)*`,
    // component: MainLayout, // Replace MainLayout with your actual main layout component
    beforeEnter: async (to) => {
      const { routeResolver } = useBladeNavigation();
      return routeResolver(to);
    },
  },
  // ... other routes ...
];
```
In this setup:

-   `/:pathMatch(.*)*` captures all paths not matched by previous routes.
-   If you use a dynamic prefix like `:sellerId`, include it as shown in the commented example. The `sellerIdRegex` helps define what constitutes a valid `sellerId`.
-   The `component` for this route should be your main application component or layout that renders `VcBladeNavigation`. You will need to ensure this is correctly imported and specified.
-   The `beforeEnter` navigation guard calls `routeResolver(to)` from `useBladeNavigation`, which then handles parsing the URL and opening the appropriate blades.

## Responsive behavior

- **Desktop**: Multiple blades are displayed side-by-side.
- **Tablet/Mobile**: Fewer blades (often just one) are visible, with back navigation provided (e.g., `VcMobileBackButton`).
The `VcBladeNavigation` component, using `isMobile` and `quantity` of visible blades, adapts the layout.

## Best practices

* **Clear blade hierarchy**: Design a logical flow of blades.
* **Focused blades**: Each blade should have a single, clear responsibility.
* **Meaningful titles**: Use descriptive titles for blades (often exposed via `defineExpose({ title: '...' })` or a reactive ref tied to the component's `title` prop if using `VcBlade`).
* **Prevent data loss**: Utilize `onBeforeClose` for blades with forms or unsaved state.
* **Parent-child communication**: Prefer the `parent:call` mechanism over global event buses.
* **Breadcrumb awareness**: Ensure titles are suitable for breadcrumbs.
* **URL design**: Define clear and consistent `url` properties on your page components that are then used by `createAppModule` for routing.
* **Permissions**: Define `permissions` properties on your page components, which are used by `createAppModule` and checked by `useBladeNavigation`.
* **Global registration**: Ensure your page components are correctly configured with necessary static properties (like `name`, `url`, `isWorkspace`, `permissions`, `menuItem`) and included in your module's `createAppModule` definition for automatic registration.

## Built-in error handling

One of the key features of the blade navigation system is its robust error handling. Each blade in the navigation system is automatically wrapped with the `ErrorInterceptor` component, which captures any errors that occur within the blade and prevents them from crashing the entire application.

### How error handling works

When an error occurs within a blade component (for example, during rendering, in a lifecycle hook, or in an event handler), the `ErrorInterceptor` surrounding the blade captures the error. The error is formatted, and the blade displays an error UI instead of its normal content. Users can dismiss the error to retry or continue using other parts of the application.

This error handling is implemented directly in the `vc-blade-navigation.vue` component's render function:

```vue
// Simplified excerpt from vc-blade-navigation.vue's render function
h(
  ErrorInterceptor,
  { key: index, capture: true },
  {
    default: ({ error, reset }) => {
      return withDirectives(
        h(VcBladeView, {
          // ...props...
          error,
          onVnodeUnmounted: reset, // Assuming reset is passed from ErrorInterceptor to VcBladeView for unmount
        }),
        // ...directives...
      );
    }
  }
)
```

### Benefits of built-in error handling

-   **Isolation**: Errors in one blade don't affect other blades or the overall application.
-   **Resilience**: The application remains functional even when individual blades encounter errors.
-   **Consistent UX**: Error presentation is consistent across all blades.
-   **Developer experience**: Reduces boilerplate for error handling in each blade.

### Error display in blades

When an error occurs, the blade's view (managed internally by the system, wrapping your component) will typically display:

*  An error icon.
* The error message.
* A button to read more about the error.

### Relationship with global error handling

-   Errors caught by blade `ErrorInterceptor`s (with `capture: true`) typically **do not** propagate to Vue's global `app.config.errorHandler`.
-   This layered approach ensures errors are handled contextually.

