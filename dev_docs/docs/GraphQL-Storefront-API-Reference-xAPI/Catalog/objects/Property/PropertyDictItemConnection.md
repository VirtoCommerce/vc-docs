# PropertyDictionaryItemConnection ==~object~==

The `PropertyDictionaryItemConnection` is a connection type that facilitates pagination and retrieval of `PropertyDictionaryItem` objects.

## Fields

| Field                                  	| Description                                                                        	|
|----------------------------------------	|-------------------------------------------------------------------------------------	|
| totalCount {==Int==}                     	|  An integer representing the total count of objects in this connection, disregarding pagination. Clients can use this information to fetch a specific number of objects and display the total count. In cases where the count is unknown or infinite scrolling is employed, this field will return `null`. 	|
| PageInfo [{==PageInfo! ==}](../PageInfo.md)   | Information about pagination in the connection, such as the current page, total pages, and page size.             	|
| PropertyDictionaryItemEdge [{==PropertyDictionaryItemEdge==}](PropertyDictItemEdge.md) 	|  A list of edges that represent the connections between nodes in the `PropertyDictionaryItemConnection`. Each edge contains a cursor for pagination and the corresponding `PropertyDictionaryItem`.          	|
| items [{==PropertyDictionaryItem==}](PropertyDictItemConnection.md)              	|  A list of all of the objects returned in the connection.                       	|
