# How-To: Working with Push Notifications using `useNotifications`

The `useNotifications` composable provides a comprehensive system for handling real-time push notifications in VC-Shell applications. This guide demonstrates the two main approaches for working with notifications: global app-wide subscriptions and blade-specific local handling.

## Prerequisites

- Understanding of Vue 3 Composition API and application lifecycle.
- Familiarity with the `useNotifications` composable (see [useNotifications API Reference](../composables/useNotifications.md)).
- Basic knowledge of VC-Shell's blade system and module architecture.
- Understanding of SignalR and real-time communication patterns.

## Core Concept

The VC-Shell notification system supports two distinct approaches:

- **Global App Subscription**: Using `notifyType` in `defineOptions` subscribes the entire application to notification types, making them available in the global notification center and throughout the app
- **Blade-Specific Handling**: Using `useNotifications(notifyType)` creates a local subscription that only affects the current blade, typically for displaying blade-specific toasts
- **Custom Templates**: Create custom display templates for notifications in the global notification center
- **Toast Integration**: Convert notifications into immediate toast feedback using the `notification` API

The key difference is scope: `defineOptions` affects the entire application, while `useNotifications(notifyType)` only affects the current blade.

```typescript
// Global subscription - affects entire app
defineOptions({
  name: 'OrderManagement',
  notifyType: 'OrderStatusChanged' // Available app-wide
});

// vs. Local subscription - only for this blade
const { setNotificationHandler } = useNotifications('OrderStatusChanged');
setNotificationHandler((notif) => {
  notification.success('Toast only visible in this blade');
});
```

## Implementation Strategies

### 1. Global App-Wide Notification Subscription

Use `defineOptions` with `notifyType` to subscribe the entire application to specific notification types:

```vue
<!-- OrderManagementBlade.vue -->
<script lang="ts" setup>
// Global subscription - makes OrderStatusChanged notifications 
// available throughout the entire application
defineOptions({
  name: 'OrderManagement',
  url: '/orders',
  notifyType: 'OrderStatusChanged' // App-wide subscription
});

// This blade content doesn't need to handle notifications directly
// They will appear in the global notification center automatically
</script>

<template>
  <div class="order-management">
    <VcTable :items="orders" />
    <!-- Notifications appear in global app bar notification center -->
  </div>
</template>
```

When you use `notifyType` in `defineOptions`:

- Notifications are available in the global notification center (app bar)
- Custom notification templates can be used to display them
- All parts of the application can access these notifications
- No additional code needed in the blade itself

### 2. Multiple Global Notification Types

Subscribe the application to multiple notification types:

```vue
<!-- ProductManagementBlade.vue -->
<script lang="ts" setup>
// Subscribe entire app to multiple notification types
defineOptions({
  name: 'ProductManagement',
  url: '/products',
  notifyType: ['ProductCreated', 'ProductUpdated', 'ProductApproved', 'ProductRejected']
});

// No notification handling code needed here
// All these notifications will be available app-wide
</script>
```

### 3. Blade-Specific Toast Notifications (Local Subscription)

Use `useNotifications(notifyType)` for blade-specific notification handling that doesn't affect the rest of the app:

```vue
<!-- InventoryBlade.vue -->
<script lang="ts" setup>
import { useNotifications, notification } from '@vc-shell/framework';

defineOptions({
  name: 'Inventory',
  url: '/inventory'
  // No notifyType here - not subscribing the app globally
});

// Local subscription - only affects this blade
const { setNotificationHandler } = useNotifications(['StockLevelChanged', 'InventoryAlert']);

// Handle notifications with blade-specific toasts
setNotificationHandler((notif) => {
  switch (notif.notifyType) {
    case 'StockLevelChanged':
      notification.info(`Stock level updated for item ${notif.data.itemName}`);
      refreshInventoryData();
      break;
      
    case 'InventoryAlert':
      notification.warning(`Inventory alert: ${notif.data.message}`);
      highlightAlertedItems(notif.data.itemIds);
      break;
  }
});

function refreshInventoryData() {
  // Refresh data specific to this blade
}

function highlightAlertedItems(itemIds: string[]) {
  // Highlight specific items in this blade's UI
}
</script>

<template>
  <div class="inventory-management">
    <VcTable :items="inventoryItems" />
    <!-- Toasts appear only when this blade is active -->
  </div>
</template>
```

### 4. Combined Approach

You can combine both approaches - global subscription for important notifications and local handling for blade-specific feedback:

```vue
<!-- OrderProcessingBlade.vue -->
<script lang="ts" setup>
import { useNotifications, notification } from '@vc-shell/framework';

// Global subscription - makes these available app-wide
defineOptions({
  name: 'OrderProcessing',
  url: '/orders/processing',
  notifyType: ['OrderCreated', 'OrderCancelled'] // Global notifications
});

// Local subscription for processing-specific events
const { setNotificationHandler } = useNotifications(['OrderProcessingStarted', 'OrderProcessingCompleted']);

// Handle local events with immediate toast feedback
setNotificationHandler((notif) => {
  switch (notif.notifyType) {
    case 'OrderProcessingStarted':
      notification.info('Order processing started...');
      updateProcessingStatus(notif.data.orderId, 'processing');
      break;
      
    case 'OrderProcessingCompleted':
      notification.success('Order processing completed!');
      updateProcessingStatus(notif.data.orderId, 'completed');
      break;
  }
});

function updateProcessingStatus(orderId: string, status: string) {
  // Update UI for specific order
}
</script>
```

### 5. Blade-Specific Notification Display

Create custom notification displays for local notifications:

```vue
<!-- CustomNotificationBlade.vue -->
<template>
  <div class="custom-notifications-blade">
    <!-- Custom notification panel for blade-specific notifications -->
    <div v-if="localNotifications.length" class="local-notifications">
      <h4>Blade-Specific Notifications</h4>
      <div 
        v-for="notif in localNotifications" 
        :key="notif.id"
        class="notification-item"
      >
        {{ notif.title }} - {{ notif.message }}
      </div>
    </div>

    <VcTable :items="data" />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { useNotifications, notification } from '@vc-shell/framework';

defineOptions({
  name: 'CustomNotifications',
  url: '/custom-notifications'
});

const data = ref([]);
const localNotifications = ref([]);

// Local subscription only
const { moduleNotifications, setNotificationHandler } = useNotifications('BladeSpecificEvent');

// Store notifications locally and show toasts
setNotificationHandler((notif) => {
  // Add to local display
  localNotifications.value.unshift(notif);
  
  // Show toast
  notification.info(`Blade event: ${notif.message}`);
  
  // Keep only last 5 notifications
  if (localNotifications.value.length > 5) {
    localNotifications.value = localNotifications.value.slice(0, 5);
  }
});
</script>
```

### 6. Notification Template for Global Notifications

Create custom templates for globally subscribed notifications:

```vue
<!-- OrderNotificationTemplate.vue -->
<template>
  <NotificationTemplate
    :title="notificationTitle"
    :notification="notification"
    icon="material-shopping_cart"
    color="var(--primary-500)"
    @click="handleNotificationClick"
  >
    <div class="order-notification">
      <p>Order #{{ notification.data.orderNumber }}</p>
      <p class="status">Status: {{ notification.data.status }}</p>
      <VcButton 
        size="sm"
        variant="outline"
        @click.stop="viewOrder"
      >
        View Order
      </VcButton>
    </div>
  </NotificationTemplate>
</template>

<script lang="ts" setup>
import { computed } from 'vue';
import { NotificationTemplate, VcButton } from '@vc-shell/framework';

interface Props {
  notification: PushNotification;
}

const props = defineProps<Props>();

// This template will be used for globally subscribed notifications
defineOptions({
  notifyType: "OrderStatusChanged"
});

const notificationTitle = computed(() => 
  `Order #${props.notification.data.orderNumber} Updated`
);

function handleNotificationClick() {
  // Handle template click
}

function viewOrder() {
  // Navigate to order details
  router.push(`/orders/${props.notification.data.orderId}`);
}
</script>
```

Then register this template in your module:

```typescript
// src/modules/orders/index.ts
import { createAppModule } from '@vc-shell/framework';
import OrderNotificationTemplate from './components/OrderNotificationTemplate.vue';

export default createAppModule(
  { /* pages */ },
  { /* locales */ },
  { 
    OrderNotification: OrderNotificationTemplate // Register template
  }
);
```

## When to Use Each Approach

### Use Global Subscription (`defineOptions` with `notifyType`) when:
- Notifications are important for the entire application
- You want notifications to appear in the global notification center
- Multiple parts of the app need to be aware of these events
- You want to create custom notification templates

### Use Local Subscription (`useNotifications(notifyType)`) when:
- You need immediate toast feedback specific to a blade
- Notifications are only relevant to the current blade's context
- You want to handle notifications without affecting the global state
- You need custom logic that's specific to the blade's workflow

## Best Practices

* **Choose the Right Scope**: Use global subscription for important app-wide events, local subscription for blade-specific feedback.

* **Avoid Duplication**: Don't use both approaches for the same notification type unless you have a specific reason.

* **Toast Appropriately**: Use local subscriptions with toasts for immediate user feedback that doesn't need to persist. For showing toasts, use the global [`notification` service API](../../Essentials/shared/components/notifications.md).

* **Template for Persistence**: Use global subscriptions with custom templates for notifications that users might need to review later in the notification center.

* **Performance**: Local subscriptions are more performant for frequent, blade-specific events.

* **User Experience**: Global notifications provide better UX for important events, local toasts for immediate feedback.

