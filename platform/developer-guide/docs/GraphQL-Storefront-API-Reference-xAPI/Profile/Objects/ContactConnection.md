# ContactConnection ==~object~==

This type represents a connection to a list of contacts.

## Fields

| Field                	                                            | Description                                                                   	|
|-----------------------------------------------------------------	|-------------------------------------------------------------------------------	|
| `totalCount`  ==Int==     	                                    | The total number of contacts in the connection.                                	|
| `pageInfo` [ ==PageInfo== ](../../Catalog/objects/PageInfo.md) 	| The information about the current page of contacts.                            	|
| `edges` [ ==ContactEdge== ](ContactEdge.md)       	            | The edges representing connections between contacts and the cursor information. 	|
| `items` [ ==ContactType== ](ContactType.md)       	            | The list of contacts in the connection.                                         	|

