# clearShipments

This mutation removes all shipping methods from the cart.

## Arguments

The `InputClearShipmentsType` represents the input object type used for clearing all shipments from a cart. 

| Field                            | Description                                                    |
|----------------------------------|----------------------------------------------------------------|
| `cartId` {==String==}            | The Id of the cart from which all shipments will be cleared.   |
| `storeId` {==String!==}          | The Id of the store associated with the cart.                  |
| `cartName` {==String==}          | The name of the cart.                                          |
| `userId` {==String==}            | The Id of the user who owns the cart.                          |
| `currencyCode` {==String==}      | The currency code for the cart.                                |
| `cultureName` {==String==}       | The culture or language associated with the cart.              |
| `cartType` {==String==}          | The type of the cart.                                          |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|--------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation clearShipments($command: InputClearShipmentsType!) {
      clearShipments(command: $command) {
        id
        shipments {
          id
          shipmentMethodCode
          shipmentMethodOption
          deliveryAddress {
            id
            line1
            line2
          }
        }
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
      "cultureName": "en-US",
      "currencyCode": "USD",
      "cartType": "cart"
    }
    ```