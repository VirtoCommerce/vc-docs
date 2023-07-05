# updateRole ==~mutation~==

This mutation updates a role.

## Arguments

The `InputUpdateRoleType!` represents the input data required to update a role.

| Field                                                                           | Description                                           |
|---------------------------------------------------------------------------------|-------------------------------------------------------|
| `role` [{==InputUpdateRoleInnerType==}](../Objects/InputUpdateRoleInnerType.md) | The updated role information.                         |


## Possible returns

| Possible return                                          	| Description                                     	|
|---------------------------------------------------------	|-------------------------------------------------	|
| [`IdentityResultType`](../Objects/IdentityResultType.md)  | The result of an identity-related operation.  	|


=== "Mutation"
    ```json linenums="1"
    mutation($command: InputUpdateRoleType!) {
    updateRole(command: $command) {
        succeeded
        errors {
        code
        description
        }
    }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
    "command": {
        "id": "e75700bb597948cca7962e0bbcfdb97c",
        "name": "Use api",
        "permissions": [
        {
            "name": "platform:setting:read"
        },
        {
            "name": "catalog:create"
        }
        ],
        "concurrencyStamp": ""
    }
    }
    ```
