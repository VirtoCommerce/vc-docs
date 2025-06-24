# `useWidgets` Composable

The `useWidgets` composable provides a robust API for managing widget components within **blades** in the VC-Shell framework. It allows components to dynamically register, unregister, update, and retrieve widgets associated with specific blades.

Blade widgets are self-contained Vue components that can be attached to blades to offer supplementary functionality, display information, or provide interactive elements. The `useWidgets` composable is the primary interface for managing the lifecycle and properties of these widgets from your Vue components.

While `useWidgets` manages the registration and state of widget metadata, the actual creation of widget UI is typically done by developing custom Vue components. It is highly recommended to use the `VcWidget` atomic component as a base for building new blade widgets to ensure visual consistency and leverage built-in functionalities.

For practical examples and step-by-step instructions on creating and registering blade widgets, refer to the [How-To: Creating and Registering Blade Widgets with `useWidgets`](../Usage-Guides/creating-and-registering-widgets-with-usewidgets.md) guide.

## API reference

### Return value

The `useWidgets()` composable returns an `IWidgetService` object with the following methods and properties:

```typescript
import { type Component, type ComponentInternalInstance, type ComputedRef, type Ref } from "vue";
import { IBladeInstance } from "@vc-shell/framework"; // Conceptual import

interface IWidget {
  id: string;
  title?: string;
  component: Component; 
  props?: Record<string, unknown>;
  events?: Record<string, (...args: any[]) => void>; 
  isVisible?: boolean | ComputedRef<boolean> | Ref<boolean> | ((blade?: IBladeInstance) => boolean);
  updateFunctionName?: string;
}

interface IWidgetRegistration {
  bladeId: string;
  widget: IWidget;
}

interface IWidgetService {
  /**
   * Registers a widget component for a specific blade.
   * @param widget - The widget configuration object (IWidget).
   * @param bladeId - The ID of the blade to associate the widget with.
   */
  registerWidget: (widget: IWidget, bladeId: string) => void;

  /**
   * Removes a previously registered widget from a specific blade.
   * @param widgetId - The ID of the widget to unregister.
   * @param bladeId - The ID of the blade from which to remove the widget.
   */
  unregisterWidget: (widgetId: string, bladeId: string) => void;

  /**
   * Retrieves an array of all widgets registered for a specific blade.
   * @param bladeId - The ID of the blade.
   * @returns An array of IWidget objects.
   */
  getWidgets: (bladeId: string) => IWidget[];

  /**
   * Removes all widgets registered for a specific blade.
   * @param bladeId - The ID of the blade.
   */
  clearBladeWidgets: (bladeId: string) => void;

  /**
   * A reactive array containing all widget registrations across all blades.
   * Each element is an IWidgetRegistration object.
   */
  registeredWidgets: IWidgetRegistration[];

  /**
   * Checks if a widget with the given ID is currently considered active.
   * Activation is typically handled by components like VcWidget.
   * @param id - The widget ID.
   */
  isActiveWidget: (id: string) => boolean;

  /**
   * Sets a widget as active. Typically called internally by widget components like VcWidget.
   * @param options - Object containing the exposed instance of the widget component and its ID.
   */
  setActiveWidget: (options: { exposed: ComponentInternalInstance["exposed"]; widgetId: string }) => void;

  /**
   * Triggers an update function on the currently active widget if `updateFunctionName` was defined in its IWidget configuration.
   * Typically called by the system or specific UI controls.
   */
  updateActiveWidget: () => void;

  /**
   * Checks if a widget with the specified ID has been registered (globally, not blade-specific).
   * @param id - The widget ID.
   */
  isWidgetRegistered: (id: string) => boolean;

  /**
   * Updates properties of an existing, registered widget.
   * @param options - Object containing the widget ID, blade ID, and a partial IWidget object with properties to update.
   */
  updateWidget: (options: { id: string; bladeId: string; widget: Partial<IWidget> }) => void;
}
```

### `IWidget` interface

This interface defines the structure for a widget object used during registration and management.

```typescript
import { type Component, type ComputedRef, type Ref } from "vue";
import { IBladeInstance } from "@vc-shell/framework"; // Conceptual import

interface IWidget {
  /** 
   * Unique identifier for the widget. Essential for updates, unregistration, and activation.
   */
  id: string;

  /** 
   * Optional: Display title for the widget. 
   * This might be used by a wrapper component (like `VcWidget`) or by the blade's widget container.
   */
  title?: string;

  /** 
   * The Vue component to be rendered for this widget. 
   * It's highly recommended to wrap components with `markRaw` from Vue if they don't need to be reactive at the registration level.
   * e.g., `component: markRaw(MyCustomWidgetComponent)`
   */
  component: Component; // Should be a more specific type like ConcreteComponent

  /** 
   * Optional: An object containing props to be passed to the `component`.
   */
  props?: Record<string, unknown>;

  /** 
   * Optional: An object mapping event names to handlers. The widget rendering system might attach these to the `component`.
   * (Note: Direct event handling in `IWidget` is less common; usually, events are handled within the widget component itself.)
   */
  events?: Record<string, (...args: any[]) => void>;

  /** 
   * Optional: Controls the visibility of the widget. 
   * Can be a static boolean, a Vue `Ref<boolean>` or `ComputedRef<boolean>`, or a function returning a boolean.
   * The function variant can receive the blade instance as an argument for contextual visibility.
   * e.g., `isVisible: (blade) => blade && blade.id === 'specific-blade'`
   */
  isVisible?: boolean | ComputedRef<boolean> | Ref<boolean> | ((blade?: IBladeInstance) => boolean);

  
  /**
   * Optional: Specifies the name of a function exposed by the widget's component that should be called
   * when `updateActiveWidget()` is invoked by the system. This allows for a standardized way to refresh
   * the content or state of the active widget.
   * Example: If `updateFunctionName` is 'refreshData', then `activeWidget.exposed.refreshData()` would be called.
   */
  updateFunctionName?: string;
}
```

## Pre-registration function (global `registerWidget`)

VC-Shell also provides a global `registerWidget(widget: IWidget, bladeId: string)` function, which can be imported directly (e.g., from `@vc-shell/framework`). This function allows modules or plugins to declare widgets for specific blades even *before* the main `useWidgets` system (and its provider) is fully initialized.

- Items added via this global function are placed in a temporary queue.
- When the widget service initializes (through its provider), it processes this queue and formally registers these pre-registered widgets.

This mechanism is useful for:
*   Core framework widgets that need to be available by default.
*   Widgets contributed by self-contained modules that should be ready as soon as their target blade might exist.

**Example of global registration:**
```typescript
// In a module's bootstrap file (e.g., my-module/index.ts)
import { registerWidget as globalRegisterWidget } from '@vc-shell/framework'; // Adjust import path as per actual export
import { markRaw } from 'vue';
import MyModuleGlobalWidget from './MyModuleGlobalWidget.vue';

const globalWidgetConfig: IWidget = {
  id: 'my-module-global-status',
  title: 'Module Status',
  component: markRaw(MyModuleGlobalWidget),
  props: { defaultMode: 'overview' },
  isVisible: true
};

// Register for a known blade ID where this widget should appear
globalRegisterWidget(globalWidgetConfig, 'dashboard-main'); 
```

## Best practices

Refer to the [How-To: Creating and Registering Blade Widgets with `useWidgets`](../Usage-Guides/creating-and-registering-widgets-with-usewidgets.md) guide for detailed best practices, including:

* Unique widget IDs.
* Component optimization (`markRaw`).
* Proper cleanup (`unregisterWidget`).
* Reactive props.
* Contextual visibility (`isVisible`).
* Leveraging `VcWidget`.
* Using `updateFunctionName`.
* Blade ID management.

## Related resources

-   [`VcBlade`](../ui-components/vc-blade.md) : The component that typically hosts and displays widgets.
-   [`VcWidget`](../ui-components/vc-widget.md) : Recommended base component for creating new widgets.
-   [How-To: Creating and Registering Blade Widgets with `useWidgets`](../Usage-Guides/creating-and-registering-widgets-with-usewidgets.md): A practical guide to widget development and registration.
-   [Vue 3 Documentation on Provide/Inject](https://vuejs.org/guide/components/provide-inject.html): For understanding the dependency injection mechanism that often underpins such composables.
