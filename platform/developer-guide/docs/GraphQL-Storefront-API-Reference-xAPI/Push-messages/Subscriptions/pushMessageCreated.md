# pushMessageCreated ==~subscription~==

This subscription is used to receive real-time updates when a new push message is created.

## Possible returns

| Possible return                                       | Description                                             |
|-------------------------------------------------------|---------------------------------------------------------|
| [`PushMessageType`](../Objects/PushMessageType.md)    | The structure containing details of the newly created push message. |

=== "Subscription"

    ```graphql linenums="1"
    subscription pushMessageCreated {
      pushMessageCreated {
        id
        shortMessage
        createdDate
        isRead
      }
    }
    ```

=== "Response"

    ```graphql linenums="1"
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