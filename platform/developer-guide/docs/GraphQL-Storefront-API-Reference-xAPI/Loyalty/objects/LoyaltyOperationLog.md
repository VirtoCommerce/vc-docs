# LoyaltyOperationLog ==~object~==

This type defines the structure of a loyalty program operation log entry and contains details about loyalty point transactions.

## Fields

| Field                                                                             | Description                                                    |
| --------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `id` ==String!==                                                                  | The Id of the log entry.                        |
| `operationType` ==String!==                                                       | The type of operation, such as **Earned** or **Redeemed**.     |
| `amount` ==Decimal!==                                                             | The number of loyalty points involved in the operation.        |
| `createdDate` ==DateTime!==                                                       | The date and time when the log entry was created.              |
| `object` [==LoyaltyOperationLogObject==](LoyaltyOperationLogObject.md)            | The related object that triggered the operation. |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../LoyaltyBalanceResult">← LoyaltyBalanceResult</a>
    <a href="../LoyaltyOperationLogConnection">LoyaltyOperationLogConnection →</a>
</div>
