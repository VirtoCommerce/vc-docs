# AddOrUpdateCartShipment

This mutation adds or updates cart shipping methods. It supports partial update, with all fields in `command.shipment` and `command.shipment.deliveryAddress` being optional.

## Query

```json
mutation ($command:InputAddOrUpdateCartShipmentType!)
{
    (command: $command)
    {
        name
        availableShippingMethods
        {
          code
          optionName
          optionDescription
        }
    }
}
```

## Variables

```json
"command": {
    "storeId": "Electronics",
    "cartName": "default",
    "userId": "b57d06db-1638-4d37-9734-fd01a9bc59aa",
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

!!! tip
	To see all possible parametrs for the `shipment` object, check out our [GitHub repository](https://github.com/VirtoCommerce/vc-module-experience-api/blob/dev/src/XPurchase/VirtoCommerce.XPurchase/Schemas/InputShipmentType.cs).