# salesRepCustomers

This query returns the customer organizations the current rep serves, each with the rep's most recent order for that customer.

## Arguments

| Argument | Description |
|----------|-------------|
| `storeId`  ==String== | The Id of the store. |
| `cultureName`  ==String== | A language to retrieve data in. |
| `after`  ==String== | The cursor value to paginate through the results. |
| `first`  ==Int== | The number of items to return. |
| `sort`  ==String== | The sorting order of the returned customers. |

## Possible returns

| Possible return | Description |
|-----------------|-------------|
| Customer connection | A paged list of the organizations the rep serves, each with `organizationId`, `organizationName`, `iconUrl`, a structured `address`, and the rep's `lastOrder` for that customer. |

The `address` is structured (the default organization address, or its first). The storefront formats it for display, for example `City, Region`. It is loaded only when selected: requesting `address` loads the organization's addresses; omit it and only scalar columns such as `organizationName` and `iconUrl` are read.

## Example

```graphql title="Query"
{
  salesRepCustomers(storeId: "B2B-store", cultureName: "en-US", first: 20, sort: "name:asc") {
    totalCount
    items {
      organizationId
      organizationName
      iconUrl
      address {
        line1
        city
        regionName
        postalCode
        countryCode
      }
      lastOrder {
        number
        createdDate
        status
        statusDisplayValue
        total {
          amount
          formattedAmount
          currency {
            code
          }
        }
        itemsCount
      }
    }
  }
}
```

Each item also exposes `orderStatistics(from, to)`, which returns the customer's `total` and `count` for a date range. Request it under aliases to add purchase columns, for example year-to-date versus last year:

```graphql title="Query with purchase columns"
query CustomersWithPurchaseColumns {
  salesRepCustomers(storeId: "B2B-store", cultureName: "en-US", first: 20, sort: "ytd-purchases") {
    totalCount
    items {
      organizationId
      organizationName
      ytd: orderStatistics(from: "2026-01-01T00:00:00Z", to: "2027-01-01T00:00:00Z") {
        total { amount formattedAmount }
        count
      }
      lastYear: orderStatistics(from: "2025-01-01T00:00:00Z", to: "2026-01-01T00:00:00Z") {
        total { amount formattedAmount }
        count
      }
    }
  }
}
```

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../customerSalesReps">← customerSalesReps query</a>
    <a href="../salesRepCustomer">salesRepCustomer query →</a>
</div>
