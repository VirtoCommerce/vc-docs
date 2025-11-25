# UpdateOrderShipmentDynamicProperties ==~mutation~==

This mutation updates dynamic properties for the order shipping method.

## Arguments

The `InputUpdateOrderShipmentDynamicPropertiesType` is a type that represents the input object for updating dynamic properties of an order shipment.

## Fields

| Field                                                                                                                | Description                                                                                   |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| `orderId`  ==String==                                                                                                | The Id of the order for which the order shipment's dynamic properties will be updated.        |
| `shipmentId`  ==String==                                                                                             | The Id of the order shipment for which the dynamic properties will be updated.                |
| `dynamicProperties` [ ==[InputDynamicPropertyValueType]!== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Profile/Objects/InputDynamicPropertyValueType) | The dynamic property value types representing the updated dynamic properties of the order shipment.|


## Possible returns

| Possible return                                                       | Description          	|
|-----------------------------------------------------------------------|---------------------	|
| [`CustomerOrderType`](../objects/customer-order-type.md)           	|  A customer order.  	|


=== "Mutation"
    ```json linenums="1"
    mutation updateOrderShipmentDynamicProperties ($command: InputUpdateOrderShipmentDynamicPropertiesType!)  
    updateOrderShipmentDynamicProperties (command: $command)
    {
        id
        shipments{
            dynamicProperties
            {
                value
                name
            }
        }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
    "command": {
        "orderId": "2be32440-ee84-4dd5-aa9b-fcbe35bf61f0",
        "shipmentId": "testshipmentid",
        "dynamicProperties": [
        {
            "name": "propery1",
            "value": "value1"
        }
        ]
    }
    }
    ```

