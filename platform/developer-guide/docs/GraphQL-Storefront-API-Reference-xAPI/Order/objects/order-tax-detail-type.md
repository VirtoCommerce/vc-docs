# OrderTaxDetailType ==~object~==

This type is a detailed breakdown of taxes applied to a shipment or order.

## Fields

| Field                     | Description                                               |
|---------------------------|-----------------------------------------------------------|
| `rate`  ==MoneyType==     | The tax rate applied to the shipment or order.            |
| `amount`  ==MoneyType==   | The tax amount calculated on the basis of the tax rate.   |
| `name`  ==String!==       | The name of the tax detail.                               |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../input-order-address-type">← InputOrderAddressType</a>
    <a href="../order-discount-type">OrderDiscountType →</a>
</div>
