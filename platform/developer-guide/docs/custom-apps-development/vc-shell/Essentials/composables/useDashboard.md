# useDashboard Composable

The `useDashboard` composable provides a convenient API for managing dashboard widgets, their layout, and permission-based visibility within VC-Shell applications.

This document details the API provided by `useDashboard`. For comprehensive examples of creating interactive dashboards, registering various widget types, and managing layouts, please refer to the [How-To: Creating Interactive Dashboards with `useDashboard`](../Usage-Guides/creating-interactive-dashboards-with-usedashboard.md) guide.

## API reference

### Return value

The `useDashboard()` function returns an instance of `IDashboardServiceAPI` (name may vary, conceptually it's the API for interacting with the service) with the following methods:

```typescript
import { type Component, type DefineComponent } from 'vue';

// Simplified conceptual API structure returned by useDashboard
interface IDashboardServiceAPI {
  /**
   * Registers a new widget to be displayed on the dashboard.
   * @param widget - An object conforming to `DashboardWidget` interface.
   */
  registerWidget: (widget: DashboardWidget) => void;

  /**
   * Retrieves an array of all `DashboardWidget` objects that the current user has permission to view.
   * The layout and actual rendering are typically handled by a dedicated dashboard component (e.g., VcDraggableDashboard).
   */
  getWidgets: () => DashboardWidget[];

  /**
   * Updates the grid position of an existing widget.
   * This is often called by the dashboard component when a user drags and drops a widget.
   * @param widgetId - The unique `id` of the widget to update.
   * @param position - An object conforming to `DashboardWidgetPosition` specifying the new x and y coordinates.
   */
  updateWidgetPosition: (widgetId: string, position: DashboardWidgetPosition) => void;

  /**
   * Retrieves the current layout of widgets as a Map.
   * Keys are widget IDs, and values are `DashboardWidgetPosition` objects.
   * This is useful for saving/restoring layouts.
   */
  getLayout: () => Map<string, DashboardWidgetPosition>;
  
  /**
   * (Potentially other methods like unregisterWidget, clearWidgets etc., if exposed by the composable)
   * unregisterWidget?: (widgetId: string) => void;
   * clearAllWidgets?: () => void;
   */
}
```

### Interfaces

#### `DashboardWidget`
Defines the structure of a dashboard widget object.

```typescript
interface DashboardWidget {
  /** Unique identifier for the widget. Essential for layout management and updates. */
  id: string;
  /** Display name of the widget, often shown in a widget header or selection list. */
  name: string;
  /** 
   * The Vue component to be rendered for this widget. 
   * It's recommended to wrap components with `markRaw` from Vue before passing them here.
   * e.g., `component: markRaw(MySalesChartWidgetComponent)`
   */
  component: Component | DefineComponent;
  /** Defines the size of the widget in grid units (width and height). */
  size: DashboardWidgetSize;
  /** Optional: Initial grid position (x, y coordinates) of the widget. */
  position?: DashboardWidgetPosition;
  /** Optional: An array of permission strings. The widget will only be visible if the user has at least one of these permissions. */
  permissions?: string[];
  /** Optional: An object containing props to be passed to the `component`. */
  props?: Record<string, unknown>;
}
```

#### `DashboardWidgetSize`
Defines the dimensions of a widget on the dashboard grid.

```typescript
interface DashboardWidgetSize {
  /** Width of the widget in grid column units. */
  width: number;
  /** Height of the widget in grid row units. */
  height: number;
}
```

#### `DashboardWidgetPosition`
Defines the coordinates of a widget on the dashboard grid.

```typescript
interface DashboardWidgetPosition {
  /** Horizontal grid position (column index, typically 0-based). */
  x: number;
  /** Vertical grid position (row index, typically 0-based). */
  y: number;
}
```

## Pre-registration function

VC-Shell provides a global `registerDashboardWidget` function that allows registration of dashboard widgets *before* the main `DashboardService` instance is created or provided. This is useful for modules or plugins that need to declare their dashboard widgets during their own initialization phase.

- Items added via this global function are placed in a temporary queue.
- When the `DashboardService` is initialized (typically via `provideDashboardService`), it processes this queue.

```typescript
import { registerDashboardWidget, type DashboardWidget } from '@vc-shell/framework';
import MyCustomDashboardWidget from './MyCustomDashboardWidget.vue'; // Example component
import { markRaw } from 'vue';

const widgetConfig: DashboardWidget = {
  id: 'my-module-widget',
  name: 'Module Stats',
  component: markRaw(MyCustomDashboardWidget),
  size: { width: 2, height: 1 },
  permissions: ['view-module-stats']
};

// Example: Pre-registering a dashboard widget in a module's setup or bootstrap.ts
registerDashboardWidget(widgetConfig);
```



## Important notes for usage

-   Widget IDs (`id`) must be unique across the entire dashboard.
-   The grid system typically uses zero-based indexing for `x` and `y` positions.
-   Widget permissions are evaluated against the current user's permissions using the VC-Shell permission system (see `usePermissions`).
-   It's highly recommended to use a standard wrapper component like `DashboardWidgetCard` inside your custom widget components for consistent styling (header, loading states, actions menu).

## Related resources

-   [How-To: Creating Interactive Dashboards with `useDashboard`](../Usage-Guides/creating-interactive-dashboards-with-usedashboard.md) - Practical examples for using this composable.
-   [`usePermissions` Composable](../composables/usePermissions.md) - For understanding how widget visibility is controlled.
-   `DraggableDashboard` - The UI component typically used to render the dashboard and manage layouts.
-   `DashboardWidgetCard` - The recommended wrapper for individual widget content for consistent styling.
-   [Vue 3 Documentation on Provide/Inject](https://vuejs.org/guide/components/provide-inject.html) - For understanding the dependency injection mechanism.
