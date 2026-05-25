# changeCartItemComment ==~mutation~==

This mutation changes cart item comments.

## Arguments

The `InputChangeCartItemCommentType` represents the input object type used for changing the comment of a specific item in a cart. 

| Field                       | Description                                                               |
|-----------------------------|---------------------------------------------------------------------------|
| `cartId` ==String==         | The Id of the cart to which the item belongs.                             |
| `storeId` ==String!==       | The Id of the store associated with the cart.                             |
| `cartName` ==String==       | The name of the cart.                                                     |
| `userId` ==String==         | The Id of the user who owns the cart.                                     |
| `currencyCode` ==String==   | The currency code associated with the cart.                               |
| `cultureName` ==String==    | The culture or language name associated with the cart.                    |
| `cartType` ==String==       | The type of the cart.                                                     |
| `lineItemId` ==String!==    | The Id of the line item for which the comment is being changed.           |
| `comment` ==String!==       | The new comment to be assigned to the line item.                          |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|

## Example

<div class="grid" markdown>

```json title="Mutation"
mutation ($command:InputChangeCartItemCommentType!) {
  (command: $command) {
    id
    items {
      sku
      productId
      comment
    }
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
  "lineItemId": "127fffb3-9840-454e-a879-c0e621d7f128"
  "comment": "nice product"
}
```

</div>