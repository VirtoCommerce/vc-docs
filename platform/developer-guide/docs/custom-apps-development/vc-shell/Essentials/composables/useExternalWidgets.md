# `useExternalWidgets` Composable

The `useExternalWidgets` composable provides a powerful API for automatically discovering, registering, and managing external widgets within **blades** in the VC-Shell framework. This composable enables loose coupling between modules by allowing external modules to register widgets that can automatically appear in compatible blades without direct dependencies.

## Overview

External widgets are a key component of VC-Shell's modular architecture. They allow:

- **Cross-module functionality**: Widgets from one module can appear in blades from another module
- **Loose coupling**: Modules don't need to know about each other directly
- **Declarative configuration**: Widgets declare their data requirements, blades provide what they can
- **Automatic discovery**: Compatible widgets are discovered and registered automatically
- **Dynamic prop resolution**: Widget props are automatically resolved from blade data

## API Reference

### Usage

```typescript
import { useExternalWidgets } from '@vc-shell/framework';

const externalWidgets = useExternalWidgets(options);
```

### Options

```typescript
interface UseExternalWidgetsOptions {
  bladeId: string;
  bladeData: Ref<Record<string, unknown>> | ComputedRef<Record<string, unknown>>;
  autoRegister?: boolean; // Default: true
  autoUpdateProps?: boolean; // Default: true
}
```

#### `bladeId`
- **Type**: `string`
- **Required**: Yes
- **Description**: Identifier for the blade. External widgets use this to target specific blade types.

**Example values**: `'product-details'`, `'order-details'`.

#### `bladeData`
- **Type**: `Ref<Record<string, unknown>>` | `ComputedRef<Record<string, unknown>>`
- **Required**: Yes
- **Description**: Reactive data object containing all information that external widgets might need. This data is used to resolve widget props based on their configuration.

#### `autoRegister`
- **Type**: `boolean`
- **Default**: `true`
- **Description**: Whether to automatically register external widgets when the composable is mounted.

#### `autoUpdateProps`
- **Type**: `boolean`
- **Default**: `true`
- **Description**: Whether to automatically update widget props when blade data changes.

### Return Value

```typescript
interface UseExternalWidgetsReturn {
  registerExternalWidgets: () => void;
  updateWidgetProps: () => void;
  unregisterExternalWidgets: () => void;
  registeredExternalWidgetIds: ComputedRef<string[]>;
}
```

#### `registerExternalWidgets`
- **Type**: `() => void`
- **Description**: Manually register external widgets for the current blade. Called automatically if `autoRegister` is `true`.

#### `updateWidgetProps`
- **Type**: `() => void`
- **Description**: Manually update props for all registered external widgets. Called automatically when `bladeData` changes if `autoUpdateProps` is `true`.

#### `unregisterExternalWidgets`
- **Type**: `() => void`
- **Description**: Remove all external widgets registered by this composable. Called automatically when the composable is unmounted.

#### `registeredExternalWidgetIds`
- **Type**: `ComputedRef<string[]>`
- **Description**: Reactive array of widget IDs that have been registered by this composable.

## Basic Usage

### Simple Blade Setup

```vue
<script setup lang="ts">
import { useExternalWidgets } from '@vc-shell/framework';
import { computed } from 'vue';

// Your blade data
const product = ref(null);
const isModified = ref(false);
const currentLocale = ref('en');

// Define blade data for external widgets
const bladeData = computed(() => ({
  item: product.value,
  isModified: isModified.value,
  currentLocale: currentLocale.value,
  readonly: false,
}));

// Register external widgets
useExternalWidgets({
  bladeId: 'product-details',
  bladeData,
});
</script>
```

### Advanced Blade Setup

```vue
<script setup lang="ts">
import { useExternalWidgets, usePermissions } from '@vc-shell/framework';
import { computed, onMounted } from 'vue';

const { hasAccess } = usePermissions();
const product = ref(null);
const isModified = ref(false);
const currentLocale = ref('en');
const loading = ref(false);

// Comprehensive blade data
const bladeData = computed(() => ({
  // Core data
  item: product.value,
  isModified: isModified.value,
  loading: loading.value,

  // Localization
  currentLocale: currentLocale.value,

  // Permissions
  readonly: !hasAccess('products:update'),
  hasEditPermissions: hasAccess('products:update'),
  hasDeletePermissions: hasAccess('products:delete'),
  hasApprovePermissions: hasAccess('products:approve'),

  // Product-specific data
  productType: product.value?.type,
  category: product.value?.category,
  status: product.value?.status,

  // UI state
  expanded: true,
  activeTab: activeTab.value,
}));

// Register external widgets with custom options
const externalWidgets = useExternalWidgets({
  bladeId: 'product-details',
  bladeData,
  autoRegister: true,
  autoUpdateProps: true,
});

// Manual control example
function refreshExternalWidgets() {
  externalWidgets.updateWidgetProps();
}

onMounted(() => {
  // Widgets are automatically registered due to autoRegister: true
  console.log('Registered widget IDs:', externalWidgets.registeredExternalWidgetIds.value);
});
</script>
```

## Manual Control

For scenarios where you need more control over widget lifecycle:

```vue
<script setup lang="ts">
import { useExternalWidgets } from '@vc-shell/framework';
import { onMounted, onUnmounted } from 'vue';

const bladeData = computed(() => ({
  item: product.value,
  isModified: isModified.value,
}));

// Disable automatic behavior
const externalWidgets = useExternalWidgets({
  bladeId: 'product-details',
  bladeData,
  autoRegister: false,
  autoUpdateProps: false,
});

onMounted(async () => {
  // Load product data first
  await loadProduct();

  // Then register widgets
  externalWidgets.registerExternalWidgets();
});

// Manual prop updates
watch(product, () => {
  externalWidgets.updateWidgetProps();
});

onUnmounted(() => {
  // Clean up widgets
  externalWidgets.unregisterExternalWidgets();
});
</script>
```

## Blade Data Best Practices

### Comprehensive Data Provision

Provide comprehensive data to maximize widget compatibility:

```typescript
const bladeData = computed(() => ({
  // Core entity
  item: entity.value,

  // State
  isModified: isModified.value,
  loading: loading.value,
  readonly: !canEdit.value,

  // User context
  currentLocale: currentLocale.value,
  currentUser: currentUser.value,

  // Permissions
  hasEditPermissions: hasAccess('entity:update'),
  hasDeletePermissions: hasAccess('entity:delete'),
  hasViewPermissions: hasAccess('entity:view'),

  // Entity-specific data
  entityType: entity.value?.type,
  entityStatus: entity.value?.status,
  entityId: entity.value?.id,

  // UI state
  expanded: isExpanded.value,
  activeSection: activeSection.value,

  // Methods (if needed by widgets)
  refresh: () => loadEntity(),
  save: () => saveEntity(),
}));
```

### Performance Considerations

Use computed properties to avoid unnecessary re-computations:

```typescript
// Good: Efficient computed property
const bladeData = computed(() => ({
  item: product.value,
  isModified: isModified.value,
  permissions: {
    canEdit: hasAccess('products:update'),
    canDelete: hasAccess('products:delete'),
  },
}));

// Avoid: Creating new objects in templates
// This will cause widgets to re-render on every template update
const bladeData = ref({
  item: product.value,
  permissions: { canEdit: hasAccess('products:update') }, // Recreated each time
});
```

## Error Handling

The composable includes built-in error handling:

```typescript
// Errors are logged to console automatically
const externalWidgets = useExternalWidgets({
  bladeId: 'product-details',
  bladeData,
});

// Widget registration errors are caught and logged
// Prop resolution errors are caught and logged
// Individual widget failures don't break the entire system
```

## Advanced Patterns

### Conditional Widget Registration

```typescript
const bladeData = computed(() => {
  const data: Record<string, unknown> = {
    item: product.value,
    isModified: isModified.value,
  };

  // Conditionally add data based on product type
  if (product.value?.type === 'digital') {
    data.downloadInfo = downloadInfo.value;
    data.licenseInfo = licenseInfo.value;
  }

  if (product.value?.type === 'physical') {
    data.shippingInfo = shippingInfo.value;
    data.inventoryInfo = inventoryInfo.value;
  }

  return data;
});
```

### Multi-Blade Support

```typescript
// Blade can support multiple types for different widget sets
const commonData = computed(() => ({
  item: entity.value,
  isModified: isModified.value,
  currentLocale: currentLocale.value,
}));

// Register for main blade type
useExternalWidgets({
  bladeId: 'product-details',
  bladeData: commonData,
});

// Also register for generic item type (for cross-cutting widgets)
useExternalWidgets({
  bladeId: 'item-details',
  bladeData: commonData,
});
```

## Related Resources

- [useWidgets Composable](./useWidgets.md): Core widget management API
- [registerExternalWidget Function](./useWidgets.md#external-widget-registration-system): Registering external widgets
- [Creating External Widgets Guide](../Usage-Guides/creating-and-registering-widgets-with-usewidgets.md#approach-2-external-widget-system): Step-by-step external widget creation
- [Modularity Guide](/platform/developer-guide/latest/custom-apps-development/vc-shell/Extensibility/modularity.md#5-external-blade-widgets): Module architecture and external widgets
