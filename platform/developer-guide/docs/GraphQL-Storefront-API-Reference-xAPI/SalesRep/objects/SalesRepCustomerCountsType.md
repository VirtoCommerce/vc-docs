# SalesRepCustomerCountsType ==~object~==

This type reports how many customers the rep is assigned and how many ordered or were newly added. Select `period` and `comparison` under aliases to build the columns you need.

## Fields

| Field | Description |
|-------|-------------|
| `assignedCustomers`  ==Int== | The number of customers assigned to the rep. |
| `period` [ ==SalesRepCustomerCountsPeriodType== ](SalesRepCustomerCountsPeriodType.md) | Customer counts for a date range. Arguments: `from` and `to` (==DateTime==). |
| `comparison` [ ==SalesRepCustomerCountsComparisonType== ](SalesRepCustomerCountsComparisonType.md) | The change between two date ranges. Arguments: `current` and `previous` date ranges. |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../CustomerCartStatisticsPeriodType">← CustomerCartStatisticsPeriodType</a>
    <a href="../SalesRepCustomerCountsPeriodType">SalesRepCustomerCountsPeriodType →</a>
</div>
