# CartConnection ==~object~==

The `CartConnection` type is used to represent a connection of carts and provides metadata and pagination information for the retrieved carts. 

## Field

| Field                                                            | Description                                                                                                            |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| `totalCount`  ==Int==                                            | The total count of carts in the connection.                                                                            |
| `pageInfo` [ ==PageInfo!== ](../../Catalog/objects/PageInfo.md)  | Information about the current page of carts.                                                                           |
| `edges`  [ ==CartEdge== ](cart-edge.md)                          | An array of edges representing the connection between carts and the cursor-based pagination information.               |
| `items`  [ ==CartType== ](cart-type.md)                          | An array of `CartType` representing the actual cart objects retrieved in the connection.                               |

