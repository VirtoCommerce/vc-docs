# PropertyConnection ==~object~==

This type and its associated fields are used to retrieve and manage properties within the platform. 

**Fields**

| Field                  	                        | Description                                                     	|
|-------------------------------------------------	|-----------------------------------------------------------------	|
| `totalCount`  ==Int==                             | The total number of properties in the connection.             	|
| `pageInfo` [ ==PageInfo!== ](../PageInfo.md)   	| The information about the current page.                          	|
| `edges` [ ==PropertyEdge== ](PropertyEdge.md) 	| A connection between a property and the `PropertyConnection`.    	|
| `items` [ ==Property== ](Property.md)          	| All the properties included in the current query result.      	|
