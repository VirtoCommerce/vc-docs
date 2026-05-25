# removeCart ==~mutation~==

This mutation allows you to remove a cart.

## Arguments

The `InputRemoveItemType` represents the input object type used for removing an item from a cart. 

| Field                            | Description                                                    |
|----------------------------------|----------------------------------------------------------------|
| `cartId`  ==String==             | The Id of the cart from which the item will be removed.        |
| `storeId`  ==String!==           | The Id of the store associated with the cart.                  |
| `cartName`  ==String==           | The name of the cart.                                          |
| `userId`  ==String==             | The Id of the user who owns the cart.                          |
| `currencyCode`  ==String==       | The currency code for the cart.                                |
| `cultureName`  ==String==        | The culture or language associated with the cart.              |
| `cartType`  ==String==           | The type of the cart.                                          |
| `lineItemId`  ==String==         | The Id of the item to be removed from the cart.                |


## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|




## Example

<div class="grid" markdown>

```json title="Mutation"
mutation ($command:InputRemoveCartType!){
  removeCart(command: $command)
}
```

```json title="Variables"
"command": {
  "cartId": "e6a7d5af-6378-44a6-b645-af9ecf702c05"
}
```

</div>