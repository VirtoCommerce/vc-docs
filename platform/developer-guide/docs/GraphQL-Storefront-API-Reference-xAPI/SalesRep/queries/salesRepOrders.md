# salesRepOrders

This query returns the orders the rep created for their customers, filterable and paged. Add `organizationId` to scope the result to one customer.

## Arguments

| Argument | Description |
|----------|-------------|
| `storeId`  ==String== | The Id of the store. |
| `organizationId`  ==String== | The Id of a customer organization to scope the orders to. Optional. |
| `after`  ==String== | The cursor value to paginate through the results. |
| `first`  ==Int== | The number of items to return. |
| `sort`  ==String== | The sorting order of the returned orders. |

## Possible returns

| Possible return | Description |
|-----------------|-------------|
| [`SalesRepOrderType`](../objects/SalesRepOrderType.md) | A paged list of the orders the rep created for their customers. |

## Example

<div class="grid" markdown>

```graphql title="Query"
{
  salesRepOrders(storeId: "B2B-store", first: 20, sort: "createdDate:desc") {
    totalCount
    items {
      id
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
```

```json title="Return"
{
  "data": {
    "salesRepOrders": {
      "totalCount": 128,
      "items": [
        {
          "id": "c3d4e5f607182930",
          "number": "SO-2026-004821",
          "createdDate": "2026-07-28T14:10:00Z",
          "status": "Processing",
          "total": { "amount": 4820.00, "formattedAmount": "$4,820.00", "currency": { "code": "USD" } },
          "itemsCount": 7
        },
        {
          "id": "d4e5f60718293041",
          "number": "SO-2026-004799",
          "createdDate": "2026-07-21T09:32:00Z",
          "status": "Completed",
          "total": { "amount": 1290.50, "formattedAmount": "$1,290.50", "currency": { "code": "USD" } },
          "itemsCount": 3
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
    <a href="../salesRepCustomer">← salesRepCustomer query</a>
    <a href="../salesRepCustomerOrderStatistics">salesRepCustomerOrderStatistics query →</a>
</div>
