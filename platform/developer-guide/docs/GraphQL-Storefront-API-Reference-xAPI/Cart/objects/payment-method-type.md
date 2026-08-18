# PaymentMethodType

This type represents a specific payment method available for use in a shopping cart or order. 

## Fields

| Field                                                       | Description                                                                                                              |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `code`  ==String==                                          | The code representing the payment method.                                                                                 |
| `name`  ==String==                                          | The name of the payment method.                                                                                          |
| `logoUrl`  ==String==                                       | The URL or path to the logo image representing the payment method.                                                       |
| `paymentMethodType`  ==String==                             | The type of the payment method.                                                                                          |
| `paymentMethodGroupType`  ==String==                        | The group type of the payment method.                                                                                    |
| `priority`  ==Int==                                         | The priority of the payment method.                                                                                      |
| `isAvailableForPartial`  ==Boolean==                        | Indicates whether the payment method is available for partial payments.                                                  |
| `currency` [ ==CurrencyType== ](currency-type.md)           | The currency used for the payment method, represented as a `CurrencyType` object.                                        |
| `price` [ ==MoneyType== ](money-type.md)                    | The base price of the payment method, represented as a `MoneyType` object.                                               |
| `priceWithTax` [ ==MoneyType== ](money-type.md)             | The price of the payment method including taxes, represented as a `MoneyType` object.                                    |
| `total` [ ==MoneyType== ](money-type.md)                    | The total cost of the payment method, represented as a `MoneyType` object.                                               |
| `totalWithTax` [ ==MoneyType== ](money-type.md)             | The total cost of the payment method including taxes, represented as a `MoneyType` object.                              |
| `discountAmount` [ ==MoneyType== ](money-type.md)           | The discount amount applied to the payment method, represented as a `MoneyType` object.                                 |
| `discountAmountWithTax` [ ==MoneyType== ](money-type.md)    | The discount amount applied to the payment method including taxes, represented as a `MoneyType` object.                |
| `taxTotal` [ ==MoneyType== ](money-type.md)                 | The total tax amount applied to the payment method, represented as a `MoneyType` object.                                |
| `taxPercentRate`  ==Decimal==                               | The tax rate percentage applied to the payment method.                                                                   |
| `taxType`  ==String==                                       | The type or category of tax applied to the payment method.                                                               |
| `taxDetails` [ ==[TaxDetailType]== ](tax-detail-type.md)    | An array of tax details associated with the payment method, represented as `[TaxDetailType]`.                            |
| `description`  ==String==                                   | The description or additional information about the payment method.                                                      |

