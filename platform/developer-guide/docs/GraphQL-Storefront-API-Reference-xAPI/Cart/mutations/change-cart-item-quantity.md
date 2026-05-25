# changeCartItemQuantity ==~mutation~==

This mutation changes the cart item quantity.

## Arguments

The `InputChangeCartItemQuantityType` represents the input object type used for changing the quantity of a specific item in a cart. 

| Field                     | Description                                                                             |
|---------------------------|-----------------------------------------------------------------------------------------|
| `cartId` ==String==     | The Id of the cart to which the item belongs.                                           |
| `storeId` ==String!==   | The Id of the store to which the cart belongs.                                          |
| `cartName` ==String==   | The name or description of the cart.                                                    |
| `userId` ==String==     | The Id of the user associated with the cart.                                            |
| `currencyCode` ==String== | The currency code for the cart.                                                       |
| `cultureName` ==String==| The culture or locale name for the cart.                                                |
| `cartType` ==String==   | The type or category of the cart.                                                       |
| `lineItemId` ==String== | The Id of the specific item within the cart for which the quantity is being changed.    |
| `quantity` ==Int!==     | The new quantity value to be set for the item.                                          |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation changeCartItemQuantity($command: InputChangeCartItemQuantityType!) {
  changeCartItemQuantity(command: $command) {
    id
    items {
      id
      name
      quantity
    }
    total {
      amount
    }
  }
}
```

```json title="Variables"
"command": {
  "cartId": "e6a7d5af-6378-44a6-b645-af9ecf702c05",
  "storeId": "B2B-store",
  "cartName": "default",
  "userId": "c50e5237-8a4c-41fe-b878-8e5a72390a08",
  "cartType": "null",
  "currencyCode": "USD",
  "cultureName":"en-US",
  "lineItemId": "e3ce8982-b5d7-4246-8d1a-840ed52368d4",
  "quantity": 1
}
```

</div>