# useNotifications Composable

The `useNotifications` composable provides the primary API for interacting with the push notification system within the VC-Shell framework. It allows components to subscribe to specific types of notifications to perform actions, load notification history, and manage notification states.

The `useNotifications` composable is a key utility for handling real-time notifications. It enables components to:

- Register as subscribers for specific notification types to execute custom logic.
- Access the complete list of notifications (e.g., for display in a global notification center like `notification-dropdown.vue`).
- Load notification history from the backend.
- Programmatically add new notifications or mark existing ones as read.

It's important to distinguish between *handling* a notification (performing an action when it arrives) and *displaying* a notification. While `useNotifications` helps with both, the visual representation of notifications in shared components like `notification-dropdown.vue` is typically customized through a separate template registration mechanism.

## API reference

### Parameters

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `notifyType` | `string \| string[]` | Optional. Specifies the type(s) of notifications the component is interested in for *handling* (executing logic). If omitted, the composable provides access to all notifications but won't filter by type for `moduleNotifications` or `setNotificationHandler`. |

### Return value

The `useNotifications` composable returns an object with the following properties and methods:

```typescript
interface INotifications {
  readonly notifications: ComputedRef<PushNotification[]>;  // All notifications, ordered by creation date (descending)
  readonly moduleNotifications: ComputedRef<PushNotification[]>;  // Notifications of the specified type(s) for local handling
  loadFromHistory(take?: number): Promise<void>;  // Load notifications history
  addNotification(message: PushNotification): void;  // Add a new notification locally
  markAsRead(message: PushNotification): void;  // Mark a notification as read (updates backend)
  markAllAsRead(): Promise<void>;  // Mark all notifications as read (updates backend)
  setNotificationHandler(handler: (notification: PushNotification) => void): void;  // Set a handler function for new notifications of the specified type(s)
}
```

### Methods

#### loadFromHistory

Loads the saved notifications history from the backend.

```typescript
loadFromHistory(take?: number): Promise<void>
```

- `take`: Optional. Number of notifications to load (default: 10).

#### addNotification

Adds a new notification to the local notification list. This is primarily for client-side generated notifications; server-sent notifications are typically added via SignalR.

```typescript
addNotification(message: PushNotification): void
```

- `message`: The notification object to add.

#### markAsRead

Marks a specific notification as read. This typically involves an API call to update the notification's state on the backend.

```typescript
markAsRead(message: PushNotification): void
```

- `message`: The notification to mark as read.

#### markAllAsRead

Marks all notifications as read. This also typically involves an API call.

```typescript
markAllAsRead(): Promise<void>
```

#### setNotificationHandler

Sets a handler function that will be called when a new notification of the specified `notifyType`(s) (provided during composable initialization) is received. This is the primary way to react to specific notifications within a component.

```typescript
setNotificationHandler(handler: (notification: PushNotification) => void): void
```

- `handler`: Function to call when a new relevant notification is received.

### Properties

#### notifications

A computed reference to an array of all notifications, ordered by creation date in descending order. This is useful for displaying a global list of notifications.

```typescript
notifications: ComputedRef<PushNotification[]>
```

#### moduleNotifications

A computed reference to an array of notifications that match the `notifyType`(s) specified when the composable was initialized. This is useful for components that only care about a subset of notifications for their internal logic.

```typescript
moduleNotifications: ComputedRef<PushNotification[]>
```

## Basic usage

### Global notification access
```typescript
const { notifications, markAllAsRead } = useNotifications();
```

### Type-specific notification handling
```typescript
const { setNotificationHandler } = useNotifications('OrderCreated');

    setNotificationHandler((notification) => {
  // Handle OrderCreated notifications
});
```

### Multiple notification types
```typescript
const { setNotificationHandler } = useNotifications(['OrderCreated', 'OrderUpdated']);
    
    setNotificationHandler((notification) => {
      switch (notification.notifyType) {
    case 'OrderCreated':
      // Handle order creation
          break;
    case 'OrderUpdated':
      // Handle order update
          break;
      }
    });
```

## Best practices

* **Scoped handling**: When using `notifyType` and `setNotificationHandler` within a component, ensure the logic is relevant to that component's scope. Global display concerns are handled separately via template registration.
* **Cleanup**: The composable handles its own internal cleanup when the component using it is unmounted. Ensure any custom logic (e.g., event listeners, timers started in handlers) is also cleaned up.
* **Error handling for API calls**: Wrap `loadFromHistory()` and `markAllAsRead()` in try/catch blocks or use an appropriate error handling strategy for API calls.
* **Debounce handlers**: If your notification handler performs expensive operations, consider debouncing it to avoid performance issues, especially if multiple notifications can arrive in quick succession.
* **Idempotency**: Design notification handlers to be idempotent if possible, as notifications could, in some rare network conditions, be delivered more than once.

## Related resources

- [Working with Push Notifications using useNotifications](../Usage-Guides/working-with-push-notifications-using-usenotifications.md) - Comprehensive guide with practical examples
- [Customizing Notifications](../Usage-Guides/customizing-notifications.md) - Guide on how to create and register custom templates for notifications
- [SignalR Plugin](/framework/core/plugins/signalR/index.ts) - The underlying plugin used for real-time communication and receiving notifications from the server
