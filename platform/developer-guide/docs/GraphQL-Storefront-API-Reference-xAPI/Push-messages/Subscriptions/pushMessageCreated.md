# pushMessageCreated ==~subscription~==

This subscription is used to receive real-time updates when a new push message is created.

## Possible returns

| Possible return                                       | Description                                             |
|-------------------------------------------------------|---------------------------------------------------------|
| [`PushMessageType`](../Objects/PushMessageType.md)    | The structure containing details of the newly created push message. |


## Example

<div class="grid" markdown>

```json title="Subscription"
subscription pushMessageCreated {
  pushMessageCreated {
    id
    shortMessage
    createdDate
    isRead
  }
}
```

```json title="Return"
{
"data": {
    "pushMessageCreated": {
      "id": "3",
      "shortMessage": "New notification",
      "createdDate": "2024-04-03T10:30:00Z",
      "isRead": false
    }
  }
}
```