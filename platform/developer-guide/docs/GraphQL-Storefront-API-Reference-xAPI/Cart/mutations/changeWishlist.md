# changeWishlist ==~mutation~==

This mutation modifies specific wishlist details.

## Arguments

The `InputChangeWishlistType!` represents the input for modifying a wishlist.

| Field                                                                   | Description                                             |
|--------------------------------------------------- ---------------------|---------------------------------------------------------|
| `listId` ==String!==                                                    | The Id of the wishlist to be modified.                  |
| `listName` ==String==                                                   | The new name for the wishlist.                          |
| `scope` [==WishlistScopeType==](../objects/wishlist-scope-type.md)      | The accessibility of the wishlist.                      |
| `description` ==String==                                                | The description of the wishlist.                        |
| `cultureName` ==String==                                                | The language to retrieve data in.                       |

## Possible returns

| Possible return                                          	| Description                                   |
|---------------------------------------------------------	|-----------------------------------------------|
| [`WishlistType`](../objects/wishlist-type.md)          	  |  The details and properties of the wishlist.  |


## Example

<div class="grid" markdown>

```json title="Mutation"
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

```json title="Variables"
{​
  "command": {​
    "listId": "4c9fac2c-cdbe-410d-be85-8e69b76c50e2",​
    "listName": "new list name",​
    "scope": "private",​
    "description": "new description"​
  } ​
}
```

</div>