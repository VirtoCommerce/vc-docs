# UserType ==~object~==

The `UserType` represents a user with its corresponding information.

## Fields

| Field                         	    | Description                                                           	|
|------------------------------------	|-----------------------------------------------------------------------	|
| `accessFailedCount`  ==Int!==         | The number of access failed attempts for the user.                        |
| `createdBy`  ==String==               | The Id of the user who created the user.                                 	|
| `createdDate`  ==DateTime==           | The date and time when the user was created.                             	|
| `email`  ==String==                   | The email address of the user.                                           	|
| `emailConfirmed`  ==Boolean!==         | Indicates whether the user's email has been confirmed.                 	|
| `id`  ==String!==                      | The Id of the user.                                                     	|
| `isAdministrator`  ==Boolean!==        | Indicates whether the user is an administrator.                         	|
| `lockoutEnabled`  ==Boolean!==         | Indicates whether the user's account can be locked out.                 	|
| `lockoutEnd`  ==DateTime==            | The date and time when the user's lockout period ends.                   	|
| `memberId`  ==String==                | The Id of the associated member.                                         	|
| `modifiedBy`  ==String==              | The Id of the user who last modified the user.                           	|
| `modifiedDate`  ==DateTime==          | The date and time when the user was last modified.                       	|
| `normalizedEmail`  ==String==         | The normalized email address of the user.                                	|
| `normalizedUserName`  ==String==      | The normalized username of the user.                                     	|
| `passwordExpired`  ==Boolean!==        | Indicates whether the user's password has expired.                      	|
| `phoneNumber`  ==String==             | The phone number of the user.                                            	|
| `phoneNumberConfirmed`  ==Boolean!==   | Indicates whether the user's phone number has been confirmed.           	|
| `photoUrl`  ==String==                | The URL of the user's photo.                                             	|
| `roles` [ ==[RoleType]== ](RoleType.md)| The roles assigned to the user.                                          |
| `permissions`  ==[String]==           | The permissions granted to the user.                                     	|
| `securityStamp`  ==String!==           | The security stamp of the user.                                         	|
| `storeId`  ==String==                 | The Id of the associated store.                                          	|
| `twoFactorEnabled`  ==Boolean!==       | Indicates whether two-factor authentication is enabled for the user.     |
| `userName`  ==String==                | The username of the user.                                                	|
| `userType`  ==String==                | The type of the user.                                                    	|
| `forcePasswordChange`  ==Boolean==    | Indicates whether the user is required to change their password.         	|
| `passwordExpiryInDays`  ==Int==       | Notifies the user about the password expiration date​.                     |
| `contact` [ ==ContactType== ](ContactType.md)| The contact associated with the user.                              |
| `lockedState`  ==Boolean==            | Indicates whether the user is in a locked state.                         	|
| `operator` [ ==UserType== ](UserType.md)| The operator associated with the user.                                  |

