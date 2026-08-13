# clearAllPushMessages ==~mutation~==

This mutation clears all push messages.

## Possible returns

| Possible return | Description                                                                               |
|-----------------|-------------------------------------------------------------------------------------------|
| `Boolean`       | Indicates whether the operation of clearing all push messages was successful or not.       |


## Example

<div class="grid" markdown>

```graphql title="Mutation"
mutation ClearAllPushMessages {
  clearAllPushMessages
}
```

```json title="Expected response"
{
  "data": {
    "clearAllPushMessages": true
  }
}
```

</div>





```graphql linenums="1"
mutation clearAllPushMessages {
clearAllPushMessages
}
```

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../markAllPushMessagesUnread">← MarkAllPushMessagesUnread mutation</a>
    <a href="../addFcmToken">AddFcmToken mutation →</a>
</div>
