# InputUpdateApplicationUserType ==~object~==

The `InputUpdateApplicationUserType` represents the input for updating an application user. 

## Fields

| Field                                  | Description                                                 |
|----------------------------------------|-------------------------------------------------------------|
| `accessFailedCount` {==Int==}          | The number of failed access attempts for the user.           |
| `email` {==String!==}                   | The updated email address of the user.                      |
| `id` {==String!==}                      | The Id of the user to be updated.                           |
| `lockoutEnabled` {==Boolean==}         | Indicates whether the user can be locked out.               |
| `lockoutEnd` {==DateTime==}            | The date and time when the user lockout ends.               |
| `memberId` {==String==}                | The Id of the associated member.                            |
| `phoneNumber` {==String==}             | The updated phone number of the user.                       |
| `phoneNumberConfirmed` {==Boolean==}   | Indicates whether the user's phone number has been confirmed. |
| `photoUrl` {==String==}                | The updated photo URL of the user.                          |
| `roles` [{==[InputAssignRoleType]==}](../Objects/InputAssignRoleType.md)| The roles assigned to the user.|
| `storeId` {==String==}                 | The Id of the store associated with the user.               |
| `twoFactorEnabled` {==Boolean==}       | Indicates whether two-factor authentication is enabled.      |
| `userName` {==String!==}                | The updated username of the user.                           |
| `userType` {==String!==}                | The updated user type of the user.                          |
| `passwordHash` {==String==}            | The hashed password of the user.                            |
| `securityStamp` {==String!==}           | The security stamp of the user.                             |

