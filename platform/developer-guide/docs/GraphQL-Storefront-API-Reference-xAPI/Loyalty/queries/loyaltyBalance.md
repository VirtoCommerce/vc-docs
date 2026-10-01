# loyaltyBalance ==~query~==

This query allows you to retrieve the loyalty balance information for a specific user. You can optionally specify an order to see how it affects the available balance.

Under [Organization mode](../overview.md#organization-mode), the query returns the calling member's organization pool instead of a personal balance. Scope is resolved from the caller's organization membership, so no argument selects which organization to read.

## Breaking changes

* `storeId` is now a required argument. Omitting it fails with:

    ```
    Argument 'storeId' of type 'String!' is required for field 'loyaltyBalance' but not provided.
    ```

    Add `storeId` to every existing call to this query before upgrading to a Loyalty release that includes this change.

## Arguments

| Argument              | Description                                               |
|-----------------------|-----------------------------------------------------------|
| `storeId` ==String!== | The Id of the store to query the loyalty balance for. Required. |
| `userId` ==String==  | The Id of the user whose loyalty balance is requested.    |
| `orderId` ==String== | The Id of an order to check balance availability against. |

## Possible returns

| Possible return                                              | Description                                                      |
| ------------------------------------------------------------ | ---------------------------------------------------------------- |
| [LoyaltyBalanceResult](../objects/LoyaltyBalanceResult.md) | Defines the fields and properties of the user’s loyalty balance. |

## Example

<div class="grid" markdown>

```graphql title="Query"
{
loyaltyBalance(
    storeId: "b2b-store"
    userId: "9c6a2f1a-24e7-4b2c-bb5d-ef5e2ad7c111"
    orderId: "f3d2a8a7-6c47-4ad0-bc8c-88e2d13f4412"
) {
    currentBalance
    resultBalance
  }
}
```

```json title="Return"
{
  "data": {
    "loyaltyBalance": {
      "currentBalance": 250,
      "resultBalance": 250
    }
  }
}
```
</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../overview">← Loyalty module overview</a>
    <a href="../loyaltyPointsHistory">LoyaltyPointsHistory query →</a>
</div>
