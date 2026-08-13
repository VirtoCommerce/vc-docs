# salesRepCustomerCounts

This query returns how many customers the rep is assigned, and how many placed orders or were newly added over the date ranges you request.

## Arguments

This query takes no arguments. The result is scoped to the authenticated rep.

## Possible returns

| Possible return | Description |
|-----------------|-------------|
| [`SalesRepCustomerCountsType`](../objects/SalesRepCustomerCountsType.md) | Assigned, ordering, and new customer counts. |

## Example

<div class="grid" markdown>

```graphql title="Query"
query MyCustomers {
  salesRepCustomerCounts {
    assignedCustomers
    thisMonth: period(from: "2026-07-01T00:00:00Z", to: "2026-08-01T00:00:00Z") {
      orderingCustomers
      newCustomers
    }
    monthOverMonth: comparison(
      current:  { from: "2026-07-01T00:00:00Z", to: "2026-08-01T00:00:00Z" }
      previous: { from: "2026-06-01T00:00:00Z", to: "2026-07-01T00:00:00Z" }
    ) {
      orderingCustomersChange
      orderingCustomersChangePercent
      newCustomersChange
    }
  }
}
```

```json title="Return"
{
  "data": {
    "salesRepCustomerCounts": {
      "assignedCustomers": 128,
      "thisMonth": {
        "orderingCustomers": 34,
        "newCustomers": 5
      },
      "monthOverMonth": {
        "orderingCustomersChange": 4,
        "orderingCustomersChangePercent": 13.33,
        "newCustomersChange": 2
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
    <a href="../salesRepCustomerCartStatistics">← salesRepCustomerCartStatistics query</a>
    <a href="../salesRepTopSellers">salesRepTopSellers query →</a>
</div>
