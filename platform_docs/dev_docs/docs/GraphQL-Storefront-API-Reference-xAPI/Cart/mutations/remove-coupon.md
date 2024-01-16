# removeCoupon ==~mutation~==

This mutation removes coupon from cart.

## Arguments

The `InputRemoveCouponType` represents the input object type used for removing a coupon from a cart. 

| Field                            | Description                                                        |
|----------------------------------|--------------------------------------------------------------------|
| `cartId` {==String==}            | The Id of the cart from which the coupon is to be removed.         |
| `storeId` {==String!==}          | The Id of the store associated with the cart.                      |
| `cartName` {==String==}          | The name of the cart.                                              |
| `userId` {==String==}            | The Id of the user who owns the cart.                              |
| `currencyCode` {==String==}      | The currency code for the cart.                                    |
| `cultureName` {==String==}       | The culture or language associated with the cart.                  |
| `cartType` {==String==}          | The type of the cart.                                              |
| `couponCode` {==String==}        | The coupon code to be removed from the cart.                       |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation removeCoupon($command: InputRemoveCouponType!) {
      removeCoupon(command: $command) {
        id
        name
        customerName
        coupons {
          code
          isAppliedSuccessfully
        }
        discounts {
          coupon
        }
        discountTotal {
          amount
        }
      }
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
      "couponCode": "CouponXAPI"
    }
    ```