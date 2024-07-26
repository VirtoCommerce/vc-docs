# TaxDetailType ==~object~==

This type represents a tax detail with its associated properties. 

## Fields

| Field                                              | Description                                                                            |
|----------------------------------------------------|----------------------------------------------------------------------------------------|
| `amount` [ ==MoneyType== ](money-type.md)          | The amount of tax applied, represented as a `MoneyType` object.                        |
| `price` [ ==MoneyType== ](money-type.md)           | The price on which the tax is calculated, represented as a `MoneyType` object.         |
| `rate` [ ==MoneyType== ](money-type.md)            | The tax rate applied, represented as a `MoneyType` object.                             |
| `name`  ==String==                                 | The name or description of the tax.                                                    |
