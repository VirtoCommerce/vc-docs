# ProcessOrderPayment ==~mutation~==

This mutation processes the order payment.

## Arguments

The `InputProcessOrderPaymentType!` represents the input object for processing a payment for an order.

| Field                                                                                            | Description                                                           |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| `orderId`  ==String==                                                                            | The Id of the order for which the payment is being processed.         |
| `paymentId`  ==String==                                                                          | The Id of the payment that needs to be processed.                     |
| `bankCardInfo` [ ==InputOrderBankCardInfoType== ](../objects/input-order-bank-card-info-type.md) | An input object containing the bank card information required for processing the payment. |

## Possible returns

| Possible return                                                                                   | Description                                    	|
|---------------------------------------------------------------------------------------------------|-----------------------------------------------	|
| [`ProcessPaymentRequestResultType`](../objects/process-payment-request-result-type.md)           	|  The result of processing a payment request.  	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation processOrderPayment ($command: InputProcessOrderPaymentType!) {
  processOrderPayment (command: $command)
  {
    isSuccess
    outerId
    htmlForm
    newPaymentStatus
    errorMessage
  }
}
```

```json title="Variables"
"command": {
"orderId":  "2be32440-ee84-4dd5-aa9b-fcbe35bf61f0",
"paymentId": "testpaymentid",
  "bankCardInfo": {
  "bankCardType": "Visa",
  "bankCardYear": 2023,
    "bankCardNumber": "4242424242424242424242",
    "bankCardMonth": 12,
    "bankCardCVV2": "422",
    "cardholderName": "FirstName LastName"
  }
}
```

</div>