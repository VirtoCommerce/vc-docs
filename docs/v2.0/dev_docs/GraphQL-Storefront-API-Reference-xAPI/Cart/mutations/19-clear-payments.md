# ClearPayments

This mutation removes all payment methods from the cart.

## Query

```json
mutation ($command:InputClearPaymentsType!)
{
    (command: $command)
    {
        name
        availablePaymentMethods
        {
          code
          name
          paymentMethodType
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
    "cartType": "cart"
}
```