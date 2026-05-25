# AddOrUpdateOrderPayment ==~mutation~==

This mutation adds or updates the payment details for the order. It supports partial update, with all fields in `command.payment` and `command.payment.billingAddress` being optional. If you provide `command.payment.id`, the existing payment will be updated.

## Fields

The `InputAddOrUpdateOrderPaymentType` is a type that represents the input object for adding or updating an order payment. 

| Field                                                                             | Description                                                       |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------|
| `orderId` {==String!==}                                                           | The Id of the order to which the payment will be added or updated.|
| `payment` [{==InputOrderPaymentType!==}](../objects/input-order-payment-type.md)  | The payment details to be added or updated for the order.         |

## Possible returns

| Possible return                                                       | Description          	|
|-----------------------------------------------------------------------|---------------------	|
| [`CustomerOrderType`](../objects/customer-order-type.md)           	  |  A customer order.  	|


=== "Mutation"
    ```json linenums="1"
    mutation addOrUpdateOrderPayment ($command: InputAddOrUpdateOrderPaymentType!) {
      addOrUpdateOrderPayment (command: $command)
    {
    id
      inPayments
      {
        id
        number
        sum
        {
          amount
        }
      }
    }}
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command": {
        "orderId": "2be32440-ee84-4dd5-aa9b-fcbe35bf61f0",
        "payment": {
          "id": "testpaymentId",
          "price": 20,
          "comment": "this is a comment"
        }
      }
    }
    ```

