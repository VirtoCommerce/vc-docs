# RegisterContactType

This type represents the details of a contact person during the registration process. 

## Fields

| Field                                                                                                         | Description                                           |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `id`  ==String!==                                                                                             | The Id of the contact.                                |
| `firstName`  ==String!==                                                                                      | The first name of the contact person.                 |
| `lastName`  ==String!==                                                                                       | The last name of the contact person.                  |
| `middleName`  ==String==                                                                                      | The middle name of the contact person.                |
| `phoneNumber`  ==String==                                                                                     | The phone number of the contact person.               |
| `birthdate`  ==Date==                                                                                         | The birthdate of the contact person.                  |
| `status`  ==String==                                                                                          | The status of the contact.                            |
| `createdBy`  ==String==                                                                                       | The user or entity who created the contact.           |
| `about`  ==String==                                                                                           | Additional information or details about the contact.  |
| `address` [ ==MemberAddressType== ](MemberAddressType.md)                                                     | The address of the contact person.                    |
| `dynamicProperties(...)` [ ==DynamicPropertyValueType== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/dynamic-property-value-type)  | The dynamic properties associated with the contact.   |

