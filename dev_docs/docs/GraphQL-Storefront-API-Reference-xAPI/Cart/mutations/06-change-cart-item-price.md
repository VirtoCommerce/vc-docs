# ChangeCartItemPrice

This mutation changes the cart item price.

## Query

```json
mutation ($command:InputChangeCartItemPriceType!)
{
    (command: $command)
    {
        id
        items
        {
            sku
            productId
            listPrice
            listPriceWithTax
            salePrice
            salePriceWithTax
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
    "productId": "9cbd8f316e254a679ba34a900fccb076",
    "price": 777
}
```