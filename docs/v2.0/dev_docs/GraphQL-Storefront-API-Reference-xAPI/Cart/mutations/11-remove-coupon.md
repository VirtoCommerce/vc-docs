# RemoveCoupon

This mutation removes coupon from cart.

## Query

```json
mutation ($command:InputRemoveCouponType!)
{
    (command: $command)
    {
        name
        coupons
        {
        	code
            isAppliedSuccessfully
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
    "couponCode": "freeItemsCouponCode",
}
```