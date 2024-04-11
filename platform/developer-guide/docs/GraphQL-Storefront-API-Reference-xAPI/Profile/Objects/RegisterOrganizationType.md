# RegisterOrganizationType

The `RegisterOrganizationType` represents the details of an organization during the registration process.

## Fields

| Field                                                                                                        | Description                                              |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| `id`  ==String!==                                                                                            | The Id of the organization.                              |
| `name`  ==String!==                                                                                          | The name of the organization.                            |
| `description`  ==String==                                                                                    | A description of the organization.                       |
| `address` [ ==MemberAddressType== ](MemberAddressType.md)                                                    | The address of the organization.                         |
| `status`  ==String==                                                                                         | The status of the organization.                          |
| `createdBy`  ==String==                                                                                      | The user or entity who created the organization.         |
| `ownerId`  ==String==                                                                                        | The Id of the owner associated with the organization.    |
| `dynamicProperties(...)` [ ==DynamicPropertyValueType== ](../../Cart/objects/dynamic-property-value-type.md) | The dynamic properties associated with the organization. |

