# createOrganization ==~mutation~==

This mutation creates an organization.

## Arguments

The `InputCreateOrganizationType!` represents the input object for creating a contact.

| Field                                                                                 | Description                                           |
|---------------------------------------------------------------------------------------|-------------------------------------------------------|
| `id` {==String==}                                                                     | The ID of the organization.                           |
| `name` {==String==}                                                                   | The name of the organization.                         |
| `memberType` {==String==}                                                             | The member type of the organization.                  |
| `addresses` [{==[InputMemberAddressType]==}](../Objects/InputMemberAddressType.md)    | The addresses associated with the organization.       |
| `phones` [{==String==}]                                                               | The phone numbers associated with the organization.   |
| `emails` [{==String==}]                                                               | The emails associated with the organization.          |
| `groups` [{==String==}]                                                               | The groups associated with the organization.          |
| `dynamicProperties` [{==InputDynamicPropertyValueType==}](../Objects/InputDynamicPropertyValueType.md) | The dynamic properties of the organization. |

## Possible returns

| Possible return                                          	| Description                                         	|
|---------------------------------------------------------	|-----------------------------------------------------	|
| [`OrgzanizationType`](../Objects/OrganizationType.md)     | Information about the organization.                	|


=== "Mutation"
    ```json linenums="1"
    mutation($command: InputCreateOrganizationType!) {
    createOrganization(command: $command) {
        id
        name
        memberType
    }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
    "command": {
        "name": "testOrganizationName",
        "emails": ["testOrg.graphql.local"],
        "dynamicProperties": [
        {
            "name": "Sector,
            "value": "test value"
        }
        ]
    }
    }
    ```
