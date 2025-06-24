# How-To: Managing Settings Menu with `useSettingsMenu`

The `useSettingsMenu` composable in VC-Shell provides a centralized way to manage and display items in the application's settings menu. This guide will walk you through common use cases for registering, organizing, and displaying settings.

## Prerequisites

- Understanding of Vue 3 Composition API.
- Familiarity with the `useSettingsMenu` composable (see [useSettingsMenu API Reference](../composables/useSettingsMenu.md)).
- Knowledge of how to create Vue components.
- Familiarity with the [`SettingsMenuItem` component API](../shared/components/settings-menu-item.md).

## Core Concept

`useSettingsMenu` allows different parts of your application to register components that should appear in a dedicated settings area. The service collects these registered items, orders them, and makes them available for display, typically by a global `SettingsMenu` component.

**Key features:**

- **Dynamic Registration**: Add or remove settings items at runtime.
- **Ordering**: Control the display order of settings items.
- **Component-Based**: Each settings item is a Vue component.
- **Pre-registration**: Register items before the main application or service initializes.

```typescript
import { useSettingsMenu } from '@vc-shell/framework';
import MyCustomSettings from './MyCustomSettings.vue';
import { onUnmounted } from 'vue';

// Inside a setup function of a Vue component or a plugin
const settingsMenu = useSettingsMenu();

// Register a new settings item
const itemId = settingsMenu.register({
  component: MyCustomSettings, // The Vue component for this setting
  order: 100,                  // Display order
  props: {                     // Props to pass to MyCustomSettings
    settingTitle: 'My Application Feature',
  },
});

// It's good practice to unregister when no longer needed
onUnmounted(() => {
  settingsMenu.unregister(itemId);
});
```

## Implementation Strategies

### 1. Creating and Registering Settings Menu Items with `SettingsMenuItem`

To ensure a uniform look and feel for all items in the settings menu, **always use** the framework-provided `SettingsMenuItem` component as the base for each registered item. This is the standard and recommended approach.

The `SettingsMenuItem` component encapsulates the standard display (icon, title, padding, hover/click behavior) and provides slots for customizing the content and trigger.

**Basic structure of a component using `SettingsMenuItem` (`MyCustomSettingEntry.vue`):**

```vue
<template>
  <SettingsMenuItem
    :title="props.menuTitle" 
    :icon="props.menuIcon" 
    @trigger:click="handleMenuClick"
  >
    <!-- 
      The "trigger" slot can be used for a fully custom trigger display,
      overriding the default title/icon.
      See LanguageSelector.vue for an example.
    -->
    <!-- 
      The "content" slot is used if your menu item needs to display 
      additional content below the trigger, such as a dropdown.
      See ThemeSelector.vue for an example.
    -->
    <template #content v-if="isDropdownOpen">
      <div class="my-custom-dropdown-content">
        <p>Dropdown content for {{ props.menuTitle }}</p>
        <!-- ... control elements ... -->
      </div>
    </template>
  </SettingsMenuItem>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
// Ensure the import path is correct for your project
import { SettingsMenuItem } from '@vc-shell/framework';

const props = defineProps<{
  menuTitle: string;
  menuIcon?: string; // or Component, if SettingsMenuItem supports it
  // ... other props specific to your setting
}>();

const isDropdownOpen = ref(false); // Example for a menu item with a dropdown

function handleMenuClick() {
  // Logic for a simple click (if there's no dropdown)
  console.log(`Clicked item: ${props.menuTitle}`);
  
  // Or logic to open/close a dropdown
  // isDropdownOpen.value = !isDropdownOpen.value;
}

// ... other component logic ...
</script>

<style scoped>
.my-custom-dropdown-content {
  padding: 10px;
  background-color: var(--secondary-50); /* Example background */
}
</style>
```

**Registering such a component:**

```typescript
import MyCustomSettingEntry from './MyCustomSettingEntry.vue';

settingsMenu.register({
  id: 'custom-entry',
  component: MyCustomSettingEntry,
  order: 160,
  props: {
    menuTitle: 'My Custom Item',
    menuIcon: 'icon-name', // Icon name or icon component
    // ... pass other necessary props
  },
});
```

Using `SettingsMenuItem` as the standard base for all menu items ensures visual consistency and predictable behavior for the settings menu throughout the application.

### 2. Pre-registering Settings Items

Sometimes, you need to ensure a settings item is available as early as possible, even before the `useSettingsMenu` composable might be conveniently used within a component's setup. This is common for core settings or settings added by modules during their initialization.

The `addSettingsMenuItem` function allows this.

```typescript
// Typically in a plugin or a module's main file (e.g., index.ts)
import { addSettingsMenuItem } from '@vc-shell/framework';
import CoreAnalyticsSettings from './CoreAnalyticsSettings.vue'; // Assume path is correct

addSettingsMenuItem({
  id: 'core-analytics',
  component: CoreAnalyticsSettings,
  order: 1, // Core settings might have a low order to appear first
  props: {
    defaultConsent: false,
  },
});
```
When using `addSettingsMenuItem`, the item is added to a queue and will be processed once the `SettingsMenuService` is initialized (usually when `provideSettingsMenu` is called, often in the root of your application).

### 3. Organizing Settings with `order`

The `order` property in `RegisterSettingsMenuItemOptions` determines the sequence in which items appear. Lower numbers appear before higher numbers. If `order` is not specified, items are typically appended in registration order.

```typescript
const settingsMenu = useSettingsMenu();

// User Profile settings (appears first in this group)
settingsMenu.register({
  id: 'user-profile',
  component: UserProfileSettings,
  order: 100,
  props: { title: 'User Profile' },
});

// Notification Preferences (appears after User Profile)
settingsMenu.register({
  id: 'notifications-pref',
  component: NotificationPreferences,
  order: 110,
  props: { title: 'Notification Preferences' },
});

// Account Security (appears after Notification Preferences)
settingsMenu.register({
  id: 'account-security',
  component: AccountSecuritySettings,
  order: 120,
  props: { title: 'Account Security' },
});
```

## Best Practices

1.  **Unique IDs**: While optional for `register`, providing a unique `id` is good practice for easier unregistration and debugging, especially for items that might be dynamically added and removed.
2.  **Cleanup**: Always call `unregister` when a settings item is no longer needed, typically in the `onUnmounted` hook of the component that registered it, to prevent memory leaks and stale entries. Pre-registered items usually don't need explicit unregistration unless the module providing them is dynamically unloaded.
3.  **Self-Contained Components**: Design your settings components to be self-contained and manage their own state and logic.
4.  **Props for Configuration**: Pass initial configuration or context to your settings components via the `props` option during registration.
5.  **Consistent Ordering**: Establish a clear strategy for the `order` property to ensure a predictable and user-friendly settings menu.
6.  **Modularity**: Leverage `useSettingsMenu` to allow different modules or parts of your application to contribute to a unified settings experience without tight coupling.

## Related Resources

- [useSettingsMenu API Reference](../composables/useSettingsMenu.md) - Detailed API documentation for the composable.
- [`SettingsMenuItem` API Reference](../shared/components/settings-menu-item.md) - Detailed API documentation for the standard settings item component.
- [Vue 3 Provide/Inject](https://vuejs.org/guide/components/provide-inject.html) - Understanding how services like `SettingsMenuService` are often made available.
