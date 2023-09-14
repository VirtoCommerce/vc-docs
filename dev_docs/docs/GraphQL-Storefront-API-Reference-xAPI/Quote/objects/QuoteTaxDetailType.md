# QuoteTaxDetailType ==~object~==

The `QuoteTaxDetailType` is an object that contains information about a tax detail associated with a quote. 

## Fields

| Field                                                      | Description                                     |
| ---------------------------------------------------------- | ----------------------------------------------- |
| `rate` [{==MoneyType==}](../../Cart/objects/money-type.md) | The tax rate applied.                           |
| `amount` [{==MoneyType==}](../../Cart/objects/money-type.md)| The tax amount calculated based on the rate.   |
| `name` {==String==}                                        | The name of the tax detail.                     |
