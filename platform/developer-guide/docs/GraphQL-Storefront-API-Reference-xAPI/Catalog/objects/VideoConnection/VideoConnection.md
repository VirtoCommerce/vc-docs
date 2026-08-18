# VideoConnection ==~object~==

This type is a connection from an object to a list of objects of `VideoType`.

## Fields

| Field                                       	| Description                                                                                                                                                     	|
|--------------------------------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| `totalCount`  ==Int==      	                | The total number of videos in this connection, disregarding pagination.                                                                                           |
| `pageInfo` [ ==PageInfo!== ](../PageInfo.md) 	| The information about the current page.                                                                                                                         	|
| `edges` [ ==VideoEdge== ](VideoEdge.md)    	| A list of edges that represent the connections between videos and other related objects.                                                                          |
| `items` [ ==VideoType== ](VideoType.md)    	| A list of all of the objects returned in the connection.                                                                                                       	|
