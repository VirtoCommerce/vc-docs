# removeWishlist ==~mutation~==

This mutation removes a wishlist.

## Arguments

The `InputRemoveWishlistType!` represents the input for removing a wishlist.

| Field                                          | Description                                       |
|------------------------------------------------|---------------------------------------------------|
| `listId`  ==String!==                          | The Id of the wishlist to be removed.             |


## Possible returns

| Possible return     	| Description                                               |
|---------------------	|-----------------------------------------------------------|
| `Boolean`          	  | Indicates whether the wishlist was successfully removed.  |


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation removeWishlist($command: InputRemoveWishlistType!) {
  removeWishlist(command: $command)
}
```

```json title="Variables"
{​
  "command": {​
    "listId": "4c9fac2c-cdbe-410d-be85-8e69b76c50e2",​
  } ​
}
```

</div>