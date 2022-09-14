# AddOrUpdateCartPayment

This mutation adds or updates cart payment. It supports partial update, with all fields in `command.payment` and `command.payment.billingAddress` being optional.

## Query

```json
mutation ($command:InputAddOrUpdateCartPaymentType!)
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
    "cartType": "cart",
    "payment": {
        "outerId": "7777-7777-7777-7777",
        "paymentGatewayCode": "code",
        "currency": "USD",
        "price": 98,
        "amount": 55,
        "dynamicProperties": [
            {
                "name": "PaymentProperty",
                "value": "test value"
            }
        ]
    },
}
```

!!! tip
	To see all possible parametrs for the `payment` object, check out our [GitHub repository](https://github.com/VirtoCommerce/vc-module-experience-api/blob/dev/src/XPurchase/VirtoCommerce.XPurchase/Schemas/InputPaymentType.cs).