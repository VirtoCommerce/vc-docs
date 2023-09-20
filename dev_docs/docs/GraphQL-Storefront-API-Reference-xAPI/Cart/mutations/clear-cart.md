# clearCart ==~mutation~==

This mutation:

* Removes all items from the cart.
* Resets promotion rewards based on the amount of items.
* Saves the cart.

## Arguments

The `InputClearCartType` represents the arguments for the ClearCart operation. 

| Field                                   | Description                                                 |
|-----------------------------------------|-------------------------------------------------------------|
| `cartId` {==String==}                   | The Id of the cart.                                         |
| `storeId` {==String!==}                 | The Id of the store.                                        |
| `cartName` {==String==}                 | The name of the cart.                                       |
| `userId` {==String!==}                  | The Id of the user.                                         |
| `currencyCode` {==String==}             | The currency code for the cart.                             |
| `cultureName` {==String==}              | The culture or locale name for the cart.                    |
| `cartType` {==String==}                 | The type or category of the cart.                           |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation($command: InputClearCartType!) {
      clearCart(command: $command) {
        name
        items {
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
      "cartId": "e6a7d5af-6378-44a6-b645-af9ecf702c05",
      "storeId": "B2B-store",
      "cartName": "default",
      "userId": "c50e5237-8a4c-41fe-b878-8e5a72390a08",
      "currencyCode": "USD",
      "cultureName":"en-US",
      "cartType": "null"
    }
    ```