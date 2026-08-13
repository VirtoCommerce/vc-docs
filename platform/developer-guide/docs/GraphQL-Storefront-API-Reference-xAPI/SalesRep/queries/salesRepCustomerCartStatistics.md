# salesRepCustomerCartStatistics

This query returns aggregated cart statistics for the caller's customers, for example the number of active carts (open projects) over a date range.

## Arguments

| Argument | Description |
|----------|-------------|
| `currencyCode`  ==String== | The currency to report amounts in. |
| `cultureName`  ==String== | A language to retrieve data in. |

## Possible returns

| Possible return | Description |
|-----------------|-------------|
| [`CustomerCartStatisticsType`](../objects/CustomerCartStatisticsType.md) | Aggregated cart statistics for the customer. |

## Example

<div class="grid" markdown>

```graphql title="Query"
query CartStatistics {
  salesRepCustomerCartStatistics(currencyCode: "USD", cultureName: "en-US") {
    activeProjects: period(from: "2026-01-01T00:00:00Z", to: "2027-01-01T00:00:00Z", filter: "active-carts") {
      count
      total {
        amount
        formattedAmount
      }
      lastCartDate
    }
  }
}
```

```json title="Return"
{
  "data": {
    "salesRepCustomerCartStatistics": {
      "activeProjects": {
        "count": 7,
        "total": { "amount": 18940.00, "formattedAmount": "$18,940.00" },
        "lastCartDate": "2026-07-30T11:22:00Z"
      }
    }
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../salesRepCustomerOrderStatistics">← salesRepCustomerOrderStatistics query</a>
    <a href="../salesRepCustomerCounts">salesRepCustomerCounts query →</a>
</div>
