# markAllPushMessagesRead ==~mutation~==

This mutation marks all push messages as read.

## Possible returns

| Possible return | Description                                                                               |
|-----------------|-------------------------------------------------------------------------------------------|
| `Boolean`       | Indicates whether the operation of marking all push messages as read was successful or not.|


## Example

<div class="grid" markdown>

```json title="Mutation"
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
