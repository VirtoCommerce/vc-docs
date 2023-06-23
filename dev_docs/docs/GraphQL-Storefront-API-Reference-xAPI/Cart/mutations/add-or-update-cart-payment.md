# AddOrUpdateCartPayment ==~mutation~==

This mutation:

* Adds or updates cart payment. 
* Supports partial update, with all fields in `command.payment` and `command.payment.billingAddress` being optional.

## Arguments

The `InputAddOrUpdateCartPaymentType` represents the input object type used for adding or updating a payment for a cart.

| Field                   | Description                                                      |
|-------------------------|------------------------------------------------------------------|
| `cartId` {==String==}                 | The ID of the cart to which the payment will be added or updated.   |
| `storeId` {==String!==}              | The ID of the store associated with the cart.                       |
| `cartName` {==String==}               | The name of the cart.                                              |
| `userId` {==String==}                 | The ID of the user who owns the cart.                               |
| `currencyCode` {==String==}           | The currency code for the cart.                                    |
| `cultureName` {==String==}            | The culture or language associated with the cart.                   |
| `cartType` {==String==}               | The type of the cart.                                              |
| `payment` {==InputPaymentType!==} | The payment details to be added or updated for the cart.           |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
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

=== "Variables"
    ```json linenums="1"
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

[See all parameters for the Payment object](https://github.com/VirtoCommerce/vc-module-experience-api/blob/dev/src/XPurchase/VirtoCommerce.XPurchase/Schemas/InputPaymentType.cs){ .md-button }