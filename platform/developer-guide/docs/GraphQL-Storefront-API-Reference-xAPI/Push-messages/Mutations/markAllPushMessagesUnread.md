# markAllPushMessagesUnread ==~mutation~==

This mutation marks all push messages as unread.

## Possible returns

| Possible return | Description                                                                               |
|-----------------|-------------------------------------------------------------------------------------------|
| `Boolean`       | Indicates whether the operation of marking all push messages as unread was successful or not.|


## Example

<div class="grid" markdown>

```graphql title="Mutation"
mutation MarkAllPushMessagesUnread {
  markAllPushMessagesUnread
}
```

```json title="Expected response"
{
  "data": {
    "markAllPushMessagesUnread": true
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../markAllPushMessagesRead">← MarkAllPushMessagesRead mutation</a>
    <a href="../clearAllPushMessages">ClearAllPushMessages mutation →</a>
</div>
