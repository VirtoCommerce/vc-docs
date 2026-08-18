# updateWishlistItems ==~mutation~==

This mutation updates items in a wishlist.

## Arguments

The `InputUpdateWishlistItemsType!` represents the input for updating items in a wishlist.

| Field                                                                                              | Description                                   |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------|
| `listId`  ==String!==                                                                              | The Id of the wishlist to be updated.         |
| `items` [ ==InputUpdateWishlistLineItem.md!== ](../objects/InputUpdateWishlistItemsType.md)        | The list of items to be updated in the wishlist.|


## Possible returns

| Possible return                                          	| Description                                   |
|---------------------------------------------------------	|-----------------------------------------------|
| [`WishlistType`](../objects/wishlist-type.md)          	|  The details and properties of the wishlist.  |


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation updateWishlistItems($command: InputUpdateWishlistItemsType!) {
  updateWishlistItems(command: $command) {
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
    "items": [
      {
        "lineItemId": "22be3704-cd77-45e8-8f1e-4a46b18881b7",
        "quantity": 3
      },
      {
        "lineItemId": "87c8c241-7522-4f9d-92c1-5851f8db5143",
        "quantity": 2
      }
    ]
  }
}
```

</div>