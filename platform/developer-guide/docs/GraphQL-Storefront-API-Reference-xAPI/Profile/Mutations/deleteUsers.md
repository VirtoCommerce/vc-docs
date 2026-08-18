# deleteUsers ==~mutation~==

This mutation deletes users.

## Arguments

The `InputDeleteUserType!` represents the input structure for deleting user data.

| Field                       | Description                                                    |
|-----------------------------|----------------------------------------------------------------|
| `userNames`  ==[String]!==  | An array of strings representing the user names to be deleted. |

## Possible returns

| Possible return                                          	| Description                                                       	|
|---------------------------------------------------------	|--------------------------------------------------------------------	|
| [`IdentityResultType`](../Objects/IdentityResultType.md)  | The result of an identity-related operation.                        	|

## Example

<div class="grid" markdown>

```json title="Mutation"
mutation($command: InputDeleteUserType!) {
  deleteUsers(command: $command) {
    succeeded
    errors{
      code
      description
    }
  }
}
```

```json title="Variables"
{
  "command": {
    "userNames": ["graphqlTestUserName2"]
  }
}
```

</div>