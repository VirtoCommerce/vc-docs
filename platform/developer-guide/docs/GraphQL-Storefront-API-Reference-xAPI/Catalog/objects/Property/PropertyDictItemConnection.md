# PropertyDictionaryItemConnection ==~object~==

This type is a connection type that facilitates pagination and retrieval of `PropertyDictionaryItem` objects.

## Fields

| Field                                  	| Description                                                                        	|
|----------------------------------------	|-------------------------------------------------------------------------------------	|
| totalCount  ==Int==                      	|  The total number of objects in this connection, disregarding pagination. 	         |
| PageInfo [ ==PageInfo! == ](../PageInfo.md)   | The information about the current page.                                        	|
| PropertyDictionaryItemEdge [ ==PropertyDictionaryItemEdge== ](PropertyDictItemEdge.md) 	|  A list of edges that represent the connections between nodes in the `PropertyDictionaryItemConnection`.	|
| items [ ==PropertyDictionaryItem== ](PropertyDictItemConnection.md)              	|  All objects returned in the connection.                       	|
