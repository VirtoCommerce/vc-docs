# markAllPushMessagesRead ==~mutation~==

This mutation marks all push messages as read.

## Possible returns

| Possible return | Description                                                                               |
|-----------------|-------------------------------------------------------------------------------------------|
| `Boolean`       | Indicates whether the operation of marking all push messages as read was successful or not.|


## Example

<div class="grid" markdown>

```graphql title="Mutation"
mutation MarkAllPushMessagesRead {
  markAllPushMessagesRead
}
```

```json title="Expected response"
{
  "data": {
    "markAllPushMessagesRead": true
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../markPushMessageUnread">← MarkPushMessageUnread mutation</a>
    <a href="../markAllPushMessagesUnread">MarkAllPushMessagesUnread mutation →</a>
</div>
