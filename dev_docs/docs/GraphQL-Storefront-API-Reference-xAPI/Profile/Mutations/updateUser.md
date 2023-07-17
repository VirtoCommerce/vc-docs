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
    mutation($command: InputUpdateUserType!) {
    updateUser(command: $command) {
        succeeded
        errors{
        code
        description
        }
    }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
    "command": {
        "id": "ae6f1cd7-957d-4b30-864c-8f40232a4df3",
        "userName": "graphqlTestUserName2",
        "userType": "Manager",
        "securityStamp": "",
        "email": "graphql2@test.local"
    }
    }
    ```
