# InputAssignRoleType ==~object~==

This type represents the input fields required for assigning a role to a user.

## Fields

| Field                             | Description                                                                                  |
|-----------------------------------|----------------------------------------------------------------------------------------------|
| `concurrencyStamp`  ==String==    | A stamp used for concurrency control to ensure data integrity.                               |
| `id`  ==String!==                 | The Id of the role.                                                                          |
| `name`  ==String!==               | The name of the role. It is a required field and provides a descriptive name for the role.   |
| `permissions` [ ==InputAssignPermissionType!== ](InputAssignPermissionType.md) | An array of permissions to assign to the role.  |

