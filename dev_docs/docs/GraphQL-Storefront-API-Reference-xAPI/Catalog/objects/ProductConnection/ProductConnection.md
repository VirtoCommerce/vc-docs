# ProductConnection ==~object~==

The `ProductConnection` represents a connection to a list of products. 

## Fields

| Field                                                 	    | Description                                                                                                                     	|
|-------------------------------------------------------------- |----------------------------------------------------------------------------------------------------------------------------------	|
| `totalCount` {==Int==}              	                        | The total number of products in the connection, regardless of pagination. It provides a count of all products that match the query criteria. |
| `pageInfo` [{==PageInfo!==}](../PageInfo.md)                 	| Information about the current page. It is used for pagination purposes.                                                         	|
| `edges` [{==ProductEdge==}](ProductEdge.md)                  	| Represents a connection between a product and the cursor associated with it.                                                   	|
| `items` [{==Product==}](../01-ProductType.md)                	| Contains the actual products returned in the connection.                                                                      	|
| `filter_facets` [{==FilterFacet==}](../Facets/FilterFacet.md)	| Represents a facet for filtering the products.                                                                                	|
| `range_facets` [{==RangeFacet==}](../Facets/RangeFacet.md)    | Represents a facet for filtering the products based on a range of values.                                                      	|
| `term_facets` [{==TermFacet==}](../Facets/TermFacet.md)       | Represents a facet for filtering the products based on discrete values.                                                           |

