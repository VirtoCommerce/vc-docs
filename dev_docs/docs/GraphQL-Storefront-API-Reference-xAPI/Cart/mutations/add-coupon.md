# AddCoupon ==~mutation~==

This mutation checks and adds coupons to a cart.

## Arguments

The `InputAddCouponType` represents the input object type used for adding a coupon to a cart.

| Field                          | Description                                                        |
|--------------------------------|--------------------------------------------------------------------|
| `cartId` {==String==}          | The ID of the cart to which the coupon code is to be applied.      |
| `storeId` {==String!==}        | The ID of the store associated with the cart.                      |
| `cartName` {==String==}        | The name of the cart.                                              |
| `userId` {==String==}          | The ID of the user who owns the cart.                              |
| `currencyCode` {==String==}    | The currency code for the cart.                                    |
| `cultureName` {==String==}     | The culture or language associated with the cart.                  |
| `cartType` {==String==}        | The type of the cart.                                              |
| `couponCode` {==String!==}     | The coupon code to apply to the cart.                              |


## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation ($command:InputAddCouponType!)
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

=== "Variables"
    ```json linenums="1"
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