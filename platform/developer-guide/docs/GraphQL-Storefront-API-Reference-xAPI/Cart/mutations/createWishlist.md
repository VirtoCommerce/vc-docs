# createWishlist ==~mutation~==

This mutation creates a new wishlist with the specified details.

## Arguments

The `InputCreateWishlistType` represents the input for creating a wishlist.

| Field                                     | Description                                             |
|-------------------------------------------|---------------------------------------------------------|
| `storeId`  ==String!==                    | The Id of the store.                                    |
| `userId`  ==String!==                     | The Id of the user associated with the wishlist.        |
| `listName`  ==String==                    | The name of the wishlist.                               |
| `cultureName`  ==String==                 | The culture or language associated with the wishlist.   |
| `currencyCode`  ==String==                | The currency code for the wishlist.                     |
| `scope`  ==String==                       | The accessibility of the wishlist.                      |
| `description`  ==String==                 | The description of the wishlist.                        |

## Possible returns

| Possible return                                          	| Description                                   |
|---------------------------------------------------------	|-----------------------------------------------|
| [`WishlistType`](../objects/wishlist-type.md)          	|  The details and properties of the wishlist.  	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation createWishlist ($command: InputCreateWishlistType!) {​
  createWishlist (command: $command) {​
    id​
    name​
    storeId​
    scope​
    description​
  }​
}
```

```json title="Variables"
{​
  "command": {​
    "storeId": "B2B-store",​
    "userId": "530dbc7b-796a-4eea-bca5-10568b3c5050",​
    "listName": "Some name",​
    "cultureName": "en-US",​
    "currencyCode": "USD",​
    "scope": "organization",​
    "description": "Some description"​
  }​
}
```

</div>