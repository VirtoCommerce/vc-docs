# updateOrganization ==~mutation~==

This mutation updates an organization.

## Arguments

The `InputUpdateOrganizationType!` represents the input object used to update an organization.

| Field                                                                                                 | Description                                               |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `id` {==String!==}                                                                                    | The Id of the organization to be updated.                 |
| `name` {==String==}                                                                                   | The updated name of the organization.                     |
| `memberType` {==String==}                                                                             | The updated member type of the organization.              |
| `addresses` [{==InputMemberAddressType==}](../Objects/InputMemberAddressType.md)                      | The updated addresses associated with the organization.   |
| `phones` {==[String]==}                                                                                 | The updated phone numbers associated with the organization.|
| `emails` {==[String]==}                                                                                 | The updated emails associated with the organization.       |
| `groups` {==[String]==}                                                                                 | The updated groups associated with the organization.       |
| `dynamicProperties` [{==InputDynamicPropertyValueType==}](../Objects/InputDynamicPropertyValueType.md)| The updated dynamic properties of the organization.        |


## Possible returns

| Possible return                                          	| Description                         	|
|---------------------------------------------------------	|--------------------------------------	|
| [`Organization`](../Objects/OrganizationType.md)          | Information about the organization.  	|


=== "Mutation"
    ```json linenums="1"
    mutation($command: InputUpdateOrganizationType!) {
      updateOrganization(command: $command) {
        id
        name
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command": {
        "id": "f8512cf2aa004ead858c286b0141e856",
        "name": "org2.com"
      }
    }
    ```
