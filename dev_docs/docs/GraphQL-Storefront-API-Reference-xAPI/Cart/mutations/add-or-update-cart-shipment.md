# addOrUpdateCartShipment ==~mutation~==

This mutation:

* Adds or updates cart shipping methods. 
* Supports partial update, with all fields in `command.shipment` and `command.shipment.deliveryAddress` being optional.

## Arguments

The `InputAddOrUpdateCartShipmentType` represents the input object type used for adding or updating a shipment for a cart. 

| Field                                 | Description                                                        |
|---------------------------------------|--------------------------------------------------------------------|
| `cartId` {==String==}                 | The Id of the cart to which the shipment will be added or updated. |
| `storeId` {==String!==}               | The Id of the store associated with the cart.                      |
| `cartName` {==String==}               | The name of the cart.                                              |
| `userId` {==String==}                 | The Id of the user who owns the cart.                              |
| `currencyCode` {==String==}           | The currency code for the cart.                                    |
| `cultureName` {==String==}            | The culture or language associated with the cart.                  |
| `cartType` {==String==}               | The type of the cart.                                              |
| `shipment` {==InputShipmentType!==}   | The shipment details to be added or updated for the cart.          |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation($command: InputAddOrUpdateCartShipmentType!) {
      addOrUpdateCartShipment(command: $command) {
        name
        availableShippingMethods {
          code
          optionName
          optionDescription
        }
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    "command": {
      "storeId": "B2B-store",
      "cartName": "default",
      "userId": "c50e5237-8a4c-41fe-b878-8e5a72390a08",
      "cultureName": "en-US",
      "currencyCode": "USD",
      "cartType": "cart",
      "shipment": {
        "fulfillmentCenterId": "7777-7777-7777-7777",
        "height": 7,
        "shipmentMethodCode": "code",
        "currency": "USD",
        "price": 98,
        "dynamicProperties": [
          {
            "name": "ShipmentProperty",
            "value": "test value"
          }
        ]
      },
    }
    ```

[See all parametrs for the Shipment object](https://github.com/VirtoCommerce/vc-module-experience-api/blob/dev/src/XPurchase/VirtoCommerce.XPurchase/Schemas/InputShipmentType.cs){ .md-button }