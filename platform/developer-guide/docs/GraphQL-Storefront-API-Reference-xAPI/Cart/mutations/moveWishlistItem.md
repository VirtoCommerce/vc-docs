# moveWishlistItem ==~mutation~==

This mutation moves a wishlist item to another wishlist.

## Arguments

The `InputMoveWishlistItemType!` represents the input for moving a wishlist item.

| Field                             | Description                                                       |
|-----------------------------------|-------------------------------------------------------------------|
| `listId`  ==String!==             | The Id of the source wishlist from which to move the item.        |
| `destinationListId`  ==String!==  | The Id of the destination wishlist to which the item will be moved.|
| `lineItemId`  ==String!==         | The Id of the wishlist item to be moved.                          |


## Possible returns

| Possible return                                          	| Description                                   |
|---------------------------------------------------------	|-----------------------------------------------|
| [`WishlistType`](../objects/wishlist-type.md)          	|  The details and properties of the wishlist.  |



=== "Mutation"
    ```json linenums="1"
    mutation moveWishlistItem($command: InputMoveWishlistItemType!) {
      moveWishlistItem(command: $command) {
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

=== "Variables"
    ```json linenums="1"
    {
      "command": {
      "listId": "52752d17-7ee3-4a01-8b3d-d0aff210bf88",
      "lineItemId":  "22be3704-cd77-45e8-8f1e-4a46b18881b7",
      "destinationListId": "71389851-d644-4aec-a69b-23994263e56b"
      }
    }
    ```
