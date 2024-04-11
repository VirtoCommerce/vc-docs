# UpdateOrderItemDynamicProperties ==~mutation~==

This mutation updates the dynamic properties for the order item.

## Arguments

The `InputUpdateOrderItemDynamicPropertiesType` is a type that represents the input object for updating dynamic properties of an order item.

## Fields

| Field                                     | Description                                                                                  |
|-------------------------------------------|----------------------------------------------------------------------------------------------|
| `orderId`  ==String==                     | The Id of the order for which the order item's dynamic properties will be updated.           |
| `lineItemId`  ==String==                  | The Id of the order item for which the dynamic properties will be updated.                   |
| `dynamicProperties` [ ==[InputDynamicPropertyValueType]!== ](../../Profile/Objects/InputDynamicPropertyValueType.md) | The dynamic property value types representing the updated dynamic properties of the order item.|

## Possible returns

| Possible return                                                       | Description          	|
|-----------------------------------------------------------------------|---------------------	|
| [`CustomerOrderType`](../objects/customer-order-type.md)           	|  A customer order  	|


=== "Mutation"
    ```json linenums="1"
    mutation updateOrderItemDynamicProperties ($command: InputUpdateOrderItemDynamicPropertiesType!) {
        updateOrderItemDynamicProperties (command: $command)
        {
            id
            items{
                dynamicProperties
                {
                    value
                    name
                }
            }
        }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
    "command": {
        "orderId": "2be32440-ee84-4dd5-aa9b-fcbe35bf61f0",
        "lineItemId": "testlineitemid",
        "dynamicProperties": [
        {
            "name": "propery1",
            "value": "value1"
        }
        ]
    }
    }
    ```

