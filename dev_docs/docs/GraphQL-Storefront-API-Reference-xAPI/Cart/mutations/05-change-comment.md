# ChangeComment

This mutation changes the cart comments.

## Query

```json
mutation ($command:InputChangeCommentType!)
{
    (command: $command)
    {
        name
        comment
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
    "comment": "Hi, Virto! :)"
}
```