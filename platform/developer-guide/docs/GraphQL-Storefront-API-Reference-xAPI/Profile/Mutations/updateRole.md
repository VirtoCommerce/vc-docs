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

```graphql title="Mutation"
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
  "command": {
    "role": {
      "id": "org-maintainer",
      "name": "Org Maintainer",
      "description": "Role for managing organization settings."
    }
  }
}
```
</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../removeMemberFromOrganization">← RemoveMemberFromOrganization mutation</a>
    <a href="../updateMemberAddresses">UpdateMemberAddresses mutation →</a>
</div>
