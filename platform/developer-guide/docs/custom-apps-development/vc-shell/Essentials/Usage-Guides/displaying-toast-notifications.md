# How-To: Displaying Toast Notifications with the `notification` Service

This guide provides practical examples of how to use the global `notification` service in VC-Shell to display immediate, short-lived toast messages to your users.

## Prerequisites

-   Understanding of Vue 3 Composition API.
-   Familiarity with the [`notification` Service API Reference](../../Essentials/shared/components/notifications.md).
-   Basic knowledge of JavaScript/TypeScript for event handling and component interaction.

## Core Concept

The `notification` service is a global utility available throughout your VC-Shell application for showing toast messages. It's ideal for:

-   Confirming successful actions (e.g., "Settings saved!").
-   Alerting users to errors (e.g., "Failed to update profile.").
-   Providing brief informational messages or warnings.

You can import `notification` directly from `@vc-shell/framework` in any Vue component's `<script setup>` or JavaScript/TypeScript file.

## Basic Toast Types

The service provides convenient methods for common toast types:

```typescript
import { notification } from '@vc-shell/framework';

// Success Toast
notification.success('Your changes have been saved successfully.');

// Error Toast
notification.error('Connection to server lost. Please try again.');

// Warning Toast
notification.warning('Your session is about to expire.');

// Info/Default Toast
notification.info('A new version of the application is available.');
// or
notification('A general piece of information for the user.');
```

## Customizing Toast Appearance and Behavior

All notification methods accept an optional second argument, an `NotificationOptions` object, to customize the toast.

### 1. Setting Timeout and Persistence

```typescript
import { notification } from '@vc-shell/framework';

// Toast that disappears after 5 seconds (5000ms)
notification.info('This message will auto-dismiss.', { timeout: 5000 });

// Persistent toast that requires manual dismissal (if VcToast provides a close button)
// or programmatic removal via notification.remove().
notification.error('Critical Error: Action required!', { timeout: false });
```

### 2. Choosing Position

```typescript
import { notification } from '@vc-shell/framework';

// Display at the top-right corner
notification.success('Profile updated!', { position: 'top-right' });

// Display at the bottom-center
notification.warning('Low disk space.', { position: 'bottom-center' });

// Set a new default position for subsequent toasts (until changed again or page reloads)
notification.setPosition('top-center');
notification.info('This will now appear at the top-center.');
```
Available positions: `'top-center'`, `'top-right'`, `'top-left'`, `'bottom-center'`, `'bottom-right'`, `'bottom-left'`.

### 3. Using Callbacks and Payload

Execute functions when a toast opens or closes, and pass custom data.

```typescript
import { notification } from '@vc-shell/framework';

const userId = 'user123';

notification.info(`Processing data for user ${userId}...`, {
  payload: { operationId: 'op_abc', timestamp: Date.now() },
  onOpen: (payload) => {
    console.log('Processing toast opened:', payload); // Logs { operationId: 'op_abc', ... }
    // trackAnalytics('toast_shown', payload.operationId);
  },
  onClose: (payload) => {
    console.log('Processing toast closed:', payload);
    // maybe trigger cleanup or next step
  }
});
```

## Advanced Usage

### 1. Showing Toasts During Async Operations

A common use case is to show a loading toast during an API call and then update it based on the outcome.

```typescript
import { notification } from '@vc-shell/framework';
// Assume 'apiService.updateSettings' is an async function that returns a Promise
// Assume 'isLoading' is a ref to manage loading state in your component

async function handleSaveSettings(settingsData: any) {
  isLoading.value = true;
  const loadingToastId = notification.info('Saving settings...', {
    timeout: false, // Keep it visible until operation completes
    position: 'top-right'
  });

  try {
    await apiService.updateSettings(settingsData);
    notification.update(loadingToastId, {
      content: 'Settings saved successfully!',
      type: 'success',
      timeout: 3000 // Auto-dismiss success message
    });
  } catch (error) {
    console.error('Failed to save settings:', error);
    notification.update(loadingToastId, {
      content: 'Error saving settings. Please try again.',
      type: 'error',
      timeout: 5000 // Keep error message visible longer
    });
  } finally {
    isLoading.value = false;
    // If the toast wasn't updated to success/error (e.g., due to an unexpected issue),
    // you might want to ensure it's removed:
    // setTimeout(() => notification.remove(loadingToastId), 500); // Failsafe removal
  }
}
```

### 2. Using Custom Vue Components as Toast Content

For richer toast content, you can pass a Vue component.

**Your Custom Toast Component (`MyInteractiveToast.vue`):**
```vue
<template>
  <div class="my-interactive-toast">
    <h4>{{ title }}</h4>
    <p>{{ message }}</p>
    <VcButton v-if="actionText && onAction" @click="onAction" size="sm">
      {{ actionText }}
    </VcButton>
  </div>
</template>

<script setup lang="ts">
import { VcButton } from '@vc-shell/framework'; // Adjust import if necessary

defineProps<{
  title: string;
  message: string;
  actionText?: string;
  onAction?: () => void;
}>();
</script>

<style scoped>
.my-interactive-toast {
  padding: 8px;
  border-left: 4px solid var(--primary-500); /* Example style */
}
</style>
```

**Displaying the Custom Toast:**
```typescript
import { notification } from '@vc-shell/framework';
import MyInteractiveToast from './MyInteractiveToast.vue'; // Adjust path

function showUpdateAvailableToast() {
  notification({
    content: MyInteractiveToast,
    props: {
      title: 'Update Available!',
      message: 'A new version of the application has been downloaded.',
      actionText: 'Refresh Now',
      onAction: () => {
        window.location.reload();
      }
    },
    position: 'bottom-right',
    timeout: false, // Keep it until user interacts or refreshes
  });
}
```
**Note:** Ensure `MyInteractiveToast.vue` is correctly imported. For complex components or if issues arise, consider using `markRaw` from Vue when passing the component: `content: markRaw(MyInteractiveToast)`.

### 3. Managing Multiple Toasts

-   **Limiting Toasts**: The `limit` option in `NotificationOptions` can suggest a maximum number of toasts for a given position and type, though the system has its own internal limits as well.
-   **Clearing Toasts**:
    -   `notification.remove(id)`: Removes a specific toast.
    -   `notification.clearPosition(position)`: Clears all toasts from one position.
    -   `notification.clearAll()`: Clears all toasts everywhere.

```typescript
// Example: Clearing all toasts from the top-right after a certain action
function cleanupUI() {
  notification.clearPosition('top-right');
  // ... other cleanup ...
}
```

## Best Practices

-   **Be Concise**: Toast messages should be short and to the point.
-   **Use Sparingly**: Overuse of toasts can annoy users. Reserve them for important, brief feedback.
-   **Non-Blocking**: Toasts should not block user interaction with the rest of the application.
-   **Actionable (If Needed)**: If a toast implies an action, provide a clear way for the user to take it (e.g., using a custom component with a button).
-   **Consider Accessibility**: Ensure toasts are accessible (e.g., can be read by screen readers, have sufficient contrast).
-   **Refer to API Docs**: For the full list of `NotificationOptions` and method signatures, always refer to the [`notification` Service API Reference](../../Essentials/shared/components/notifications.md).

By following these examples, you can effectively use the `notification` service to provide timely and relevant feedback to users throughout your VC-Shell application. 
