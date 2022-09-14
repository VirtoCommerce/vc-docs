# MergeCart

This mutation merges two carts. You can use it to merge an anonymous cart with a user cart after user authentication.

## Query

```json
mutation ($command:InputMergeCartType!)
{
    (command: $command)
    {
        id
        isAnonymous
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
    "secondCartId": "7777-7777-7777-7777",
}
```