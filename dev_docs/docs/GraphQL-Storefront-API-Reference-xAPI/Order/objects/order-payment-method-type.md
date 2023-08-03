# OrderPaymentMethodType ==~object~==

The `OrderPaymentMethodType` represents a payment method available for orders.

## Fields

| Field                                                                 | Description                                                               |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------|
| `taxDetails` [{==[OrderTaxDetailType]==}](order-tax-detail-type.md)   | Tax details associated with the payment method.                           |
| `taxPercentRate` {==Decimal!==}                                       | The tax percent rate applied to the payment method.                       |
| `taxTotal` {==MoneyType==}                                            | The total tax amount for the payment method.                              |
| `taxType` {==String!==}                                               | The type of tax applied to the payment method.                            |
| `typeName` {==String!==}                                              | The name of the payment method type.                                      |
| `storeId` {==String!==}                                               | The Id of the store to which the payment method belongs.                  |
| `totalWithTax` {==MoneyType==}                                        | The total amount of the payment method, including tax.                    |
| `total` {==MoneyType==}                                               | The total amount of the payment method.                                   |
| `discountAmount` {==MoneyType==}                                      | The amount of the discount applied to the payment method.                 |
| `discountAmountWithTax` {==MoneyType==}                               | The amount of the discount applied to the payment method, including tax.  |
| `price` {==MoneyType==}                                               | The price of the payment method.                                          |
| `priceWithTax` {==MoneyType==}                                        | The price of the payment method, including tax.                           |
| `currency` {==CurrencyType==}                                         | The currency used for the payment method.                                 |
| `isAvailableForPartial` {==Boolean!==}                                | Indicates whether the payment method is available for partial payment.    |
| `priority` {==Int!==}                                                 | The priority of the payment method.                                       |
| `isActive` {==Boolean!==}                                             | Indicates whether the payment method is active or not.                    |
| `logoUrl` {==String==}                                                | The URL of the logo associated with the payment method.                   |
| `code` {==String!==}                                                  | The code of the payment method.                                           |
| `description` {==String!==}                                           | A description of the payment method.                                      |
| `paymentMethodType` {==Int!==}                                        | The type of the payment method.                                           |
| `paymentMethodGroupType` {==Int!==}                                   | The group type of the payment method.                                     |