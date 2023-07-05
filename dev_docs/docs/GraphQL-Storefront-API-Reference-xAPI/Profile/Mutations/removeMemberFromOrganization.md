# removeMemberFromOrganization ==~mutation~==

This mutation removes a member from an organization.

## Arguments

The `InputRemoveMemberFromOrganizationType!` represents the input object used to remove a member from an organization.

| Field                          | Description                           |
|--------------------------------|---------------------------------------|
| `contactId` {==String==}       | The Id of the contact.                |
| `organizationId` {==String==}  | The Id of the organization.           |


## Possible returns

| Possible return                                         | Description                                                       	   |
|-------------------------------------------------------- |----------------------------------------------------------------------- |
| [`ContactType`](../Objects/MemberType.md)               |  A contact and various fields to describe the contact's information.   |


=== "Mutation"
    ```json linenums="1"
    mutation removeMemberFromOrganization(
    $command: InputRemoveMemberFromOrganizationType!
    ) {
    removeMemberFromOrganization(command: $command) {
        id
        name
        organizations {
        items {
            name
            id
        }
        }
    }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
    "command": {
        "contactId": "2be32440-ee84-4dd5-aa9b-fcbe35bf61f0",
        "organizationId": "23eed211-ee84-4dd5-aa9b-dsacg32210"
    }
    }
    ```
