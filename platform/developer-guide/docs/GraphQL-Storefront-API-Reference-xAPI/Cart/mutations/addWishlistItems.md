# addWishlistItems ==~mutation~==

This mutation adds multiple items to a wishlist.

## Arguments

The `InputAddWishlistItemsType!` represents the input for adding items to a wishlist.

| Field                                                                                 | Description                                              |
|---------------------------------------------------------------------------------------|----------------------------------------------------------|
| `listId` ==String!==                                                                  | The Id of the wishlist to which the item will be added.  |
| `listItems` [==InputNewWishlistItemType!==](../objects/InputNewWishlistItemType.md)   | The list of items to be added to the wishlist.           |


## Possible returns

| Possible return                                          	| Description                                   |
|---------------------------------------------------------	|-----------------------------------------------|
| [`WishlistType`](../objects/wishlist-type.md)          	|  The details and properties of the wishlist.  |


=== "Mutation"
    ```json linenums="1"
    mutation addWishlistItems($command: InputAddWishlistItemsType!) {
      addWishlistItems(command: $command)
        {
          id
          items {
            id
            name  
          }
        }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command":{
        "listId": "feb44d0f-efbd-4f26-8916-5096a25247d7",
        "listItems": [
          {
          "productId": "e248fe8b-45df-4dc0-8de2-3bd5fc360adb",
          "quantity": 1
          },
          {
          "productId": "ffd1bc36-4756-4e6a-88ee-0d7ae70d539c",
          "quantity": 1
          }
        ]
      }
    }
    ```