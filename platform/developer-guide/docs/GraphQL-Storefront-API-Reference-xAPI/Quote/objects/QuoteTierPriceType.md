# QuoteTierPriceType ==~object~==

The `QuoteTierPriceType` is an object that contains information about tiered pricing associated with a quote item. 

## Fields

| Field                                                             | Description                                                |
| ----------------------------------------------------------------- | ---------------------------------------------------------- |
| `quantity`  ==Long!==                                             | The quantity for which the price applies.                  |
| `price` [ ==MoneyType== ](../../Cart/objects/money-type.md)       | The price associated with the specified quantity or range. |
