# VcStatusIcon Component

The `VcStatusIcon` component is an atom used throughout the VC-Shell framework for displaying a visual status indicator using icons. It provides a simple way to represent success or error states.

## Storybook

[VcStatusIcon Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/atoms-vcstatusicon--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=atoms-vcstatusicon--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcStatusIcon :status="true" />
</template>

<script lang="ts" setup>
import { VcStatusIcon } from '@vc-shell/framework';
</script>
```

## Props

| Prop      | Type      | Default     | Description                                             |
| --------- | --------- | ----------- | ------------------------------------------------------- |
| `status`  | `boolean` | `undefined` | Whether to show success (true) or error (false) status  |

## CSS Variables

The status icon component uses CSS variables for theming, which can be customized:

```css
:root {
  --status-success-main-color: var(--success-400);  /* Color used for success status icon */
  --status-info-main-color: var(--info-300);        /* Color used for error/info status icon */
}
```

## Examples

### Success Status Icon

```vue
<template>
  <VcStatusIcon :status="true" />
</template>

<script lang="ts" setup>
import { VcStatusIcon } from '@vc-shell/framework';
</script>
```

### Error Status Icon

```vue
<template>
  <VcStatusIcon :status="false" />
</template>

<script lang="ts" setup>
import { VcStatusIcon } from '@vc-shell/framework';
</script>
```

### With Status Text

```vue
<template>
  <div class="tw-flex tw-items-center tw-gap-2">
    <VcStatusIcon :status="isConnected" />
    <span>{{ isConnected ? 'Connected' : 'Disconnected' }}</span>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcStatusIcon } from '@vc-shell/framework';

const isConnected = ref(true);
</script>
```

### Dynamic Status

```vue
<template>
  <div class="tw-flex tw-flex-col tw-items-center tw-gap-4">
    <div class="tw-flex tw-items-center tw-gap-2">
      <VcStatusIcon :status="serverStatus" />
      <span>Server is {{ serverStatus ? 'online' : 'offline' }}</span>
    </div>
    
    <VcButton @click="toggleStatus">
      {{ serverStatus ? 'Simulate server down' : 'Simulate server up' }}
    </VcButton>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { VcStatusIcon, VcButton } from '@vc-shell/framework';

const serverStatus = ref(true);

function toggleStatus() {
  serverStatus.value = !serverStatus.value;
}
</script>
```

### Status Icons in a List

```vue
<template>
  <div class="tw-space-y-4">
    <div 
      v-for="service in services" 
      :key="service.id" 
      class="tw-flex tw-justify-between tw-items-center tw-p-3 tw-border-b tw-border-[color:var(--neutrals-100)]"
    >
      <div>
        <div class="tw-font-medium">{{ service.name }}</div>
        <div class="tw-text-sm tw-text-[color:var(--neutrals-500)]">{{ service.description }}</div>
      </div>
      <div class="tw-flex tw-items-center tw-gap-2">
        <span class="tw-text-sm">{{ service.status ? 'Available' : 'Unavailable' }}</span>
        <VcStatusIcon :status="service.status" />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { VcStatusIcon } from '@vc-shell/framework';

const services = [
  { 
    id: 1, 
    name: 'Authentication Service', 
    description: 'Handles user authentication',
    status: true 
  },
  { 
    id: 2, 
    name: 'Payment Gateway', 
    description: 'Processes payment transactions',
    status: false 
  },
  { 
    id: 3, 
    name: 'Order Management', 
    description: 'Tracks and processes orders',
    status: true 
  },
  { 
    id: 4, 
    name: 'Product Catalog', 
    description: 'Manages product information',
    status: true 
  }
];
</script>
```

### Status Dashboard

```vue
<template>
  <div class="tw-grid tw-grid-cols-1 md:tw-grid-cols-2 tw-gap-4">
    <div 
      v-for="system in systems" 
      :key="system.id" 
      class="tw-p-4 tw-bg-white tw-border tw-border-[color:var(--neutrals-200)] tw-rounded-md"
    >
      <div class="tw-flex tw-justify-between tw-items-center">
        <h3 class="tw-font-medium">{{ system.name }}</h3>
        <VcStatusIcon :status="system.status" />
      </div>
      <div class="tw-mt-2 tw-text-sm tw-text-[color:var(--neutrals-600)]">
        {{ system.description }}
      </div>
      <div class="tw-mt-4 tw-pt-3 tw-border-t tw-border-[color:var(--neutrals-100)] tw-flex tw-justify-between tw-items-center">
        <span class="tw-text-xs tw-text-[color:var(--neutrals-500)]">
          Last checked: {{ system.lastChecked }}
        </span>
        <span :class="[
          'tw-text-xs tw-font-medium',
          system.status 
            ? 'tw-text-[color:var(--success-500)]' 
            : 'tw-text-[color:var(--danger-500)]'
        ]">
          {{ system.status ? 'Operational' : 'Down' }}
        </span>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { VcStatusIcon } from '@vc-shell/framework';

const systems = [
  {
    id: 1,
    name: 'API Gateway',
    description: 'Primary entry point for all API requests',
    status: true,
    lastChecked: '5 minutes ago'
  },
  {
    id: 2,
    name: 'Database Cluster',
    description: 'Primary data storage system',
    status: true,
    lastChecked: '2 minutes ago'
  },
  {
    id: 3,
    name: 'Search Service',
    description: 'Handles product and content search',
    status: false,
    lastChecked: '7 minutes ago'
  },
  {
    id: 4,
    name: 'Authentication Service',
    description: 'Manages user authentication and authorization',
    status: true,
    lastChecked: '3 minutes ago'
  }
];
</script>
```

### Status Indicator with Feature Flags

```vue
<template>
  <div class="tw-space-y-3">
    <div 
      v-for="feature in features" 
      :key="feature.id" 
      class="tw-flex tw-items-center tw-justify-between tw-p-2 tw-border tw-border-[color:var(--neutrals-200)] tw-rounded"
    >
      <div>
        <div class="tw-font-medium">{{ feature.name }}</div>
        <div class="tw-text-xs tw-text-[color:var(--neutrals-500)]">{{ feature.description }}</div>
      </div>
      <div class="tw-flex tw-items-center">
        <VcStatusIcon :status="feature.enabled" />
        <span class="tw-ml-2 tw-text-sm">{{ feature.enabled ? 'Enabled' : 'Disabled' }}</span>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { VcStatusIcon } from '@vc-shell/framework';

const features = [
  {
    id: 'new-dashboard',
    name: 'New Dashboard UI',
    description: 'Redesigned dashboard with enhanced visualization',
    enabled: true
  },
  {
    id: 'ai-recommendations',
    name: 'AI Recommendations',
    description: 'Product recommendations powered by machine learning',
    enabled: false
  },
  {
    id: 'multi-currency',
    name: 'Multi-currency Support',
    description: 'Support for multiple currencies in checkout',
    enabled: true
  }
];
</script>
```
