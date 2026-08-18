# Draggable Dashboard Component

The `DraggableDashboard` component provides a flexible, interactive grid layout for displaying dashboard widgets in VC-Shell applications. It features a drag-and-drop interface for widget arrangement, automatic layout calculations, collision detection, and layout persistence.

The Draggable Dashboard creates a responsive grid system where widgets can be positioned and rearranged by users through intuitive drag-and-drop interactions. It automatically handles widget positioning, collision detection, and layout persistence, making it easy to create personalized dashboard experiences.

## Component structure

```vue
<template>
  <DraggableDashboard ref="dashboardRef" />
</template>

<script setup>
import { ref } from 'vue';
import { DraggableDashboard } from '@vc-shell/framework';

const dashboardRef = ref(null);
</script>
```

## Features

- **Drag and drop widget arrangement**: Intuitive widget positioning through drag-and-drop
- **Automatic layout calculation**: Smart widget arrangement with collision detection
- **Responsive grid system**: Adapts to different screen sizes
- **Layout persistence**: Automatically saves widget positions to localStorage
- **Widget displacement**: Automatically repositions widgets during dragging to prevent overlaps
- **Animation and transitions**: Smooth visual feedback during interaction
- **Permission-based widgets**: Integrates with VC-Shell permission system

## API reference

### Props

The `DraggableDashboard` component does not accept any direct props. Its behavior and content (the widgets) are managed through the `useDashboard` composable. You register widgets, and the `DraggableDashboard` component consumes them from this shared service.

### Events

| Event | Payload | Description |
|-------|---------|-------------|
| `layout-changed` | `Map<string, DashboardWidgetPosition>` | Emitted when the dashboard layout changes |

### Public methods

The component exposes the following methods when accessed via a template ref:

| Method | Parameters | Return | Description |
|--------|------------|--------|-------------|
| `rearrangeWidgets()` | None | void | Reorganizes widgets into rows in an optimal arrangement |
| `recalculateLayout()` | None | void | Manually triggers a recalculation of the layout |
| `saveLayout()` | None | void | Manually saves the current layout to localStorage |
| `useBuiltInPositions()` | None | boolean | Resets widget positions to their built-in positions, returns true if successful |

## Basic usage example

```vue
<template>
  <div class="dashboard-page">
    <h1>Application Dashboard</h1>
    
    <!-- Dashboard controls -->
    <div class="dashboard-controls tw-mb-6">
      <VcButton @click="dashboardRef.rearrangeWidgets()">Rearrange</VcButton>
      <VcButton @click="dashboardRef.saveLayout()">Save Layout</VcButton>
      <VcButton @click="dashboardRef.useBuiltInPositions()">Reset</VcButton>
    </div>
    
    <!-- Dashboard Component -->
    <DraggableDashboard 
      ref="dashboardRef"
      @layout-changed="handleLayoutChange" 
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { DraggableDashboard, useDashboard } from '@vc-shell/framework';
import { VcButton } from '@vc-shell/framework';
import SalesWidget from './widgets/SalesWidget.vue';
import OrdersWidget from './widgets/OrdersWidget.vue';
import InventoryWidget from './widgets/InventoryWidget.vue';

// Create a reference to the dashboard component
const dashboardRef = ref(null);

// Register dashboard widgets
onMounted(() => {
  const dashboard = useDashboard();
  
  // Register widgets with the dashboard service
  dashboard.registerWidget({
    id: 'sales',
    name: 'Sales Overview',
    component: SalesWidget,
    size: { width: 2, height: 1 },
    position: { x: 0, y: 0 }
  });
  
  dashboard.registerWidget({
    id: 'orders',
    name: 'Recent Orders',
    component: OrdersWidget,
    size: { width: 1, height: 2 },
    position: { x: 2, y: 0 }
  });
  
  dashboard.registerWidget({
    id: 'inventory',
    name: 'Inventory Status',
    component: InventoryWidget,
    size: { width: 3, height: 1 },
    position: { x: 0, y: 1 }
  });
});

// Handle layout changes
function handleLayoutChange(layout) {
  console.log('Dashboard layout changed:', layout);
}
</script>
```

## Widget registration

Widgets must be registered with the Dashboard Service (`useDashboard`) to appear in the `DraggableDashboard`. This is typically done during the `onMounted` lifecycle hook of the component that sets up the dashboard (e.g., a specific dashboard page) or within a dedicated module initialization file.

```typescript
import { onMounted } from 'vue';
import { useDashboard } from '@vc-shell/framework';
import SalesWidget from './SalesWidget.vue'; // Your custom widget component

// Typically in the setup function of your dashboard page component
onMounted(() => {
  const dashboard = useDashboard();
  
  dashboard.registerWidget({
    id: 'sales-widget',             // Unique identifier for the widget
    name: 'Sales Overview',         // Display name (often shown in widget selection UI)
    component: SalesWidget,         // The Vue component for the widget's content
    size: { width: 2, height: 1 },  // Size in grid units (e.g., 2 columns wide, 1 row high)
    position: { x: 0, y: 0 },       // Optional: Initial position on the grid (x, y coordinates)
    permissions: ['view-sales'],    // Optional: Array of permission strings required to see this widget
    props: { period: 'monthly' }    // Optional: Props to pass down to the SalesWidget component
  });
  
  // Register other widgets...
});
```
For more details on creating widget components, refer to the `DashboardWidgetCard` documentation and the How-To guide on creating interactive dashboards.

## Create custom dashboard widgets

When creating widgets for use with the `DraggableDashboard` component, it's recommended to use the `DashboardWidgetCard` component as a container:

```vue
<!-- SalesWidget.vue -->
<template>
  <DashboardWidgetCard
    header="Sales Overview"
    icon="material-trending_up"
    :loading="loading"
  >
    <template #actions>
      <VcButton icon="material-refresh" size="sm" variant="text" @click="refreshData" />
    </template>
    
    <template #content>
      <div class="tw-p-6">
        <!-- Widget specific content -->
        <div class="tw-text-3xl tw-font-bold">{{ totalSales }}</div>
        <div class="tw-mt-4">
          <SalesChart :data="chartData" />
        </div>
      </div>
    </template>
  </DashboardWidgetCard>
</template>

<script setup>
import { ref } from 'vue';
import { DashboardWidgetCard, VcButton } from '@vc-shell/framework';
import SalesChart from './SalesChart.vue';

const loading = ref(false);
const totalSales = ref('$24,500');
const chartData = ref([25, 40, 35, 50, 45, 60, 70]);

async function refreshData() {
  loading.value = true;
  try {
    // Fetch data
    await new Promise(resolve => setTimeout(resolve, 1000));
    totalSales.value = '$26,300';
    chartData.value = [30, 45, 40, 55, 50, 65, 75];
  } finally {
    loading.value = false;
  }
}
</script>
```

## Grid system

The draggable dashboard uses a grid system with the following properties:

- Default grid of 12 columns (configurable)
- Each widget specifies its width and height in grid units
- Widget positions are specified as `{ x, y }` coordinates on the grid
- Widgets cannot overlap; the system automatically handles displacement during drag operations

## Layout persistence

The draggable dashboard automatically saves widget positions to localStorage. This behavior can be customized by:

* Using the `saveLayout()` method to manually trigger saves
* Listening to the `layout-changed` event to implement custom persistence

## Styling

The component uses CSS variables for theming:

```scss
:root {
  --dashboard-background: var(--additional-50);
  --dashboard-grid-line: var(--neutrals-200);
  --dashboard-grid-line-active: var(--neutrals-300);
  --dashboard-grid-border: var(--neutrals-300);
  --dashboard-preview-bg: var(--primary-100);
  --dashboard-preview-border: var(--primary-500);
  --dashboard-valid-bg: var(--secondary-100);
  --dashboard-valid-border: var(--secondary-500);
  --dashboard-cell-height: 80px;
  --dashboard-cell-gap-vertical: 24px;
  --dashboard-cell-gap-horizontal: 18px;
  --dashboard-widget-gap: 20px;
  --dashboard-animation-duration: 200ms;
  --dashboard-animation-timing: cubic-bezier(0.4, 0, 0.2, 1);
  --dashboard-transition-duration: 0.35s;
  --dashboard-transition-timing: cubic-bezier(0.25, 0.1, 0.25, 1);
  --dashboard-drag-scale: 1.02;
  --dashboard-gap: 20px;
}
```
