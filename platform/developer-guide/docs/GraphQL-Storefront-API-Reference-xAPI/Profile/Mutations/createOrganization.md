# createOrganization ==~mutation~==

This mutation creates an organization.

## Arguments

The `InputCreateOrganizationType!` represents the input object for creating a contact.

| Field                                                                                 | Description                                           |
|---------------------------------------------------------------------------------------|-------------------------------------------------------|
| `id`  ==String==                                                                      | The Id of the organization.                           |
| `name`  ==String==                                                                    | The name of the organization.                         |
| `memberType`  ==String==                                                              | The member type of the organization.                  |
| `addresses` [ ==[InputMemberAddressType]== ](../Objects/InputMemberAddressType.md)    | The addresses associated with the organization.       |
| `phones`  ==[String]==                                                                | The phone numbers associated with the organization.   |
| `emails`  ==[String]==                                                                | The emails associated with the organization.          |
| `groups`  ==[String]==                                                                | The groups associated with the organization.          |
| `dynamicProperties` [ ==InputDynamicPropertyValueType== ](../Objects/InputDynamicPropertyValueType.md) | The dynamic properties of the organization. |

## Possible returns

| Possible return                                          	| Description                                         	|
|---------------------------------------------------------	|-----------------------------------------------------	|
| [`OrgzanizationType`](../Objects/OrganizationType.md)     | Information about the organization.                	|


## Example

<div class="grid" markdown>

```graphql title="Mutation"
mutation createOrganization  ($command: InputCreateOrganizationType!) {
  createOrganization (command: $command) {
    id
    name
  }
}
```

```json title="Variables"
{
  "command": {
    "name": "NewOrgADMIN",
    "addresses": {
      "city": "Berlin",
      "countryCode": "DE",
      "countryName": "German",
      "email": "t123@t123.com",
      "line1": "line1",
      "firstName": "first123",
      "postalCode": "44232",
      "description": "test"
    }
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../deleteUsers">← DeleteUsers mutation</a>
    <a href="../updateOrganization">UpdateOrganization mutation →</a>
</div>
