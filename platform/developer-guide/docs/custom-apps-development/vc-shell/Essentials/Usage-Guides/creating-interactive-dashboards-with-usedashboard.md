# How-To: Creating Interactive Dashboards with `useDashboard`

The `useDashboard` composable provides a powerful way to create customizable, interactive dashboard interfaces in VC-Shell applications. This guide demonstrates how to effectively register widgets, manage layouts, and implement permission-based visibility for comprehensive dashboard solutions.

## Prerequisites

- Understanding of Vue 3 Composition API, including `ref` and `computed`.
- Familiarity with the `useDashboard` composable (see [useDashboard API Reference](../composables/useDashboard.md)).
- Basic knowledge of Vue component lifecycle hooks (`onMounted`, `onUnmounted`).
- Understanding of VC-Shell's permission system and UI components.

## Core Concept

Dashboard widgets are interactive components that can be arranged in a grid layout. The `useDashboard` service manages:

- **Widget Registration**: Adding widgets to the dashboard with metadata
- **Layout Management**: Positioning widgets in a grid system
- **Permission Control**: Showing/hiding widgets based on user permissions
- **Dynamic Updates**: Real-time widget position and visibility changes

The dashboard uses a grid system where widgets are positioned using `x` (column) and `y` (row) coordinates, with `width` and `height` defining the space they occupy.

```typescript
import { useDashboard } from '@vc-shell/framework';

const dashboard = useDashboard();

// Register a widget
dashboard.registerWidget({
  id: 'sales-overview',
  name: 'Sales Overview',
  component: SalesWidget,
  size: { width: 2, height: 1 },
  position: { x: 0, y: 0 }
});
```

## Implementation Strategies

### 1. Basic Dashboard Setup

Start with a simple dashboard implementation in your main application:

```vue
<!-- Dashboard.vue -->
<template>
  <div class="dashboard-page">
    <h1 class="tw-text-2xl tw-font-bold tw-mb-6">Application Dashboard</h1>
    
    <DraggableDashboard 
      ref="dashboardRef"
      @layout-changed="handleLayoutChange" 
    />
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { DraggableDashboard, useDashboard } from '@vc-shell/framework';
import SalesWidget from './widgets/SalesWidget.vue';
import OrdersWidget from './widgets/OrdersWidget.vue';

const dashboardRef = ref(null);
const dashboard = useDashboard();

onMounted(() => {
  // Register basic widgets
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
});

function handleLayoutChange(layout) {
  console.log('Layout changed:', layout);
  // Optional: Save layout to server
}
</script>
```

### 2. Creating Dashboard Widget Components

Design widgets using the `DashboardWidgetCard` component for consistency:

```vue
<!-- SalesWidget.vue -->
<template>
  <DashboardWidgetCard
    header="Sales Overview"
    icon="material-trending_up"
    :loading="isLoading"
  >
    <template #actions>
      <VcButton 
        icon="material-refresh" 
        size="sm" 
        variant="text" 
        @click="refreshData"
      />
    </template>
    
    <template #content>
      <div class="tw-p-6">
        <div class="tw-text-3xl tw-font-bold">{{ salesTotal }}</div>
        <div class="tw-flex tw-items-center tw-mt-2">
          <VcIcon 
            :icon="trendIcon" 
            :class="trendClass" 
            size="sm" 
          />
          <span :class="trendClass">{{ trendPercentage }}%</span>
        </div>
        <div class="tw-mt-4">
          <SalesChart :data="chartData" />
        </div>
      </div>
    </template>
  </DashboardWidgetCard>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue';
import { DashboardWidgetCard, VcButton, VcIcon } from '@vc-shell/framework';
import SalesChart from './SalesChart.vue';

const isLoading = ref(false);
const salesTotal = ref('$15,892');
const trendPercentage = ref(12.5);

const trendIcon = computed(() => {
  return trendPercentage.value >= 0 
    ? 'material-trending_up' 
    : 'material-trending_down';
});

const trendClass = computed(() => {
  return trendPercentage.value >= 0 
    ? 'tw-text-[var(--success-500)]' 
    : 'tw-text-[var(--error-500)]';
});

const chartData = ref([42, 58, 65, 72, 81, 95, 102]);

async function refreshData() {
  isLoading.value = true;
  try {
    // Fetch updated data
    await new Promise(resolve => setTimeout(resolve, 1000));
    salesTotal.value = '$16,275';
    trendPercentage.value = 15.2;
    chartData.value = [45, 62, 70, 78, 85, 92, 110];
  } finally {
    isLoading.value = false;
  }
}
</script>
```

### 3. Permission-Based Widget Visibility

Control widget visibility based on user permissions:

```typescript
// usePermissionBasedDashboard.ts
import { useDashboard, usePermissions } from '@vc-shell/framework';
import { onMounted } from 'vue';

export function usePermissionBasedDashboard() {
  const dashboard = useDashboard();
  const { hasPermission } = usePermissions();

  function registerWidgetsWithPermissions() {
    // Basic widgets (available to all users)
    dashboard.registerWidget({
      id: 'sales',
      name: 'Sales Overview',
      component: SalesWidget,
      size: { width: 2, height: 1 },
      position: { x: 0, y: 0 }
    });
    
    // Admin-only widgets
    if (hasPermission('admin')) {
      dashboard.registerWidget({
        id: 'admin-panel',
        name: 'Admin Panel',
        component: AdminPanelWidget,
        size: { width: 2, height: 1 },
        position: { x: 0, y: 2 },
        permissions: ['admin']
      });
    }
    
    // Marketing widgets
    if (hasPermission('marketing')) {
      dashboard.registerWidget({
        id: 'campaigns',
        name: 'Marketing Campaigns',
        component: CampaignsWidget,
        size: { width: 1, height: 1 },
        position: { x: 2, y: 1 },
        permissions: ['marketing']
      });
    }
    
    // Multi-permission widgets
    if (hasPermission('admin') && hasPermission('reports')) {
      dashboard.registerWidget({
        id: 'advanced-reports',
        name: 'Advanced Reports',
        component: AdvancedReportsWidget,
        size: { width: 3, height: 2 },
        position: { x: 0, y: 3 },
        permissions: ['admin', 'reports']
      });
    }
  }

  return {
    registerWidgetsWithPermissions
  };
}
```

### 4. Dynamic Widget Registration

Register widgets dynamically based on application state or user data:

```typescript
// useDynamicDashboard.ts
import { useDashboard } from '@vc-shell/framework';
import { ref, watch } from 'vue';

export function useDynamicDashboard() {
  const dashboard = useDashboard();
  const userRole = ref('user');
  const availableModules = ref([]);

  // Watch for role changes and update widgets
  watch(userRole, (newRole) => {
    registerRoleBasedWidgets(newRole);
  });

  // Watch for module changes and add module-specific widgets
  watch(availableModules, (modules) => {
    registerModuleWidgets(modules);
  }, { deep: true });

  function registerRoleBasedWidgets(role: string) {
    // Clear existing role-specific widgets
    const existingWidgets = dashboard.getWidgets();
    const roleWidgetIds = existingWidgets
      .filter(w => w.id.startsWith(`${role}-`))
      .map(w => w.id);
    
    // Register new widgets based on role
    if (role === 'manager') {
      dashboard.registerWidget({
        id: 'manager-overview',
        name: 'Manager Overview',
        component: ManagerOverviewWidget,
        size: { width: 3, height: 1 },
        position: { x: 0, y: 0 }
      });
    } else if (role === 'analyst') {
      dashboard.registerWidget({
        id: 'analyst-tools',
        name: 'Analytics Tools',
        component: AnalystToolsWidget,
        size: { width: 2, height: 2 },
        position: { x: 0, y: 0 }
      });
    }
  }

  function registerModuleWidgets(modules: string[]) {
    modules.forEach((module, index) => {
      dashboard.registerWidget({
        id: `module-${module}`,
        name: `${module} Dashboard`,
        component: getModuleWidget(module),
        size: { width: 1, height: 1 },
        position: { x: index % 3, y: Math.floor(index / 3) + 1 }
      });
    });
  }

  return {
    userRole,
    availableModules,
    registerRoleBasedWidgets,
    registerModuleWidgets
  };
}
```

## Best Practices

1. **Widget Design Consistency**: Always use `DashboardWidgetCard` as the base component for widgets to ensure consistent styling and behavior.

2. **Grid System Understanding**: 
   - Use appropriate widget sizes (1x1 for small widgets, 2x1 for medium, 3x1 for wide)
   - Consider mobile responsiveness when designing widget layouts
   - Leave space for future widgets in your initial positioning

3. **Permission Management**: 
   - Register widgets conditionally based on user permissions
   - Use descriptive permission names that align with your application's role system
   - Consider graceful degradation when permissions change

4. **Widget Registration Timing**:
   - Register widgets early in the application lifecycle
   - Use `onMounted` for component-level registration
   - Consider module-level registration for better organization

5. **Error Handling**:
   - Implement error boundaries in widget components
   - Provide fallback content for failed widgets
   - Log widget registration and layout errors appropriately

## Related Resources

- [useDashboard API Reference](../composables/useDashboard.md)
- [DraggableDashboard Component](../shared/components/draggable-dashboard.md)
- [Dashboard Widget Card Component](../shared/components/dashboard-widget-card.md)
- [usePermissions Composable](../composables/usePermissions.md) 
