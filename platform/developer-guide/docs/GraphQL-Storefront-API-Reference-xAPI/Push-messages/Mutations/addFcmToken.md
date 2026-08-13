# addFcmToken ==~mutation~==

This mutation is used to add a Firebase Cloud Messaging (FCM) token to the system.

## Arguments

The [InputAddFcmTokenType!](../Objects/InputAddFcmTokenType.md) is used to provide the necessary input for the mutation.

| Field                     | Description                                      |
|---------------------------|--------------------------------------------------|
| `token` ==String!==       | The FCM token to be added.                       |

## Possible returns

| Possible return | Description                                                                               |
|-----------------|-------------------------------------------------------------------------------------------|
| `Boolean`       | Indicates whether the FCM token was successfully added.                                   |


## Example

<div class="grid" markdown>

```graphql title="Mutation"
mutation {
  addFcmToken(command: { token: "qwerty" })
}
```

```json title="Variables"
{
  "command": {
    "token": "qwerty"
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../clearAllPushMessages">← ClearAllPushMessages mutation</a>
    <a href="../deleteFcmToken">DeleteFcmToken mutation →</a>
</div>
