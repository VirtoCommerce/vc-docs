# deleteFcmToken ==~mutation~==

This mutation is used to delete a Firebase Cloud Messaging (FCM) token from the system.

## Arguments

The [InputDeleteFcmTokenType!](../Objects/InputDeleteFcmTokenType.md) is used to provide the necessary details for deleting an FCM token.

| Field                     | Description                                      |
|---------------------------|--------------------------------------------------|
| `token` ==String!==       | The FCM token to be deleted.                       |

## Possible returns

| Possible return | Description                                                                               |
|-----------------|-------------------------------------------------------------------------------------------|
| `Boolean`       | Indicates whether the FCM token was successfully deleted.                                   |

=== "Mutation"

    ```graphql linenums="1"
    mutation {
      deleteFcmToken(command: { token: "qwerty" })
    }
    ```

=== "Variables"

    ```json linenums="1"
    {
      "command": {
        "token": "qwerty"
      }
    }
    ```

