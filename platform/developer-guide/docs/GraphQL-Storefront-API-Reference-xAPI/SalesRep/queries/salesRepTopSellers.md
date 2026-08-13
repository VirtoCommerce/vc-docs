# salesRepTopSellers

This query returns the best-selling products for the rep's customers, ranked by units or revenue over a date range.

## Arguments

| Argument | Description |
|----------|-------------|
| `storeId`  ==String== | The Id of the store. |
| `organizationId`  ==String== | The Id of a customer organization to scope the result to. Omit it for a cross-customer dashboard. |
| `sort`  ==String== | The ranking order. Use a [salesRepTopSellerSortRules](salesRepTopSellerSortRules.md) name, such as `by-units` (default) or `by-revenue`. |
| `period` | The date range to rank over, as `{ from, to }`. |
| `take`  ==Int== | The number of products to return. |
| `cultureName`  ==String== | A language to retrieve data in. |
| `filter`  ==String== | A [salesRepTopSellerFilterRules](salesRepTopSellerFilterRules.md) name that restricts the result to that category's subtree. Optional. |

## Possible returns

| Possible return | Description |
|-----------------|-------------|
| [`SalesRepTopSellerType`](../objects/SalesRepTopSellerType.md) | A ranked list of best-selling products. |

## Example

<div class="grid" markdown>

```graphql title="Query"
query TopProducts {
  salesRepTopSellers(
    storeId: "B2B-store"
    organizationId: "f081c52234754c9c8229aa42d6a19220"
    sort: "by-revenue"
    period: { from: "2026-06-23T00:00:00Z", to: "2026-07-23T00:00:00Z" }
    take: 5
    cultureName: "en-US"
  ) {
    rank
    productId
    name
    sku
    imageUrl
    units
    revenue {
      amount
      formattedAmount
      currency {
        code
      }
    }
  }
}
```

```json title="Return"
{
  "data": {
    "salesRepTopSellers": [
      {
        "rank": 1,
        "productId": "9cbd8f316e2547e0a1b0f2c3d4e5f6a7",
        "name": "Cordless Drill 20V",
        "sku": "DRL-20V-001",
        "imageUrl": "https://media.example.com/catalog/drill-20v.jpg",
        "units": 320,
        "revenue": { "amount": 41600.00, "formattedAmount": "$41,600.00", "currency": { "code": "USD" } }
      },
      {
        "rank": 2,
        "productId": "1a2b3c4d5e6f7081a2b3c4d5e6f70819",
        "name": "Safety Goggles",
        "sku": "SFG-114",
        "imageUrl": "https://media.example.com/catalog/goggles.jpg",
        "units": 540,
        "revenue": { "amount": 10800.00, "formattedAmount": "$10,800.00", "currency": { "code": "USD" } }
      }
    ]
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../salesRepCustomerCounts">← salesRepCustomerCounts query</a>
    <a href="../salesRepTopSellerSortRules">salesRepTopSellerSortRules query →</a>
</div>
