# ClearCart ==~mutation~==

This mutation:

* Removes all items from the cart.
* Resets promotion rewards based on the amount of items.
* Saves the cart.

## Arguments

The `InputClearCartType` represents the arguments for the ClearCart operation. 

| Field                                | Description                                                                                  |
|------------------------------------ ----|----------------------------------------------------------------------------------------------|
| `cartId` {==String==}                   | The identifier of the cart.                                                                  |
| `storeId` {==String!==}                 | The identifier of the store.                                                                 |
| `cartName` {==String==}                 | The name of the cart.                                                                        |
| `userId` {==String!==}                  | The identifier of the user.                                                                  |
| `currencyCode` {==String==}             | The currency code for the cart.                                                              |
| `cultureName` {==String==}              | The culture or locale name for the cart.                                                     |
| `cartType` {==String==}                 | The type or category of the cart.                                                            |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"

    mutation ($command:InputClearCartType!)
    {
        (command: $command)
        {
            name
            items
            {
                id
                sku
            }
            itemsCount
            itemsQuantity
        }
    }
    ```

=== "Variables"
    ```json linenums="1"

    "command": {
        "storeId": "Electronics",
        "cartName": "default",
        "userId": "b57d06db-1638-4d37-9734-fd01a9bc59aa",
        "cultureName": "en-US",
        "currencyCode": "USD",
        "cartType": "cart"
    }
    ```