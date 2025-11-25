# WishlistConnection ==~object~==

This type represents a connection to a list of wishlists.

## Fields

| Field                                                             | Description                                                                   |
| ---------------------------------------------------------------   | ----------------------------------------------------------------------------- |
| `totalCount`  ==Int==                                             | The total number of wishlists in the connection.                              |
| `pageInfo` [ ==PageInfo!== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/PageInfo)   | Information about the current page and navigation in the connection.          |
| `edges` [ ==[WishlistEdge]== ](wishlist-edge.md)                  | A list of edges representing wishlists in the connection.                     |
| `items` [ ==[WishlistType]== ](wishlist-type.md)                  | The list of wishlists in the connection.                                      |
