# useSettingsMenu Composable

The `useSettingsMenu` composable provides a convenient API for managing settings menu items in VC-Shell applications. It allows components to register, organize, and access settings-related components that will be displayed in the application's settings menu.

This document focuses on the API provided by `useSettingsMenu`. For detailed examples, usage patterns, and best practices for creating and managing settings menu items, please refer to the [How-To: Managing Settings Menu with `useSettingsMenu`](../Usage-Guides/managing-settings-menu-with-usesettingsmenu.md) guide.

## API reference

### Return value

The `useSettingsMenu` composable returns an object (`ISettingsMenuService`) with the following properties and methods:

```typescript
import { type ComputedRef, type Component } from 'vue';

interface ISettingsMenuService {
  /** 
   * A reactive array of all registered settings menu items, sorted by their 'order' property. 
   * Suitable for direct use in a `v-for` directive to render the menu.
   */
  items: ComputedRef<SettingsMenuItem[]>;

  /**
   * Registers a new settings menu item.
   * @param options - An object conforming to `RegisterSettingsMenuItemOptions`.
   * @returns The `id` of the registered item (either the one provided or an auto-generated UUID).
   */
  register: (options: RegisterSettingsMenuItemOptions) => string;

  /**
   * Removes a settings menu item from the service.
   * @param id - The unique identifier of the settings menu item to remove.
   */
  unregister: (id: string) => void;
}
```

### Interfaces

#### `SettingsMenuItem`
Defines the structure of a registered settings menu item.

```typescript
import { type Component } from 'vue';

interface SettingsMenuItem {
  /** Unique identifier for the menu item. */
  id: string;
  /** The Vue component to be rendered for this settings item. */
  component: Component;
  /** 
   * Optional numeric value to determine the item's position in the menu. 
   * Lower numbers appear first. Defaults to an order that places it after 
   * previously registered items without a specific order.
   */
  order?: number;
  /** Optional: An object containing props to be passed to the `component`. */
  props?: Record<string, unknown>;
}
```

#### `RegisterSettingsMenuItemOptions`
Defines the options object used when calling `register`.

```typescript
import { type Component } from 'vue';

interface RegisterSettingsMenuItemOptions {
  /** 
   * Optional: A unique identifier for the item. 
   * If not provided, a UUID will be automatically generated.
   */
  id?: string;
  /** The Vue component to be rendered for this settings item. */
  component: Component;
  /** Optional: Numeric value for ordering. */
  order?: number;
  /** Optional: Props to pass to the `component`. */
  props?: Record<string, unknown>;
}
```

## Pre-registration function

VC-Shell also provides a global `addSettingsMenuItem` function. This allows modules or plugins to declare settings menu items even *before* the main settings management system is fully initialized via `provideSettingsMenu()`. 

- Items added via `addSettingsMenuItem` are placed in a temporary queue.
- When the settings system is initialized by `provideSettingsMenu()`, it processes this queue and integrates these pre-registered items.

This is particularly useful for core framework settings or settings contributed by self-contained modules.

```typescript
import { addSettingsMenuItem, type RegisterSettingsMenuItemOptions } from '@vc-shell/framework'; // Ensure correct import path
import MyCoreSettingComponent from './MyCoreSettingComponent.vue';
import { markRaw } from 'vue';

const coreSettingOptions: RegisterSettingsMenuItemOptions = {
  id: 'core-feature-x',
  component: markRaw(MyCoreSettingComponent),
  order: 10,
  props: { initialValue: true }
};

// Example: Pre-registering a setting in a module's bootstrap file
addSettingsMenuItem(coreSettingOptions);
```

## Related resources

-   [How-to: Managing settings menu with `useSettingsMenu`](../Usage-Guides/managing-settings-menu-with-usesettingsmenu.md) - Practical guide with examples for using this composable.
-   [Vue 3 documentation on provide/inject](https://vuejs.org/guide/components/provide-inject.html) - For understanding the dependency injection mechanism.
