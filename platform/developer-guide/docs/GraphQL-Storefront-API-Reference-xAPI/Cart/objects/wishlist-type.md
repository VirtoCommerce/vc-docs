# WishlistType ==~object~==

The `WishlistType` represents the details and properties of a wishlist.

## Fields

| Field                                                         | Description                                                 |
|---------------------------------------------------------------|-------------------------------------------------------------|
| `id`  ==String!==                                             | The Id of the wishlist.                                     |
| `name`  ==String!==                             	            | The name of the wishlist.                                   |
| `storeId`  ==String!==                                        | The Id of the store associated with the wishlist.           |
| `customerId`  ==String==                        	            | The Id of the customer associated with the wishlist.        |
| `customerName`  ==String==                      	            | The name of the customer associated with the wishlist.      |
| `currency` [ ==CurrencyType== ](currency-type.md)             | The currency associated with the wishlist.                  |
| `items` [ ==LineItemType== ](line-item-type.md)               | A list of line items (products) in the wishlist.            |
| `itemsCount`  ==Int==                                         | The total number of items in the wishlist.                  |
| `scope` [ ==WishlistScopeType== ](wishlist-scope-type.md)     | The accessibility of the wishlist.                          |
| `description`  ==String==                                     | A description of the wishlist.                              |
| `modifiedDate`  ==DateTime==                                  | The date the wishlist was modified.                         |

