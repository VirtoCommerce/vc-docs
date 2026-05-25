# removeShipment ==~mutation~==

This mutation removes shipping methods from the cart.

## Arguments

The `InputRemoveShipmentType` represents the input object type used for removing a shipment from a cart. 

| Field                             | Description                                                           |
|-----------------------------------|-----------------------------------------------------------------------|
| `cartId`  ==String==              | The Id of the cart from which the shipment is to be removed.          |
| `storeId`  ==String!==            | The Id of the store associated with the cart.                         |
| `cartName`  ==String==            | The name of the cart.                                                 |
| `userId`  ==String==              | The Id of the user who owns the cart.                                 |
| `currencyCode`  ==String==        | The currency code for the cart.                                       |
| `cultureName`  ==String==         | The culture or language associated with the cart.                     |
| `cartType`  ==String==            | The type of the cart.                                                 |
| `shipmentId`  ==String==         | The Id of the shipment to be removed from the cart.                   |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|



## Example

<div class="grid" markdown>

```json title="Mutation"
    mutation removeShipment($command: InputRemoveShipmentType!) {
      removeShipment(command: $command) {
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

```json title="Variables"
"command": {
  "cartId": "e6a7d5af-6378-44a6-b645-af9ecf702c05",
  "storeId": "B2B-Store",
  "cartName": "default",
  "userId": "c50e5237-8a4c-41fe-b878-8e5a72390a08",
  "currencyCode": "USD",
  "cultureName":"en-US",
  "cartType": "null",
  "shipmentId": "80e594ba-23ae-4da3-8981-d48c0c2f1141"
}
```

</div>