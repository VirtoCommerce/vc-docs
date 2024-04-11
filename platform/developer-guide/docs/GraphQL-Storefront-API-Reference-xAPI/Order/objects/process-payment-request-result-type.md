# ProcessPaymentRequestResultType ==~object~==

The `ProcessPaymentRequestResultType` is a type that represents the result of a payment processing request. 

## Fields

| Field                             | Description                                                                                                              |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `isSuccess`  ==Boolean!==         | Indicates whether the payment processing was successful.                                                                 |
| `htmlForm`  ==String==            | An HTML form that may be provided for redirecting the user to an external payment gateway for additional payment steps.  |
| `newPaymentStatus`  ==String==    | A field indicating the new payment status resulting from the payment processing.                                         |
| `outerId`  ==String==             | The external identifier associated with the payment transaction.                                                         |
| `redirectUrl`  ==String==         | The URL that may be provided for redirecting the user to an external payment gateway for completing the payment process. |
| `errorMessage`  ==String==        | The error message providing additional information in case the payment processing was not successful.                    |

