# rejectGiftItems ==~mutation~==

This mutation rejects gift items from a cart.

## Arguments

The `InputRejectGiftItemsType!` represents the input type required for rejecting gift items from a cart.

| Field                     | Description                                                 |
|---------------------------|-------------------------------------------------------------|
| `cartId` ==String==       | The Id for the cart.                                        |
| `storeId` ==String!==     | The Id of the store associated with the cart.               |
| `cartName` ==String==     | The name of the cart.                                       |
| `userId` ==String!==      | The Id of the user associated with the cart.                |
| `currencyCode` ==String== | The currency code used in the cart.                         |
| `cultureName` ==String==  | The culture name associated with the cart.                  |
| `cartType` ==String==     | The type of the cart.                                       |
| `ids` ==[String]!==       | An array of Ids for the items to be rejected from the cart. |


## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|

## Example

<div class="grid" markdown>

```json title="Mutation"
mutation rejectGiftItems($command: InputRejectGiftItemsType!) {
  rejectGiftItems(command: $command) {
    id
    name
    items {
      id
      productId
      name
      quantity
    }
    total {
      grandTotal {
        amount
        currency
      }
    }
  }
}
```

```json title="Variables"
{
  "command": {
    "cartId": "d8f3c7c1-1234-4567-89ab-987654321000",
    "storeId": "B2B-store",
    "cartName": "default",
    "userId": "john.doe",
    "currencyCode": "USD",
    "cultureName": "en-US",
    "cartType": "ShoppingCart",
    "ids": [
      "gift-lineitem-1",
      "gift-lineitem-2"
    ]
  }
}
```

</div>