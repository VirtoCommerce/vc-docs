# MemberType ==~object~==

The `MemberType` represents a member entity.

## Fields

| Field                                                                     | Description                                                                                                      |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| `id` {==String!==}                                                        | The Id of the member.                                                                                            |
| `outerId` {==String==}                                                    | The external Id of the member.                                                                                   |
| `memberType` {==String!==}                                                | The type of the member.                                                                                          |
| `name` {==String==}                                                       | The name of the member.                                                                                          |
| `status` {==String==}                                                     | The current status of the member.                                                                                |
| `phones` {==String!==}                                                    | An array of phone numbers associated with the member.                                                            |
| `emails` {==String!==}                                                    | An array of email addresses associated with the member.                                                          |
| `groups` {==String!==}                                                    | An array of group names that the member belongs to.                                                              |
| `seoObjectType` {==String==}                                              | The SEO  object type associated with the member.                                                                 |
| `seoInfo(...)` [{==SeoInfo==}](../../Catalog/objects/SeoInfo.md)          | Request-related SEO-info.                                                                                        |
| `defaultBillingAddress` [{==MemberAddressType==}](MemberAddressType.md)   | The default billing address for the member.                                                                      |
| `defaultShippingAddress` [{==MemberAddressType==}](MemberAddressType.md)  | The default shipping address for the member.                                                                     |
| `addresses(...)` [{==MemberAddressConnection==}](MemberAddressConnection.md) | A connection to retrieve the addresses associated with the member.                                            |
| `dynamicProperties(...)` [{==DynamicPropertyValueType!==}](../../Cart/objects/dynamic-property-value-type.md)| An array of dynamic properties associated with the member.                    |

