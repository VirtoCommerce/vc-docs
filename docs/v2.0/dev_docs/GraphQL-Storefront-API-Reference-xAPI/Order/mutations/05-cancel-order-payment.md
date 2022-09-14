# CancelOrderPayment

This mutation cancels order payment.

## Query

```
mutation {
  cancelOrderPayment(
    command: {
      payment: {
        orderId: "9d27c868-2e31-4ab4-861b-909bc3f86657"
        operationType: "PaymentIn"
        number: "PA1508131823002"
        isApproved: false
        status: "Authorized"
        comment: null
        isCancelled: false
        customerId: "0cda0396-43fe-4034-a20e-d0bab4c88c93"
        sum: 100
        currency: "USD"
        taxDetails: { name: "State tax", amount: 10, rate: 0.1 }
        taxTotal: 10
        discounts: { discountAmount: 11, discountAmountWithTax: 11, currency: "USD" }
      }
    }
  )
}

```