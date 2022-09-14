# RemoveShipment

This mutation removes shipping methods from the cart.

## Query

```json
mutation ($command:InputRemoveShipmentType!)
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
    "shipmentId": "7777-7777-7777-7777",
}
```