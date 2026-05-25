# cloneWishlist ==~mutation~==

This mutation creates a copy of an existing wishlist, optionally modifying key fields such as name, description, and scope.

## Arguments

The `InputCloneWishlistType!` represents the input for cloning a wishlist.

| Field                                                              | Description                                               |
| ------------------------------------------------------------------ | --------------------------------------------------------- |
| `storeId` ==String!==                                              | The Id of the store where the wishlist belongs.           |
| `userId` ==String!==                                               | The Id of the user for whom the wishlist is being cloned. |
| `cultureName` ==String==                                           | The language in which to retrieve localized data.         |
| `currencyCode` ==String==                                          | The currency to be used when cloning the wishlist.        |
| `scope` [==WishlistScopeType==](../objects/wishlist-scope-type.md) | The visibility scope of the cloned wishlist.              |
| `listId` ==String!==                                               | The Id of the existing wishlist to be cloned.             |
| `listName` ==String==                                              | The name of the new cloned wishlist.                      |
| `description` ==String==                                           | A description for the cloned wishlist.                    |

## Possible returns

| Possible return                               | Description                                      |
| --------------------------------------------- | ------------------------------------------------ |
| [`WishlistType`](../objects/wishlist-type.md) | The newly cloned wishlist and its full contents. |


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation cloneWishlist($command: InputCloneWishlistType!) {
  cloneWishlist(command: $command) {
    id
    name
    customerId
    scope
    itemsCount
    description
    items {
      id
      product {
        availabilityData {
          isActive
          inventories {
            fulfillmentCenterId
          }
        }
      }
    }
  }
}
```

```json title="Variables"
{
  "command": {
    "storeId": "B2B-store",
    "userId": "user2",
    "cultureName": "en-US",
    "currencyCode": "USD",
    "scope": "Private",
    "listId": "wishlist1",
    "listName": "This is a cloned wishlist",
    "description": "This is my description"
  }
}
```

</div>