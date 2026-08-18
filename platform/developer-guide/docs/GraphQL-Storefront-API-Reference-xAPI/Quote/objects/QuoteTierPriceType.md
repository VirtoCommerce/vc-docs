# QuoteTierPriceType ==~object~==

This type is an object that contains information about tiered pricing associated with a quote item. 

## Fields

| Field                                                             | Description                                                |
| ----------------------------------------------------------------- | ---------------------------------------------------------- |
| `quantity`  ==Long!==                                             | The quantity for which the price applies.                  |
| `price` [ ==MoneyType== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/money-type)       | The price associated with the specified quantity or range. |
