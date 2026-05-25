# ProductAssociationConnection ==~object~==

This type represents a connection from an object to a list of objects of the `ProductAssociation` type. 

## Fields

| Field                                   	    | Description                                                                                                                                        	|
|---------------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------	|
| `totalCount`  ==Int==                     	| The total number of objects in this connection, disregarding pagination.                                                                              |
| `pageInfo`  [ ==PageInfo== ](../PageInfo.md) 	| Information about the current page. It is used for pagination purposes.                                                                               |
| `edges` [ ==ProductAssociationEdge== ](ProductAssociationEdge.md)  	|  The connections between nodes in the `ProductAssociationConnection`.                                                      	|
| `items`  [ ==ProductAssociation== ](ProductAssociation.md)     	    |  `ProductAssociation` objects returned in the connection.                                                                   	|
