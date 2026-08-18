# updateCartPaymentDynamicProperties ==~mutation~==

This mutation updates dynamic properties for the cart payment method.

## Arguments

The `InputUpdateCartPaymentDynamicPropertiesType` represents the input object type used for updating dynamic properties of a specific cart payment. 

| Field                                  | Description                                                                |
|----------------------------------------|----------------------------------------------------------------------------|
| `cartId`  ==String==                   | The Id of the cart containing the payment to update the dynamic properties.|
| `storeId`  ==String!==                 | The Id of the store associated with the cart.                              |
| `cartName`  ==String==                 | The name of the cart.                                                      |
| `userId`  ==String==                   | The Id of the user who owns the cart.                                      |
| `currencyCode`  ==String==             | The currency code for the cart.                                            |
| `cultureName`  ==String==              | The culture or language associated with the cart.                          |
| `cartType`  ==String==                 | The type of the cart.                                                      |
| `paymentId`  ==String==                | The Id of the cart payment to update the dynamic properties.               |
| `dynamicProperties`  ==[InputDynamicPropertyValueType]!==  | The updated dynamic properties of the cart payment.    |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation updateCartShipmentDynamicProperties(
  $command: InputUpdateCartShipmentDynamicPropertiesType!
) {
  updateCartShipmentDynamicProperties(command: $command) {
    id
    shipments {
      id
      dynamicProperties {
        name
        value
        valueType
        dictionaryItem {
          label
          name
          id
        }
      }
    }
  }
}
```

```json title="Variables"
"command": {
  "cartId": "e6a7d5af-6378-44a6-b645-af9ecf702c05",
  "storeId": "B2B-Store",
  "userId": "c50e5237-8a4c-41fe-b878-8e5a72390a08",
  "currencyCode": "USD",
  "cultureName": "en-US",
  "cartName": "default",
  "shipmentId":"3de4c66b-c178-44c2-87d1-8fe2a3e392c0",
  "dynamicProperties": [
    {
      "name": "Purchase order number",
      "value": "Test22"
    },
    {
      "name": "Shipment_decimal",
      "value": "2.6"
    },
    {
      "name": "Shipment_decimal",
      "value": "4.55"
    },
    {
      "name": "Shipment_Integer_multi",
      "value": "23"
    },
    {
      "name": "Shipment_Integer_multi",
      "value": "66"
    }
  ]
}
```

</div>