# addCoupon ==~mutation~==

This mutation allows you to add a coupon to a cart.

## Arguments

The `InputAddCouponType!` represents the input object for adding a coupon to a cart.

| Field                       | Description                                      |
|-----------------------------|--------------------------------------------------|
| `storeId`  ==String!==      | The Id of the store.                             |
| `userId`  ==String!==       | The Id of the user.                              |
| `couponCode`  ==String!==   | The coupon code.                                 |
| `cartId`  ==String==        | The Id of the cart.                              |
| `cartName`  ==String==      | The name of the cart.                            |
| `currencyCode`  ==String==  | The currency code.                               |
| `cultureName`  ==String==   | A language to retrieve data in.                  |
| `cartType`  ==String==      | The type of the cart.                            |

## Possible returns

| Possible return                           | Description                                                         |
|-------------------------------------------|---------------------------------------------------------------------|
| [`CartType`](../../Cart/objects/cart-type.md)      | The properties and fields associated with a shopping cart.          |

## Example

<div class="grid" markdown>

```json title="Mutation"
mutation {
  addCoupon(
    command: {
      storeId: "B2B-store"
      userId: "d9d8b0f5-4f5a-4b1e-9e3c-2c7b1e5a3f8d"
      cartId: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      couponCode: "SUMMER20"
    }
  ) {
    id
    coupons {
      code
      isApplied
    }
  }
}
```

```json title="Return"
{
  "data": {
    "addCoupon": {
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "coupons": [
        {
          "code": "SUMMER20",
          "isApplied": true
        }
      ]
    }
  }
}
```

</div>