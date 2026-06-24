# ProcessPaymentRequestResultType ==~object~==

This type represents the result of a payment processing request. 

## Fields

| Field                             | Description                                                                                                              |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `isSuccess`  ==Boolean!==         | Indicates whether the payment processing was successful.                                                                 |
| `htmlForm`  ==String==            | An HTML form that may be provided for redirecting the user to an external payment gateway for additional payment steps.  |
| `newPaymentStatus`  ==String==    | A field indicating the new payment status resulting from the payment processing.                                         |
| `outerId`  ==String==             | The external identifier associated with the payment transaction.                                                         |
| `redirectUrl`  ==String==         | The URL that may be provided for redirecting the user to an external payment gateway for completing the payment process. |
| `errorMessage`  ==String==        | The error message providing additional information in case the payment processing was not successful.                    |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../payment-in-type">← PaymentInType</a>
    <a href="../input-order-bank-card-info-type">InputOrderBankCardInfoType →</a>
</div>
