# markPushMessageUnread ==~mutation~==

This mutation marks a specific push message as unread.

## Arguments

The [InputMarkPushMessageUnreadType!](../Objects/InputMarkPushMessageUnreadType.md) is used for a command to mark a push message as unread.

| Field                     | Description                                      |
|---------------------------|--------------------------------------------------|
| `messageId` ==String!==   | The Id of the push message to be marked as unread. |

## Possible returns

| Possible return | Description                                                                               |
|-----------------|-------------------------------------------------------------------------------------------|
| `Boolean`       | Indicates whether the operation of marking the push message as unread was successful or not.|


## Example

```graphql linenums="1"
mutation markPushMessageUnread($command: InputMarkPushMessageUnreadType!) {
markPushMessageUnread(command: $command)
}
```
