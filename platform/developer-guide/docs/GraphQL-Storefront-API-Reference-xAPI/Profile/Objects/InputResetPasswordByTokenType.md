# InputResetPasswordByTokenType ==~object~==

The `InputResetPasswordByTokenType` represents the input for resetting a user's password.  

## Fields

| Field                           | Description                                                            |
|---------------------------------|------------------------------------------------------------------------|
| `token`  ==String!==            | The reset password token received by the user.                         |
| `userId`  ==String!==           | The Id of the user for whom the password is being reset.               |
| `newPassword`  ==String!==      | The new password to set for the user.                                  |
