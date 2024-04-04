# PushMessagesResponseType ==~object~==

The `PushMessagesResponseType` defines the structure of the response containing push messages.

## Fields

| Field                                                             | Description                                            |
|-------------------------------------------------------------------|--------------------------------------------------------|
| `unreadCount` ==Int!==                                            | The count of unread push messages.                     |
| `items` [==[PushMessageType!]!==](../Objects/PushMessageType.md)  | An array containing individual push messages.          |

