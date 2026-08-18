# clearAllPushMessages ==~mutation~==

This mutation clears all push messages.

## Possible returns

| Possible return | Description                                                                               |
|-----------------|-------------------------------------------------------------------------------------------|
| `Boolean`       | Indicates whether the operation of clearing all push messages was successful or not.       |


## Example

<div class="grid" markdown>

```json title="Mutation"
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
