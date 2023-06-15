# ProductAssociationConnection ==~object~==

The `ProductAssociationConnection` represents a connection from an object to a list of objects of the `ProductAssociation` type. It facilitates pagination and retrieval of product associations.

## Fields

| Field                                   	    | Description                                                                                                                                        	|
|---------------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------	|
| `totalCount` {==Int==}                    	| An integer representing the total count of objects in this connection, disregarding pagination. This count allows clients to fetch the first set of objects by specifying a limit, such as "5", and retrieve the total count to display information like "5 of 83". In cases where the exact count is unknown or infinite scrolling is implemented, this field will return null. |
| `pageInfo`  [{==PageInfo==}](../PageInfo.md) 	| Information about the pagination in the connection, including details about the current page, total pages, and page size. It provides data necessary for implementing pagination logic and navigating through the associated product associations.  |
| `edges` [{==ProductAssociationEdge==}](ProductAssociationEdge.md)  	|  A list of edges that represent the connections between nodes in the `ProductAssociationConnection`. |                              	|
| `items`  [{==ProductAssociation==}](ProductAssociation.md)     	    |  A list of ProductAssociation objects returned in the connection. This field is provided as a convenience for quickly exploring the API. It allows fetching all the associated product associations without querying for the edges explicitly. Note that this shortcut cannot be used if clients require the cursor field on the edge for efficient pagination. In such cases, the full `{ edges { node } }` version should be used instead. 	|
