# registerByInvitation ==~mutation~==

This mutation is used to register a user by invitation.

## Arguments

The `InputRegisterByInvitationType!` represents the input object for registering a user through an invitation.

| Field          | Description                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------|
| `userId`  ==String!==       | The Id of the user receiving the invitation.                                       |
| `token`  ==String!==        | The invitation token used to validate and authorize the registration process.      |
| `firstName`  ==String!==    | The first name of the user being registered.                                       |
| `lastName`  ==String!==     | The last name of the user being registered.                                        |
| `phone`  ==String==         | The phone number of the user being registered.                                     |
| `username`  ==String!==     | The username chosen by the user being registered.                                  |
| `password`  ==String!==     | The password chosen by the user being registered.                                  |
| `customerOrderId`  ==String==  | The customer order Id to be associated with this user. <br> It triggers the `transferOrder` command and associates the order with the provided `userId`. |

## Possible returns

| Possible return                                          	             | Description                                         	|
|------------------------------------------------------------------------|-----------------------------------------------------	|
| [`CustomIdentityResultType`](../Objects/CustomIdentityResultType.md)   | The outcome of identity-related operations.         	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation registerByInvitation($command: InputRegisterByInvitationType!) {
  registerByInvitation(command: $command) {
    succeeded
    errors
    {
      code
      description
    }
  }
}
```

```json title="Variables"
{
  "command": {
    "userId": "testuserid",
    "token":  "This is token",
    "firstName":  "firstName",
    "lastName": "lastName",
    "username": "testUserName",
    "password": "TestPassword"
  }
}
```

</div>