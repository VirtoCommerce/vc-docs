# LoyaltyBalanceResult ==~object~==

This type defines the structure of a loyalty balance result and contains information about the current and resulting balances after an operation. Under [Organization mode](../overview.md#organization-mode), `currentBalance` is the organization's shared total rather than a personal balance: every member of that organization reads the same value.

## Fields

| Field                         | Description                                                                |
| ----------------------------- | -------------------------------------------------------------------------- |
| `currentBalance` ==Decimal!== | The current balance of the loyalty account before the operation.           |
| `resultBalance` ==Decimal!==  | The balance after applying the operation requested via `orderId`. Its distinction from `currentBalance` has not been independently confirmed against a live `orderId`; observed responses show the same value in both fields. Verify this against your own environment before relying on a specific difference between the two. |

This type has only the two fields above: there is no `balance`, `available`, or `currency` field. Confirm field names against your environment's live schema (introspect `/graphql`) rather than an older schema snapshot.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../queries/loyaltyPointsHistory">← LoyaltyPointsHistory query</a>
    <a href="../LoyaltyOperationLog">LoyaltyOperationLog →</a>
</div>
