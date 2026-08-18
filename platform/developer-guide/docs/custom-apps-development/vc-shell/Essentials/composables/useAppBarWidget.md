# useAppBarWidget Composable

The `useAppBarWidget` composable provides a convenient API for managing widgets (icons, buttons, custom components) displayed in the application's main navigation bar (AppBar).

This document details the API provided by `useAppBarWidget`. For practical examples of how to create and integrate various types of AppBar widgets, please refer to the [How-To: Adding App Bar Widgets with `useAppBarWidget`](../Usage-Guides/adding-app-bar-widgets-with-useappbarwidget.md) guide.

## API reference

### Return value

The `useAppBarWidget()` function returns an instance of `IAppBarWidgetServiceAPI` (name may vary, conceptually it's the API for interacting with the service) with the following methods and properties:

```typescript
import { type ComputedRef, type Component, type DefineComponent } from 'vue';

interface IAppBarWidgetServiceAPI {
  /** 
   * A reactive array of all registered `AppBarWidget` items, sorted by their `order` property. 
   * Suitable for direct use in a `v-for` directive to render the AppBar widgets.
   */
  items: ComputedRef<AppBarWidget[]>;

  /**
   * Registers a new widget in the AppBar.
   * @param options - An object conforming to `RegisterAppBarWidgetOptions`.
   * @returns The `id` of the registered widget (either the one provided or an auto-generated UUID).
   */
  register: (options: RegisterAppBarWidgetOptions) => string;

  /**
   * Removes a widget from the AppBar by its unique identifier.
   * @param id - The `id` of the widget to remove.
   */
  unregister: (id: string) => void;
}
```

### Interfaces

#### `AppBarWidget`
Defines the structure of a registered AppBar widget object.

```typescript
interface AppBarWidget {
  /** Unique identifier for the widget. */
  id: string;
  /** 
   * Optional numeric value to determine the widget's position in the AppBar. 
   * Widgets are typically sorted by this value in ascending order (lower numbers appear first/leftmost).
   */
  order?: number;
  /** 
   * Optional: The icon to display for the widget. 
   * Can be a string reference (e.g., Material Design Icon name like 'material-notifications') or an imported Vue component.
   */
  icon?: Component | string;
  /** 
   * Optional: A Vue component to be rendered, often as a dropdown or panel when the widget is activated.
   * It's recommended to wrap components with `markRaw` from Vue before passing them here if they don't need to be reactive themselves, to optimize performance.
   * e.g., `component: markRaw(MyCustomPanelComponent)`
   */
  component?: Component | DefineComponent; // DefineComponent allows for async components too
  /** Optional: An object containing props to be passed to the `component` if one is provided. */
  props?: Record<string, unknown>;
  /** 
   * Optional: A callback function to execute when the widget (e.g., its icon) is clicked.
   * Often used for simple actions or to toggle the visibility of an associated `component`.
   */
  onClick?: () => void;
  /** 
   * Optional: Name of a target slot where the widget should be rendered if the AppBar supports multiple named widget areas.
   * (Usage depends on the specific AppBar implementation in your application).
   */
  slot?: string;
  /** 
   * Optional: Indicates whether a badge should be shown on the widget icon (e.g., for notifications).
   * Can be a static boolean value or a function that returns a boolean (for reactive badges).
   */
  badge?: boolean | (() => boolean);
}
```

#### `RegisterAppBarWidgetOptions`
Defines the options object used when calling `register`.

```typescript
interface RegisterAppBarWidgetOptions extends Omit<AppBarWidget, "id" | "component"> {
  /** 
   * Optional: A unique identifier for the widget. 
   * If not provided, a UUID will be automatically generated.
   */
  id?: string;
  /** 
   * Optional: A Vue component to be rendered.
   * Recommended to use `markRaw()` for static components.
   */
  component?: Component | DefineComponent; // Allowing for markRaw or async components
}
```

## Pre-registration function

VC-Shell provides a global `addAppBarWidget` function that allows registration of AppBar widgets *before* the main `AppBarWidgetService` instance is created or provided. This is useful for modules or plugins that need to declare their AppBar widgets during their own initialization phase.

- Items added via this global function are placed in a temporary queue.
- When the `AppBarWidgetService` is initialized (typically via `provideAppBarWidgetService`), it processes this queue.

```typescript
import { addAppBarWidget } from '@vc-shell/framework';
import MyCustomWidgetComponent from './MyCustomWidgetComponent.vue'; // Example component
import { markRaw } from 'vue';

// Example: Pre-registering an AppBar widget in a module's setup or bootstrap.
addAppBarWidget({
  id: 'my-module-widget',
  icon: 'material-extension',
  order: 50,
  component: markRaw(MyCustomWidgetComponent),
  onClick: () => console.log('Module widget clicked!')
});
```

## Related Resources

- [How-To: Adding App Bar Widgets with `useAppBarWidget`](../Usage-Guides/adding-app-bar-widgets-with-useappbarwidget.md) - Practical examples for using this composable.
- [Vue 3 Documentation on Provide/Inject](https://vuejs.org/guide/components/provide-inject.html) - For understanding the dependency injection mechanism that often underpins such composables.
