# UpdateOrderPaymentDynamicProperties

This mutation updates dynamic properties for the order payment.

## Query

```
mutation ($command: InputUpdateOrderPaymentDynamicPropertiesType!)
{
    updateOrderPaymentDynamicProperties(command: $command)
    {
        inPayments
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

#### Variables

```
"command": {
    "orderId": "d548c750-5a74-4e54-b72b-f5209f44caa6",
    "paymentId": "0859f1e8-16e8-4924-808b-47e03560085d",
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