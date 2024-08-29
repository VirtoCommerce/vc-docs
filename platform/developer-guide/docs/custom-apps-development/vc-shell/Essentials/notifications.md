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

### Update toast

To update a toast, update its content, type, and timeout. The basic usage looks like this:

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

### Duplicate prevention

To prevent duplicate toasts, set a `notificationId`:

```typescript linenums="1"
import { notification } from "@vc-shell/framework";

notification("My notification text!", {
  notificationId: "my-notification-id",
});
```

### Toast removal

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

To see a toast notification, watch the `moduleNotifications` and display the relevant notifications as toasts:

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

### Notification dropdown list

All globally registered notification templates are displayed in the notification dropdown list. To register a notification template, you need to create a component that will be used as a template and register it in the module initialization file.

#### Create custom notification templates

Each module can have a notification template that will be displayed in the notification dropdown. If no template is provided, the default template will be used.

1. Create a basic template using the `VcNotificationTemplate` component from `@vc-shell/framework`. You can pass your markup in Vue's default slot, or you can create your own template from scratch. Here's the basic usage with `VcNotificationTemplate`:

    ```html title="my-module-name/components/notifications/template.vue" linenums="1"
    <VcNotificationTemplate
      :color="notificationStyle.color"
      :title="notification.title"
      :icon="notificationStyle.icon"
      :notification="notification"
      @click="onClick"
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

    /**
     * Required to emit `notificationClick` event.
     */
    export interface Emits {
        (event: "notificationClick"): void;
    }

    defineProps<Props>();

    defineOptions({
      inheritAttrs: false,
      notifyType: "MyPushNotificationDomainEvent",
    });

    const emit = defineEmits<Emits>();

    const { openBlade, resolveBladeByName } = useBladeNavigation();

    const notificationStyle = {
      color: "#87b563",
      icon: "fas fa-percentage",
    };

    /**
     * Handles click on notification. Usually used to open a blade.
     */
    async function onClick() {
        if (props.notification.notifyType === "MyPushNotificationDomainEvent") {
            emit("notificationClick");
            await openBlade(
                {
                    blade: resolveBladeByName("ListBlade"),
                    param: props.notification.id,
                },
                true,
            );
        }
    }
    </script>
    ```

    !!! note
        Here we have a `notificationClick` event that is emitted when the notification is clicked. This event is required. If you don't emit it, the notification list will not be closed when the notification is clicked.

1. Make your template globally available. To do this, add it to the module initialization file when initializing the module:

    ```typescript title="my-module-name/index.ts" linenums="1"
    import * as pages from "./pages";
    import * as locales from "./locales";
    import * as notificationTemplates from "./components/notifications";
    import { createAppModule } from "@vc-shell/framework";

    export default createAppModule(pages, locales, notificationTemplates);

    export * from "./pages";
    export * from "./composables";
    ```