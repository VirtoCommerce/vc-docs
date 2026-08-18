# `notification` Service API for Toast Messages

The `notification` service in VC-Shell provides a flexible and customizable API to display temporary **toast messages** to users. It supports different types of notifications (success, error, warning, and default), multiple positioning options, and custom content. This document describes the public API for using this service to show toast notifications.

The `notification` service offers a global API to create and manage toast notifications. Individual toast messages are rendered using the `VcToast` UI component (an internal framework component). This service is primarily for immediate, short-lived feedback to the user.

For handling persistent push notifications (which might also trigger toasts), see the `useNotifications` composable and related documentation.

## Key features

-   Four notification types: `success`, `error`, `warning`, and `default` (for neutral toasts).
-   Multiple positioning options (e.g., `top-center`, `top-right`, `bottom-left`).
-   Auto-dismiss with configurable `timeout` or persistent toasts (`timeout: false`).
-   Support for custom content using strings, HTML, or Vue components.
-   Animation effects for entrance and exit of toasts.
-   Position-specific limits (`limit`) and queuing.
-   Programmatic update (`update`) and removal (`remove`, `clearPosition`, `clearAll`) of toasts.
-   Lifecycle callbacks (`onOpen`, `onClose`) for toasts.
-   Support for custom styling via CSS variables.

## Usage

### Basic usage

```typescript
import { notification } from '@vc-shell/framework';

// Show a default toast
notification('This is a basic toast message');

// Show a success toast
notification.success('Operation completed successfully');

// Show an error toast
notification.error('An error occurred');

// Show a warning toast
notification.warning('Please note this action cannot be undone');
```

### Notification options

The `notification` function and its type-specific variants (`success`, `error`, `warning`) accept an optional second argument, an `NotificationOptions` object, to customize the toast's behavior and appearance.

```typescript
import { notification } from '@vc-shell/framework';

// Show a success toast with custom options
notification.success('File uploaded successfully!', {
  timeout: 5000,                // Duration in milliseconds (5 seconds)
  position: 'top-right',        // Position on the screen
  pauseOnHover: true,           // Pause timeout when hovering
  limit: 3,                     // Maximum number of toasts in this position for this type
  onOpen: (payload) => {        // Callback when toast appears
    console.log('Toast opened', payload);
  },
  onClose: (payload) => {       // Callback when toast closes
    console.log('Toast closed', payload);
  },
  payload: { fileId: 'xyz123' } // Custom data to pass to callbacks
});
```

### Persistent toasts

To create a toast that doesn't auto-dismiss, set `timeout: false`.

```typescript
import { notification } from '@vc-shell/framework';

notification.warning('Your session will expire in 5 minutes. Please save your work.', {
  timeout: false,  // Disable auto-dismiss
  position: 'top-center'
});
```

### Custom component toasts

You can use a Vue component as the content of a toast.

```vue
<!-- MyCustomToastContent.vue -->
<template>
  <div class="custom-toast">
    <h4>{{ title }}</h4>
    <p>{{ message }}</p>
    <VcButton @click="takeAction">Take Action</VcButton>
  </div>
</template>

<script setup>
import { VcButton } from '@vc-shell/framework'; // Assuming VcButton is available
defineProps({ title: String, message: String, actionCallback: Function });

function takeAction() {
  if (props.actionCallback) props.actionCallback();
}
</script>
```

```typescript
// In another component or setup script
import { notification } from '@vc-shell/framework';
import MyCustomToastContent from './MyCustomToastContent.vue'; // Path to your component

function showCustomToast() {
  notification({
    content: MyCustomToastContent, // Pass the component definition
    props: {                       // Props for MyCustomToastContent
      title: 'Profile Update Required',
      message: 'Please complete your profile to continue.',
      actionCallback: () => console.log('Profile action taken!'),
    },
    timeout: 0, // Disable auto-dismiss for interactive toasts
    position: 'bottom-right'
  });
}
</script>
```
**Note**: When passing components as content, ensure they are imported and passed correctly (e.g., `markRaw` might be needed in some advanced scenarios, but usually direct import works).

### Update Toasts

You can update an existing toast's content, type, or other options using its ID.

```typescript
import { notification } from '@vc-shell/framework';

// Create an initial toast and store its ID
const uploadNotificationId = notification.info('Uploading file...', {
  timeout: false,
  position: 'bottom-right'
});

// Later, update the toast
function onUploadComplete(success: boolean) {
  if (success) {
    notification.update(uploadNotificationId, {
      content: 'File uploaded successfully!',
      type: 'success',
      timeout: 3000 // Auto-dismiss after 3 seconds
    });
  } else {
    notification.update(uploadNotificationId, {
      content: 'File upload failed. Please try again.',
      type: 'error',
      timeout: 5000
    });
  }
}

// To update position or other properties:
function moveNotificationToTop() {
  notification.update(uploadNotificationId, {
    position: 'top-right'
  });
}
```

### Clear toasts

```typescript
import { notification } from '@vc-shell/framework';

// Remove a specific toast by ID
// notification.remove(uploadNotificationId); // Assuming uploadNotificationId is defined

// Clear all toasts currently displayed in a specific position
notification.clearPosition('top-right');

// Clear all toasts currently displayed across all positions
notification.clearAll();
```

### Set global default position

You can change the default position for subsequently created toasts.

```typescript
import { notification } from '@vc-shell/framework';

// Set global default position for all subsequent notifications
notification.setPosition('bottom-right');

// This toast will now appear at bottom-right by default
notification.success('This toast will appear at bottom-right unless overridden.');
```

## API reference

### `notification(content, options?)`

Shows a toast message.

-   `content` (string | Component): The message string or a Vue component to render.
-   `options` (NotificationOptions, optional): Options to customize the toast.
-   Returns: `string | number` - The ID of the created toast.

Type-specific variants:
-   `notification.success(content, options?)`
-   `notification.error(content, options?)`
-   `notification.warning(content, options?)`
-   `notification.info(content, options?)` (Often an alias for 'default' or a distinct info style)

### Management functions

-   `notification.remove(notificationId)`: Removes a specific toast by its ID.
-   `notification.clearAll()`: Clears all toasts from all positions.
-   `notification.clearPosition(position)`: Clears all toasts from a specific `NotificationPosition`.
-   `notification.update(notificationId, options)`: Updates an existing toast. `notificationId` is the ID of the toast to update. `options` is an object with properties to change.
-   `notification.setPosition(position)`: Sets the default `NotificationPosition` for new toasts.

### `NotificationOptions` interface

```typescript
interface NotificationOptions {
  // Core options
  type?: 'default' | 'success' | 'error' | 'warning' | 'info'; // Added 'info' for completeness
  position?: 'top-center' | 'top-right' | 'top-left' | 'bottom-center' | 'bottom-right' | 'bottom-left';
  timeout?: number | false;  // Duration in ms, or false for no timeout
  pauseOnHover?: boolean;    // Pause timeout on hover (default: true)
  
  // Content options
  content?: string | Component;  // Text or Vue component to render
  props?: Record<string, any>; // Props to pass if content is a component
  
  // Limit options
  limit?: number;  // Max number of toasts at this position (default: 3 for some types)
  
  // Identification
  notificationId?: string | number;  // Custom ID (auto-generated if not provided)
  
  // Callbacks
  onOpen?: (payload: any) => void;   // Called when toast appears
  onClose?: (payload: any) => void;  // Called when toast closes
  payload?: any;                     // Custom data for callbacks, passed to onOpen/onClose
}
```

## Styling

The notification system uses the `VcToast` component internally for rendering and inherits its CSS variables for styling. You can customize the appearance by overriding these variables in your global CSS or theme-specific stylesheets:

```css
/* Example CSS variables VcToast might use */
:root {
  /* Main colors and styles */
  --notification-background: var(--additional-50);
  --notification-border-radius: var(--multivalue-border-radius);
  --notification-border-color: var(--neutrals-200);
  --notification-dismiss-color: var(--secondary-500);
  --notification-content-color: var(--neutrals-600);

  /* Color indicators for types */
  --notification-warning: var(--warning-500);
  --notification-error: var(--danger-500);
  --notification-success: var(--success-500);
  --notification-info: var(--info-500);

  /* Effects */
  --notification-shadow-color: var(--neutrals-300);
  --notification-shadow: 2px 2px 11px rgb(from var(--notification-shadow-color) r g b / 40%);
  --notification-hover-shadow: 2px 2px 15px rgb(from var(--notification-shadow-color) r g b / 60%);

  /* Variables for animation */
  --notification-animation-duration: 300ms;
  --notification-animation-timing: cubic-bezier(0.175, 0.885, 0.32, 1.275); /* Spring animation */
  --notification-slide-distance: 30px;

  /* Sizes */
  --notification-indicator-width: 4px;
}
```

## Best practices

* **Choose the right type**: Use `success`, `error`, `warning`, or `info`/`default` appropriately for the message's intent.
* **Position strategically**:
    *   `top-right` or `bottom-right` are common for general feedback.
    *   `top-center` might be used for more critical, brief system messages.
* **Message length**: Keep toast messages concise. For detailed information, link to another part of the UI or use a modal.
* **Timeouts**:
    *   Use `false` (persistent) for critical errors or messages requiring user action before dismissal.
    *   Use short timeouts (2000-5000ms) for confirmations or brief info.
* **Limit usage**: Avoid overwhelming users with too many toasts. Use the `limit` option if necessary. The system usually has a default limit per position.
* **Distinguish from push notifications**: This `notification` service is for immediate toasts. For persistent notifications that appear in a notification center, use the `useNotifications` composable and system. See [How-To: Working with Push Notifications using `useNotifications`](/platform/developer-guide/latest/custom-apps-development/vc-shell/Essentials/Usage-Guides/working-with-push-notifications-using-usenotifications).

## Examples

### Form submission feedback

```typescript
import { notification } from '@vc-shell/framework';
// Assume setLoading is a ref elsewhere
// Assume api.saveData exists

async function submitForm(formData: any) {
  // setLoading(true); // Example: manage loading state
  let tempNotificationId: string | number | undefined;
  try {
    tempNotificationId = notification.info('Saving changes...', {
      timeout: false, // Keep it visible while saving
      position: 'top-right'
    });
    
    await api.saveData(formData); // Your API call
    
    if (tempNotificationId) notification.remove(tempNotificationId); // Remove loading toast
    notification.success('Changes saved successfully!', {
      position: 'top-right',
      timeout: 3000
    });
  } catch (error: any) {
    if (tempNotificationId) notification.remove(tempNotificationId); // Remove loading toast
    notification.error('Failed to save changes: ' + (error.message || 'Unknown error'), {
      position: 'top-right',
      timeout: 5000 // Keep error visible longer
    });
  } finally {
    // setLoading(false);
  }
}
```

### Multi-step process feedback

```typescript
import { notification } from '@vc-shell/framework';
// Assume uploadFiles and processUploadedFiles exist

async function processFiles(files: File[]) {
  const processToastId = notification.info('Starting file process...', {
    timeout: false,
    position: 'bottom-right'
  });
  
  try {
    notification.update(processToastId, { content: 'Uploading files...' });
    await uploadFiles(files); // Step 1
    
    notification.update(processToastId, { content: 'Files uploaded, now processing...' });
    await processUploadedFiles(files); // Step 2
    
    notification.update(processToastId, {
      content: 'All files processed successfully!',
      type: 'success',
      timeout: 3000 // Auto-dismiss success message
    });
  } catch (error: any) {
    notification.update(processToastId, {
      content: 'Error during file processing: ' + (error.message || 'Unknown error'),
      type: 'error',
      timeout: 5000 // Keep error message longer
    });
  }
}
```
