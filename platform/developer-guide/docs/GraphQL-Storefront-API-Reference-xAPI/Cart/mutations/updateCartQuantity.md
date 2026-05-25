# updateCartQuantity ==~mutation~==

This mutation updates the quantity of one or more items in a specific shopping cart.

## Arguments

The `InputUpdateCartQuantity` type represents the input object used to specify which cart items should have their quantities updated.

| Field                                     | Description                                                                        |
| ------------- | ---------------------------------------------------------------------------------------------------------------|
| `cartId` ==String==                       | The ID of the cart whose item quantities will be updated.                          |
| `storeId` ==String!==                     | The ID of the store associated with the cart.                                      |
| `cartName` ==String==                     | The name of the cart.                                                              |
| `userId` ==String!==                      | The ID of the user who owns the cart.                                              |
| `currencyCode` ==String==                 | The currency code for the cart.                                                    |
| `cultureName` ==String==                  | The culture or language associated with the cart.                                  |
| `cartType` ==String==                     | The type of the cart.                                                              |
| `items` ==[InputUpdateCartQuantityItem](../objects/InputUpdateCartQuantityItem.md)== | A list of cart items and their new quantities. Each item specifies which product line to update and the desired quantity. |

## Possible returns

| Possible return                       | Description                                                |
| ------------------------------------- | ---------------------------------------------------------- |
| [`CartType`](../objects/cart-type.md) | The properties and fields associated with a shopping cart. |


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation updateCartQuantity($command: InputUpdateCartQuantity!) {
  updateCartQuantity(command: $command) {
    id
    items {
      id
      productId
      quantity
      extendedPrice
    }
  }
}
```

```json title="Variables"
"command": {
  "cartId": "e6a7d5af-6378-44a6-b645-af9ecf702c05",
  "storeId": "B2B-Store",
  "userId": "c50e5237-8a4c-41fe-b878-8e5a72390a08",
  "currencyCode": "USD",
  "cultureName": "en-US",
  "items": [
    {
      "id": "9c42e7de-4b53-4b65-bbb2-8a7f327321ae",
      "quantity": 3
    },
    {
      "id": "1cbb8c57-5a11-47c8-996d-fd48e75f022f",
      "quantity": 1
    }
  ]
}
```

</div>