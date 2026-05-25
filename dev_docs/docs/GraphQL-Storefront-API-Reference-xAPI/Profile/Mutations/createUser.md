# createUser ==~mutation~==

This mutation creates a user.

## Arguments

The `InputCreateUserType!` represents the input object for creating a user.

| Field                                                  | Description                                                                                                         |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `applicationUser` [{==InputCreateApplicationUserType==}](../Objects/InputCreateApplicationUserType.md) | The input data for creating an application user, which includes the user's details. |

## Possible returns

| Possible return                                          	| Description                                                       	|
|---------------------------------------------------------	|--------------------------------------------------------------------	|
| [`IdentityResultType`](../Objects/IdentityResultType.md)  | The result of an identity-related operation.                        	|


=== "Mutation"
    ```json linenums="1"
    mutation($command: InputCreateUserType!) {
      createUser(command: $command) {
        succeeded
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
{
  "command": {"applicationUser": {
    "email": "graphql@test.local",
    "userName": "graphqlTestUserName",
    "userType": "Customer",
    "createdBy": "admin"
  }
 }
}
    ```
