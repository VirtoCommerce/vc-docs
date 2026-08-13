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
| [`SalesRepCustomerType`](../objects/SalesRepCustomerType.md) | A paged list of the customer organizations the rep serves. |

## Example

<div class="grid" markdown>

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

```json title="Return"
{
  "data": {
    "salesRepCustomers": {
      "totalCount": 42,
      "items": [
        {
          "organizationId": "7b8c1f2a3d4e5f60",
          "organizationName": "Acme Industrial Supplies",
          "iconUrl": "https://media.example.com/orgs/acme.png",
          "address": {
            "line1": "482 Warehouse Ave",
            "city": "Columbus",
            "regionName": "Ohio",
            "postalCode": "43004",
            "countryCode": "US"
          },
          "lastOrder": {
            "number": "SO-2026-004821",
            "createdDate": "2026-07-28T14:10:00Z",
            "status": "Processing",
            "total": { "amount": 4820.00, "formattedAmount": "$4,820.00", "currency": { "code": "USD" } },
            "itemsCount": 7
          }
        }
      ]
    }
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../customerSalesReps">← customerSalesReps query</a>
    <a href="../salesRepCustomer">salesRepCustomer query →</a>
</div>
