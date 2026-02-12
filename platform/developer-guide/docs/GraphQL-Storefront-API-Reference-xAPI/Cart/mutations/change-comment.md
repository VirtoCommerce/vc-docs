# changeComment ==~mutation~==

This mutation changes the cart comments.

## Arguments

The `InputChangeCommentType` represents the input object type used for changing the comment or note associated with a cart.  


| Field                   | Description                                                                  |
|----------------------------|---------------------------------------------------------------------------|
| `cartId` ==String==      | The Id of the cart.                                                       |
| `storeId` ==String!==    | The Id of the store.                                                      |
| `cartName` ==String==    | The name of the cart.                                                     |
| `userId` ==String!==     | The Id of the user.                                                       |
| `currencyCode` ==String==| The currency code for the cart.                                           |
| `cultureName` ==String==} | The culture or locale name for the cart.                                  |
| `cartType` ==String==    | The type or category of the cart.                                         |
| `comment` ==String==     | The new comment or note to be associated with the cart.                   |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation($command: InputChangeCommentType!) {
  changeComment(command: $command) {
    name
    comment
  }
}
```

```json title="Variables"
"command": {
    "storeId": "B2B-store",
    "cartName": "default",
    "userId": "c50e5237-8a4c-41fe-b878-8e5a72390a08",
    "cultureName": "en-US",
    "currencyCode": "USD",
    "cartType": "cart",
    "comment": "Hi, Virto! :)"
}
```

</div>