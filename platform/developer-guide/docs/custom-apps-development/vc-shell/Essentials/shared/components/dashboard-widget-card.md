# Dashboard Widget Card Component

The `DashboardWidgetCard` component is a reusable UI element designed for displaying dashboard widgets in VC-Shell applications. It provides a consistent layout structure with a header, action buttons, and content area for widget data visualization.

The dashboard widget card serves as the container for individual widget content within draggable dashboard layouts. It provides a consistent styling and structure for dashboard widgets while allowing for customizable content through slots.

## Component structure

```vue
<DashboardWidgetCard 
  header="Sales Overview" 
  icon="material-trending_up"
  :loading="isLoading"
>
  <!-- Widget content goes here -->
</DashboardWidgetCard>
```

## API reference

### Props

| Prop      | Type      | Default     | Description                                      |
| :-------- | :-------- | :---------- | :----------------------------------------------- |
| `header`  | `string`  | `undefined` | The header text to display in the widget.        |
| `icon`    | `string`  | `undefined` | Optional icon name (Material Design) for the header. |
| `loading` | `boolean` | `false`     | If true, displays a loading indicator over the content area. |

### Slots

| Slot      | Description                                                                 |
| :-------- | :-------------------------------------------------------------------------- |
| `header`  | Allows providing custom markup for the entire header section, replacing the default structure (icon + title text). |
| `actions` | For placing interactive elements like buttons or menus in the top-right corner of the header. | 
| `content` | The main area for the widget's body content.                                |

## Styling

The component uses custom CSS variables for theming:

```scss
:root {
  --dashboard-widget-card-header-color: var(--additional-50);
  --dashboard-widget-card-header-text-color: var(--neutrals-950);
  --dashboard-widget-card-icon-color: var(--neutrals-950);
  --dashboard-widget-card-header-border-color: var(--neutrals-200);
}
```

## Basic usage example

```vue
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
      <VcButton 
        icon="material-more_vert" 
        size="sm" 
        variant="text" 
        @click="showMenu"
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

<script setup lang="ts">
import { ref, computed } from 'vue';
import { DashboardWidgetCard } from '@vc-shell/framework';
import { VcButton, VcIcon } from '@vc-shell/framework';
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

function showMenu() {
  // Show widget options menu
  console.log('Show widget menu');
}
</script>
```

## Create custom widget with DashboardWidgetCard

When implementing custom widgets for a dashboard, the `DashboardWidgetCard` provides the outer container while you supply the specific visualization or content:

```vue
<!-- SalesWidget.vue -->
<template>
  <DashboardWidgetCard 
    header="Sales Data" 
    icon="material-analytics"
    :loading="loading"
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
        <!-- Your specific sales widget content here -->
      </div>
    </template>
  </DashboardWidgetCard>
</template>
```

## Usage with draggable dashboard

The `DashboardWidgetCard` component is designed to work with the `DraggableDashboard` component, but requires an additional step using `useDashboard` to register the widget:

```typescript
import { useDashboard } from '@vc-shell/framework';
import SalesWidget from './SalesWidget.vue';

export function registerDashboardWidgets() {
  const dashboard = useDashboard();
  
  dashboard.registerWidget({
    id: 'sales-overview',
    name: 'Sales Overview',
    component: SalesWidget,
    size: { width: 2, height: 1 },
    position: { x: 0, y: 0 }
  });
}
```
