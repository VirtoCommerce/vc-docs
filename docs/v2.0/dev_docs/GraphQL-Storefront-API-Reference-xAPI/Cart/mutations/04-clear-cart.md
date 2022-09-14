# ClearCart

This mutation removes all items from the cart, resets promotion rewards based on the amount of items, and saves the cart.

## Query

```json
mutation ($command:InputClearCartType!)
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

## Variables

```json
"command": {
    "storeId": "Electronics",
    "cartName": "default",
    "userId": "b57d06db-1638-4d37-9734-fd01a9bc59aa",
    "cultureName": "en-US",
    "currencyCode": "USD",
    "cartType": "cart"
}
```