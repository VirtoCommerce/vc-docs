# changePurchaseOrderNumber ==~mutation~==

This mutation changes purchase order number.

## Arguments

The `InputChangePurchaseOrderNumber` represents the input object for changing the purchase order number of a cart.

| Field                      | Description                                                                                  |
|----------------------------|----------------------------------------------------------------------------------------------|
| `cartId` {==String==}      | The Id of the cart where the purchase order number needs to be changed.                      |
| `storeId` {==String!==}    | The Id of the store associated with the cart.                                                |
| `cartName` {==String==}    | The name of the cart.                                                                        |
| `userId` {==String!==}     | The Id of the user who owns the cart.                                                        |
| `currencyCode` {==String==}| The currency code associated with the cart.                                                  |
| `cultureName` {==String==} | The language to retrieve data in.                                                            |
| `cartType` {==String==}    | The type of the cart (optional).                                                             |
| `purchaseOrderNumber` {==String==} | The new purchase order number to be set for the cart.                                |


## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|--------------------------------------------------------------	|
| [`CartType`](../../Cart/objects/cart-type.md)           	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation changePurchaseOrderNumber ($command: InputChangePurchaseOrderNumber!) {
      changePurchaseOrderNumber (command: $command) {
      id
        name
        purchaseOrderNumber
      addresses
        {
          id
        }
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    "command": {
      "storeId": "2be32440-ee84-4dd5-aa9b-fcbe35bf61f0",
      "userId": "23eed211-ee84-4dd5-aa9b-dsacg32210",
        "purchaseOrderNumber": "test purchase order"
    }
    ```
