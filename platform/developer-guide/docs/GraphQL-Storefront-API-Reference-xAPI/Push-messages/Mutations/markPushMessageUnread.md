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

<div class="grid" markdown>

```graphql title="Mutation"
mutation markPushMessageUnread($command: InputMarkPushMessageUnreadType!) {
  markPushMessageUnread(command: $command)
}
```

```json title="Variables"
{
  "command": {
    "messageId": "80d92257-5286-4fe2-933c-e1280d16677f"
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../markPushMessageRead">← MarkPushMessageRead mutation</a>
    <a href="../markAllPushMessagesRead">MarkAllPushMessagesRead mutation →</a>
</div>
