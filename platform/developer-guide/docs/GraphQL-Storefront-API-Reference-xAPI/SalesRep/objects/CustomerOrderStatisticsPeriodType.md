# CustomerOrderStatisticsPeriodType ==~object~==

This type reports aggregated order totals for a date range.

## Fields

| Field | Description |
|-------|-------------|
| `total` [ ==MoneyType== ](../../Cart/objects/money-type.md) | The total order value. |
| `count`  ==Int== | The number of orders. |
| `average` [ ==MoneyType== ](../../Cart/objects/money-type.md) | The average order value. |
| `firstOrderDate`  ==DateTime== | The date of the first order. |
| `lastOrderDate`  ==DateTime== | The date of the most recent order. |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../CustomerOrderStatisticsType">← CustomerOrderStatisticsType</a>
    <a href="../CustomerOrderStatisticsComparisonType">CustomerOrderStatisticsComparisonType →</a>
</div>
