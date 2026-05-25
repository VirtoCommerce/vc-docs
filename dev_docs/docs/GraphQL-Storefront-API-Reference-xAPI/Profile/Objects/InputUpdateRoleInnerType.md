# InputUpdateRoleInnerType ==~object~==

The `InputUpdateRoleInnerType` represents the input data required to update the details of a role.  

## Fields

| Field                                                                                     | Description                                         |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------|
| `concurrencyStamp` {==String==}                                                           | The concurrency stamp of the role.                  |
| `id` {==String!==}                                                                        | The Id of the role to be updated.                   |
| `name` {==String!==}                                                                      | The updated name of the role.                       |
| `description` {==String==}                                                                | The updated description of the role.                |
| `permissions` [{==InputAssignPermissionType!==}](../Objects/InputAssignPermissionType.md) | The updated permissions assigned to the role.       |
