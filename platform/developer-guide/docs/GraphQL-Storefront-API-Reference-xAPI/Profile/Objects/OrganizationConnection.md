# OrganizationConnection ==~object~==

The `OrganizationConnection` provides information about the connection to a list of organizations.

## Fields

| Field                                  	                                    | Description                                                      	                            |
|----------------------------------------------------------------------------	|-------------------------------------------------------------------------------------------	|
| `totalCount`  ==Int==                   	                                    | The total number of organizations in the connection.             	                            |
| `pageInfo` [ ==PageInfo== ](../../Catalog/objects/PageInfo.md)              	| The information about the current page  in the paginated list of organizations.               |
| `edges` [ ==OrganizationEdge== ](OrganizationEdge.md)                      	| The edges in the connection, representing individual organizations.                           |
| `items` [ ==Organization== ](OrganizationType.md)        	                    | The list of organizations in the connection.                                              	|

