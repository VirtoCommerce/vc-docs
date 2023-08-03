# PaymentTransactionType ==~object~==

The `PaymentTransactionType` represents a specific transaction attempt associated with a payment. 

## Fields

| Field                             | Description                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------|
| `id` {==String!==}                | The Id of the payment transaction.                                                                |
| `isProcessed` {==Boolean==}       | Indicates whether the payment transaction has been processed.                                     |
| `processedDate` {==DateTime==}    | The date and time when the payment transaction was processed.                                     |
| `processError` {==String==}       | An optional description of any error that occurred during the payment transaction processing.     |
| `processAttemptCount` {==Int!==}  | The number of attempts made to process the payment transaction.                                   |
| `requestData` {==String==}        | The data associated with the payment transaction request.                                         |
| `responseData` {==String==}       | The data associated with the payment transaction response.                                        |
| `responseCode` {==String==}       | The response code received from the payment gateway during transaction processing.                |
| `gatewayIpAddress` {==String==}   | The IP address of the payment gateway used during the transaction processing.                     |
| `type` {==String!==}              | The type of the payment transaction.                                                              |
| `status` {==String!==}            | The status of the payment transaction, indicating its current state, such as "Completed" or "Pending". |
| `note` {==String!==}              | An optional note or comment related to the payment transaction.                                   |
| `amount` {==MoneyType==}          | The amount associated with the payment transaction.                                               |

