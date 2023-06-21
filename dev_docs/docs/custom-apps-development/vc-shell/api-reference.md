# API reference

The VcBlade API reference provides detailed information about the props, events, and slots available for the VcBlade component. The following sections outline the different aspects of the VcBlade API:

* Props

    | Prop                                      | Default    | Description                                                                                                                    |
    | ----------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------ |
    | `icon` {==String==}                       | undefined  | Font Awesome icon to display in the blade header.                                                                              |
    | `title` {==String==}                      | undefined  | Title to display in the blade header.                                                                                          |
    | `subtitle` {==String==}                   | undefined  | Subtitle to display in the blade header.                                                                                       |
    | `width` {==Number==}/{==String==}         | "30%"      | The minimum width of the blade in pixels or as a percentage.                                                                   |
    | `expanded` {==Boolean==}                  | true       | Handled by the VcVladeNavigation component, the state depends on the number of active blades. You can watch this value to perform actions, such as changing the table layout when two blades are active.|
    | `expandable` {==String==}                 | true       | Activates the ability to expand and collapse the component by default.                                                         |
    | `closable` {==String==}                   | true       | Determines whether the blade has a close button.                                                                               |
    | `toolbarItems`  {==IBladeToolbar[]==}     | () => []   | An array of items to be displayed in the toolbar                                                                               |

* Events

    | Event       | Description           |
    | ----------- | --------------------- |
    | `close`     | Close blade event.    |
    | `expand`    | Expand blade event.   |
    | `collapse`  | Collapse blade event. |

* Slots

    | Slot        | Description                                                 |
    | ----------- | ----------------------------------------------------------- |
    | `default`   | Blade content.                                              |
    | `action`    | Any component or data to display in blade header.           |

## useBladeNavigation composable API reference

### Properties

| Property                                       | Description                                                                                     |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `blades` {==IBladeContainer[]==}               | An array containing opened blades with their index number.                                      |
| `workspaceOptions` {==Record<string,unknown>==}| An object containing key-value pairs used as options for the workspace blade.                   |
| `workspaceParam` {==String==}                  | A string containing blade parameter used by param prop in the workspace blade.                  |
| `bladesRefs` {==IBladeRef[]==}                 | Blades refs used to store opened blades.                                                        |


### Methods

* ```openBlade: <Blade extends ComponentPublicInstance = ComponentPublicInstance>({ blade, param, options, onOpen, onClose }: IBladeEvent<Blade>, isWorkspace = false) => void``` - opens a blade with the specified configuration.

    * Parameters

        | Property                                                                                                      | Description                                                        |
        | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
        | `blade` {==BladeConstructor<T>==}                                                                             | Blade component.                                                   |
        | `options` (optional)  {==ExtractedBladeOptions<InstanceType<BladeConstructor<T>>["$props"], "options">==}     | Key-value pairs with blade options, extracted from the component.  |
        | `param` (optional)    {==String==}                                                                            | String with blade parameter.                                       |
        | `onOpen` (optional)   {==() => void==}                                                                        | Method called when the blade is opened.                            |
        | `onClose` (optional)  {==() => void==}                                                                        | Method called when the blade is closed.                            |

    * Return: `void`

* ```closeBlade: (index: number) => Promise<boolean>``` - closes an opened blade or all opened blades.

    * Parameters

        | Property               | Description                                                  |
        | ---------------------- | ------------------------------------------------------------ |
        | `index` {==Number==}   | Id of the opened blade.                                      |


    * Return: `Promise<boolean>`. Returns `false` if closing the blade was prevented by the `onBeforeClose` method in the blade component.

* ```onParentCall: (index: number, args: IParentCallArgs) => void``` - calls any function on the parent blade, if it has been exposed there.

    * Parameters

        | Parameter                       | Description                                                            |
        |---------------------------------|------------------------------------------------------------------------|
        | `index` {==number==}            | Index of the parent blade.                                             |
        | `args`  {==IParentCallArgs==}   | Object containing the method name, arguments, and an optional callback.|


    * Return: `void`

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

### NotificationOptions interface

| Property                                  | Description                                              |
| ----------------------------------------- | -------------------------------------------------------- |
| limit {==Number==}                        | Limit the number of toasts displayed (default 3)         |
| pauseOnHover {==Boolean==}                | Pause timeout on hover                                   |
| timeout {==Number {==Boolean==}           | Accept a duration in ms or false (default 3000)          |
| content {==String==}                      | Text to be displayed in toast                            |
| notificationId {==Number==}/ {==String==} | ID of toast notification                                 |
| type {==NotificationType==}               | Default value - 'default'                                |
| onOpen {==<T>(payload: T) => void==}      | Method that is called when the toast is opened           |
| onClose {==<T>(payload: T) => void==}     | Method that is called when the toast closes              |
| payload {==String {==Record<string, any>==}| Any string or object data that will be used as an argument to the onOpen and onClose method |
| updateId {==String {==Number==}           | ID of updated toast notification. Used during update     |


## useNotifications composable API reference

### Properties

| Property                                                    | Description                                                               |
| ----------------------------------------------------------- | ------------------------------------------------------------------------- |
| `notifications` {==ComputedRef<PushNotification[]>==}       | An array containing push notification objects received from the backend.  |
| `moduleNotifications` {==ComputedRef<PushNotification[]>==} | A computed array of notifications that belong to a particular module, specified when initializing the useNotifications function with the notifyType argument. |


### Methods

* `loadFromHistory(take?: number): Promise<void>` - loads the saved history of notifications from the backend.

    * Parameters

        | Property                                                    | Description                                                               |
        | ----------------------------------------------------------- | ------------------------------------------------------------------------- |
        | `take` (optional) {==Number==}                              | Number of notifications to load.                                          |

    * Return: `Promise<void>`

* `addNotification(message: PushNotification): void` - an internal method used in an embedded signalR plugin that adds a received notification to the notifications array.

    * Parameters

        | Property                                                    | Description                                                               |
        | ----------------------------------------------------------- | ------------------------------------------------------------------------- |
        | `message` {==PushNotification==}                            | Notification message.                                                     |

    * Return: `void`

* `markAsRead(message: PushNotification): void` - marks a particular notification as read.

    * Parameters

        | Property                                                    | Description                                                               |
        | ----------------------------------------------------------- | ------------------------------------------------------------------------- |
        | `message` {==PushNotification==}                            | Notification message.                                                     |


    * Return: `void`

* `markAllAsRead(): void` - marks all notifications as read in the notification dropdown.

    * Returns: `void`

## VcNotificationTemplate component


| Prop  | Description                 |
| ----- | --------------------------- |
| color | Icon circle color           |
| title | Title of the notification   |
| icon  | Any icon from Font Awesome  |
