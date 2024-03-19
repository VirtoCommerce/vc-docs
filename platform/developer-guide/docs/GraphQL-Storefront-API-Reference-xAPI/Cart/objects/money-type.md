# MoneyType ==~object~==

The `MoneyType` type represents a monetary value with associated currency information. 

## Fields

| Field                                                | Description                                                                                                                                         |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `amount`  ==Decimal!==                               | The amount of money, represented as a decimal value.                                                                                                |
| `currency` [ ==CurrencyType== ](currency-type.md)    | The currency type associated with the money value, represented as a `CurrencyType` object.                                                          |
| `decimalDigits`  ==Int!==                            | The number of decimal digits used to represent the amount.                                                                                          |
| `formattedAmount`  ==String!==                       | The formatted string representation of the amount, including the currency symbol and decimal separator.                                             |
| `formattedAmountWithoutCurrency`  ==String!==        | The formatted string representation of the amount, without the currency.                                                                            |
| `formattedAmountWithoutPoint`  ==String!==           | The formatted string representation of the amount, without the decimal separator and the fractional part.                                           |
| `formattedAmountWithoutPointAndCurrency`  ==String!== | The formatted string representation of the amount, without the decimal separator, the fractional part, and the currency symbol.                    |



