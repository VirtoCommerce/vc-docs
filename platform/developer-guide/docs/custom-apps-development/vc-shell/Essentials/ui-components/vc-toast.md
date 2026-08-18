# VcToast Component

The `VcToast` component is a flexible notification system that displays temporary messages to users. It supports different types of notifications (success, error, warning, info) and can be configured for various use cases.

## Storybook

[VcToast Storybook](https://vc-shell-storybook.govirto.com/?path=/docs/molecules-vctoast--docs)

<iframe
  src="https://vc-shell-storybook.govirto.com/iframe.html?id=molecules-vctoast--docs&viewMode=story&shortcuts=false&singleStory=true"
  width="1000"
  height="500"
></iframe>

## Basic Usage

```vue
<template>
  <VcToast
    content="Operation completed successfully!"
    type="success"
    :timeout="5000"
    :pauseOnHover="true"
  />
</template>

<script lang="ts" setup>
import { VcToast } from '@vc-shell/framework';
</script>
```

## Notification Service Usage (Recommended)

For application-wide notifications, it's recommended to use the notification service instead of directly using the component:

```ts
import { notification } from '@vc-shell/framework';

// Show a default notification
notification('This is a notification message');

// Show a success notification
notification.success('Operation completed successfully!');

// Show an error notification
notification.error('An error occurred while processing your request.');

// Show a warning notification
notification.warning('Please review your information before proceeding.');
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `content` | `string \| Component` | `undefined` | The content to display in the notification |
| `notificationId` | `number \| string` | `undefined` | Unique identifier for the notification |
| `updateId` | `number \| string` | `undefined` | ID used to trigger updates to the notification |
| `type` | `'default' \| 'success' \| 'error' \| 'warning'` | `'default'` | The type of notification which determines the icon and color |
| `timeout` | `number \| boolean` | `5000` | Duration in milliseconds before auto-dismissing. Set to `false` to disable auto-dismiss |
| `pauseOnHover` | `boolean` | `true` | Whether to pause the timeout when hovering over the notification |
| `limit` | `number` | `undefined` | Maximum number of lines to display |
| `position` | `'top-center' \| 'top-right' \| 'top-left' \| 'bottom-center' \| 'bottom-right' \| 'bottom-left'` | `'top-center'` | Position of the notification on screen |

## Events

| Event | Payload | Description |
|-------|---------|-------------|
| `close` | `number \| string \| undefined` | Emitted when the notification is closed, with the notification ID |

## CSS Variables

```css
:root {
  /* Main colors and styles */
  --notification-background: var(--additional-50);          /* Background color of the notification */
  --notification-border-radius: var(--multivalue-border-radius); /* Border radius of the notification */
  --notification-border-color: var(--neutrals-200);        /* Border color of the notification */
  --notification-dismiss-color: var(--secondary-500);      /* Color of the dismiss/close button */
  --notification-content-color: var(--neutrals-600);       /* Text color of the notification content */

  /* Color indicators for types */
  --notification-warning: var(--warning-500);              /* Color for warning type indicator */
  --notification-error: var(--danger-500);                 /* Color for error type indicator */
  --notification-success: var(--success-500);              /* Color for success type indicator */
  --notification-info: var(--info-500);                    /* Color for info/default type indicator */

  /* Effects */
  --notification-shadow-color: var(--neutrals-300);        /* Base color for shadow effects */
  --notification-shadow: 2px 2px 11px rgb(from var(--notification-shadow-color) r g b / 40%); /* Shadow for normal state */
  --notification-hover-shadow: 2px 2px 15px rgb(from var(--notification-shadow-color) r g b / 60%); /* Shadow on hover */

  /* Variables for animation */
  --notification-animation-duration: 300ms;                /* Duration of entrance/exit animations */
  --notification-animation-timing: cubic-bezier(0.175, 0.885, 0.32, 1.275); /* Animation timing function */
  --notification-slide-distance: 30px;                     /* Distance for slide animations */

  /* Sizes */
  --notification-indicator-width: 4px;                     /* Width of the colored type indicator */
}
```

## Notification Service API

The notification service provides the following methods:

| Method | Description |
|--------|-------------|
| `notification(content, options?)` | Shows a default notification |
| `notification.success(content, options?)` | Shows a success notification |
| `notification.error(content, options?)` | Shows an error notification |
| `notification.warning(content, options?)` | Shows a warning notification |
| `notification.update(id, options)` | Updates an existing notification |
| `notification.remove(id)` | Removes a specific notification |
| `notification.clearAll()` | Removes all notifications |
| `notification.setPosition(position)` | Sets the default position for notifications |

## Examples

### Basic Toast Types

```vue
<template>
  <div class="tw-space-y-4">
    <VcButton @click="showDefault">Show Default</VcButton>
    <VcButton @click="showSuccess">Show Success</VcButton>
    <VcButton @click="showError">Show Error</VcButton>
    <VcButton @click="showWarning">Show Warning</VcButton>
  </div>
</template>

<script lang="ts" setup>
import { notification } from '@vc-shell/framework';
import { VcButton } from '@vc-shell/framework';

const showDefault = () => {
  notification('This is a default notification');
};

const showSuccess = () => {
  notification.success('Operation completed successfully!');
};

const showError = () => {
  notification.error('An error occurred while processing your request.');
};

const showWarning = () => {
  notification.warning('Please review your information before proceeding.');
};
</script>
```

### Persistent Notification (No Auto-dismiss)

```vue
<template>
  <VcButton @click="showPersistent">Show Persistent Notification</VcButton>
</template>

<script lang="ts" setup>
import { notification } from '@vc-shell/framework';
import { VcButton } from '@vc-shell/framework';

const showPersistent = () => {
  notification('This notification will not disappear automatically.', {
    timeout: false,
  });
};
</script>
```

### Different Positions

```vue
<template>
  <div class="tw-grid tw-grid-cols-3 tw-gap-4">
    <VcButton @click="showTopLeft">Top Left</VcButton>
    <VcButton @click="showTopCenter">Top Center</VcButton>
    <VcButton @click="showTopRight">Top Right</VcButton>
    <VcButton @click="showBottomLeft">Bottom Left</VcButton>
    <VcButton @click="showBottomCenter">Bottom Center</VcButton>
    <VcButton @click="showBottomRight">Bottom Right</VcButton>
  </div>
</template>

<script lang="ts" setup>
import { notification } from '@vc-shell/framework';
import { VcButton } from '@vc-shell/framework';

const showTopLeft = () => {
  notification('Top Left Notification', { position: 'top-left' });
};

const showTopCenter = () => {
  notification('Top Center Notification', { position: 'top-center' });
};

const showTopRight = () => {
  notification('Top Right Notification', { position: 'top-right' });
};

const showBottomLeft = () => {
  notification('Bottom Left Notification', { position: 'bottom-left' });
};

const showBottomCenter = () => {
  notification('Bottom Center Notification', { position: 'bottom-center' });
};

const showBottomRight = () => {
  notification('Bottom Right Notification', { position: 'bottom-right' });
};
</script>
```

### Updating a Notification

```vue
<template>
  <div class="tw-space-y-4">
    <VcButton @click="showUpdateableNotification">Show Notification</VcButton>
    <VcButton @click="updateNotification" :disabled="!notificationId">
      Update Notification
    </VcButton>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { notification } from '@vc-shell/framework';
import { VcButton } from '@vc-shell/framework';

const notificationId = ref<string | number | null>(null);
let updateCount = 0;

const showUpdateableNotification = () => {
  notificationId.value = notification('This notification can be updated', {
    timeout: false,
  });
};

const updateNotification = () => {
  if (notificationId.value) {
    updateCount++;
    const type = updateCount % 3 === 0 
      ? 'warning' 
      : updateCount % 3 === 1 
        ? 'success' 
        : 'error';
    
    notification.update(notificationId.value, {
      content: `This notification has been updated ${updateCount} times`,
      type,
    });
  }
};
</script>
```

### Custom Component as Content

```vue
<template>
  <VcButton @click="showCustomNotification">
    Show Custom Notification
  </VcButton>
</template>

<script lang="ts" setup>
import { h, defineComponent } from 'vue';
import { notification } from '@vc-shell/framework';
import { VcButton } from '@vc-shell/framework';

const showCustomNotification = () => {
  // Create a custom component
  const CustomNotificationContent = defineComponent({
    setup() {
      const handleClick = () => {
        alert('Button in notification clicked!');
      };
      
      return () => h('div', [
        h('div', { class: 'tw-font-bold tw-mb-2' }, 'Custom Notification'),
        h('div', { class: 'tw-mb-2' }, 'This is a custom component inside a notification.'),
        h('button', {
          class: 'tw-bg-[var(--primary-500)] tw-text-white tw-px-3 tw-py-1 tw-rounded',
          onClick: handleClick
        }, 'Click me')
      ]);
    }
  });

  // Show notification with the custom component
  notification(CustomNotificationContent, {
    timeout: false,
  });
};
</script>
```

### Form Submission Feedback

```vue
<template>
  <VcForm @submit.prevent="submitForm">
    <VcInput
      v-model="email"
      label="Email Address"
      placeholder="Enter your email"
      required
      :error="!!emailError"
      :errorMessage="emailError"
    />
    
    <VcInput
      v-model="name"
      label="Full Name"
      placeholder="Enter your full name"
      required
      :error="!!nameError"
      :errorMessage="nameError"
    />
    
    <div class="tw-mt-4">
      <VcButton type="submit" variant="primary">Submit</VcButton>
    </div>
  </VcForm>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { notification } from '@vc-shell/framework';
import { VcForm, VcInput, VcButton } from '@vc-shell/framework';

const email = ref('');
const name = ref('');
const emailError = ref('');
const nameError = ref('');

const submitForm = () => {
  // Reset errors
  emailError.value = '';
  nameError.value = '';
  
  // Basic validation
  let isValid = true;
  
  if (!email.value) {
    emailError.value = 'Email is required';
    isValid = false;
  } else if (!/^\S+@\S+\.\S+$/.test(email.value)) {
    emailError.value = 'Please enter a valid email';
    isValid = false;
  }
  
  if (!name.value) {
    nameError.value = 'Name is required';
    isValid = false;
  }
  
  if (isValid) {
    // Simulate API call
    setTimeout(() => {
      // Show success notification
      notification.success('Form submitted successfully!');
      
      // Reset form
      email.value = '';
      name.value = '';
    }, 1000);
  } else {
    // Show error notification
    notification.error('Please fix the errors in the form.');
  }
};
</script>
```
