# SalesRepCustomerType ==~object~==

This type represents a customer organization the rep serves, as shown in the customers list.

## Fields

| Field | Description |
|-------|-------------|
| `organizationId`  ==String!== | The Id of the customer organization. |
| `organizationName`  ==String== | The name of the customer organization. |
| `accountId`  ==String== | The Id of the organization's account. |
| `accountType`  ==String== | The account type of the organization. |
| `iconUrl`  ==String== | A link to the organization's icon. |
| `address` [ ==SalesRepAddressType== ](SalesRepAddressType.md) | The organization's default address. |
| `lastOrder` [ ==SalesRepOrderType== ](SalesRepOrderType.md) | The rep's most recent order for the customer. |
| `orderStatistics` [ ==CustomerOrderStatisticsPeriodType== ](CustomerOrderStatisticsPeriodType.md) | Aggregated order totals for the customer over a date range. Arguments: `from` and `to` (==DateTime==), and `currencyCode` (==String==). |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../SalesRepContactType">← SalesRepContactType</a>
    <a href="../SalesRepCustomerDetailsType">SalesRepCustomerDetailsType →</a>
</div>
