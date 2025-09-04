# How-To: Creating and Registering Blade Widgets with `useWidgets`

This guide provides a practical walkthrough on how to create custom widget components and register them for display within specific **blades** in your VC-Shell application using the `useWidgets` composable and the external widget system.

## Prerequisites

-   Understanding of Vue 3 Composition API (`ref`, `computed`, `defineExpose`).
-   Familiarity with the [`useWidgets` API Reference](../composables/useWidgets.md).
-   Knowledge of the `VcWidget` atomic component, recommended as a base for blade widgets.
-   Basic understanding of VC-Shell's blade system.

## Core Concepts

-   **Blade Widgets**: Self-contained Vue components designed to offer supplementary information or interactive elements within a VC-Shell blade.
-   **`useWidgets` Composable**: The primary API for managing the registration, state, and lifecycle of these blade widgets.
-   **`VcWidget` Component**: A standardized UI component provided by VC-Shell, ideal for building custom blade widgets with a consistent look and feel.
-   **External Widgets**: Widgets registered by external modules that can automatically appear in compatible blades without tight coupling.

## Widget Registration Approaches

VC-Shell provides two main approaches for widget registration:

1. **Direct Registration**: For widgets specific to a particular blade
2. **External Widget System**: For widgets that should be available across multiple blade types from different modules

## Approach 1: Direct Widget Registration

### Step 1: Creating Your Blade Widget Component

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
import { ref, computed, defineProps, defineEmits, defineExpose, onMounted, watch } from 'vue';

const props = defineProps<{
  productId: string;
  initialStock?: number;
  modelValue?: any; // For two-way binding
}>();

const emit = defineEmits<{
  'update:modelValue': [value: any];
  'stock-updated': [stock: number];
}>();

const stockLevel = ref(props.initialStock || 0);
const widgetTitle = computed(() => `Stock: ${props.productId}`);
const stockIcon = computed(() => stockLevel.value > 0 ? 'material-inventory_2' : 'material-production_quantity_limits');

// Watch for stock changes and emit custom events
watch(stockLevel, (newStock) => {
  emit('stock-updated', newStock);

  // Update model value with stock information
  emit('update:modelValue', {
    productId: props.productId,
    stock: newStock,
    timestamp: Date.now()
  });
});

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

### Step 2: Registering the Widget for a Specific Blade

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
    events: {
      "update:modelValue": (val: unknown) => {
        // Handle model value updates from the widget
        console.log("Widget model updated:", val);
      },
      "stock-updated": (newStock: number) => {
        // Handle custom events emitted by the widget
        console.log("Stock updated to:", newStock);
      }
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
- `events`: Define event handlers for events emitted by the widget (e.g., `update:modelValue`, custom events).
- `bladeId`: Specifies which blade the widget belongs to.
- `updateFunctionName`: Allows the widget to be updated via `updateActiveWidget()`.

## Approach 2: External Widget System

The external widget system allows modules to register widgets that can automatically appear in compatible blades from other modules without tight coupling.

### Step 1: Creating an External Widget Component

External widgets are created similarly to direct widgets, but they should be more generic and configurable:

```vue
<!-- MyExternalProductWidget.vue -->
<template>
  <VcWidget
    title="Product Status"
    :value="displayValue"
    :icon="widgetIcon"
    @click="handleClick"
  />
</template>

<script setup lang="ts">
import { VcWidget } from '@vc-shell/framework';
import { computed } from 'vue';

interface Props {
  item?: any;           // Generic item from blade
  isModified?: boolean; // Modification state
  currentLocale?: string; // Current language
  readonly?: boolean;   // Read-only state
}

const props = defineProps<Props>();

const displayValue = computed(() => {
  if (!props.item) return 'No data';
  return props.isModified ? 'Modified' : 'Saved';
});

const widgetIcon = computed(() =>
  props.isModified
    ? 'material-edit'
    : 'material-check'
);

function handleClick() {
  if (!props.readonly && props.item) {
    console.log('External widget clicked for item:', props.item.id);
  }
}

// Expose refresh function
defineExpose({
  refresh: () => {
    console.log('External widget refreshed');
  }
});
</script>
```

### Step 2: Registering the External Widget

Register the external widget in your module's `index.ts` file:

```typescript
// In your module's index.ts
import { registerExternalWidget } from '@vc-shell/framework';
import { markRaw } from 'vue';
import MyExternalProductWidget from './components/widgets/MyExternalProductWidget.vue';

// Register external widget during module initialization
registerExternalWidget({
  id: 'my-module-product-widget',
  component: markRaw(MyExternalProductWidget),
  targetBlades: ['product-details'], // Specify compatible blade types
  config: {
    requiredData: ['item'], // Data that must be provided by the blade
    optionalData: ['isModified', 'currentLocale', 'readonly'], // Optional data
    fieldMapping: {
      // If blade uses different field names, map them here
      // 'widgetProp': 'bladeDataKey'
    }
  },
  isVisible: (blade) => {
    // Dynamic visibility based on blade param
    return !!blade?.param;
  },
  updateFunctionName: 'refresh'
});
```

### Step 3: Using External Widgets in Blades

Blades can automatically discover and register external widgets using the `useExternalWidgets` composable:

```typescript
// In your blade component (e.g., ProductDetailsBlade.vue)
import { useExternalWidgets } from '@vc-shell/framework';
import { computed } from 'vue';

// Define the data that external widgets might need
const bladeData = computed(() => ({
  item: product.value,
  isModified: isModified.value,
  currentLocale: currentLocale.value,
  readonly: isReadonly.value,
  // Add any other data that widgets might need
  productType: product.value?.type,
  hasPermissions: hasEditPermissions.value,
}));

// Register external widgets for this blade
const externalWidgets = useExternalWidgets({
  bladeId: 'product-details',
  bladeData,
  autoRegister: true,      // Automatically register widgets on mount
  autoUpdateProps: true,   // Automatically update widget props when blade data changes
});

// Optional: Manual control
onMounted(() => {
  // Manual registration if autoRegister is false
  // externalWidgets.registerExternalWidgets();
});

onUnmounted(() => {
  // Clean up external widgets
  externalWidgets.unregisterExternalWidgets();
});
```

### Step 4: Advanced External Widget Configuration

For more complex scenarios, you can use custom prop resolvers:

```typescript
registerExternalWidget({
  id: 'advanced-product-widget',
  component: markRaw(AdvancedProductWidget),
  targetBlades: ['product-details'],
  config: {
    // Custom function to resolve props from blade data
    propsResolver: (bladeData: Record<string, unknown>) => {
      const item = bladeData.item as any;

      return {
        productId: item?.id,
        productName: item?.name,
        status: bladeData.isModified ? 'modified' : 'saved',
        canEdit: !bladeData.readonly && bladeData.hasPermissions,
        locale: bladeData.currentLocale || 'en',
        // Transform or compute additional props
        displayPrice: item?.price ? `$${item.price}` : 'N/A',
      };
    }
  },
  isVisible: (blade) => blade?.expanded !== false,
});
```

## Step 3: Handling Widget Events

Widgets can emit events that can be handled by their parent components. This is particularly useful for two-way data binding and custom widget interactions.

**Setting up Event Handlers:**

When registering a widget, you can define event handlers in the `events` property:

```typescript
// Example: Widget with blade context binding
const bladeContext = ref<DetailsBladeContext>({
  scope: { canEdit: true },
  data: null
});

const contextAwareWidgetConfig: IWidget = {
  id: 'context-aware-widget',
  component: markRaw(MyContextWidget),
  props: {
    modelValue: bladeContext, // Pass reactive context
  },
  events: {
    // Handle two-way binding with modelValue
    "update:modelValue": (val: unknown) => {
      bladeContext.value = val as DetailsBladeContext;
      console.log("Blade context updated:", val);
    },
    // Handle custom widget events
    "widget-action": (actionType: string, payload: any) => {
      console.log(`Widget action: ${actionType}`, payload);
      // Handle widget-specific actions
    }
  },
  isVisible: computed(() => bladeContext.value.scope?.canEdit),
  updateFunctionName: "refresh"
};
```

**Real-world Example: Product Details Widget with Context Binding**

```typescript
// In ProductDetailsBlade.vue
const productContext = ref({
  productId: 'PROD123',
  isEditable: true,
  lastModified: null
});

const productWidgetConfig: IWidget = {
  id: 'product-details-widget',
  component: markRaw(ProductDetailsWidget),
  props: {
    modelValue: productContext,
  },
  events: {
    "update:modelValue": (val: unknown) => {
      productContext.value = val as typeof productContext.value;
      // Auto-save changes or trigger validation
      saveProductContext(productContext.value);
    },
    "product-saved": (productData: any) => {
      // Handle successful product save
      showSuccessNotification('Product saved successfully');
    },
    "validation-error": (errors: string[]) => {
      // Handle validation errors
      showErrorNotification(errors.join(', '));
    }
  },
  isVisible: computed(() => productContext.value.isEditable)
};
```

## Step 4: Updating Widget State or Props

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

For external widgets using `useExternalWidgets`, cleanup is handled automatically:

```typescript
// External widgets are automatically cleaned up when the composable is unmounted
// But you can also manually clean them up:
const externalWidgets = useExternalWidgets({
  bladeId: 'product-details',
  bladeData,
});

onUnmounted(() => {
  externalWidgets.unregisterExternalWidgets();
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
5.  **Event Handling**: Use the `events` property to handle widget events, especially for two-way data binding with `update:modelValue`.
6.  **`VcWidget` Base**: Utilize `VcWidget` as the base for blade widgets for consistency.
7.  **`updateFunctionName`**: Define for widgets that need external refresh/update triggers.
8.  **Blade Context**: Manage `bladeId` carefully for correct widget association.
9.  **External Widget Design**:
     - Design external widgets to be generic and configurable
     - Clearly define required vs optional data
     - Use appropriate prop names that make sense across different blade types
     - Handle missing data gracefully
10. **Error Handling**: Implement proper error handling in custom `propsResolver` functions.
11. **Performance**: Use `autoUpdateProps: false` in `useExternalWidgets` if you need manual control over prop updates.
12. **Documentation**: Document the data requirements and behavior of your external widgets.

## Comparison: Direct vs External Widgets

| Aspect | Direct Registration | External Widget System |
|--------|-------------------|----------------------|
| **Coupling** | Tight - widget specific to blade | Loose - widget works across blades |
| **Reusability** | Limited to specific blade | High - works across compatible blades |
| **Configuration** | Manual prop passing | Declarative data requirements |
| **Discovery** | Manual registration in each blade | Automatic discovery and registration |
| **Complexity** | Simple and direct | More complex but more flexible |
| **Use Case** | Blade-specific functionality | Cross-cutting concerns, analytics, status |

This guide equips you to build and manage dynamic, modular widgets within your VC-Shell application's blades, enhancing user experience and information display while maintaining clean architecture.

## Related Resources

-   [`useWidgets` API Reference](../composables/useWidgets.md)
-   [`useExternalWidgets` API Reference](../composables/useExternalWidgets.md)
-   [`VcWidget` Component Documentation](../ui-components/vc-widget.md)
-   [`VcBlade` Component Documentation](../ui-components/vc-blade.md)
-   [Modularity in VC-Shell Applications](../../Extensibility/modularity.md)
