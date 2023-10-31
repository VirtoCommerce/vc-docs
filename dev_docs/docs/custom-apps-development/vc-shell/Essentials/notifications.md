# Notifications

An application can have two types of notifications:

1. **Toasts (Push Notifications):** These are used for short, immediate notifications, such as new push notifications or the results of certain actions.
2. **Notification Dropdown Lists:** This feature is used to display more detailed notifications in the top bar menu. These notifications include information like the notification name, time, and a description, often used for conveying the status of long-running tasks.

To start working with push notifications, import the `useNotifications` composable from `@vc-shell/framework`. This composable allows you to work with notifications in a specific module by specifying the `notifyType` as an identifier.

## Toasts

To display notifications as toasts, you can use the `notification` method imported from `@vc-shell/framework`. There are two options for displaying toast notifications:

=== "Option 1"

    This option provides a single method where you specify the type of notification through the options object:

    ```typescript linenums="1"

    import { notification } from "@vc-shell/framework";

    notification("My notification text!", {
        type: "default", // or one of success, error, warning
    });
    ```

=== "Option 2"

    This option offers separate methods for each notification type, making it more explicit and straightforward to display different types of toast notifications:

    ```typescript linenums="1"

    import { notification } from "@vc-shell/framework";

    notification("My default notification text!");
    notification.success("My success notification text!");
    notification.error("My error notification text!");
    notification.warning("My warning notification text!");
    ```

### Update Toast

When you need to update a toast, you can update its content, type, and timeout. The basic usage looks like this:

```typescript linenums="1"
import { ref } from "vue";
import { notification } from "@vc-shell/framework";

const notificationId = ref();

function showToast() {
  notificationId.value = notification("My notification text!", {
    timeout: false,
  });
}

function updateToast() {
  notification.update(notificationId.value, {
    content: "My updated notification text!",
    type: "error",
    timeout: 3000,
  });
}
```

### Duplicate Prevention

To prevent duplicate toasts, you can set a `notificationId`:

```typescript linenums="1"
import { notification } from "@vc-shell/framework";

notification("My notification text!", {
  notificationId: "my-notification-id",
});
```

### Toast Removing

You can remove all visible toasts or a specific toast:

=== "Remove all visible toasts"

    ```typescript linenums="1"
    import { notification } from "@vc-shell/framework";

    notification.clearAll();
    ```

=== "Remove a particular toast"

    ```typescript linenums="1"
    import { notification } from "@vc-shell/framework";

    const notificationId = ref();

    function showToast() {
      notificationId.value = notification("My notification text!");
    }

    function removeToast() {
      notification.remove(notificationId.value);
    }
    ```

## How to use notifications in modules

To use notifications in modules, you can leverage toast notifications and dropdown lists to provide user updates and alerts.

### Toasts

When displaying push notifications for a specific module, you need to pass an argument to the `useNotifications` method, specifying the type of push notification supported by this module:

```typescript linenums="1"
import { watch } from "vue";
import { useNotifications } from "@vc-shell/framework";

const { moduleNotifications, markAsRead } = useNotifications("YourNotificationType");
```

If you want to see a toast notification, you can watch the `moduleNotifications` and display the relevant notifications as toasts:

```typescript linenums="1"
watch(
  moduleNotifications,
  (newVal) => {
    newVal.forEach((message) => {
    // example of success notification type
      notification.success(message.title, {
        onClose() {
          markAsRead(message);
        },
      });
    });
  },
  { deep: true }
);
```

### Notification Dropdown List

To display your templates in a dropdown list, you need to pass all global templates to the `VcNotificationDropdown` component in the `App.vue` file. The `VcNotificationDropdown` component should be located in the toolbar, so you should pass an array of toolbar components to the `VcApp` component as props.

The most basic usage looks like this:

```typescript title="App.vue" linenums="1"

import { markRaw, computed } from 'vue';
import { toolbarComposer, notificationTemplatesSymbol, useNotifications, VcNotificationDropdown } from '@vc-shell/framework';

const { notifications, markAllAsRead } = useNotifications();
const pages = inject('pages'); // Globally available module pages of the application
const notificationTemplates = inject('notificationTemplates'); // Globally available templates

const toolbarItems = computed(() => toolbarComposer([
  {
      isAccent: notifications.value.some((item) => item.isNew), // Indicator of new unread notifications
      component: markRaw(VcNotificationDropdown), // VcNotificationDropdown component
      options: {
        title: "Notifications", // Dropdown button title
        notifications: notifications.value, // Notifications array
        templates: notificationTemplates, // Injected notification templates
        onOpen() {
          // When the dropdown is opened, all notifications are marked as read
          if (notifications.value.some((x) => x.isNew)) {
            markAllAsRead();
          }
        },
      },
    },
])
```

#### Creating Custom Notification Templates

Each module can have a notification template that will be displayed in the notification dropdown. If no template is provided, the default template will be used.

1. Create a basic template using the `VcNotificationTemplate` component from `@vc-shell/framework`. You can pass your markup in Vue's default slot, or you can create your own template from scratch. Here's the basic usage with `VcNotificationTemplate`:

    ```html title="my-module-name/components/notifications/template.vue" linenums="1"
    <VcNotificationTemplate
      :color="notificationStyle.color"
      :title="notification.title"
      :icon="notificationStyle.icon"
    >
      <!-- any content -->
    </VcNotificationTemplate>
    ```
    ```typescript linenums="1"
    <script lang="ts" setup>
    import { PushNotification } from "@vc-shell/framework";

    export interface Props {
      notification: PushNotification;
    }

    defineProps<Props>();

    defineOptions({
      inheritAttrs: false,
      notifyType: "MyPushNotificationDomainEvent",
    });

    const notificationStyle = {
      color: "#87b563",
      icon: "fas fa-percentage",
    };
    </script>
    ```

2. Make your template globally available. To do this, add it to the module initialization file when initializing the module:

    ```typescript title="my-module-name/index.ts" linenums="1"
    import * as pages from "./pages";
    import * as locales from "./locales";
    import * as notificationTemplates from "./components/notifications";
    import { createAppModule } from "@vc-shell/framework";

    export default createAppModule(pages, locales, notificationTemplates);

    export * from "./pages";
    export * from "./composables";
    ```

#### Performing Actions on Click

You have the ability to perform actions by clicking on these notifications. For example, you can open the blade to which the notification belongs. To do this:

1. Create a click handler in the module itself:

```typescript title="my-module-name/pages/<blade>.vue" linenums="1"
<script lang="ts" setup>
defineOptions({
  url: "/my-blade",
  scope: {
    notificationClick(notification: PushNotification) {
      if (notification.notifyType !== "MyPushNotificationDomainEvent") return;
      return {
        // Here, return the props that your blade accepts, like param or options object
        param: 'my-order-id',
      };
    },
  },
});
</script>
```

2. Add an async `onClick` method in the dropdown component initialization object in the `App.vue` file to handle this click:

```typescript title="App.vue" linenums="1"
const { openBlade } = useBladeNavigation();

const toolbarItems = computed(() => toolbarComposer([
  {
      // ...
      options: {
        // ...
        async onClick(notification: PushNotification) {
          if (notification) {
            for (const page of pages) {
              const notificationClickFn = page.scope?.notificationClick;
              if (notificationClickFn && typeof notificationClickFn === "function") {
                const bladeData = notificationClickFn(notification);

                if (bladeData) {
                  openBlade({
                    ...bladeData,
                    blade: page,
                  });

                      break;
                    }
                  }
                }
              }
            },
          },
        },
])
```
