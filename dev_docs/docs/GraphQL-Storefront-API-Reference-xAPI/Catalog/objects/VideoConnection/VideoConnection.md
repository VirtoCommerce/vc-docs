# VideoConnection ==~object~==

The `VideoConnection` is a connection from an object to a list of objects of `VideoType`.

## Fields

| Field                    	| Description                                                                                                                                                                        	|
|--------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| `totalCount` {==Int==}     	| A count of the total number of videos in this connection, disregarding pagination. It allows a client to fetch a specific number of videos by specifying the first argument, and then fetch the total count to display information like "5 of 83". In cases where infinite scrolling is employed or the exact count is unknown, this field will return null.                                          	|
| `pageInfo` [{==PageInfo!==}](../PageInfo.md) 	| Information about pagination in the connection.                                                                                                                  	|
| `edges` [{==VideoEdge==}](VideoEdge.md)    	    | A list of edges that represent the connections between videos and other related objects.                                                                         	|
| `items` [{==VideoType==}](VideoType.md)    	    | A list of all of the objects returned in the connection. This is a convenience field provided for quickly exploring the API; rather than querying for `{ edges { node } }` when no edge data is needed, this field can be used instead. Note that when clients need to fetch the cursor field on the edge to enable efficient pagination, this shortcut cannot be used, and the full `{ edges { node } }` version should be used instead. 	|
