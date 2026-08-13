# CustomerCartStatisticsType ==~object~==

This type reports aggregated cart statistics for a customer's carts. Select `period` under aliases to build the columns you need.

## Fields

| Field | Description |
|-------|-------------|
| `period` [ ==CustomerCartStatisticsPeriodType== ](CustomerCartStatisticsPeriodType.md) | Aggregated cart figures for a date range. Arguments: `from` and `to` (==DateTime==), and `filter` (==String==), a [salesRepCartFilterRules](../queries/salesRepCartFilterRules.md) name that defaults to `active-carts`. |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../CustomerOrderStatisticsComparisonType">← CustomerOrderStatisticsComparisonType</a>
    <a href="../CustomerCartStatisticsPeriodType">CustomerCartStatisticsPeriodType →</a>
</div>
