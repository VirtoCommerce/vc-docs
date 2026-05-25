# createUser ==~mutation~==

This mutation creates a user.

## Arguments

The `InputCreateUserType!` represents the input object for creating a user.

| Field                                                  | Description                                                                                                         |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `applicationUser` [ ==InputCreateApplicationUserType== ](../Objects/InputCreateApplicationUserType.md) | The input data for creating an application user, which includes the user's details. |

## Possible returns

| Possible return                                          	| Description                                                       	|
|---------------------------------------------------------	|--------------------------------------------------------------------	|
| [`IdentityResultType`](../Objects/IdentityResultType.md)  | The result of an identity-related operation.                        	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation($command: InputCreateUserType!) {
  createUser(command: $command) {
    succeeded
  }
}
```

```json title="Variables"
{
  "command": {"applicationUser": {
    "email": "graphql@test.local",
    "userName": "graphqlTestUserName",
    "userType": "Customer",
    "createdBy": "admin"
  }
 }
}
```

</div>