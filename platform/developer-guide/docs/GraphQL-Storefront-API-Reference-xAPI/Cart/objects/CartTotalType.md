# CartTotalType ==~object~==

This type represents one total bucket for a single currency present in the cart. A cart returns one `CartTotalType` per currency, for example a separate bucket for loyalty points alongside the primary currency.

## Fields

| Field                                            | Description                                                                 |
|--------------------------------------------------|-----------------------------------------------------------------------------|
| `isDefaultTotalCurrency` ==Boolean!==           | Indicates whether this bucket is the cart's primary total currency.         |
| `total` [==MoneyType!==](money-type.md)          | The total for this currency.                                                |
| `subTotal` [==MoneyType!==](money-type.md)       | The subtotal for this currency before taxes and discounts.                  |
| `taxTotal` [==MoneyType!==](money-type.md)       | The total tax for this currency.                                            |
| `discountTotal` [==MoneyType!==](money-type.md)  | The total discount for this currency.                                       |

This type has no `currencyCode` scalar. Read the currency from any `MoneyType.currency.code`, or branch on `isDefaultTotalCurrency`.

![Readmore](../media/readmore.png){: width="25"} [Mixed-currency carts](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Loyalty/overview#mixed-currency-carts)

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../cart-type">← CartType</a>
    <a href="../cart-connection">CartConnection →</a>
</div>
