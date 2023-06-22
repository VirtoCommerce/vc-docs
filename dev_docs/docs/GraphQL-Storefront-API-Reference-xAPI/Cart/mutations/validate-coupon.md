# ValidateCoupon ==~mutation~==

This mutation validates coupons.

## Arguments

The `InputValidateCouponType` represents the input object type used for validating a coupon for a cart.

| Field                          | Description                                                      |
|--------------------------------|------------------------------------------------------------------|
| `cartId` {==String==}          | The ID of the cart for which the coupon will be validated.       |
| `storeId` {==String!==}        | The ID of the store associated with the cart.                    |
| `cartName` {==String==}        | The name of the cart.                                            |
| `userId` {==String==}          | The ID of the user who owns the cart.                            |
| `currencyCode` {==String==}    | The currency code for the cart.                                  |
| `cultureName` {==String==}     | The culture or language associated with the cart.                |
| `cartType` {==String==}        | The type of the cart.                                            |
| `coupon` {==String==}          | The coupon code to be validated for the cart.                    |


=== "Mutation"
    ```json linenums="1"
    mutation ($command:InputValidateCouponType!)
    {
        (command: $command)
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
        "coupon": {
            "code": "freeItemsCouponCode"
        },
    }
    ```