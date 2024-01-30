# AuthorizePayment ==~mutation~==

This mutation finalizes the first step of payment processing.

## Arguments

The `InputAuthorizePaymentType!` is a type that represents the input object for authorizing a payment. It provides the necessary context and data for performing the payment authorization action.

| Field                                                                       | Description                                                               |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `orderId` {==String==}                                                      | The Id of the order for which the payment is being authorized.            |
| `paymentId` {==String==}                                                    | The Id of the payment for which the authorization is being performed.     |
| `parameters` [{==[InputKeyValueType]==}](../objects/input-key-value-type.md)| Additional parameters required for the authorization process.             |

## Possible returns

| Possible return                                                             | Description                                          	|
|-----------------------------------------------------------------------------|------------------------------------------------------	|
| [`AuthorizePaymentResultType`](../objects/authorize-payment-result-type.md) |  The result of authorizing a payment for an order.   	|


=== "Mutation"
    ```json linenums="1"
    mutation ($command: InputAuthorizePaymentType!) {
      authorizePayment(command: $command) {
        isSuccess
        errorMessage
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {"command": {
        "orderId": "d548c750-5a74-4e54-b72b-f5209f44caa6",
        "paymentId": "0859f1e8-16e8-4924-808b-47e03560085d",
        "parameters": [
          {
            "key": "key1",
            "value": "value1"
          },
          {
            "key": "key2",
            "value": "value2"
          }
          ]
    }
    }
    ```
