# AuthorizePayment

This mutation finalizes the first step of payment processing.

## Query

```
mutation ($command: InputAuthorizePaymentType!) {
  authorizePayment(command: $command) {
    isSuccess
    errorMessage
  }
}
```

## Variables

```
"command": {
    "orderId": "d548c750-5a74-4e54-b72b-f5209f44caa6",
    "paymentId": "0859f1e8-16e8-4924-808b-47e03560085d",
    "parameters": [
      {
        key: "key1",
        value: "value1"
      },
      {
        key: "key2",
        value: "value2"
      }
  }
```