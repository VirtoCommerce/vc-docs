# API Reference

## VcBlade Component

The VcBlade API reference offers detailed information about the props, events, and slots available for the VcBlade component. The following sections provide a comprehensive overview of the VcBlade API.

### Props

| Props            | Default   | Description                                                                                                        |
| --------------- | --------- | ------------------------------------------------------------------------------------------------------------------ |
| `icon` {==String==} | undefined | The Font Awesome icon to display in the blade header.                                                              |
| `title` {==String==}| undefined | The title to display in the blade header.                                                                         |
| `subtitle` {==String==} | undefined | The subtitle to display in the blade header.                                                                  |
| `width` {==Number==} {==String==}   | "30%" | The minimum width of the blade in pixels or as a percentage.                                                   |
| `expanded` {==Boolean==}  | true | Handled by the `VcBladeNavigation` component, the state depends on the number of active blades. You can watch this value to perform actions, such as changing the table layout when two blades are active.
| `expandable` {==Boolean==} | true | Activates the ability to expand and collapse the component by default.                                         |
| `closable` {==Boolean==} | true | Determines whether the blade has a close button.                                                                 |
| `toolbarItems` {==IBladeToolbar[]==} | () => [] | An array of items to be displayed in the toolbar.                                                              |

### Events

| Event       | Description          |
| ----------- | -------------------- |
| `close`     | Close blade event.   |
| `expand`    | Expand blade event.  |
| `collapse`  | Collapse blade event. |

### Slots

| Slot        | Description                                            |
| ----------- | ------------------------------------------------------ |
| `default`   | Blade content.                                         |
| `action`    | Any component or data to display in the blade header. |

## useBladeNavigation Composable

### Properties

| Name                   | Description                                                             |
| -------------------------- | ----------------------------------------------------------------------- |
| `blades` {==IBladeContainer[]==} | An array containing opened blades with their index number.        |
| `workspaceOptions` {==Object==} | An object containing key-value pairs used as options for the workspace blade. |
| `workspaceParam` {==String==}  | A string containing the blade parameter used by the `param` prop in the workspace blade. |
| `bladesRefs` {==IBladeRef[]==} | Blade refs used to store opened blades. |
| `lastBladeData` {==BladeData==} | Last opened blade data storage. |
| `activeBlade` {==IBladeContainer==} | Blade on which the user is focused. |
| `bladesRefs` {==IBladeRef[]==} | Blade refs used to store opened blades. |

### Methods

#### `openBlade`

Opens a blade with the specified configuration.

* Type
    **openBlade**: ```<Blade extends ComponentPublicInstance = ComponentPublicInstance>({ blade, param, options, onOpen, onClose }: IBladeEvent<Blade>, isWorkspace = false) => void```

* Parameters

    | Name                                                                                                      | Description                                                        |
    | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
    | `blade` {==BladeConstructor<T>==}                                                                             | Blade component.                                                   |
    | `options` (optional)  {==ExtractedBladeOptions==}                                                             | Key-value pairs with blade options, extracted from the component.  |
    | `param` (optional)    {==String==}                                                                            | String with blade parameter.                                       |
    | `onOpen` (optional)   {==() => void==}                                                                        | Method called when the blade is opened.                            |
    | `onClose` (optional)  {==() => void==}                                                                        | Method called when the blade is closed.                            |

* Returns: `void`

#### `closeBlade`

Closes an opened blade or all opened blades.

* Type

    **closeBlade**: ```(index: number) => Promise<boolean>```

* Parameters

    | Name               | Description                                                  |
    | ---------------------- | ------------------------------------------------------------ |
    | `index` {==Number==}   | Id of the opened blade.                                      |


* Returns: `Promise<boolean>`. Returns `false` if closing the blade was prevented by the `onBeforeClose` method in the blade component.

#### `onParentCall`

Calls any function on the parent blade, if it has been exposed there.

* Type

    **onParentCall**: ```(index: number, args: IParentCallArgs) => void```

* Parameters

    | Name                       | Description                                                            |
    |---------------------------------|------------------------------------------------------------------------|
    | `index` {==number==}            | Index of the parent blade.                                             |
    | `args`  {==IParentCallArgs==}   | Object containing the method name, arguments, and an optional callback.|


* Returns: `void`

#### `resolveBlades`

Resolves blades from vue-router's navigation guard `to` param. Used to display blades after page reload or accessing via direct link. Returns a string containing the URL of the latest opened workspace.

* Type:

    **resolveBlades**: ```(to: RouteLocationNormalized) => string```

* Parameters

    | Name                             | Description               |
    |----------------------------------|---------------------------|
    | `to` {==RouteLocationNormalized==} | Vue router's route record |

* Returns: `string`

#### `resolveUnknownRoutes`

Resolves erroneous and unknown navigation routes. Used as a navigation hook for a Vue router.

* Type:

    **resolveUnknownRoutes**: ```(to: RouteLocationNormalized) => string```

* Parameters

    | Name                             | Description               |
    |----------------------------------|---------------------------|
    | `to` {==RouteLocationNormalized==} | Vue router's route record |

* Returns: `string`

#### `resolveLastBlade`

Resolves last opened blade on page reload or accessing via a direct link.

* Type:

    **resolveLastBlade**: ```(pages: BladePageComponent[]) => void```

* Parameters

    | Name                             | Description     |
    |----------------------------------|-----------------|
    | `pages` {==BladePageComponent[]==} | Array of blades |

* Returns: `void`

#### `resolveBladeByName`

Allows you to resolve a blade component using its registered name. Supports both runtime and regular blade components.

* Type:

    **resolveBladeByName**: ```(name: string) => BladeConstructor```

* Parameters

    | Name              | Description                                 |
    |-------------------|---------------------------------------------|
    | `name` {==String==} | Blade component name or ID in dynamic views |

* Returns: `BladeConstructor`

## Notifications

The `notification` method is used to display toast notifications.

Method signatures are as follows:

- `notification(content: string, options?: NotificationOptions): string | number;`
- `error(content: string, options?: NotificationOptions): string | number;`
- `warning(content: string, options?: NotificationOptions): string | number;`
- `success(content: string, options?: NotificationOptions): string | number;`
- `clearAll(): void;`
- `remove(notificationId?: number | string): void;`
- `update(notificationId: string | number, options: NotificationOptions): void;`

### NotificationOptions Interface

| Property                  | Description                                        |
| ------------------------- | -------------------------------------------------- |
| `limit` {==Number==}         | Limit the number of toasts displayed (default 3)  |
| `pauseOnHover` {==Boolean==} | Pause timeout on hover                             |
| `timeout` {==Number==} {==Boolean==} | Accept a duration in ms or false (default 3000) |
| `content` {==String==}       | Text to be displayed in toast                      |
| `notificationId` {==Number==} {==String==} | ID of toast notification                 |
| `type` {==NotificationType==} | Default value - 'default'                      |
| `onOpen` {==<T>(payload: T) => void==} | Method called when the toast is opened   |
| `onClose` {==<T>(payload: T) => void==} | Method called when the toast closes     |
| `payload` {==String==}{==Record<string,any>==} | Any string or object data used as an argument to the `onOpen` and `onClose` method |
| `updateId` {==String==} {==Number==} | ID of updated toast notification, used during an update |

## useNotifications Composable

### Properties

| Property                       | Description                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------- |
| `notifications` {==ComputedRef<PushNotification[]>==} | An array containing push notification objects received from the backend. |
| `moduleNotifications` {==ComputedRef<PushNotification[]>==} | A computed array of notifications that belong to a particular module, specified when initializing the `useNotifications` function with the `notifyType` argument. |

### Methods

#### `loadFromHistory`

Loads the saved history of notifications from the backend.

* Type

    **loadFromHistory**: `(take?: number): Promise<void>`

* Parameters

    | Property                                                    | Description                                                               |
    | ----------------------------------------------------------- | ------------------------------------------------------------------------- |
    | `take` (optional) {==Number==}                              | Number of notifications to load.                                          |

* Returns: `Promise<void>`

#### `addNotification`

An internal method used in an embedded `signalR` plugin that adds a received notification to the notifications array.

* Type

    **addNotification**: `(message: PushNotification): void`

* Properties

    | Property                                                    | Description                                                               |
    | ----------------------------------------------------------- | ------------------------------------------------------------------------- |
    | `message` {==PushNotification==}                            | Notification message.                                                     |

* Returns: `void`

#### `markAsRead`

Marks a particular notification as read.

* Type

    **markAsRead**: `(message: PushNotification): void`

* Properties

    | Property                                                    | Description                                                               |
    | ----------------------------------------------------------- | ------------------------------------------------------------------------- |
    | `message` {==PushNotification==}                            | Notification message.                                                     |


    * Return: `void`

* `markAllAsRead(): void` - marks all notifications as read in the notification dropdown.

* Returns: `void`

#### `markAllAsRead`

Marks all notifications as read.

* Type

    **markAllAsRead**: `(): void`

* Returns: `void`

## VcNotificationTemplate component

| Props  | Description                   |
| ----- | ----------------------------- |
| `color` | Icon circle color.         |
| `title` | Title of the notification. |
| `icon`  | Any icon from Font Awesome. |
