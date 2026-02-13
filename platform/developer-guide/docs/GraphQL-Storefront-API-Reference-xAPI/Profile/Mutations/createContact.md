# createContact ==~mutation~==

This mutation creates a contact.

## Arguments

The `InputCreateContactType!` represents the input object for creating a contact.

| Field                                                                 | Description                                                             |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------|
| `id`  ==String!==                                                     | The Id of the contact.                                                  |
| `outerId`  ==String==                                                 | The external Id of the contact.                                         |
| `memberType`  ==String!==                                             | The type of the contact.                                                |
| `name`  ==String==                                                    | The name of the contact.                                                |
| `status`  ==String==                                                  | The status of the contact.                                              |
| `phones`  ==[String]!==                                               | The phone numbers associated with the contact.                          |
| `emails`  ==[String]!==                                               | The email addresses associated with the contact.                        |
| `groups`  ==[String]!==                                               | The groups to which the contact belongs.                                |
| `seoObjectType`  ==String!==                                          | The type of object that the contact is associated with.                 |
| `seoInfo(...)` [ ==SeoInfo== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/SeoInfo)   | SEO information related to the contact.        |
| `defaultBillingAddress` [ ==MemberAddressType== ](../Objects/MemberAddressType.md)                           | The default billing address of the contact.                        |
| `defaultShippingAddress` [ ==MemberAddressType== ](../Objects/MemberAddressType.md)                          | The default shipping address of the contact.                       |
| `addresses(...)` [ ==MemberAddressConnection== ](../Objects/MemberAddressConnection.md)                      | A connection to a list of addresses associated with the contact.   |
| `dynamicProperties(...)` [ ==DynamicPropertyValueType== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/dynamic-property-value-type) | Dynamic properties of the contact.                                 |
| `firstName`  ==String!==                                              | The first name of the contact.                                          |
| `lastName`  ==String!==                                               | The last name of the contact.                                           |
| `middleName`  ==String==                                              | The middle name of the contact.                                         |
| `fullName`  ==String!==                                               | The full name of the contact.                                           |
| `about`  ==String!==                                                  | Information about the contact.                                          |
| `birthDate`  ==Date==                                                 | The birth date of the contact.                                          |
| `securityAccounts` [ ==UserType== ](../Objects/UserType.md)           | Security accounts associated with the contact.                          |
| `organizationId`  ==String==                                          | The Id of the organization associated with the contact.                 |
| `organizationsIds`  ==[String]!==                                     | The Ids of the organizations associated with the contact.               |
| `organizations(...)` [ ==OrganizationConnection== ](../Objects/OrganizationConnection.md)  | A connection to a list of organizations associated with the contact.    |

## Possible returns

| Possible return                                          	| Description                                                       	|
|---------------------------------------------------------	|--------------------------------------------------------------------	|
| [`ContactType`](../Objects/ContactType.md)                | A contact and various fields to describe the contact's information.  	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation createContact($command: InputCreateContactType!) {
  createContact(command: $command) {
    fullName
    id
    lastName
    name
  }
}
```

```json title="Variables"
{
  "command": {
    "name": "UserA",
    "memberType": "Contact",
    "addresses": [],
    "fullName": "UserA",
    "firstName": "UserA",
    "lastName": "UserA"
  }
}
```

</div>