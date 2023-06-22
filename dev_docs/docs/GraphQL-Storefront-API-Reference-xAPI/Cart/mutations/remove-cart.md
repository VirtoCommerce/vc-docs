# RemoveCart ==~mutation~==
This mutation allows you to remove a cart.

## Arguments

The `InputRemoveItemType` represents the input object type used for removing an item from a cart. 

| Field              | Description                                                    |
|--------------------|----------------------------------------------------------------|
| `cartId` {==String==}            | The ID of the cart from which the item will be removed.               |
| `storeId` {==String!==}         | The ID of the store associated with the cart.                         |
| `cartName` {==String==}          | The name of the cart.                                                |
| `userId` {==String==}            | The ID of the user who owns the cart.                                 |
| `currencyCode` {==String==}      | The currency code for the cart.                                      |
| `cultureName` {==String==}       | The culture or language associated with the cart.                     |
| `cartType` {==String==}          | The type of the cart.                                                |
| `lineItemId` {==String==}        | The ID of the item to be removed from the cart.                       |


## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation ($command:InputRemoveCartType!)
    {
        (command: $command)
    }
    ```

=== "Variables"
    ```json linenums="1"
    "command": {
        "cartId": "7777-7777-7777-7777"
    }
    ```