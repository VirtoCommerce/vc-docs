# inviteUser ==~mutation~==

This mutation allows to invite users.

## Arguments

The `InputInviteUserType!` represents the input for inviting users.

| Field                                     | Description                                                                       |
|-------------------------------------------|-----------------------------------------------------------------------------------|
| `storeId` {==String!==}                   | The Id of the store for which the user is being invited.                          |
| `organizationId` {==String!==}            | The Id of the organization to which the invited user will be associated.          |
| `urlSuffix` {==String==}                  | The URL suffix to be appended to the invitation URL.                              |
| `emails` [{==String!==}]                  | An array of email addresses of the users to be invited.                           |
| `message` {==String==}                    | A message to include in the invitation email.                                     |
| `roleIds` [{==String!==}]                 | An array of role Ids to assign to the invited users.                              |


## Possible returns

| Possible return                                          	             | Description                                	|
|------------------------------------------------------------------------|---------------------------------------------	|
| [`CustomIdentityResultType`](../Objects/CustomIdentityResultType.md)   | The outcome of identity-related operations. 	|


=== "Mutation"
    ```json linenums="1"
    mutation inviteUSer ($command: InputInviteUserType!){
    inviteUser(command:$command)
    {
        succeeded
        errors
        {parameter
        code
        description}
    }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command": {
        "storeId": "Electronics",
        "organizationId": "72c4d52a-9504-4704-8009-6335f68ad092" ,
        "emails":
        [
          "test_user@test1.com",
          "test_user@test2.com"
        ]
      }
    }
    ```
