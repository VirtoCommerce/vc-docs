# pushMessages ==~query~==

This query is used to retrieve push messages, including the unread count and the list of messages.

## Arguments

| Argument              | Description                                                                        |
|-----------------------|------------------------------------------------------------------------------------|
| `after` ==String==    | The cursor to fetch messages after a specific point.                               |
| `first` ==Int==       | The number of messages to retrieve.                                                |
| `keyword` ==String==  | A keyword to filter the messages.                                                  |
| `sort` ==String==        | The sorting criteria for the messages.                                          |
| `unreadOnly` ==Boolean== | Flag indicating whether to retrieve only unread messages.                       |
| `withHidden` ==Boolean== | Flag indicating whether to include hidden messages.                             |
| `cultureName` ==String== | A language to retrieve data in.                                                 |

## Possible returns

| Possible return                                                       | Description                                             |
|-----------------------------------------------------------------------|---------------------------------------------------------|
| [`PushMessageConnection`](../Objects/PushMessageConnection.md)      | The structured data for push messages response.         |


## Examples

=== "Query"

    ```graphql linenums="1"
    {
      pushMessages (unreadOnly: true, cultureName: "en-Us") {
        unreadCount
        items {
          id
          shortMessage
          createdDate
          isRead
        }
      }
    }
    ```

=== "Return"

    ```json linenums="1"
    {
      "data": {
        "pushMessages": {
          "unreadCount": 2,
          "items": [
            {
              "id": "1",
              "shortMessage": "New notification",
              "createdDate": "2024-04-02T08:15:00Z",
              "isRead": false
            },
            {
              "id": "2",
              "shortMessage": "Important update",
              "createdDate": "2024-04-01T16:30:00Z",
              "isRead": false
            }
          ]
        }
      }
    }
    ```