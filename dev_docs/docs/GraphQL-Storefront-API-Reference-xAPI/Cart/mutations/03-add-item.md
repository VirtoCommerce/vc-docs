# AddItem

This mutation validates an item and adds it to the cart; it also recalculates promotion rewards and taxes and applies it to the cart.

## Query

```
mutation ($command:InputAddItemType!)
{
    (command: $command)
    {
        name
        items
        {
            id
            sku
        }
        itemsCount
        itemsQuantity
    }
}
```

#### Variables

```json
"command": {
    "storeId": "Electronics",
    "cartName": "default",
    "userId": "b57d06db-1638-4d37-9734-fd01a9bc59aa",
    "cultureName": "en-US",
    "currencyCode": "USD",
    "cartType": "cart",
    "productId": "9cbd8f316e254a679ba34a900fccb076",
    "quantity": 1,
    "dynamicProperties": [
        {
            "name": "ItemProperty",
            "value": "test value"
        }
    ]
}
```