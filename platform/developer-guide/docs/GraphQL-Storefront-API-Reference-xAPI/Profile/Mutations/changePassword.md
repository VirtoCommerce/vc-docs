# changePassword ==~mutation~==

This mutation changes the password.

## Arguments

The `InputChangePasswordType!` represents the input object for changing a user's password. 

| Field                     | Description                                                                                                                  |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------|
| `userId`  ==String!==     | The Id of the user for whom the password change is being performed.                                                            |
| `oldPassword`  ==String!==  | The current or old password associated with the user account.                                                                 |
| `newPassword`  ==String!==  | The new password to set for the user.                                                                                        |


## Possible returns

| Possible return                                          	            | Description                                         	|
|---------------------------------------------------------------------	|------------------------------------------------------	|
| [`CustomIdentityResultType`](../Objects/CustomIdentityResultType.md)  | The outcome of identity-related operations.         	|


=== "Mutation"
    ```json linenums="1"
    mutation changePassword($command: InputChangePasswordType!)  
    changePassword(command: $command) {
    succeeded
        errors
        {
        code
        description
        }
    }

    ```

=== "Variables"
    ```json linenums="1"
    {
    "command": {
        "userId": "testuserid",
        "newPassword": "Password1",
        "oldPassword": "Password2"
    }
    }
    ```
