# Customizing Notifications in VC-Shell

VC-Shell provides a flexible system for displaying notifications. While the `useNotifications` composable handles the logic and data access for notifications, their visual appearance, especially in global components like `notification-dropdown.vue`, is managed through a template registration mechanism. This allows developers to define custom Vue components to render different types of notifications.

## Overview

When a notification is received (e.g., via SignalR or added manually), the system attempts to find a registered template that matches the notification's `notifyType`. If a matching template is found, that Vue component is used to render the notification. If no specific template is registered for a given `notifyType`, a default template is used.

This approach allows for:
- Consistent branding and styling of notifications across the application.
- Tailored display of information based on the notification type.
- Rich interactive notifications, as the templates are Vue components.

## How to Register a Custom Notification Template

Notification templates are Vue components that are registered with the VC-Shell framework during application setup. This is typically done in your application's `main.ts` or a dedicated module initialization file.

### 1. Create Your Notification Template Component

First, create a Vue component that will render your custom notification. This component will receive the `PushNotification` object as a prop and should use the base `NotificationTemplate` for consistent styling and structure.

**Example: `ProductUpdateNotification.vue`** (Using `NotificationTemplate` as a base)

```vue
<template>
  <NotificationTemplate
    :title="computedTitle"
    :notification="props.notification"
    :icon="notificationIcon"
    :color="notificationColor"
    @click="handleNotificationClick"
  >
    <!-- Custom content for this notification type goes into the default slot -->
    <p class="tw-text-sm tw-text-gray-700">{{ notification.message }}</p>
    <img
      v-if="notification.data?.imageUrl"
      :src="notification.data.imageUrl"
      alt="Product Image"
      class="tw-mt-2 tw-max-w-full tw-h-auto tw-rounded"
    />
    <VcButton
        v-if="notification.data?.productId"
        size="sm"
        variant="outline"
        class="tw-mt-2"
        @click.stop="handleViewDetails"
      >
        View Product Details
    </VcButton>
  </NotificationTemplate>
</template>

<script lang="ts" setup>
import { computed } from 'vue';
// Adjust paths as per your project structure
import { NotificationTemplate, type PushNotification, VcButton } from '@vc-shell/framework';
// import { useRouter } from 'vue-router'; // If navigation is needed

interface ProductNotificationData {
  imageUrl?: string;
  productId?: string;
  productName?: string;
  // Add other product-specific data fields if necessary
}

interface Props {
  notification: PushNotification<ProductNotificationData>;
}

const props = defineProps<Props>();
// const router = useRouter(); // Uncomment if navigation is needed

const computedTitle = computed(() => {
  // You can customize the title based on notification data
  return props.notification.data?.productName
    ? `Update for ${props.notification.data.productName}`
    : props.notification.title || 'Product Update';
});

const notificationIcon = computed(() => {
  // Determine icon based on notification content or type
  return 'material-shopping_bag'; // Example icon
});

const notificationColor = computed(() => {
  // Determine color based on notification content or type
  return 'var(--primary-500)'; // Example color
});

function handleNotificationClick() {
  console.log('Notification clicked:', props.notification.id);
  // Implement general click action for the notification if needed
  // e.g., markAsRead(props.notification) can be called here or in a global handler
}

function handleViewDetails() {
  if (props.notification.data?.productId) {
    console.log('Navigating to product details:', props.notification.data.productId);
    // Example navigation:
    // router.push({ name: 'product-details', params: { id: props.notification.data.productId } });
  }
}

// It's good practice to also define the notifyType if this component is meant
// to be automatically picked up by its type.
// This is usually done where the component is registered or if it's a self-registering module.
defineOptions({
  inheritAttrs: false,
  notifyType: "ProductUpdateNotificationEvent", // Example: This specific type will be used for registration
});
</script>

<style scoped>
/* Add any specific styles for your custom content here if needed */
/* The base NotificationTemplate already provides general styling. */
</style>
```

**Key points for your template component:**

- **Import `NotificationTemplate`**: And other necessary components like `VcButton` or types like `PushNotification` from `@vc-shell/framework`.
- **Use `NotificationTemplate` in your `<template>`**: This is the root or main wrapper.
- **Pass Props to `NotificationTemplate`**:
    - `notification`: The raw notification object.
    - `title`: A computed title for the notification.
    - `icon` (optional): Name of the Material Design icon.
    - `color` (optional): A CSS color variable or hex code for emphasis (often used for the icon background or a side border, depending on `NotificationTemplate`'s internal styling).
- **Use the Default Slot**: Place your custom markup (text, images, buttons specific to this notification type) *inside* the `<NotificationTemplate>` tags. This content will be rendered in the designated area by the base template.
- **Handle Custom Actions**: Implement methods for any interactive elements within your custom slot (e.g., `handleViewDetails`). Use `@click.stop` on interactive elements if you also have a main `@click` on `NotificationTemplate` to prevent event bubbling if necessary.
- **`defineOptions`**: If this component is intended to be automatically associated with a `notifyType` for registration, you can include `notifyType` in `defineOptions`.
- The `PushNotification` type can have a generic `data` property. Type this more specifically (e.g., `PushNotification<ProductNotificationData>`) if your notification type always includes certain data.

### 2. Register the Template

Notification templates are typically registered when a VC-Shell module is initialized using the `createAppModule` function. This function accepts an argument for `notificationTemplates`, where you provide an object mapping `notifyType` strings to your custom template components.

**Example: Registering in a module definition file (e.g., `src/modules/your-module/index.ts`)**

```typescript
// src/modules/your-module/index.ts
import { createAppModule } from '@vc-shell/framework'; // Adjust path as necessary

// Import your custom notification template components
import ProductUpdateNotification from './components/notifications/ProductUpdateNotification.vue';
import AnotherCustomNotification from './components/notifications/AnotherCustomNotification.vue';

// Import pages, locales, other components for this module
// import MyPages from './pages';
// import myLocales from './locales';

const notificationTemplates = {
  // The key here is NOT directly used for lookup;
  // the notifyType defined within the component itself is crucial.
  // However, it's good practice to use a descriptive key.
  ProductUpdate: ProductUpdateNotification, // ProductUpdateNotification.vue should define options.notifyType = "ProductUpdateNotificationEvent"
  NewOrder: AnotherCustomNotification,      // AnotherCustomNotification.vue should define options.notifyType = "NewOrderReceivedEvent"
};

export default createAppModule(
  { /* your pages */ },
  { /* your locales */ },
  notificationTemplates,
  { /* other module components */ }
);
```

**Key points for registration:**

-   **`createAppModule`**: This is the standard way to package and register different parts of a VC-Shell module, including pages, locales, and notification templates.
-   **`notificationTemplates` Object**: You pass an object to `createAppModule` where keys are descriptive names (for organization) and values are your imported Vue notification template components.
-   **`notifyType` in Component**: Crucially, each of your template components (e.g., `ProductUpdateNotification.vue`) **must** define its `notifyType` via `defineOptions({ notifyType: "YourSpecificNotifyType" })`. The `createAppModule` function iterates through the provided templates and uses this embedded `notifyType` to populate an internal `notificationTemplatesMap`.
-   The `notificationTemplatesMap` (usually available via `app.config.globalProperties.notificationTemplatesMap`) is then used by components like `Notification.vue` (internal to `NotificationDropdown`) to find and render the correct template based on the `notifyType` of an incoming push notification.

### Where to Register

-   **Module Initialization File**: This is the primary and recommended way. When you define a module (e.g., for Products, Orders, etc.), you include its specific notification templates as part of its definition using `createAppModule`. This keeps module-specific concerns encapsulated.
    
    ```typescript
    // Example: apps/vendor-portal/src/modules/offers/index.ts
    import { createAppModule } from '@vc-shell/framework';
    import OfferCreatedDomainEvent from './components/notifications/OfferCreatedDomainEvent.vue';
    // ... other imports for pages, locales ...

    const notificationTemplates = {
      OfferCreated: OfferCreatedDomainEvent, // OfferCreatedDomainEvent.vue defines notifyType: "OfferCreatedDomainEvent"
    };

    export default createAppModule(
      { /* offer pages */ },
      { /* offer locales */ },
      notificationTemplates
    );
    ```

-   **Application Entry Point (`main.ts`)**: While `createAppModule` is module-centric, global or truly shared notification templates could potentially be registered by ensuring they are part of a `notificationTemplates` object that gets processed by the root application setup if it also uses a mechanism similar to `createAppModule` for its core features, or by directly manipulating `app.config.globalProperties.notificationTemplatesMap` during the initial app setup (though this is less common and more direct manipulation should be handled with care).

    The `framework/index.ts` or similar core framework initialization files are responsible for setting up the initial `notificationTemplatesMap` and potentially registering globally default templates.

## Default Notification Template

VC-Shell usually provides a default notification template. This template is used if no custom template is registered for a specific `notifyType`.

## Best Practices

- **Keep Templates Focused:** Notification templates should primarily be concerned with the presentation of notification data. Complex logic related to what happens *after* a notification is interacted with (e.g., navigating, marking as read) might be handled by events emitted from the template or by the `useNotifications` handlers in other components.
- **Consistent `notifyType`:** Ensure the `notifyType` string used for registration exactly matches the `notifyType` property of the incoming push notifications.
- **Performance:** Keep notification templates lightweight. Avoid overly complex computations or heavy assets directly within the template if possible, especially if many notifications can be displayed at once.
- **Modularity:** Register templates within the relevant module or application scope to maintain separation of concerns.

