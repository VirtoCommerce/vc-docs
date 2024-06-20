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

=== "Mutation"

    ```graphql linenums="1"
    mutation {
      addFcmToken(command: { token: "qwerty" })
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

