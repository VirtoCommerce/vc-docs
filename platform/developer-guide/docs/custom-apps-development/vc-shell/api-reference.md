# API Reference

The VcBlade API reference provides detailed information about the props, events, and slots available for the VcBlade component. The following sections outline the different aspects of the VcBlade API:

## VcBlade component

### Props

| Prop                                      | Default    | Description                                                                                                                    |
| ----------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `icon` ==String==                       | undefined  | Font Awesome icon to display in the blade header.                                                                              |
| `title` ==String==                      | undefined  | Title to display in the blade header.                                                                                          |
| `subtitle` ==String==                   | undefined  | Subtitle to display in the blade header.                                                                                       |
| `width` ==Number== ==String==         | "30%"      | The minimum width of the blade in pixels or as a percentage.                                                                   |
| `expanded` ==Boolean==                  | true       | Handled by the VcVladeNavigation component, the state depends<br>on the number of active blades. You can watch this value<br>to perform actions, such as changing the table layout when two blades are active.|
| `expandable` ==String==                 | true       | Activates the ability to expand and collapse the component by default.                                                         |
| `closable` ==String==                   | true       | Determines whether the blade has a close button.                                                                               |
| `toolbarItems`  ==IBladeToolbar[]==     | () => []   | An array of items to be displayed in the toolbar                                                                               |

### Events

| Event       | Description           |
| ----------- | --------------------- |
| `close`     | Close blade event.    |
| `expand`    | Expand blade event.   |
| `collapse`  | Collapse blade event. |

### Slots

| Slot        | Description                                                 |
| ----------- | ----------------------------------------------------------- |
| `default`   | Blade content.                                              |
| `action`    | Any component or data to display in blade header.           |

## useBladeNavigation composable

### Properties

| Name                                                                              | Description                                                                                     |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `blades` `ComputedRef<BladeRouteRecordLocationNormalized \| undefined>`         |  An array containing active blade components on given route.                                    |
| `currentBladeNavigationData` `ComputedRef<BladeVNode["props"]["navigation"]>`   |  An object containing the current blade navigation data.                                        |

### Methods

#### `openBlade`

Opens a blade with the specified configuration.

* Type

    ```**openBlade**: ```<Blade extends Component>( { blade, param, options, onOpen, onClose }: IBladeEvent<Blade>,
    isWorkspace?: boolean ) => Promise<void | NavigationFailure>```

* Parameters

    | Name                                           	| Description                                                       	|
    |------------------------------------------------	|-------------------------------------------------------------------	|
    | `blade` ==BladeConstructor==                   	| Blade component.                                                  	|
    | `options` (optional) ==ExtractedBladeOptions== 	| Key-value pairs with blade options, extracted from the component. 	|
    | `param` (optional) ==String==                  	| String with blade parameter.                                      	|
    | `onOpen` (optional) ==() => void==             	| Method called when the blade is opened.                           	|
    | `onClose` (optional) ==() => void==            	| Method called when the blade is closed.                           	|

* Returns: Promise<void | NavigationFailure>

#### `closeBlade`

Closes an opened blade or all opened blades.

* Type

    ```**closeBlade**: ```(index: number) => Promise<boolean>```

* Parameters

    | Name                                    	| Description                           	|
    |-----------------------------------------	|---------------------------------------	|
    | `index` ==Number==                      	| Id of the opened blade.               	|

* Returns: ```Promise<boolean>```

#### `onBeforeClose`

Allows you to perform actions before closing a blade. If the method returns `false`, the blade will not be closed.

* Type

    ```**onBeforeClose**: ```(callback: () => Promise<boolean | undefined>) => void```

* Parameters

    | Name                                    	| Description                           	|
    |-----------------------------------------	|---------------------------------------	|
    | `callback` ==() => Promise<boolean | undefined>==                      	| Callback function.               	|

* Returns: `void`

#### `onParentCall`

Calls any function on the parent blade, if it has been exposed there.

* Type

    **onParentCall**: ```(parentExposedMethods: Record<string, any>, args: IParentCallArgs) => void```

* Parameters

    | Name                       | Description                                                            |
    |---------------------------------|------------------------------------------------------------------------|
    | `parentExposedMethods` ==Record<string, any>== | Object containing the parent blade's exposed methods. |
    | `args`  ==IParentCallArgs==   | Object containing the method name, arguments, and an optional callback.|


* Returns: `void`

#### `routeResolver`

Resolves and generates routes after page reload or accessing via direct link. Used only in Vue router configuration:

```typescript
const routes = [
 ...,
 {
    path: "/:pathMatch(.*)*",
    component: App,
    beforeEnter: async (to) => {
      const { routeResolver } = useBladeNavigation();
      return routeResolver(to);
    },
  },
]
```

* Type:

    **routeResolver**: ```(to: RouteLocationNormalized) => Promise<{
    name: RouteRecordName | undefined;
    params: RouteParams;
} | undefined> | undefined```

* Parameters

    | Name                             | Description               |
    |----------------------------------|---------------------------|
    | `to` ==RouteLocationNormalized== | Vue router's route record |

* Returns: `Promise<{
    name: RouteRecordName | undefined;
    params: RouteParams;
} | undefined> | undefined`

#### `resolveBladeByName`

Allows you to resolve a blade component using its registered name. Supports both runtime and regular blade components.

* Type:

    **resolveBladeByName**: ```(name: string) => BladeInstanceConstructor```

* Parameters

    | Name              | Description                                 |
    |-------------------|---------------------------------------------|
    | `name` ==String== | Blade component name or ID in dynamic views |

* Returns: `BladeInstanceConstructor`

#### `getNavigationQuery`

Returns the URL query for selected blade.

* Type:

    **getNavigationQuery**: ```() => Record<string, string | number> | undefined```

* Returns: `Record<string, string | number> | undefined`

#### `setNavigationQuery`

Sets the URL query for selected blade.

* Type:

    **setNavigationQuery**: ```(query: Record<string, string | number>) => void```

* Returns: `void`

## Notifications

The `notification` method is used to display toast notifications.

Method signatures are as follows:

* `notification(content: string, options?: NotificationOptions): string | number;`
* `error(content: string, options?: NotificationOptions): string | number;`
* `warning(content: string, options?: NotificationOptions): string | number;`
* `success(content: string, options?: NotificationOptions): string | number;`
* `clearAll(): void;`
* `remove(notificationId?: number | string): void;`
* `update(notificationId: string | number, options: NotificationOptions): void;`

### NotificationOptions Interface

| Property                              | Description                                        |
| ------------------------------------- | -------------------------------------------------- |
| `limit` ==Number==                  | Limit the number of toasts displayed (default 3).  |
| `pauseOnHover` ==Boolean==          | Pause timeout on hover.                             |
| `timeout` ==Number== ==Boolean==  | Accept a duration in ms or false (default 3000). |
| `content` ==String==                | Text to be displayed in toast.                      |
| `notificationId` ==Number== ==String== | ID of toast notification.                 |
| `type` ==NotificationType==         | Default value - 'default'.                      |
| `onOpen` ==<T>(payload: T) => void==| Method called when the toast is opened.   |
| `onClose` ==<T>(payload: T) => void==| Method called when the toast closes.     |
| `payload` ==String====Record<string,any>== | Any string or object data used as an argument to the `onOpen` and `onClose` method. |
| `updateId` ==String== ==Number==  | ID of updated toast notification, used during an update. |

## useNotifications Composable

### Properties

| Property                                                    | Description                                                               |
| ----------------------------------------------------------- | ------------------------------------------------------------------------- |
| `notifications` ==ComputedRef<PushNotification[]>==       | An array containing push notification objects received from the backend.  |
| `moduleNotifications` ==ComputedRef<PushNotification[]>== | A computed array of notifications that belong to a particular module,<br>specified when initializing the useNotifications function with the notifyType argument. |


### Methods

#### `loadFromHistory`

Loads the saved notifications history from the backend.

* Type

    `loadFromHistory(take?: number): Promise<void>`

* Parameters

    | Property                                                    | Description                                                               |
    | ----------------------------------------------------------- | ------------------------------------------------------------------------- |
    | `take` (optional) ==Number==                              | Number of notifications to load.                                          |


* Returns: `Promise<void>`

#### `addNotification`

An internal method used in an embedded `signalR` plugin that adds a received notification to the notifications array.

* Type

    `addNotification(message: PushNotification): void`

* Parameters

    | Property                                                    | Description                                                               |
    | ----------------------------------------------------------- | ------------------------------------------------------------------------- |
    | `message` ==PushNotification==                            | Notification message.                                                     |

* Returns: `void`

#### `markAsRead`

Marks a particular notification as read.

* Type

    `markAsRead(message: PushNotification): void`

* Parameters

    | Property                                                    | Description                                                               |
    | ----------------------------------------------------------- | ------------------------------------------------------------------------- |
    | `message` ==PushNotification==                            | Notification message.                                                     |


* Returns: `void`

#### `markAllAsRead`

Marks all notifications as read.

* Type

    `markAllAsRead(): void`

* Returns: `void`

## VcNotificationTemplate Component

| Prop    | Description                  |
| ------- | ---------------------------- |
| `color` | Icon circle color.           |
| `title` | Title of the notification.   |
| `icon`  | Any icon from Font Awesome.  |
