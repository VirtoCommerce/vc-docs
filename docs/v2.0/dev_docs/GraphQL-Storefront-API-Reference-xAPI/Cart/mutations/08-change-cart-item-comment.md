# ChangeCartItemComment

This mutation changes cart item comments.

## Query

```json
mutation ($command:InputChangeCartItemCommentType!)
{
    (command: $command)
    {
        id
        items
        {
            sku
            productId
            comment
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
    "lineItemId": "9cbd8f316e254a679ba34a900fccb076",
    "comment": "nice product"
}
```