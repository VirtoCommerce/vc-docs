# CustomerOrderStatisticsType ==~object~==

This type reports aggregated order statistics for a customer organization. Select `period` and `comparison` under aliases to build the columns you need.

## Fields

| Field | Description |
|-------|-------------|
| `currencyCode`  ==String== | The currency amounts are reported in. |
| `period` [ ==CustomerOrderStatisticsPeriodType== ](CustomerOrderStatisticsPeriodType.md) | Aggregated totals for a date range. Arguments: `from` and `to` (==DateTime==). Omit both for lifetime figures. |
| `comparison` [ ==CustomerOrderStatisticsComparisonType== ](CustomerOrderStatisticsComparisonType.md) | The change between two date ranges. Arguments: `current` and `previous` date ranges. |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../SalesRepAddressType">← SalesRepAddressType</a>
    <a href="../CustomerOrderStatisticsPeriodType">CustomerOrderStatisticsPeriodType →</a>
</div>
