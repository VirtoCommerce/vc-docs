# How-To: Creating and Registering Blade Widgets with `useWidgets`

This guide provides a practical walkthrough on how to create custom widget components and register them for display within specific **blades** in your VC-Shell application using the `useWidgets` composable.

## Prerequisites

-   Understanding of Vue 3 Composition API (`ref`, `computed`, `defineExpose`).
-   Familiarity with the [`useWidgets` API Reference](../composables/useWidgets.md).
-   Knowledge of the `VcWidget` atomic component, recommended as a base for blade widgets.
-   Basic understanding of VC-Shell's blade system.

## Core Concepts

-   **Blade Widgets**: Self-contained Vue components designed to offer supplementary information or interactive elements within a VC-Shell blade.
-   **`useWidgets` Composable**: The primary API for managing the registration, state, and lifecycle of these blade widgets.
-   **`VcWidget` Component**: A standardized UI component provided by VC-Shell, ideal for building custom blade widgets with a consistent look and feel.

## Step 1: Creating Your Blade Widget Component

When building a new widget for a blade, using `VcWidget` as its foundation is highly recommended. This ensures visual consistency with the VC-Shell framework and provides common widget functionalities.

**Example: `ProductStockWidget.vue`**

This widget displays stock information for a product and could be used within a product details blade.

```vue
// ProductStockWidget.vue
<template>
  <VcWidget
    :title="widgetTitle"
    :value="stockLevel"
    :icon="stockIcon"
    @click="handleWidgetClick"
  />
</template>

<script setup lang="ts">
import { VcWidget } from '@vc-shell/framework'; // Adjust import path if necessary
import { ref, computed, defineProps, defineExpose, onMounted } from 'vue';

const props = defineProps<{
  productId: string;
  initialStock?: number;
}>();

const stockLevel = ref(props.initialStock || 0);
const widgetTitle = computed(() => `Stock: ${props.productId}`);
const stockIcon = computed(() => stockLevel.value > 0 ? 'material-inventory_2' : 'material-production_quantity_limits');

async function fetchStock() {
  // Simulate API call to fetch stock
  await new Promise(resolve => setTimeout(resolve, 500));
  const newStock = Math.floor(Math.random() * 100);
  stockLevel.value = newStock;
  console.log(`Stock for ${props.productId} updated to: ${stockLevel.value}`);
}

function handleWidgetClick() {
  console.log(`ProductStockWidget for ${props.productId} clicked.`);
  // Maybe open a stock history blade or refresh stock
  fetchStock();
}

onMounted(() => {
  fetchStock(); // Initial stock fetch
});

// Expose a function to be called via updateActiveWidget
defineExpose({
  refreshStock: fetchStock
});
</script>
```

## Step 2: Registering the Widget for a Specific Blade

Widgets are registered using the `useWidgets` composable, typically within the `setup` function of the component that defines or manages the blade.

```typescript
// In your blade component (e.g., ProductDetailsBlade.vue)
import { useWidgets, type IWidget } from '@vc-shell/framework';
import { onMounted, onUnmounted, markRaw, ref, computed } from 'vue';
import ProductStockWidget from './ProductStockWidget.vue'; // Path to your widget
import { BladeInstance } from '@vc-shell/framework';

const currentBlade = inject<IBladeInstance>(BladeInstance); // Inject the current blade instance
const currentProductId = ref('PROD123'); // Product ID for context

const { registerWidget, unregisterWidget } = useWidgets();

onMounted(() => {
  const stockWidgetConfig: IWidget = {
    id: `stock-widget-${currentProductId.value}`, // Unique ID for this widget instance
    component: markRaw(ProductStockWidget),      // Your widget component
    props: {
      productId: currentProductId.value,
      initialStock: 10, // Example initial prop
    },
    isVisible: computed(() => currentProductId.value !== 'PROD_ARCHIVED'), // Conditional visibility
    updateFunctionName: 'refreshStock' // Matches the function exposed by ProductStockWidget
  };
  
  registerWidget(stockWidgetConfig, currentBlade.value.id);
});

onUnmounted(() => {
  unregisterWidget(`stock-widget-${currentProductId.value}`, currentBlade.value.id);
});
```
**Key Points:**

- `id`: Must be unique for each widget instance within a blade.
- `component`: Use `markRaw()` for performance.
- `props`: Pass any necessary reactive or static data to your widget component.
- `bladeId`: Specifies which blade the widget belongs to.
- `updateFunctionName`: Allows the widget to be updated via `updateActiveWidget()`.


## Step 3: Updating Widget State or Props

**Updating Widget Props:**
Use `updateWidget` to change a widget's properties like `isVisible` or `props` after registration.

```typescript
const { updateWidget } = useWidgets();

function toggleWidgetVisibility(widgetId: string, isVisible: boolean) {
  updateWidget({
    id: widgetId,
    bladeId: currentBladeId.value, // Ensure this is the correct blade ID
    widget: { isVisible },
  });
}

// If currentProductId changes, the 'productId' prop of ProductStockWidget will update automatically
// because it was passed as `currentProductId.value` (a reactive ref) during registration.
// For props not initially bound to a reactive source, or to change other IWidget fields:
function updateWidgetDetails(widgetId: string, newProps: Partial<IWidget['props']>) {
   updateWidget({
    id: widgetId,
    bladeId: currentBladeId.value,
    widget: { props: newProps } // Can also update .title, .isVisible etc.
  });
}
```

**Triggering a Widget's Exposed Function:**
If a widget, like `ProductStockWidget`, exposes a function via `defineExpose` and its `updateFunctionName` was set during registration, you can trigger this function on the "active" widget. `VcWidget` often handles setting itself as active on click.

```typescript
const { updateActiveWidget, isActiveWidget, setActiveWidget } = useWidgets();

// Example: Force a stock refresh on the active widget
function refreshActiveWidgetStock() {
  // VcWidget typically calls setActiveWidget on click.
  // If not using VcWidget or needing programmatic activation, you might need to call setActiveWidget first.
  // e.g., if you have the widget's exposed instance:
  // setActiveWidget({ exposed: productStockWidgetInstance.exposed, widgetId: `stock-widget-${currentProductId.value}` });

  // Then call the exposed function (e.g., 'refreshStock')
  // This assumes `stock-widget-${currentProductId.value}` is currently the active widget.
  if (isActiveWidget(`stock-widget-${currentProductId.value}`)) {
    updateActiveWidget(); // This will attempt to call 'refreshStock' on the active widget
  } else {
    console.warn("Stock widget is not active. Cannot refresh.");
  }
}
```

## Step 5: Unregistering Blade Widgets

Always unregister widgets when the component that registered them (usually the blade itself) is unmounted.

```typescript
// (Already shown in Step 2)
import { onUnmounted } from 'vue';
// ...
onUnmounted(() => {
  unregisterWidget(`stock-widget-${currentProductId.value}`, currentBladeId.value);
  // To remove all widgets for the current blade:
  // clearBladeWidgets(currentBladeId.value);
});
```

## Global Pre-registration for Core Widgets

For widgets that are part of the core framework or foundational modules and need to be available very early, VC-Shell offers a global `registerWidget` function (distinct from the one returned by `useWidgets()`).

```typescript
// In a module's main setup file (e.g., my-module/index.ts)
import { registerWidget as globalRegisterWidget, type IWidget } from '@vc-shell/framework';
import { markRaw } from 'vue';
import MySystemStatusWidget from './internal/MySystemStatusWidget.vue';

const systemWidget: IWidget = {
  id: 'system-status-main',
  component: markRaw(MySystemStatusWidget),
  props: { updateInterval: 60000 },
};

// Register for a known blade ID, e.g., a main dashboard blade
globalRegisterWidget(systemWidget, 'app-dashboard-main');
```

## Best Practices

1.  **Unique IDs**: Ensure `IWidget.id` is unique for each widget instance on a blade.
2.  **`markRaw`**: Use `markRaw` for `IWidget.component` for better performance.
3.  **Cleanup**: Always use `unregisterWidget` or `clearBladeWidgets` in `onUnmounted`.
4.  **Reactivity**: Pass reactive data to widgets via their `props` for dynamic updates.
5.  **`VcWidget` Base**: Utilize `VcWidget` as the base for blade widgets for consistency.
6.  **`updateFunctionName`**: Define for widgets that need external refresh/update triggers.
7.  **Blade Context**: Manage `bladeId` carefully for correct widget association.

This guide equips you to build and manage dynamic, modular widgets within your VC-Shell application's blades, enhancing user experience and information display.

## Related Resources

-   [`useWidgets` API Reference](../composables/useWidgets.md)
-   [`VcWidget` Component Documentation](../ui-components/vc-widget.md)
-   [`VcBlade` Component Documentation](../ui-components/vc-blade.md)
