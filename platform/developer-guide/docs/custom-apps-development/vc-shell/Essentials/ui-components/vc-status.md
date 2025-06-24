# VcStatus Component

The `VcStatus` component is an atom used throughout the VC-Shell framework for displaying status indicators with different visual styles. It's used to represent the state of items or processes in the application.

## Storybook

[VcStatus Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vcstatus--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vcstatus--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcStatus variant="success">Completed</VcStatus>
</template>

<script lang="ts" setup>
import { VcStatus } from '@vc-shell/framework';
</script>
```

## Props

| Prop       | Type                                                                           | Default  | Description                                                        |
| ---------- | ------------------------------------------------------------------------------ | -------- | ------------------------------------------------------------------ |
| `variant`  | `'info' \| 'warning' \| 'danger' \| 'success' \| 'light-danger' \| 'info-dark' \| 'primary'` | `'info'` | Visual style of the status indicator                               |
| `outline`  | `boolean`                                                                      | `false`  | **DEPRECATED**: Whether to show only the outline                   |
| `extend`   | `boolean`                                                                      | `false`  | Whether to use an extended layout with more padding & square corners |
| `dot`      | `boolean`                                                                      | `false`  | Whether to display only a colored dot without text                 |

## Slots

| Slot       | Description                                                |
| ---------- | ---------------------------------------------------------- |
| `default`  | Content of the status indicator (text or complex content)  |

## CSS Variables

The status component uses CSS variables for theming, which can be customized:

```css
:root {
  --status-padding: 4px 14px;                   /* Default padding for status component */
  --status-padding-extended: 8px;               /* Padding for extended status variant */
  --status-dot-size: 10px;                      /* Size of dot-only status indicator */
  --status-text-color: var(--neutrals-700);     /* Default text color for status content */

  --status-border-radius: 20px;                 /* Border radius for standard status */
  --status-border-radius-extended: 4px;         /* Border radius for extended status */
  --status-border-width: 1px;                   /* Width of the border around the status component */
  
  --status-border-color: var(--neutrals-500);   /* Default border color */
  --status-bg-color: var(--additional-50);      /* Default background color */

  /* Info variant colors */
  --status-info-color: var(--additional-950);   /* Text color for info variant */
  --status-info-main-color: var(--info-500);    /* Dot color for info variant */
  --status-info-bg-color: var(--info-50);       /* Background color for info variant */

  /* Warning variant colors */
  --status-warning-color: var(--additional-950); /* Text color for warning variant */
  --status-warning-main-color: var(--warning-500); /* Dot color for warning variant */
  --status-warning-bg-color: var(--warning-50); /* Background color for warning variant */

  /* Danger variant colors */
  --status-danger-color: var(--additional-950); /* Text color for danger variant */
  --status-danger-main-color: var(--danger-500); /* Dot color for danger variant */
  --status-danger-bg-color: var(--danger-50);   /* Background color for danger variant */

  /* Success variant colors */
  --status-success-color: var(--additional-950); /* Text color for success variant */
  --status-success-main-color: var(--success-500); /* Dot color for success variant */
  --status-success-bg-color: var(--success-50); /* Background color for success variant */

  /* Light danger variant colors */
  --status-light-danger-color: var(--additional-950); /* Text color for light danger variant */
  --status-light-danger-main-color: var(--danger-300); /* Dot color for light danger variant */
  --status-light-danger-bg-color: var(--danger-50); /* Background color for light danger variant */

  /* Info dark variant colors */
  --status-info-dark-color: var(--additional-50); /* Text color for info dark variant */
  --status-info-dark-main-color: var(--info-600); /* Dot color for info dark variant */
  --status-info-dark-bg-color: var(--info-600);  /* Background color for info dark variant */

  /* Primary variant colors */
  --status-primary-color: var(--additional-950); /* Text color for primary variant */
  --status-primary-main-color: var(--primary-500); /* Dot color for primary variant */
  --status-primary-bg-color: var(--primary-50); /* Background color for primary variant */
}
```

## Examples

### Basic Status

```vue
<template>
  <VcStatus>Status text</VcStatus>
</template>

<script lang="ts" setup>
import { VcStatus } from '@vc-shell/framework';
</script>
```

### Status Variants

```vue
<template>
  <div class="tw-space-y-2">
    <VcStatus variant="info">Information</VcStatus>
    <VcStatus variant="success">Success</VcStatus>
    <VcStatus variant="warning">Warning</VcStatus>
    <VcStatus variant="danger">Error</VcStatus>
    <VcStatus variant="primary">Primary</VcStatus>
    <VcStatus variant="info-dark">Info Dark</VcStatus>
    <VcStatus variant="light-danger">Light Danger</VcStatus>
  </div>
</template>

<script lang="ts" setup>
import { VcStatus } from '@vc-shell/framework';
</script>
```

### Dot-Only Display Mode

```vue
<template>
  <div class="tw-flex tw-items-center tw-gap-2">
    <VcStatus variant="success" dot />
    <span>Item is active</span>
  </div>
</template>

<script lang="ts" setup>
import { VcStatus } from '@vc-shell/framework';
</script>
```

### Extended Status for Rich Content

```vue
<template>
  <VcStatus extend variant="danger">
    <div class="tw-flex tw-flex-row tw-items-center">
      <VcIcon icon="material-warning" size="xl" variant="danger" class="tw-mr-3" />
      <div>
        <h3 class="tw-font-bold">Error Status</h3>
        <p>There was an error processing your request. Please try again later.</p>
      </div>
    </div>
  </VcStatus>
</template>

<script lang="ts" setup>
import { VcStatus, VcIcon } from '@vc-shell/framework';
</script>
```

### Status with Dynamic Variant

```vue
<template>
  <VcStatus :variant="orderStatus.variant">
    {{ orderStatus.label }}
  </VcStatus>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue';
import { VcStatus } from '@vc-shell/framework';

const status = ref('processing');

const orderStatus = computed(() => {
  switch (status.value) {
    case 'completed':
      return { variant: 'success', label: 'Completed' };
    case 'cancelled':
      return { variant: 'danger', label: 'Cancelled' };
    case 'processing':
      return { variant: 'info', label: 'Processing' };
    case 'on-hold':
      return { variant: 'warning', label: 'On Hold' };
    default:
      return { variant: 'info', label: 'Unknown' };
  }
});
</script>
```

### Table with Status Indicators

```vue
<template>
  <table class="tw-min-w-full tw-border-collapse">
    <thead>
      <tr class="tw-bg-[color:var(--neutrals-100)]">
        <th class="tw-p-2 tw-text-left">Order ID</th>
        <th class="tw-p-2 tw-text-left">Customer</th>
        <th class="tw-p-2 tw-text-left">Date</th>
        <th class="tw-p-2 tw-text-left">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="order in orders" :key="order.id" class="tw-border-t tw-border-[color:var(--neutrals-200)]">
        <td class="tw-p-2">#{{ order.id }}</td>
        <td class="tw-p-2">{{ order.customer }}</td>
        <td class="tw-p-2">{{ order.date }}</td>
        <td class="tw-p-2">
          <VcStatus :variant="getStatusVariant(order.status)">
            {{ order.status }}
          </VcStatus>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script lang="ts" setup>
import { VcStatus } from '@vc-shell/framework';

const orders = [
  { id: '1001', customer: 'John Doe', date: '2023-06-15', status: 'Completed' },
  { id: '1002', customer: 'Jane Smith', date: '2023-06-16', status: 'Processing' },
  { id: '1003', customer: 'Robert Johnson', date: '2023-06-17', status: 'On Hold' },
  { id: '1004', customer: 'Emily Davis', date: '2023-06-18', status: 'Cancelled' },
];

function getStatusVariant(status: string) {
  switch (status) {
    case 'Completed':
      return 'success';
    case 'Processing':
      return 'info';
    case 'On Hold':
      return 'warning';
    case 'Cancelled':
      return 'danger';
    default:
      return 'info';
  }
}
</script>
```

### Status with Count Badge

```vue
<template>
  <div class="tw-flex tw-items-center tw-gap-4">
    <div class="tw-flex tw-items-center">
      <VcStatus variant="success" dot />
      <span class="tw-ml-2">Active</span>
      <VcBadge class="tw-ml-2" variant="success">{{ activeTasks }}</VcBadge>
    </div>
    
    <div class="tw-flex tw-items-center">
      <VcStatus variant="danger" dot />
      <span class="tw-ml-2">Failed</span>
      <VcBadge class="tw-ml-2" variant="danger">{{ failedTasks }}</VcBadge>
    </div>
    
    <div class="tw-flex tw-items-center">
      <VcStatus variant="warning" dot />
      <span class="tw-ml-2">Pending</span>
      <VcBadge class="tw-ml-2" variant="warning">{{ pendingTasks }}</VcBadge>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { VcStatus, VcBadge } from '@vc-shell/framework';

const activeTasks = 12;
const failedTasks = 3;
const pendingTasks = 5;
</script>
```
