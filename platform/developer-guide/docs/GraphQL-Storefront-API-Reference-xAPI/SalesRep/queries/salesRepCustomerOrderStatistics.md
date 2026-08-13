# salesRepCustomerOrderStatistics

This query returns aggregated order statistics for a single customer organization: totals, counts, and averages over the date ranges you request, plus period-over-period comparisons.

## Arguments

| Argument | Description |
|----------|-------------|
| `organizationId`  ==String== | The Id of the customer organization. |
| `currencyCode`  ==String== | The currency to report amounts in. |
| `cultureName`  ==String== | A language to retrieve data in. |

## Possible returns

| Possible return | Description |
|-----------------|-------------|
| [`CustomerOrderStatisticsType`](../objects/CustomerOrderStatisticsType.md) | Aggregated order statistics for the customer. |

## Example

<div class="grid" markdown>

```graphql title="Query"
query CustomerSalesData {
  salesRepCustomerOrderStatistics(organizationId: "f081c52234754c9c8229aa42d6a19220", currencyCode: "USD", cultureName: "en-US") {
    currencyCode
    mtd: period(from: "2026-07-01T00:00:00Z", to: "2026-08-01T00:00:00Z") {
      total { amount formattedAmount }
      count
      average { amount formattedAmount }
    }
    mtdVsLastYear: comparison(
      current:  { from: "2026-07-01T00:00:00Z", to: "2026-08-01T00:00:00Z" }
      previous: { from: "2025-07-01T00:00:00Z", to: "2025-08-01T00:00:00Z" }
    ) {
      totalChange { amount }
      totalChangePercent
      countChange
      countChangePercent
    }
    ytd: period(from: "2026-01-01T00:00:00Z", to: "2027-01-01T00:00:00Z") {
      total { amount formattedAmount }
      count
      average { amount formattedAmount }
      lastOrderDate
    }
    ytdVsLastYear: comparison(
      current:  { from: "2026-01-01T00:00:00Z", to: "2027-01-01T00:00:00Z" }
      previous: { from: "2025-01-01T00:00:00Z", to: "2026-01-01T00:00:00Z" }
    ) {
      totalChange { amount }
      totalChangePercent
      countChange
      countChangePercent
    }
    sinceDate: period {
      firstOrderDate
      lastOrderDate
    }
  }
}
```

```json title="Return"
{
  "data": {
    "salesRepCustomerOrderStatistics": {
      "currencyCode": "USD",
      "mtd": {
        "total": { "amount": 48250.00, "formattedAmount": "$48,250.00" },
        "count": 12,
        "average": { "amount": 4020.83, "formattedAmount": "$4,020.83" }
      },
      "mtdVsLastYear": {
        "totalChange": { "amount": 6300.00 },
        "totalChangePercent": 15.02,
        "countChange": 3,
        "countChangePercent": 33.33
      },
      "ytd": {
        "total": { "amount": 312800.00, "formattedAmount": "$312,800.00" },
        "count": 84,
        "average": { "amount": 3723.81, "formattedAmount": "$3,723.81" },
        "lastOrderDate": "2026-07-28T14:10:00Z"
      },
      "ytdVsLastYear": {
        "totalChange": { "amount": 41200.00 },
        "totalChangePercent": 15.16,
        "countChange": 9,
        "countChangePercent": 12.00
      },
      "sinceDate": {
        "firstOrderDate": "2019-03-12T09:41:00Z",
        "lastOrderDate": "2026-07-28T14:10:00Z"
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
    <a href="../salesRepOrders">← salesRepOrders query</a>
    <a href="../salesRepCustomerCartStatistics">salesRepCustomerCartStatistics query →</a>
</div>
