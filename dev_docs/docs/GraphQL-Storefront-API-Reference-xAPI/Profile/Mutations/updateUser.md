# updateUser ==~mutation~==

This mutation updates a user information.

## Arguments

The `InputUpdateUserType!` represents the input object for creating a contact.

| Field                                                                                                  | Description                                                                             |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| `applicationUser` [{==InputUpdateApplicationUserType==}](../Objects/InputUpdateApplicationUserType.md) | The input data for updating an application user, which includes the user's details.     |

## Possible returns

| Possible return                                          	| Description                                                       	|
|---------------------------------------------------------	|--------------------------------------------------------------------	|
| [`IdentityResultType`](../Objects/IdentityResultType.md)  | The result of an identity-related operation.                        	|


=== "Mutation"
    ```json linenums="1"
    mutation updateUser($command: InputUpdateUserType!) {
      updateUser(command: $command) {
        succeeded
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
    "command": {
        "id": "916abee5-1b4d-4f1f-80f2-8be0a55cf011",
        "userName": "graphqlTestUserName2",
        "userType": "Customer",
        "roles": [],
        "securityStamp": "",
        "email": "graphql2@test.local"
        "storeId": "B2B-Store"
      }
    }
    ```
