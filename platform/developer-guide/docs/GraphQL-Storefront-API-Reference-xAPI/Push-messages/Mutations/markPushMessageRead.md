# markPushMessageRead ==~mutation~==

This mutation marks a specific push message as read.

## Arguments

The [InputMarkPushMessageReadType!](../Objects/InputMarkPushMessageReadType.md) is used for a command to mark a push message as read.

| Field                     | Description                                      |
|---------------------------|--------------------------------------------------|
| `messageId` ==String!==   | The Id of the push message to be marked as read. |

## Possible returns

| Possible return | Description                                                                               |
|-----------------|-------------------------------------------------------------------------------------------|
| `Boolean`       | Indicates whether the operation of marking the push message as read was successful or not.|



## Example

<div class="grid" markdown>

```json title="Mutation"
mutation markPushMessageRead($command: InputMarkPushMessageReadType!) {
  markPushMessageRead(command: $command)
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