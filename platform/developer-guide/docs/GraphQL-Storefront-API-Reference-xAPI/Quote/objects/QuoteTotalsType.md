# QuoteTotalsType ==~object~==

This type is an object used to store and manage various financial or pricing-related totals associated with a quote.  

## Fields

| Field                                                                         | Description                         |
| ----------------------------------------------------------------------------- | ------------------------------------|
| `originalSubTotalExlTax` [ ==MoneyType== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/money-type)  | The original subtotal excluding tax.|
| `subTotalExlTax` [ ==MoneyType== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/money-type)          | The subtotal excluding tax.         |
| `shippingTotal` [ ==MoneyType== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/money-type)           | The total shipping cost.            |
| `discountTotal` [ ==MoneyType== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/money-type)           | The total discount applied.         |
| `taxTotal` [ ==MoneyType== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/money-type)                | The total tax amount.               |
| `adjustmentQuoteExlTax` [ ==MoneyType== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/money-type)   | The adjustment amount excluding tax.|
| `grandTotalExlTax` [ ==MoneyType== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/money-type)        | The grand total excluding tax.      |
| `grandTotalInclTax` [ ==MoneyType== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Cart/objects/money-type)       | The grand total including tax.      |

