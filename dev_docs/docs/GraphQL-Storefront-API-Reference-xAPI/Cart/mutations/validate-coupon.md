# validateCoupon ==~mutation~==

This mutation validates coupons.

## Arguments

The `InputValidateCouponType` represents the input object type used for validating a coupon for a cart.

| Field                          | Description                                                      |
|--------------------------------|------------------------------------------------------------------|
| `cartId` {==String==}          | The Id of the cart for which the coupon will be validated.       |
| `storeId` {==String!==}        | The Id of the store associated with the cart.                    |
| `cartName` {==String==}        | The name of the cart.                                            |
| `userId` {==String==}          | The Id of the user who owns the cart.                            |
| `currencyCode` {==String==}    | The currency code for the cart.                                  |
| `cultureName` {==String==}     | The culture or language associated with the cart.                |
| `cartType` {==String==}        | The type of the cart.                                            |
| `coupon` {==String==}          | The coupon code to be validated for the cart.                    |


=== "Mutation"
    ```json linenums="1"
    mutation ($command:InputValidateCouponType!){
      validateCoupon(command: $command)
    }
    ```

=== "Variables"
    ```json linenums="1"
    "command": {
      "cartId": "e6a7d5af-6378-44a6-b645-af9ecf702c05",
      "storeId": "B2B-store",
      "cartName": "default",
      "userId": "c50e5237-8a4c-41fe-b878-8e5a72390a08",
      "currencyCode": "USD",
      "cultureName":"en-US",
      "cartType": "null",
      "coupon": ""
      },
    }
    ```