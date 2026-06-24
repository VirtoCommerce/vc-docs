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

## Example

<div class="grid" markdown>

```json title="Mutation"
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

```json title="Variables"
{
  "command": {
    "userId": "testuserid",
    "newPassword": "Password1",
    "oldPassword": "Password2"
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../resetPasswordByToken">← ResetPasswordByToken mutation</a>
    <a href="../../../Push-messages/overview">Push Messages module overview →</a>
</div>
