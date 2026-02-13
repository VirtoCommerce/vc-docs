# updateRole ==~mutation~==

This mutation updates a role.

## Arguments

The `InputUpdateRoleType!` represents the input data required to update a role.

| Field                                                                           | Description                                           |
|---------------------------------------------------------------------------------|-------------------------------------------------------|
| `role` [==InputUpdateRoleInnerType==](../Objects/InputUpdateRoleInnerType.md) | The updated role information.                         |


## Possible returns

| Possible return                                          	| Description                                     	|
|---------------------------------------------------------	|-------------------------------------------------	|
| [`IdentityResultType`](../Objects/IdentityResultType.md)  | The result of an identity-related operation.  	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation updateRole ($command: InputUpdateRoleType!) {
  updateRole (command: $command) {
    errors {
      code
      description
    }
    succeeded
  }
}
```

```json title="Variables"
{
  "command": {"contactId": "550e9b14-ddde-46fe-bc28-0afec83ade96", "organizationId": "689a72757c754bef97cde51afc663430"}
}
```

</div>