# OrderDiscountType ==~object~==

This type represents a discount applied to an order or shipment. 

## Fields

| Field                         | Description                                                                   |
|-------------------------------|-------------------------------------------------------------------------------|
| `amount`  ==MoneyType==       | The discount amount applied to the order or shipment.                         |
| `coupon`  ==String==          | The coupon code associated with the discount, if the discount is coupon-based.|
| `promotionId`  ==String==     | The Id of the promotion associated with the discount.                         |
| `promotionName`  ==String==   | The name of the promotion associated with the discount. |
| `promotionDescription`  ==String==     | A brief description of the promotion associated with the discount. |

