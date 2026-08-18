# How-To: Adding App Bar Widgets with `useAppBarWidget`

The `useAppBarWidget` composable provides a powerful way to extend the application's navigation bar with custom widgets. This guide demonstrates how to effectively register, manage, and implement app bar widgets in your VC-Shell applications.

## Prerequisites

- Understanding of Vue 3 Composition API, including `ref` and `computed`.
- Familiarity with the `useAppBarWidget` composable (see [useAppBarWidget API Reference](../composables/useAppBarWidget.md).)
- Basic knowledge of Vue component lifecycle hooks (`onMounted`, `onUnmounted`).
- Understanding of VC-Shell's component architecture and UI components.

## Core Concept

App Bar widgets are interactive elements displayed in the application's top navigation bar. They can include:

- **Icons**: Visual indicators for the widget's purpose
- **Components**: Custom Vue components that render when activated
- **Click Handlers**: Functions executed when the widget is clicked
- **Badges**: Visual indicators for notifications or status
- **Ordering**: Control over widget positioning in the app bar

The `useAppBarWidget` service manages widget registration, unregistration, and provides access to all registered widgets through a reactive computed property.

```typescript
import { useAppBarWidget } from '@vc-shell/framework';

const { register, unregister, items } = useAppBarWidget();

// Register a widget
const widgetId = register({
  icon: 'bell',
  component: NotificationPanel,
  badge: () => hasNotifications.value
});

// Clean up when component unmounts
onUnmounted(() => {
  unregister(widgetId);
});
```

## Implementation Strategies

### 1. Basic Widget Registration in App Component

The most common pattern is to register widgets in your main App component:

```typescript
// App.vue
import { useAppBarWidget, usePermissions } from '@vc-shell/framework';
import { VendorSwitcher } from '../components';

const { register: registerAppBarWidget } = useAppBarWidget();
const { hasAccess } = usePermissions();

// Conditional registration based on permissions
if (isAdministrator.value || hasAccess("operator:resources")) {
  registerAppBarWidget({
    id: "vendor-switcher",
    icon: ProfileIcon,
    component: VendorSwitcher,
    order: 20,
    props: {
      isExpanded: isVendorSwitcherExpanded,
      "onUpdate:isExpanded": handleVendorSwitcherUpdate,
    },
    onClick: () => {
      isVendorSwitcherExpanded.value = true;
    },
  });
}
```

### 2. Simple Click Handler Widget

For widgets that only need to trigger an action without a complex component:

```typescript
// Register a help widget
const { register } = useAppBarWidget();

register({
  id: 'help',
  icon: 'help_outline',
  onClick: () => {
    // Open help dialog or navigate to help page
    showHelpDialog();
  },
  order: 30
});
```

### 3. Widget with Badge Indicator

Add visual indicators for notifications or status:

```typescript
const unreadCount = ref(0);
const hasNotifications = computed(() => unreadCount.value > 0);

register({
  id: 'notifications',
  icon: 'notifications',
  component: NotificationPanel,
  badge: hasNotifications,
  order: 10
});
```

### 4. Widget with Dynamic Props

Pass reactive data to your widget component:

```typescript
const currentUser = ref(null);
const isExpanded = ref(false);

register({
  id: 'user-menu',
  icon: 'account_circle',
  component: UserMenu,
  props: {
    user: currentUser,
    isExpanded: isExpanded,
    "onUpdate:isExpanded": (value) => isExpanded.value = value
  },
  order: 100
});
```

### 5. Conditional Widget Registration

Register widgets based on user permissions or application state:

```typescript
import { usePermissions, useUser } from '@vc-shell/framework';

const { hasAccess } = usePermissions();
const { isAdministrator } = useUser();

// Only show admin tools for administrators
if (isAdministrator.value || hasAccess("admin:access")) {
  register({
    id: 'admin-tools',
    icon: 'admin_panel_settings',
    component: AdminToolsPanel,
    order: 5
  });
}
```

## Best Practices

* **Unique Widget IDs**: Always provide unique `id` values for your widgets to avoid conflicts and enable proper management.

* **Proper Cleanup**: Always unregister widgets in the `onUnmounted` lifecycle hook to prevent memory leaks and duplicate registrations.

* **Reactive Badge Logic**: Use computed properties or reactive functions for badge conditions to ensure they update automatically when underlying data changes.

* **Consistent Ordering**: Use the `order` property strategically to maintain a logical flow in the app bar (e.g., notifications before user profile).

* **Error Handling**: Implement proper error handling in widget click handlers and component logic.

## Widget Component Structure

When creating a widget component, follow these patterns:

### Basic Widget Component

```vue
<!-- MyWidget.vue -->
<template>
  <div class="my-widget">
    <!-- Widget content -->
    <div class="my-widget__header">
      <h3>{{ title }}</h3>
    </div>
    <div class="my-widget__content">
      <!-- Your widget content here -->
    </div>
  </div>
</template>

<script lang="ts" setup>
// Any props you need to pass to the widget
interface Props {
  isExpanded?: boolean;
  title?: string;
}

const props = defineProps<Props>();

const emit = defineEmits<{
  (e: "update:isExpanded", value: boolean): void;
  (e: "close"): void;
}>();

// Widget logic here
</script>
```

### Widget with Sidebar Pattern

For complex widgets, you can use the Sidebar component:

```vue
<template>
  <Sidebar
    :is-expanded="isExpanded"
    position="left"
    @close="onClose"
  >
    <template #header="{ header }">
      <div class="widget__header">
        <p class="widget__title">{{ title }}</p>
        <component :is="header" />
      </div>
    </template>
    <template #content>
      <!-- Widget content -->
    </template>
  </Sidebar>
</template>
```

By following these patterns and best practices, you can create powerful and user-friendly app bar widgets that enhance the overall user experience of your VC-Shell application.

