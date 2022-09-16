# ValidateCoupon

This mutation validates coupons.

## Query

```json
mutation ($command:InputValidateCouponType!)
{
    (command: $command)
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
    "coupon": {
        "code": "freeItemsCouponCode"
    },
}
```