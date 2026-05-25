# Property ==~object~==

The `propertyType` represents a type or category of properties. Properties are used to provide additional information or attributes for products and variations.

## Fields

| Field                                                                	| Description                                                                       	|
|----------------------------------------------------------------------	|-----------------------------------------------------------------------------------	|
| `id` {==String==}                                                 	| The Id of the property type.                                                         	|
| `name` {==String!==}                                              	| The name of the property type.                                                       	|
| `hidden` {==Boolean!==}                                           	| Indicates whether the property type is hidden or visible.                           	|
| `multivalue` {==Boolean!==}                                       	| Indicates whether the property type allows multiple values.                       	|
| `displayOrder` {==Int==}                                          	| The order in which the property type should be displayed.                         	|
| `label` {==String==}                                              	| The label of the property type.                                   	                |
| `type` {==String==}                                               	| The type or category of the propertyType.                                         	|
| `valueType` {==String==}                                          	| The data type of the property values.                                             	|
| `value` {==PropertyValue==}                                       	| The default value or values associated with the property type.                    	|
| `valueId` {==String==}                                            	| The Id of the default value for the property type.                 	                |
| `propertyDictItems(...)` [{==PropertyDictionaryItemsConnection==}](PropertyDictItemConnection.md)  	| A connection to retrieve the dictionary items associated with the property type.  	|