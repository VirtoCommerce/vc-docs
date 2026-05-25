# OrganizationConnection ==~object~==

This type provides information about the connection to a list of organizations.

## Fields

| Field                                  	                                    | Description                                                      	                            |
|----------------------------------------------------------------------------	|-------------------------------------------------------------------------------------------	|
| `totalCount`  ==Int==                   	                                    | The total number of organizations in the connection.             	                            |
| `pageInfo` [ ==PageInfo== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/PageInfo)              	| The information about the current page  in the paginated list of organizations.               |
| `edges` [ ==OrganizationEdge== ](OrganizationEdge.md)                      	| The edges in the connection, representing individual organizations.                           |
| `items` [ ==Organization== ](OrganizationType.md)        	                    | The list of organizations in the connection.                                              	|

