# CurrencyType ==~object~==

The `CurrencyType` is utilized to store information about a specific currency.

## Fields

| Field                         | Description                                                                      |
|-------------------------------|----------------------------------------------------------------------------------|
| `code` ==String!==            | The code of the currency, such as USD or EUR.                                    |
| `symbol` ==String==           | The symbol used to represent the currency, such as $ for US Dollar.              |
| `exchangeRate` ==Decimal==    | The exchange rate of the currency relative to a base currency.                   |
| `customFormatting` ==String== | An optional field that provides custom formatting for displaying the currency.   |
| `englishName` ==String!==     | The English name of the currency.                                                |
| `cultureName` ==String!==     | The culture name associated with the currency.                                   |
