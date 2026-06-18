# Loyalty

The **Loyalty** module provides functionality for creating, managing, and applying loyalty programs within the system. It enables store managers to define reward rules, track customer transactions, and allow buyers to use loyalty points as a payment method.

| Queries                                                                                                | Objects                                                                                                     |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| [loyaltyBalance](queries/loyaltyBalance.md)<br>[loyaltyPointsHistory](queries/loyaltyPointsHistory.md) | [LoyaltyBalanceResult](objects/LoyaltyBalanceResult.md)<br>[LoyaltyOperationLog](objects/LoyaltyOperationLog.md)<br>[LoyaltyOperationLogConnection](objects/LoyaltyOperationLogConnection.md)<br>[LoyaltyOperationLogEdge](objects/LoyaltyOperationLogEdge.md)<br>[LoyaltyOperationLogObject](objects/LoyaltyOperationLogObject.md) |

## Mixed-currency carts

When a buyer pays with loyalty points, the cart holds totals in more than one currency, for example US dollars (`USD`) and points (`PTS`). The scalar cart totals (`total`, `subTotal`, `discountTotal`) stay in the primary currency. The [`cartTotals`](../Cart/objects/CartTotalType.md) array returns one [`CartTotalType`](../Cart/objects/CartTotalType.md) bucket per currency present, with each currency read from the nested `MoneyType`:

```graphql title="Query"
query Cart($storeId: String!, $cartName: String!, $currencyCode: String!) {
  cart(storeId: $storeId, cartName: $cartName, currencyCode: $currencyCode) {
    total { amount }                 # primary currency only
    cartTotals {                     # all currencies
      isDefaultTotalCurrency
      subTotal { amount currency { code } }
      discountTotal { amount currency { code } }
      total { amount currency { code } }
    }
  }
}
```

In a mixed `USD` and `PTS` cart, the points appear as a separate bucket with `discountTotal: 0`:

```json title="Response"
{ "data": { "cart": {
  "total": { "amount": 154.80 },
  "cartTotals": [
    { "isDefaultTotalCurrency": true,  "subTotal": { "amount": 160.00, "currency": { "code": "USD" } }, "discountTotal": { "amount": 16.00, "currency": { "code": "USD" } }, "total": { "amount": 154.80, "currency": { "code": "USD" } } },
    { "isDefaultTotalCurrency": false, "subTotal": { "amount": 240.00, "currency": { "code": "PTS" } }, "discountTotal": { "amount": 0.00,  "currency": { "code": "PTS" } }, "total": { "amount": 240.00, "currency": { "code": "PTS" } } }
  ]
} } }
```

To add a points-priced product, pass [`itemCurrencyCode`](../Cart/mutations/add-item.md) on the `addItem` mutation.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-loyalty)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-loyalty/releases)