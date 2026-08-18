# addCoupon ==~mutation~==

This mutation checks and adds coupons to a cart.

## Arguments

The `InputAddCouponType` represents the input object type used for adding a coupon to a cart.

| Field                        | Description                                                        |
|------------------------------|--------------------------------------------------------------------|
| `cartId` ==String==          | The ID of the cart to which the coupon code is to be applied.      |
| `storeId` ==String!==        | The ID of the store associated with the cart.                      |
| `cartName` ==String==        | The name of the cart.                                              |
| `userId` ==String==          | The ID of the user who owns the cart.                              |
| `currencyCode` ==String==    | The currency code for the cart.                                    |
| `cultureName` ==String==     | The culture or language associated with the cart.                  |
| `cartType` ==String==        | The type of the cart.                                              |
| `couponCode` ==String!==     | The coupon code to apply to the cart.                              |


## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|






## Example

<div class="grid" markdown>

```json title="Mutation"
mutation addCoupon($command: InputAddCouponType!) {
  addCoupon(command: $command) {
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

```json title="Variables"
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

</div>