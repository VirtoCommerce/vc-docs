# DynamicContentItemType ==~object~==

The `DynamicContentItemType` represents a type or category of dynamic content items. 

## Fields

| Field                                       	                                        | Description                                       	                                    |
|-------------------------------------------------------------------------------------- |----------------------------------------------------------------------------------------	|
| `id` {==String!==}     	                                                            | The Id of the dynamic content item type.                                                  |
| `contentType` {==String!==}                                              	            | The content type of the dynamic content item type.                                        |
| `name` {==String!==}                                                                  | The name of the dynamic content item type.                                                |
| `description` {==String!==}                                                           | The description of the dynamic content item type.                                         |
| `priority` {==Int!==}                                                                 | The priority of the dynamic content item type.                                            |
| `dynamicProperties(...)` [{==DynamicPropertyValueType==}](../../Cart/objects/dynamic-property-value-type.md)| The dynamic properties associated with the dynamic content item type.                     |

