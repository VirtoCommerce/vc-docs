# QuoteTotalsType ==~object~==

The `QuoteTotalsType` is an object used to store and manage various financial or pricing-related totals associated with a quote.  

## Fields

| Field                                                                         | Description                         |
| ----------------------------------------------------------------------------- | ------------------------------------|
| `originalSubTotalExlTax` [{==MoneyType==}](../../Cart/objects/money-type.md)  | The original subtotal excluding tax.|
| `subTotalExlTax` [{==MoneyType==}](../../Cart/objects/money-type.md)          | The subtotal excluding tax.         |
| `shippingTotal` [{==MoneyType==}](../../Cart/objects/money-type.md)           | The total shipping cost.            |
| `discountTotal` [{==MoneyType==}](../../Cart/objects/money-type.md)           | The total discount applied.         |
| `taxTotal` [{==MoneyType==}](../../Cart/objects/money-type.md)                | The total tax amount.               |
| `adjustmentQuoteExlTax` [{==MoneyType==}](../../Cart/objects/money-type.md)   | The adjustment amount excluding tax.|
| `grandTotalExlTax` [{==MoneyType==}](../../Cart/objects/money-type.md)        | The grand total excluding tax.      |
| `grandTotalInclTax` [{==MoneyType==}](../../Cart/objects/money-type.md)       | The grand total including tax.      |

