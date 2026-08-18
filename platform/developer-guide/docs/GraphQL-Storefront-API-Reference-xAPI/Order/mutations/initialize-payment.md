# InitializePayment ==~mutation~==

This mutation initiates the payment processing.

## Arguments

The `InputInitializePaymentType!` is a type used as an input for initializing a payment. 

| Field                     | Description                                                                  |
|---------------------------|------------------------------------------------------------------------------|
| `orderId` ==String==    | The Id of the order for which the payment initialization is requested.       |
| `paymentId` ==String==  | The Id of the payment for which the initialization is requested.             |

## Possible returns

| Possible return                                                               | Description                          |
|-------------------------------------------------------------------------------|--------------------------------------|
| [`InitializePaymentResultType`](../objects/initialize-payment-result-type.md) | The result of initializing a payment.|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation ($command: InputInitializePaymentType!)
{
    initializePayment(command: $command)
    {
        isSuccess
        errorMessage
        storeId
        paymentId
        orderId
        orderNumber
        paymentMethodCode
        paymentActionType
        actionRedirectUrl
        publicParameters 
          {
            key
            value
          }
        }
}
```

```json title="Variables"
{"command": 
  {
    "orderId": "d548c750-5a74-4e54-b72b-f5209f44caa6",
    "paymentId": "0859f1e8-16e8-4924-808b-47e03560085d"
  }
}
```

</div>