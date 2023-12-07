# renameWishlist ==~mutation~==

This mutation renames a wishlist.

## Arguments

The `InputRenameWishlistType!` represents the input for renaming a wishlist.

| Field                                                   | Description                                             |
|---------------------------------------------------------|---------------------------------------------------------|
| `listId` {==String!==}                                  | The Id of the wishlist to be renamed.                   |
| `listName` {==String==}                                 | The new name for the wishlist.                          |

## Possible returns

| Possible return                                          	| Description                                   |
|---------------------------------------------------------	|-----------------------------------------------|
| [`WishlistType`](../objects/wishlist-type.md)          	|  The details and properties of the wishlist.  |


=== "Mutation"
    ```json linenums="1"
    mutation renameWishlist($command: InputRenameWishlistType!) {
      renameWishlist(command: $command) {
        id
        name
        scope
        description
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command": {
        "id": "4c9fac2c-cdbe-410d-be85-8e69b76c50e2",
        "name": "new list name",
        "scope": "private",
        "description": "new description"
      }
    }
    ```
