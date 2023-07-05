# UpdateOrderShipmentDynamicProperties

This mutation updates dynamic properties for the order shipping method.

## Query

```
mutation ($command: InputUpdateOrderShipmentDynamicPropertiesType!)
{
    updateOrderShipmentDynamicProperties(command: $command)
    {
        shipments
        {
            id
            dynamicProperties
            {
                name
                value
                valueType
                dictionaryItem
                {
                    label
                    name
                    id
                }
            }
        }
    }
}
```

#### Variables:

```
"command": {
    "orderId": "d548c750-5a74-4e54-b72b-f5209f44caa6",
    "shipmentId": "79b8f095-9740-4353-998b-e1c4dd577ee6",
    "dynamicProperties": [
        {
            "name": "Example string property",
            "value": "12345678"
        },
        {
            "name": "Example multilanguage property",
            "locale":"de-DE",
            "value": "hallo welt"
        },
        {
            "name": "Example dictionary property",
            "value": "578fadeb1d2a40b3b08b1daf8db09463"
        }
  	]
  }
}
```