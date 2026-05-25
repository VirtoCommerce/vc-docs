# PaymentInType ==~object~==

This type represents the received incoming payment. Each `PaymentInType` instance represents a specific payment made by a customer to complete a purchase or settle an order. 

## Fields

| Field                                                                                                          | Description                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| `id`  ==String!==                                                                                              | The Id of the payment transaction.                                                  |
| `organizationId`  ==String==                                                                                   | The Id of the organization associated with the payment transaction.               |
| `organizationName`  ==String==                                                                                 | The name of the organization associated with the payment transaction.                           |
| `customerName`  ==String==                                                                                     | The name of the customer associated with the payment transaction.                                 |
| `customerId`  ==String!==                                                                                      | The Id of the customer associated with the payment transaction.                    |
| `purpose`  ==String==                                                                                          | The purpose or reason for the payment.                                                            |
| `gatewayCode`  ==String==                                                                                      | The code representing the payment gateway used for the transaction.                               |
| `incomingDate`  ==DateTime==                                                                                   | The date and time when the payment was received or credited.                                      |
| `outerId`  ==String==                                                                                          | An external identifier for the payment, used for integration with external systems.      |
| `operationType`  ==String!==                                                                                   | The type of payment operation.                            |
| `number`  ==String!==                                                                                          | The number assigned to the payment transaction.                               |
| `isApproved`  ==Boolean==                                                                                      | Indicates whether the payment transaction is approved or not.                         |
| `status`  ==String==                                                                                           | The status of the payment transaction, indicating its current state. |
| `comment`  ==String==                                                                                          | An additional information related to the payment transaction.                 |
| `isCancelled`  ==Boolean==                                                                                     | Indicates whether the payment transaction is cancelled or not.                         |
| `cancelledDate`  ==DateTime==                                                                                  | The date and time when the payment transaction was cancelled.                     |
| `cancelReason`  ==String==                                                                                     | The reason for canceling the payment transaction.                                   |
| `parentOperationId`  ==String==                                                                                | The Id of the parent payment operation.                            |
| `objectType`  ==String!==                                                                                      | The type of object.                                              |
| `createdDate`  ==DateTime!==                                                                                   | The date and time when the payment transaction was created.                                         |
| `modifiedDate`  ==DateTime==                                                                                   | The date and time when the payment transaction was last modified.                                  |
| `createdBy`  ==String==                                                                                        | The user or entity who created the payment transaction.                                            |
| `modifiedBy`  ==String==                                                                                       | The user or entity who last modified the payment transaction.                                      |
| `authorizedDate`  ==DateTime==                                                                                 | The date and time when the payment was authorized.                                 |
| `capturedDate`  ==DateTime==                                                                                   | The date and time when the payment was captured.                                   |
| `voidedDate`  ==DateTime==                                                                                     | The date and time when the payment was voided.                                     |
| `orderId`  ==String==                                                                                          | The Id of the associated order for which the payment was made.                    |
| `price`  ==MoneyType==                                                                                         | The amount of the payment transaction.                                                             |
| `sum`  ==MoneyType==                                                                                           | The total amount of the payment, including any taxes or additional charges.                       |
| `tax`  ==MoneyType==                                                                                           | The amount of tax included in the payment.                                                         |
| `paymentMethod` [ ==OrderPaymentMethodType== ](order-payment-method-type.md)                                   | The payment method used for the transaction.                                               |
| `currency` [ ==CurrencyType== ](currency-type.md)                                                              | The currency used for the payment transaction.                                                    |
| `billingAddress` [ ==OrderAddressType== ](order-address-type.md)                                               | The billing address associated with the payment transaction.                                  |
| `vendor` [ ==CommonVendor== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/CommonVendor/Commonvendor)                              | The common vendor associated with the payment transaction.                                        |
| `transactions` [ ==[PaymentTransactionType]== ](payment-transaction-type.md)                                   | Payment transaction details associated with the payment.                         |
| `order` [ ==CustomerOrderType!== ](customer-order-type.md)                                                     | The customer order associated with the payment transaction.                                      |
| `dynamicProperties(...)` [ ==[DynamicPropertyValueType]== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/dynamic-property-value-type) | Dynamic property value types. |

