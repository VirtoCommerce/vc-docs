# QuoteTaxDetailType ==~object~==

This type is an object that contains information about a tax detail associated with a quote. 

## Fields

| Field                                                      | Description                                     |
| ---------------------------------------------------------- | ----------------------------------------------- |
| `rate` [ ==MoneyType== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/money-type) | The tax rate applied.                           |
| `amount` [ ==MoneyType== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/money-type)| The tax amount calculated based on the rate.   |
| `name`  ==String==                                         | The name of the tax detail.                     |
