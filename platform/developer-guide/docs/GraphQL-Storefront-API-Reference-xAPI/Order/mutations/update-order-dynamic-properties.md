# UpdateOrderDynamicProperties ==~mutation~==

This mutation updates the dynamic properties of the order.

## Arguments

The `InputUpdateOrderDynamicPropertiesType` is a type that represents the input object for updating dynamic properties of an order. 

| Field                                                                                                                   | Description                                                                            |
|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `orderId`  ==String==                                                                                                   | The Id of the order for which the dynamic properties will be updated.                  |
| `dynamicProperties` [ ==[InputDynamicPropertyValueType]!== ](../../Profile/Objects/InputDynamicPropertyValueType.md)    | Dynamic property value types representing the updated dynamic properties of the order. |

## Possible returns

| Possible return                                                       | Description          	|
|-----------------------------------------------------------------------|---------------------	|
| [`CustomerOrderType`](../objects/customer-order-type.md)           	|  A customer order.  	|


=== "Mutation"
    ```json linenums="1"
    mutation updateOrderDynamicProperties ($command: InputUpdateOrderDynamicPropertiesType!) {
        updateOrderDynamicProperties (command: $command)
        {
            id
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
        "dynamicProperties": [
        {
            "name": "propery1",
            "value": "value1"
        }
        ]
      }
    }
    ```

