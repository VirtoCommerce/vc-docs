# InputOrderPaymentType ==~object~==

The `InputOrderPaymentType` is a type that represents the input object for creating or updating an order payment. 

## Fields

| Field                                                                                                               | Description                                                                     |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| `id` {==OptionalString==}                                                                                           | The Id for the payment.                                                         |
| `outerId` {==OptionalString==}                                                                                      | The external Id for the payment.                                                |
| `paymentGatewayCode` {==OptionalString==}                                                                           | The code that represents the payment gateway used for the payment.              |
| `currency` {==OptionalString==}                                                                                     | The currency code for the payment amount.                                       |
| `price` {==OptionalDecimal==}                                                                                       | The price associated with the payment.                                          |
| `amount` {==OptionalDecimal==}                                                                                      | The amount of money to be paid.                                                 |
| `vendorId` {==OptionalString==}                                                                                     | The Id of the vendor associated with the payment.                               |
| `comment` {==OptionalString==}                                                                                      | The comment about the payment.                                                  |
| `billingAddress` [{==InputOrderAddressType==}](../objects/input-order-address-type.md)                              | The billing address associated with the payment.                                |
| `dynamicProperties` [{==[InputDynamicPropertyValueType]==}](../../Profile/Objects/InputDynamicPropertyValueType.md) | The dynamic property value types.                                               |

