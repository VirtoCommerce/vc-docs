# resetPasswordByToken ==~mutation~==

This mutation is used to reset a user's password using a reset token.

## Arguments

The `InputResetPasswordByTokenType!` represents the input object for resetting a user's password using a reset token.

| Field                   | Description                                                                                                                         |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `token`  ==String!==    | The reset token used to verify the authenticity of the password reset request.                                                      |
| `userId`  ==String!==   | The Id of the user for whom the password reset is being performed.                                                                   |
| `newPassword`  ==String!==  | The new password to set for the user.                                                                                            |


## Possible returns

| Possible return                                          	            | Description                                                       	|
|--------------------------------------------------------------------	|--------------------------------------------------------------------	|
| [`CustomIdentityResultType`](../Objects/CustomIdentityResultType.md)  | The outcome of identity-related operations.                        	|


=== "Mutation"
    ```json linenums="1"
    mutation resetPasswordByToken ($command:InputResetPasswordByTokenType){
    resetPasswordByToken(command:$command)
    {
        succeeded
        errors{
        code
        parameter
        description
        }
    }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
    "command":{
        "token":"token_1",
        "userId":"UseId_1",
        "newPassword":"qwERTY2345"
    }
    }
    ```
