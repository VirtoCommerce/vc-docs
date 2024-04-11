# InitizalizePaymentResultType ==~object~==

The `InitializePaymentResultType` is a type that represents the result of initializing a payment. 

## Fields

| Field                                                                 | Description                                                                           |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| `isSuccess`  ==Boolean!==                                             | Indicates whether the payment initialization process was successful.                  |
| `errorMessage`  ==String==                                            | The error message describing the cause of the error.                                  |
| `storeId`  ==String==                                                 | The Id of the store associated with the payment.                                      |
| `paymentId`  ==String==                                               | The Id of the payment for which the initialization was performed.                     |
| `orderId`  ==String==                                                 | The Id of the order associated with the payment.                                      |
| `orderNumber`  ==String==                                             | The order number associated with the payment.                                         |
| `paymentMethodCode`  ==String==                                       | The code representing the payment method used for the payment.                        |
| `paymentActionType`  ==String==                                       | The type of payment action performed during the initialization process.               |
| `actionRedirectUrl`  ==String==                                       | The URL to redirect the user after the payment initialization process.                |
| `actionHtmlForm`  ==String==                                          | An HTML form that can be used to submit payment data to an external payment gateway.  |
| `publicParameters` [ ==[KeyValueType]== ](../objects/key-value-type.md) | Additional public parameters that may be needed for the payment process.            |

