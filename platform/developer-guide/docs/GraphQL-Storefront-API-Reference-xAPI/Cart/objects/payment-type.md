# PaymentType ==~object~==

This type represents a payment made within a shopping cart or order. 

## Fields

| Field                                                                                       | Description                                                                                                          |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| `id`  ==String==                                                                            | The unique identifier of the payment.                                                                                |
| `outerId`  ==String==                                                                       | The outer identifier of the nt.                                                                                      |
| `paymentGatewayCode`  ==String==                                                            | The code representing the payment gateway used for the payment.                                                      |
| `purpose`  ==String==                                                                       | The purpose or reason for the payment.                                                                               |
| `currency` [ ==CurrencyType== ](currency-type.md)                                           | The currency used for the payment, represented as a `CurrencyType` object.                                           |
| `amount` [ ==MoneyType== ](money-type.md)                                                   | The amount of the payment, represented as a `MoneyType` object.                                                      |
| `billingAddress` [ ==CartAddressType== ](cart-address-type.md)                              | The billing address associated with the payment, represented as a `CartAddressType` object.                          |
| `price` [ ==MoneyType== ](money-type.md)                                                    | The base price of the payment, represented as a `MoneyType` object.                                                  |
| `priceWithTax` [ ==MoneyType== ](money-type.md)                                             | The price of the payment including taxes, represented as a `MoneyType` object.                                       |
| `total` [ ==MoneyType== ](money-type.md)                                                    | The total cost of the payment, represented as a `MoneyType` object.                                                  |
| `totalWithTax` [ ==MoneyType== ](money-type.md)                                             | The total cost of the payment including taxes, represented as a `MoneyType` object.                                  |
| `discountAmount` [ ==MoneyType== ](money-type.md)                                           | The discount amount applied to the payment, represented as a `MoneyType` object.                                     |
| `discountAmountWithTax` [ ==MoneyType== ](money-type.md)                                    | The discount amount applied to the payment including taxes, represented as a `MoneyType` object.                     |
| `taxTotal` [ ==MoneyType== ](money-type.md)                                                 | The total tax amount applied to the payment, represented as a `MoneyType` object.                                    |
| `taxPercentRate`  ==Decimal==                                                               | The tax rate percentage applied to the payment.                                                                      |
| `taxType`  ==String==                                                                       | The type or category of tax applied to the payment.                                                                  |
| `taxDetails` [ ==[TaxDetailType]== ](tax-detail-type.md)                                    | An array of tax details associated with the payment, represented as `[TaxDetailType]`.                               |
| `discounts` [ ==[DiscountType]== ](discount-type.md)                                        | An array of discounts applied to the payment, represented as `[DiscountType]`.                                       |
| `comment`  ==String==                                                                       | A comment or additional information related to the payment.                                                          |
| `vendor` [ ==CommonVendor== ](../../Catalog/objects/CommonVendor/Commonvendor.md)           | The vendor associated with the payment.                                                                              |
| `dynamicProperties(...)` [ ==[DynamicPropertyValueType]== ](dynamic-property-value-type.md) | The dynamic properties associated with the payment, represented as an array of `DynamicPropertyValueType` objects.   |

