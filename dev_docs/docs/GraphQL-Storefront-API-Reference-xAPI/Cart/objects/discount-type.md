# DiscountType ==~object~==

The `DiscountType` represents a discount applied to a shopping cart or order.

## Fields

| Field                                                 | Description                                                                          |
|-------------------------------------------------------|--------------------------------------------------------------------------------------|
| `coupon` {==String==}                                 | The coupon code associated with the discount.                                         |
| `description` {==String==}                            | The description or additional information about the discount.                         |
| `promotionId` {==String==}                            | The ID of the promotion associated with the discount.                                 |
| `amount` {==Decimal==}                                | The discount amount without taxes.                                                    |
| `moneyAmount` [{==MoneyType==}](money-type.md)        | The discount amount represented as a `MoneyType` object.                              |
| `amountWithTax` {==Decimal==}                         | The discount amount including taxes.                                                  |
| `moneyAmountWithTax` [{==MoneyType==}](money-type.md) | The discount amount including taxes represented as a `MoneyType` object.              |

