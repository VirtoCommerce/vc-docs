# UpdateOrderItemDynamicProperties ==~mutation~==

This mutation updates the dynamic properties for the order item.

## Arguments

The `InputUpdateOrderItemDynamicPropertiesType` is a type that represents the input object for updating dynamic properties of an order item.

## Fields

| Field                                     | Description                                                                                  |
|-------------------------------------------|----------------------------------------------------------------------------------------------|
| `orderId`  ==String==                     | The Id of the order for which the order item's dynamic properties will be updated.           |
| `lineItemId`  ==String==                  | The Id of the order item for which the dynamic properties will be updated.                   |
| `dynamicProperties` [ ==[InputDynamicPropertyValueType]!== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Profile/Objects/InputDynamicPropertyValueType) | The dynamic property value types representing the updated dynamic properties of the order item.|

## Possible returns

| Possible return                                                       | Description          	|
|-----------------------------------------------------------------------|---------------------	|
| [`CustomerOrderType`](../objects/customer-order-type.md)           	|  A customer order  	|



## Example

<div class="grid" markdown>

```json title="Mutation"
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

```json title="Variables"
{
  "command": {
    "orderId": "2be32440-ee84-4dd5-aa9b-fcbe35bf61f0",
    "lineItemId": "testlineitemid",
    "dynamicProperties": [
      {
        "name": "property1",
        "value": "value1"
      }
    ]
  }
}
```

</div>