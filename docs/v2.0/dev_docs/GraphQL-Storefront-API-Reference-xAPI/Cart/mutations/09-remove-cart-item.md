# RemoveCartItem

This mutation enables removing an item from the cart.

## Query

```json
mutation ($command:InputRemoveItemType!)
{
    (command: $command)
    {
        id
        items
        {
            sku
            productId
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
    "cartType": "cart",
    "lineItemId": "9cbd8f316e254a679ba34a900fccb076",
}
```