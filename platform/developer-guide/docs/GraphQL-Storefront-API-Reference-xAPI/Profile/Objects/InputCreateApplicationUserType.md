# InputCreateApplicationUserType

This type represents the fields and their types for creating an application user.

## Fields

| Field                                                                                       | Description                                                                |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `createdBy`  ==String==                                                                     | The Id of the user who created the application user.                       |
| `createdDate`  ==DateTime==                                                                 | The date and time when the application user was created.                   |
| `email`  ==String!==                                                                        | The email address of the application user.                                 |
| `id`  ==String==                                                                            | The Id of the application user.                                            |
| `lockoutEnabled`  ==Boolean==                                                               | Indicates whether the application user is locked out.                      |
| `lockoutEnd`  ==DateTime==                                                                  | The date and time when the lockout period for the application user ends.   |
| `logins` [ ==InputApplicationUserLoginType== ](../Objects/InputApplicationUserLoginType.md) | An array of login information for the application user.                    |
| `memberId`  ==String==                                                                      | The Id of the member associated with the application user.                 |
| `password`  ==String==                                                                      | The password for the application user.                                     |
| `phoneNumber`  ==String==                                                                   | The phone number associated with the application user.                     |
| `phoneNumberConfirmed`  ==Boolean==                                                         | Indicates whether the phone number of the application user is confirmed.   |
| `photoUrl`  ==String==                                                                      | The URL of the photo associated with the application user.                 |
| `roles` [ ==InputAssignRoleType== ](../Objects/InputAssignRoleType.md)                      | An array of roles to assign to the application user.                       |
| `storeId`  ==String==                                                                       | The Id of the store associated with the application user.                  |
| `twoFactorEnabled`  ==Boolean==                                                             | Indicates whether two-factor authentication is enabled for the application user. |
| `userName`  ==String!==                                                                     | The username for the application user.                                     |
| `userType`  ==String!==                                                                     | The type of the application user.                                          |
| `passwordExpired`  ==Boolean==                                                              | Indicates whether the password for the application user has expired.       |

