# `useToolbar` Composable API Reference

The `useToolbar` composable provides a convenient API for managing toolbar items for different blades in VC-Shell applications. This composable allows components to register, update, and manage toolbar elements within the application's UI, specifically targeting the toolbar of the current blade context.

## Return value

The `useToolbar` composable returns an object (`ToolbarUtility`) with the following methods and properties:

```typescript
interface ToolbarUtility {
  /**
   * Registers a toolbar item (button or other UI element) for the current blade.
   * The item is automatically associated with the active blade and cleaned up on component unmount.
   */
  registerToolbarItem: (toolbarItem: IToolbarItem) => void;

  /**
   * Removes a previously registered toolbar item by its ID from the current blade.
   */
  unregisterToolbarItem: (toolbarItemId: string) => void;

  /**
   * Updates properties of an existing, registered toolbar item.
   * Only the specified properties in the `toolbarItem` argument are updated.
   */
  updateToolbarItem: (id: string, toolbarItem: Partial<IToolbarItem>) => void;

  /**
   * Retrieves an array of all toolbar items currently registered for the active blade.
   * Note: This typically reflects items registered via useToolbar. Items passed via VcBlade's
   * `toolbar-items` prop might be managed separately by VcBlade itself.
   */
  getToolbarItems: () => IToolbarItem[];

  /**
   * Removes all toolbar items that were registered via `useToolbar` for the current blade.
   * This is often called automatically on component unmount for items registered by that component.
   */
  clearBladeToolbarItems: () => void;

  /**
   * Checks if a toolbar item with the specified ID is registered for a given blade ID.
   */
  isToolbarItemRegistered: (id: string, bladeId: string) => boolean;

  /**
   * A reactive Vue Ref containing a Map where keys are blade IDs and values are arrays
   * of IToolbarItem objects registered for that blade. This allows observing all toolbar
   * items managed by the ToolbarService.
   */
  registeredToolbarItems: Ref<Map<string, IToolbarItem[]>>;
}
```

## `IToolbarItem` interface

This interface defines the structure for a toolbar item object:

```typescript
interface IToolbarItem {
  /** 
   * Unique identifier for the toolbar item. 
   * Crucial for updates, unregistration, and preventing conflicts.
   */
  id: string;

  /** 
   * The display text for the toolbar item. 
   * Can be a static string or a Vue `ComputedRef<string>` for dynamic titles.
   */
  title: string | ComputedRef<string>;

  /** 
   * Optional: Name of a Material Design icon, path to an SVG, or a Vue component to be rendered as the icon.
   * Can be a static string or a Vue component.
   */
  icon?: string | Component;

  /** 
   * Optional: A number determining the order of the item in the toolbar. 
   * Higher values are typically displayed first (e.g., further to the left).
   */
  priority?: number;

  /** 
   * Optional: Controls the visibility of the toolbar item. 
   * Defaults to `true`. Can be a static boolean or a Vue `Ref<boolean>` / `ComputedRef<boolean>` for dynamic visibility.
   */
  isVisible?: boolean | Ref<boolean> | ComputedRef<boolean>;

  /** 
   * Optional: Controls whether the toolbar item is interactive (enabled/disabled). 
   * Defaults to `false` (enabled). Can be a static boolean or a Vue `Ref<boolean>` / `ComputedRef<boolean>` for dynamic state.
   */
  isDisabled?: boolean | Ref<boolean> | ComputedRef<boolean>;

  /** 
   * Optional: A function to be executed when the toolbar item is clicked.
   */
  clickHandler?: () => void;

  /**
   * Optional: A Vue component to be rendered instead of a standard button.
   * If provided, other properties like title, icon, clickHandler might be ignored or handled by the custom component itself.
   */
  component?: Component;

  /**
   * Optional: Properties to pass to the custom `component` if one is provided.
   */
  props?: Record<string, any>;
}
```

## Basic method signatures and usage snippets

Below are brief examples illustrating the invocation of each method. For comprehensive usage patterns, refer to the "How-To: Managing Blade Toolbars with `useToolbar`" guide.

### `registerToolbarItem`

Registers a new item. 

```typescript
import { useToolbar } from '@vc-shell/framework';
import { ref, computed } from 'vue';

const { registerToolbarItem } = useToolbar();
const isItemVisible = ref(true);

registerToolbarItem({
  id: 'my-unique-button',
  title: 'My Action',
  icon: 'material-save',
  priority: 100,
  isVisible: isItemVisible,
  isDisabled: computed(() => !isItemVisible.value),
  clickHandler: () => console.log('Action clicked!'),
});
```

### `unregisterToolbarItem`

Removes an item by its ID.

```typescript
// Assuming 'my-unique-button' was previously registered
const { unregisterToolbarItem } = useToolbar();

unregisterToolbarItem('my-unique-button');
```

### `updateToolbarItem`

Updates properties of an existing item.

```typescript
const { updateToolbarItem } = useToolbar();

// Assuming 'my-unique-button' is registered
updateToolbarItem('my-unique-button', {
  title: 'Save Changes', // Update title
  isDisabled: false,       // Enable the button
});
```

### `getToolbarItems`

Retrieves items for the current blade.

```typescript
const { getToolbarItems } = useToolbar();

const currentBladeItems: IToolbarItem[] = getToolbarItems();
console.log(currentBladeItems);
```

### `clearBladeToolbarItems`

Clears all items registered by `useToolbar` for the current blade.

```typescript
const { clearBladeToolbarItems } = useToolbar();

clearBladeToolbarItems();
```

### `isToolbarItemRegistered`

Checks if an item is registered for a specific blade.

```typescript
import { inject } from 'vue';
import { BladeInstance } from '@vc-shell/framework/injection-keys'; // Example injection key

const { isToolbarItemRegistered } = useToolbar();
const currentBlade = inject(BladeInstance, { id: 'fallback-blade' }); // Get current blade context

const isRegistered = isToolbarItemRegistered('my-unique-button', currentBlade.id);
console.log('Is registered:', isRegistered);
```

### `registeredToolbarItems` (Property)

Accessing the reactive map of all toolbar items.

```typescript
import { useToolbar } from '@vc-shell/framework';
import { watch } from 'vue';

const { registeredToolbarItems } = useToolbar();

watch(registeredToolbarItems, (newItemsMap) => {
  console.log('All registered toolbar items changed:', newItemsMap);
}, { deep: true });
```

## Pre-registration function

VC-Shell provides a global `addToolbarItem` function. This allows modules or plugins to declare toolbar items even *before* the main toolbar management system is fully initialized via `provideToolbarService()`.

- Items added via this global function are typically placed in a temporary queue.
- When the toolbar system is initialized, it processes this queue and integrates these pre-registered items, associating them with the specified blade context if required by the function's signature (e.g., `addToolbarItem(bladeId, item)`).

This is useful for core framework toolbar items or items contributed by self-contained modules that need to be available as soon as their target blade context might exist.

```typescript
import { addToolbarItem, type IToolbarItem } from '@vc-shell/framework'; // Ensure correct import path
import MyCustomToolbarComponent from './MyCustomToolbarComponent.vue';
import { markRaw } from 'vue';

const coreToolbarItem: IToolbarItem = {
  id: 'core-action-xyz',
  title: 'Core Action',
  icon: 'material-star',
  priority: 10,
  clickHandler: () => console.log('Core Action executed')
};

// Example: Pre-registering a toolbar item for a specific blade ID
// The exact signature of addToolbarItem (e.g., if it requires a bladeId) can vary.
// If bladeId is not part of addToolbarItem, the item might be globally available or require further association.
addToolbarItem('my-target-blade-id', coreToolbarItem);

// Example for a custom component toolbar item
const customCompItem: IToolbarItem = {
  id: 'custom-toolbar-comp',
  component: markRaw(MyCustomToolbarComponent),
  priority: 20,
  props: { initialMode: 'view' }
};
addToolbarItem('my-target-blade-id', customCompItem);
```

## Related resources

-   [How-to: Managing blade toolbars with `useToolbar`](../Usage-Guides/managing-blade-toolbars-with-usetoolbar.md) - For 
detailed usage patterns and best practices.
-   [Vue 3 documentation on provide/inject](https://vuejs.org/guide/components/provide-inject.html) - For understanding the dependency injection mechanism that often underpins such composables.
