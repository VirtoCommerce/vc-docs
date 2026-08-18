# removeCartItem ==~mutation~==

This mutation enables removing an item from the cart.

## Arguments

The `InputRemoveItemType` represents the input object type used for removing a specific item from a cart.

| Field                           | Description                                                        |
|---------------------------------|--------------------------------------------------------------------|
| `cartId`  ==String==            | The ID of the cart from which the item is to be removed.           |
| `storeId`  ==String!==          | The ID of the store associated with the cart.                      |
| `cartName`  ==String==          | The name of the cart.                                              |
| `userId`  ==String==            | The ID of the user who owns the cart.                              |
| `currencyCode`  ==String==      | The currency code for the cart.                                    |
| `cultureName`  ==String==       | The culture or language associated with the cart.                  |
| `cartType`  ==String==          | The type of the cart.                                              |
| `lineItemId`  ==String==        | The ID of the line item to be removed from the cart.               |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|--------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


## Example

<div class="grid" markdown>

```json title="Mutation"
    mutation removeCartItem ($command: InputRemoveItemType!) {
      removeCartItem (command: $command) {
        items{
          id
          quantity
          product{
            id
          }
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
  "lineItemId": "a3c9e72a-5b33-48c2-90b4-780886f54ec8"
}
```

</div>