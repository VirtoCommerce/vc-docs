# changeOrganizationContactRole ==~mutation~==

This mutation changes the role of an organization contact.

## Arguments

The `InputChangeOrganizationContactRoleType!` provides the necessary input values to modify the role of an organization contact. 

| Argument                  | Description                                                              |
|---------------------------|--------------------------------------------------------------------------|
| `userId` {==String==}     | The Id of the organization contact whose role is being modified.         |
| `roleIds` {==[String!]==} | An array of role Ids representing the new roles assigned to the contact. |


## Possible returns

| Possible return                                          	            | Description                                         	|
|---------------------------------------------------------------------	|------------------------------------------------------	|
| [`CustomIdentityResultType`](../Objects/CustomIdentityResultType.md)  | The result of an identity-related operation.         	|


=== "Mutation"
    ```json linenums="1"
    mutation changeOrganizationContactRole($command:  InputChangeOrganizationContactRoleType!){
    changeOrganizationContactRole(command:$command){
        succeeded
        errors
        {
        code
        description
        }
    }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
    "command":
    {
        "userId": "237a4784-d25f-419e-b4d7-cf151393d1cc",
        "roleIds": ["org-maintainer","purchasing-agent"]
        }
    }
    ```
