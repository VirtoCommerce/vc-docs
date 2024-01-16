# FacetRangeType ==~object~==

The `FacetRangeType` represents a specific range within a range facet, allowing users to filter products based on the specified range of values. 

## Fields

| Field                      	| Description                                                                                                                                                                    	|
|----------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| `count` {==Long==}           	| The number of products within the specific range.                                                                                                                              	|
| `from` {==Long==}            	| The minimum value of the range.                                                                                                                                                	|
| `includeFrom` {==Boolean!==} 	| Indicates whether the minimum value of the range should be included when filtering products.<br>If set to true, products with values equal to the minimum value will be included. 	|
| `fromStr` {==String==}       	| The minimum value of the range as a formatted string.                                                                                                                          	|
| `max` {==Long==}             	| The maximum value of the range.                                                                                                                                                	|
| `min` {==Long==}             	| The minimum value of the range.                                                                                                                                                	|
| `to` {==Long==}              	| The maximum value of the range.                                                                                                                                                	|
| `includeTo` {==Boolean!==}   	| Indicates whether the maximum value of the range should be included when filtering products.<br>If set to true, products with values equal to the maximum value will be included. 	|
| `toStr` {==String==}         	| The maximum value of the range as a formatted string.                                                                                                                          	|
| `total` {==Long==}           	| The total count of products within the entire range facet.                                                                                                                     	|
| `label` {==String==}         	| A label of the range.                                                                                                                                                          	|
| `isSelected` {==Boolean==}  	| Indicates whether the range is currently selected as a filter.                                                                                                                 	|