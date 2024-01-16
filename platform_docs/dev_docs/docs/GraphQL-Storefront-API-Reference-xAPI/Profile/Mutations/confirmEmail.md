# confirmEmail ==~mutation~==

This mutation allows to confirm email to complete email verification and allow customer sign-in.

## Arguments

The `InputConfirmEmailType` represents the input for the `confirmEmail` mutation.

| Field                                     | Description                                                                       |
|-------------------------------------------|-----------------------------------------------------------------------------------|
| `userId` {==String!==}                    | The Id of the user undergoing email confirmation.                                 |
| `token` {==String!==}                     | The verification token associated with the email confirmation process.            |


## Possible returns

| Possible return                                          	             | Description                                	|
|------------------------------------------------------------------------|---------------------------------------------	|
| [`CustomIdentityResultType`](../Objects/CustomIdentityResultType.md)   | The outcome of identity-related operations. 	|


=== "Mutation"
    ```json linenums="1"
    mutation ($command: InputConfirmEmailType){
      confirmEmail(command:$command)
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command": {
        "userId": 4162ff51-c880-4e42-bc4b-4bfd120a0bdf",
        "token: CfDJ88BluBQSMjM5OhRGBcqa2bBAuYkKMUo18c..."
      }
    }
    ```
