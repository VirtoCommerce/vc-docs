# unselectAllCartItems ==~mutation~==

This mutation allows you to unselect all cart items within a shopping cart.

## Arguments

The `InputChangeCartItemsSelectedType` represents a set of input parameters for unselecting all cart items. 

| Field                            | Description                                                          |
|----------------------------------|----------------------------------------------------------------------|
| `cartId` {==String==}            | The Id of the cart.                                                  |
| `storeId` {==String!==}          | The Id of the store.                                                 |
| `cartName` {==String==}          | The name or description of the cart.                                 |
| `userId` {==String!==}           | The Id of the user.                                                  |
| `currencyCode` {==String==}      | The currency code for the cart.                                      |
| `cultureName` {==String==}       | The culture or locale name for the cart.                             |
| `cartType` {==String==}          | The type of the cart.                                                |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation unselectAllCartItems($command: InputChangeAllCartItemsSelectedType!) {
      unselectAllCartItems(command: $command) {
        id
        items {
          id
          name
          selectedForCheckout
        }
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    "command":{
      "storeId": "B2B-store",
      "userId": "23a7f0e9-0186-4293-b511-bf894583fd3b",
      "cartId": "3095ebfe-1de6-4a75-9774-2c4dfdb3d002",
      "currencyCode": "USD",
      "cultureName": "en-US",
      "cartName": "default",
    }
    ```