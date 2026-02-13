# loyaltyBalance ==~query~==

This query allows you to retrieve the loyalty balance information for a specific user. You can optionally specify an order to see how it affects the available balance.

## Arguments

| Argument              | Description                                               |
|-----------------------|-----------------------------------------------------------|
| `userId` ==String!==  | The Id of the user whose loyalty balance is requested.    |
| `orderId` ==String!== | The Id of an order to check balance availability against. |

## Possible returns

| Possible return                                              | Description                                                      |
| ------------------------------------------------------------ | ---------------------------------------------------------------- |
| [LoyaltyBalanceResult](../objects/LoyaltyBalanceResult.md) | Defines the fields and properties of the user’s loyalty balance. |

## Example

<div class="grid" markdown>

```json title="Query"
{
loyaltyBalance(
    userId: "9c6a2f1a-24e7-4b2c-bb5d-ef5e2ad7c111"
    orderId: "f3d2a8a7-6c47-4ad0-bc8c-88e2d13f4412"
) {
    balance
    availableBalance
    reservedBalance
    currency
  }
}
```

```json title="Return"
{
  "data": {
    "loyaltyBalance": {
    "balance": 250,
    "availableBalance": 200,
    "reservedBalance": 50,
    "currency": "USD"
    }
  }
}
```

</div>