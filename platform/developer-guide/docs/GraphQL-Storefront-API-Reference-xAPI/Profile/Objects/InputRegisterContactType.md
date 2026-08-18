# InputRegisterContactType ==~object~==

This type represents the input object for registering a contact. 

## Fields

| Field                                                                                         | Description                                                           |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| `firstName`  ==String!==                                                                      | The first name of the contact.                                        |
| `lastName`  ==String!==                                                                       | The last name of the contact.                                         |
| `middleName`  ==String==                                                                      | An optional middle name of the contact.                               |
| `phoneNumber`  ==String==                                                                     | The phone number of the contact.                                      |
| `birthdate`  ==Date==                                                                         | The birthdate of the contact.                                         |
| `address` [ ==InputMemberAddressType== ](InputMemberAddressType.md)                           | The address associated with the contact.                              |
| `about`  ==String==                                                                           | The description or additional information about the contact.          |
| `dynamicProperties` [ ==InputDynamicPropertyValueType== ](InputDynamicPropertyValueType.md)   | An array of dynamic property value types, allowing the inclusion of custom properties and values for the contact. |
