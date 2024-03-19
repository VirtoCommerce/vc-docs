# removeWishlistItem ==~mutation~==

This mutation removes an item from a wishlist.

## Arguments

The `InputRemoveWishlistItemType!` represents the input for removing an item from a wishlist.

| Field                                                                     | Description                                             |
|---------------------------------------------------------------------------|---------------------------------------------------------|
| `listId` ==String!==                                                     | The Id of the wishlist to remove an item from.          |
| `lineItemId` ==String!==                                                 | The Id of the line item to remove.                      |


## Possible returns

| Possible return                                          	| Description                                   |
|---------------------------------------------------------	|-----------------------------------------------|
| [`WishlistType`](../objects/wishlist-type.md)          	|  The details and properties of the wishlist.  |


=== "Mutation"
    ```json linenums="1"
    mutation removeWishlistItem($command: InputRemoveWishlistItemType!) {
      removeWishlistItem(command: $command) {
      id
      name
      storeId
      customerId
      customerName
      currency
      items
      itemsCount
      scope
      description
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {​
      "command": {​
        "listId": "4c9fac2c-cdbe-410d-be85-8e69b76c50e2",​
        "itemId": "62c0e60e-5314-4a38-8e5d-49a154db99cd"
      } ​
    }
    ```
