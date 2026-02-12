# validateCoupon ==~query~==

This is to query whether the provided coupon is valid or not.

## Arguments

| Field                        | Description                                                      |
|------------------------------|------------------------------------------------------------------|
| `cartId` ==String==          | The Id of the cart for which the coupon will be validated.       |
| `storeId` ==String!==        | The Id of the store associated with the cart.                    |
| `cartName` ==String==        | The name of the cart.                                            |
| `userId` ==String==          | The Id of the user who owns the cart.                            |
| `currencyCode` ==String==    | The currency code for the cart.                                  |
| `cultureName` ==String==     | The culture or language associated with the cart.                |
| `cartType` ==String==        | The type of the cart.                                            |
| `coupon` ==String==          | The coupon code to be validated for the cart.                    |


## Possible returns

| Possible return               | Description                                     |
|-------------------------------|-------------------------------------------------|
| `Boolean`                     |  Shows whether the coupon is valid or not.    	|



## Example

<div class="grid" markdown>

```json title="Query"
    query {
      validateCoupon(
        storeId: "B2B-store",
        userId: "123",
        currencyCode:"USD"
        cultureName:"en-US"
        cartName:"default"
        coupon:"123"
      )
    }
```

```json title="Return"
    {
      "data": {
        "validateCoupon": false
      }
    }
```

</div>