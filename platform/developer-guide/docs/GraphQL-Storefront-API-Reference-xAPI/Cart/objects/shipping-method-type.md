# ShipmentMethodType ==~object~==

The `ShippingMethodType` represents a shipping method available for selection within a shopping cart or order. 

## Fields

| Field                                                       | Description                                                                                                              |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `id`  ==String==                                            | The unique identifier of the shipping method.                                                                            |
| `code`  ==String==                                          | The code representing the shipping method.                                                                               |
| `logoUrl`  ==String==                                       | The URL or path to the logo or image representing the shipping method.                                                   |
| `optionName`  ==String==                                    | The name or title of the shipping method option or variant.                                                              |
| `optionDescription`  ==String==                             | A description or additional information about the shipping method option.                                                |
| `priority`  ==Int==                                         | The priority or order in which the shipping method should be displayed or considered.                                    |
| `currency` [ ==CurrencyType== ](currency-type.md)           | The currency used for the pricing of the shipping method, represented as a `CurrencyType` object.                        |
| `price` [ ==MoneyType== ](money-type.md)                    | The base price of the shipping method, represented as a `MoneyType` object.                                              |
| `priceWithTax` [ ==MoneyType== ](money-type.md)             | The price of the shipping method including taxes, represented as a `MoneyType` object.                                   |
| `total` [ ==MoneyType== ](money-type.md)                    | The total cost of the shipping method, represented as a `MoneyType` object.                                              |
| `totalWithTax` [ ==MoneyType== ](money-type.md)             | The total cost of the shipping method including taxes, represented as a `MoneyType` object.                              |
| `discountAmount` [ ==MoneyType== ](money-type.md)           | The discount amount applied to the shipping method, represented as a `MoneyType` object.                                 |
| `discountAmountWithTax` [ ==MoneyType== ](money-type.md)    | The discount amount applied to the shipping method including taxes, represented as a `MoneyType` object.                 |

