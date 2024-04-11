# InputRegisterOrganizationType ==~object~==

The `InputRegisterOrganizationType` represents the input object for registering an organization. 

| Field                                                                                         | Description                                                                                                       |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| `name`  ==String!==                                                                           | The name of the organization.                                                                                     |
| `description`  ==String==                                                                     | The description of the organization                                                                               |
| `dynamicProperties` [ ==InputDynamicPropertyValueType== ](InputDynamicPropertyValueType.md)   | An array of dynamic property value types, allowing the inclusion of custom properties and values for the organization.|
| `address` [ ==InputMemberAddressType== ](InputMemberAddressType.md)                           | The address associated with the organization.                                                                     |
