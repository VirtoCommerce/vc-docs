# UpdateOrderPaymentDynamicProperties ==~mutation~==

This mutation updates dynamic properties for the order payment.

## Arguments

The `InputUpdateOrderPaymentDynamicPropertiesType` is a type that represents the input object for updating dynamic properties of an order payment.

## Fields

| Field                                     | Description                                                                                                   |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `orderId`  ==String==                     | An optional identifier of the order for which the order payment's dynamic properties will be updated.        |
| `paymentId`  ==String==                   | An optional identifier of the order payment for which the dynamic properties will be updated.                |
| `dynamicProperties` [ ==[InputDynamicPropertyValueType]!== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Profile/Objects/InputDynamicPropertyValueType) | Dynamic property value types representing the updated dynamic properties of the order payment.|

## Possible returns

| Possible return                                                       | Description          	|
|-----------------------------------------------------------------------|---------------------	|
| [`CustomerOrderType`](../objects/customer-order-type.md)           	|  A customer order.  	|


=== "Mutation"
    ```json linenums="1"
    mutation updateOrderPaymentDynamicProperties ($command: InputUpdateOrderPaymentDynamicPropertiesType!) {
        updateOrderPaymentDynamicProperties (command: $command)
        {
            id
            inPayments{
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
    "command": {
    "orderId":  "2be32440-ee84-4dd5-aa9b-fcbe35bf61f0",
    "paymentId":  "testpaymentid",
    "dynamicProperties": [
        {"name": "propery1",
        "value": "value1"}
    ]

    }
    ```

