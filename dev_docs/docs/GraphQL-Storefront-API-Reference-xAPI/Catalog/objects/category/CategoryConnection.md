# CategoryConnection ==~object~==

The `CategoryConnection` represents a connection to a list of categories. 

## Fields

| Field                                           	| Description                                                                 	|
|------------------------------------------------	|-----------------------------------------------------------------------------	|
| `totalCount` {==Int==}                           	| The total number of categories in the connection, regardless of pagination. 	|
| `pageInfo` [{==PageInfo!==}](../PageInfo.md)     	| Information about the current page.                                         	|
| `edges` [{==CategoryEdge==}](CategoryEdge.md) 	| A connection between a category and the cursor associated with it.          	|
| `items` [{==Category==}](CategoryType.md)     	| The actual categories returned in the connection.                           	|