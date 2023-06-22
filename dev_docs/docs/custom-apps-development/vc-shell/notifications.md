# Notifications

An application can have two types of notifications:

* Toasts (push). They are used for short notifications, such as new push notification or result of some action.
* A list of notifications in the top bar menu (dropdown). It is used to display detailed notifications with their name, time, and description e.g. status of long running tasks.

To start working with push notifications, import `useNotifications` composable from @vc-shell/framework.

`useNotifications` has one argument `notifyType?: string | string[]`, which is an identifier for the type of notifications displayed in a particular module.

## Toasts (push)

To display notifications as a toast, there is a notification method imported from @vc-shell/framework.

There are two options for displaying the type of toast:

=== "Option 1"

    Provides a single method where you specify the type of the notification through the options object:

    ```typescript linenums="1"

    import { notification } from "@vc-shell/framework";

    notification("My notification text!", {
      type: "default", // or one of success, error, warning
    });
    ```

=== "Option 2"

    Offers separate methods for each notification type, making it more explicit and straightforward to display different types of toast notifications.

    ```typescript linenums="1"

    import { notification } from "@vc-shell/framework";

    notification("My default notification text!");
    notification.success("My success notification text!");
    notification.error("My error notification text!");
    notification.warning("My warning notification text!");
    ```

### Update toast

When you update toast, all options and content are inherited.

The most basic usage looks like this:

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

To prevent duplicate toasts, set a `notificationId`.

```typescript linenums="1"
import { notification } from "@vc-shell/framework";

notification("My notification text!", {
  notificationId: "my-notification-id",
});
```

### Toast removing

=== "Remove all visible toasts"

    ```typescript linenums="1"
    import { notification } from "@vc-shell/framework";

    notification.clearAll();
    ```

=== "Remove particular toast"

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



### Toasts (push notifications)

If you want to display push notifications for a specific module, when initializing the `useNotifications` method, you need to pass an argument to it, which is the type of push notification supported by this module.

`moduleNotifications` - array of notifications for a specific module.

The most basic usage looks like this:

```typescript linenums="1"
import { watch } from "vue";
import { useNotifications } from "@vc-shell/framework";

const { moduleNotifications, markAsRead } = useNotifications("YourNotificationType");
```

And if you want to see a toast thereof:

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

### Dropdown list

To display your template in a dropdown list, you need to pass all global templates to the `VcNotificationDropdown` component in **App.vue** file. Since this component must be located in the toolbar, you should pass an array of toolbar components to `VcApp` component as props.

The most basic usage looks like this:

```typescript title="App.vue" linenums="1"

import { markRaw, computed } from 'vue';
import { toolbarComposer, notificationTemplatesSymbol, useNotifications, VcNotificationDropdown } from '@vc-shell/framework';

const { notifications, markAllAsRead } = useNotifications();
const pages = inject('pages'); // injected globally available module pages of application
const notificationTemplates = inject('notificationTemplates'); // injected globally available templates

const toolbarItems = computed(() => toolbarComposer([
  {
      isAccent: notifications.value.some((item) => item.isNew), // Indicator of new unread notifications
      component: markRaw(VcNotificationDropdown), // VcNotificationDropdown component
      options: {
        title: "Notifications", // dropdown button title
        notifications: notifications.value, // notifications array
        templates: notificationTemplates, // injected notification templates
        onOpen() {
          // When dropdown is opened, all notifications are marked as read
          if (notifications.value.some((x) => x.isNew)) {
            markAllAsRead();
          }
        },
      },
    },
])
```

#### Create custom notification template

Each module can have notification template that will be displayed in the notification dropdown. If no template is provided, the default will be used.

Notification template should be stored in the particular module in the **<my-module-name>/components/notifications** folder.

1. Create basic template using `VcNotificationTemplate` component from @vc-shell/framework, to which you can pass your markup in Vue's default slot, or you can create your own template from scratch. The most basic usage with `VcNotificationTemplate` looks like this:

    ```html title="<my-module-name>/ components/ notifications/ <template>.vue" linenums="1"
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

1. Make your template globally available. To do this, when initializing the module, you should add it to the module initialization file:

    ```typescript title="<my-module-name>/index.ts" linenums="1"

    import * as pages from "./pages";
    import * as locales from "./locales";
    import * as notificationTemplates from "./components/notifications";
    import { createAppModule } from "@vc-shell/framework";

    export default createAppModule(pages, locales, notificationTemplates);

    export * from "./pages";
    export * from "./composables";
    ```

#### Performing actions on click

You also have the ability to perform any actions by clicking on these notifications, for example, it is possible to open the blade to which this notification belongs. To do this:

1. Make a click handler in the module itself:

    ```typescript title="<my-module-name>/pages/<blade>.vue" linenums="1"

    <script lang="ts" setup>
    defineOptions({
      url: "/my-blade",
      scope: {
        notificationClick(notification: PushNotification) {
          if (notification.notifyType !== "MyPushNotificationDomainEvent") return;
          return {
            // here you should return props that your blade accepts like param or options object
            param: 'my-order-id',
          };
        },
      },
    });
    </script>
    ```

2. Add async `onClick` method in the dropdown component initialization object in the **App.vue** file to handle this click:

    ```typescript title="App.vue" linenums="1"

    const { openBlade } = useBladeNavigation();

    const toolbarItems = computed(() => toolbarComposer([
      {
          ...
          options: {
            ...
            /**
            * notification click handler
            */
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
