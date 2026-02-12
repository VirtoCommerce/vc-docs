# addWishlistItem ==~mutation~==

This mutation adds an item to a wishlist.

## Arguments

The `InputAddWishlistItemType!` represents the input for adding an item to a wishlist.

| Field                                               | Description                                              |
|-----------------------------------------------------|----------------------------------------------------------|
| `listId` ==String!==                                | The Id of the wishlist to which the item will be added.  |
| `productId` ==String!==                             | The Id of the product to add to the wishlist.            |
| `quantity` ==Int==                                  | The product quantity to add to the wishlist.             |

## Possible returns

| Possible return                                          	| Description                                   |
|---------------------------------------------------------	|-----------------------------------------------|
| [`WishlistType`](../objects/wishlist-type.md)          	|  The details and properties of the wishlist.  |


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation addWishlistItem($command: InputAddWishlistItemType!) {
  addWishlistItem(command: $command) {
    id
    name
    items {
      id
      quantity
      product {
        name
      }
    }
  }
}
```

```json title="Variables"
{
  "command": {
  "listId": "52752d17-7ee3-4a01-8b3d-d0aff210bf88",
  "productId" : "baa4931161214690ad51c50787b1ed94"
  }
}
```

</div>