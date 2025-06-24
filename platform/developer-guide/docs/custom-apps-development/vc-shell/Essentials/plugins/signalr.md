# SignalR Plugin

The SignalR Plugin provides real-time communication capabilities for VC-Shell applications. It integrates with Microsoft SignalR to enable server-initiated updates, push notifications, and real-time data synchronization between the server and client.

The SignalR Plugin establishes a persistent connection between the client and the VirtoCommerce Platform, allowing bidirectional communication. This is primarily used for receiving instant notifications and other real-time events. The actual handling and display of these notifications within the application are managed by the `useNotifications` composable.

For practical guidance on how to work with incoming push notifications, please refer to the [How-To: Working with Push Notifications using `useNotifications`](../Usage-Guides/working-with-push-notifications-using-usenotifications.md) guide.

## Features

- **Real-time Event Delivery**: Enables the client to receive events pushed by the server.
- **Automatic Reconnection**: The plugin automatically handles connection drops and attempts to reconnect.
- **Creator-Specific Event Filtering**: Allows filtering of system-wide events based on a `creator` identifier. This means an application can subscribe to specific categories of system events.
- **Authentication Integration**: The connection lifecycle is automatically managed based on the user's authentication state.

## Setup

The SignalR Plugin is automatically registered and configured when you use the `VcShellFramework`. The primary configuration option you might set is the `creator` identifier. This identifier is used by the plugin to filter incoming "System Events" (`SendSystemEvents`). Your application will only process system events where the `creator` field in the event message matches the `creator` value configured here.

```typescript
// Example: main.ts
import { createApp } from 'vue';
import VcShellFramework from '@vc-shell/framework';
import App from './App.vue';

const app = createApp(App);

app.use(VcShellFramework, {
  router,
  signalR: {
    // The 'creator' your application instance should listen to for SendSystemEvents.
    // This should match the 'creator' field of the PushNotification messages you expect to receive.
    // For example, if a backend service sends system events with creator: 'order-processing-alerts',
    // then you would set creator: 'order-processing-alerts' here to receive them.
    creator: 'yourSpecificEventSourceIdentifier' 
  }
  // Other options...
});
```
If the `creator` is not specified or does not match any incoming system events, your application instance might not receive or process those specific system-wide notifications. General notifications (sent via the "Send" method by SignalR) are not typically filtered by this `creator` value on the client-side plugin.

## Notification handling flow

1.  The SignalR plugin establishes and maintains a connection to the `/pushNotificationHub`.
1.  When the server sends a message, it can be a general notification (typically via a SignalR method like `Send`) or a system event (typically via `SendSystemEvents`).
1.  For messages received via `SendSystemEvents`:
    *   The plugin checks if a `creator` was configured during setup.
    *   If configured, it compares this `creator` with the `creator` field in the incoming `PushNotification` message.
    *   The message is processed further by this application instance only if the `creator` values match (or if no `creator` was configured for filtering on the client).
1.  General notifications (not `SendSystemEvents`) are typically processed directly.
1.  Received and appropriately filtered messages are then passed to the `useNotifications` composable (specifically, its `addNotification` function).
1.  The `useNotifications` system then handles the display of these notifications as toasts or in the notification center, according to its configuration and any custom templates. (See the [How-To guide on `useNotifications`](../Usage-Guides/working-with-push-notifications-using-usenotifications.md) for details).

Developers typically do not need to interact directly with SignalR connection events (`connection.on(...)`) for standard notification handling, as this is abstracted by `useNotifications`.

## Push Notification Structure

Incoming push notifications are expected to have the following `PushNotification` structure. This is important when you are interpreting the data within notifications handled by `useNotifications` or when creating custom notification templates.

```typescript
interface PushNotification {
  id?: string;          // Optional unique ID for the notification
  title: string;       // Notification title
  message?: string;     // Main content/description of the notification (often used instead of description)
  description?: string; // Optional: Alternative or additional description
  createdDate?: string; // Optional: Timestamp of creation
  creator?: string;     // Optional: The source/creator of the notification. 
                        // For SendSystemEvents, this is used for client-side filtering based on the 'creator' in SignalR setup.
  notifyType?: string;  // Optional: Type like 'info', 'warning', 'error', 'success'. 
                        // Can be used by useNotifications for styling or by custom templates.
  // Other custom data properties can be included as needed
  [key: string]: any; 
}
```

## Connection management

The SignalR Plugin automatically manages the connection lifecycle:
-   It attempts to connect when an authenticated user session starts.
-   It disconnects when the user logs out.
-   It handles automatic reconnections in case of temporary network issues.

You generally do not need to manually start or stop the SignalR connection.

## Best practices

* **Specific `creator` for system events**: If your application needs to listen to specific categories of system-wide events (those sent via `SendSystemEvents`), ensure the `creator` specified in the `VcShellFramework` setup matches the `creator` identifier used in those event messages from the server. This ensures correct filtering.
* **Rely on `useNotifications`**: For handling the logic and display of incoming notifications, use the `useNotifications` composable as described in its [How-To guide](../Usage-Guides/working-with-push-notifications-using-usenotifications.md). Avoid direct manipulation of the SignalR connection for this purpose.
* **Understand `PushNotification` Structure**: Familiarize yourself with the `PushNotification` interface to correctly interpret notification data, especially the role of the `creator` field for system events.
* **Server-Side Logic**: Remember that SignalR is a transport mechanism. The logic for *what* to send, *when*, and with which `creator` identifier (for system events) resides on the server (VirtoCommerce Platform).

## Related resources

-   [How-To: Working with Push Notifications using `useNotifications`](../Usage-Guides/working-with-push-notifications-using-usenotifications.md): The primary guide for handling notifications in your application.
-   [useNotifications Composable](../composables/useNotifications.md): API reference for the notifications composable.
-   [Microsoft SignalR Documentation](https://docs.microsoft.com/en-us/aspnet/core/signalr/introduction): For a deeper understanding of the underlying SignalR technology.
