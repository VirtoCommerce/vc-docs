# changeWishlist ==~mutation~==

This mutation modifies specific wishlist details.

## Arguments

The `InputChangeWishlistType!` represents the input for modifying a wishlist.

| Field                                                                     | Description                                             |
|--------------------------------------------------- -----------------------|---------------------------------------------------------|
| `listId` {==String!==}                                                    | The Id of the wishlist to be modified.                  |
| `listName` {==String==}                                                   | The new name for the wishlist.                          |
| `scope` [{==WishlistScopeType==}](../objects/wishlist-scope-type.md)      | The accessibility of the wishlist.                      |
| `description` {==String==}                                                | The description of the wishlist.                        |

## Possible returns

| Possible return                                          	| Description                                   |
|---------------------------------------------------------	|-----------------------------------------------|
| [`WishlistType`](../objects/wishlist-type.md)          	  |  The details and properties of the wishlist.  |


=== "Mutation"
    ```json linenums="1"
    mutation changeWishlist ($command: InputChangeWishlistType!) {​
      changeWishlist (command: $command) {​
        id​
        name​
        name​
        scope​
        description​
      } ​
    }
    ```

=== "Variables"
    ```json linenums="1"
    {​
      "command": {​
        "listId": "4c9fac2c-cdbe-410d-be85-8e69b76c50e2",​
        "listName": "new list name",​
        "scope": "private",​
        "description": "new description"​
      } ​
    }
    ```
