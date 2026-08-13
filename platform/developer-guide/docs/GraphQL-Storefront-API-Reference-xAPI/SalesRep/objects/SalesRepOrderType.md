# SalesRepOrderType ==~object~==

This type represents an order the rep created for a customer.

## Fields

| Field | Description |
|-------|-------------|
| `id`  ==ID!== | The Id of the order. |
| `number`  ==String== | The order number. |
| `organizationId`  ==String== | The Id of the customer organization. |
| `organizationName`  ==String== | The name of the customer organization. |
| `createdDate`  ==DateTime!== | The date the order was created. |
| `status`  ==String== | The order status. |
| `total` [ ==MoneyType== ](../../Cart/objects/money-type.md) | The order total. |
| `itemsCount`  ==Int!== | The number of line items. |
| `itemsQuantity`  ==Int!== | The total quantity of items. |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../SalesRepCustomerDetailsType">← SalesRepCustomerDetailsType</a>
    <a href="../SalesRepAddressType">SalesRepAddressType →</a>
</div>
