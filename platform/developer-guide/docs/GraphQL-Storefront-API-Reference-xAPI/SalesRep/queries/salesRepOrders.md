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
| Order connection | A paged list of the orders the rep created, each with `id`, `number`, `createdDate`, `status`, `total`, and `itemsCount`. |

## Example

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

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../salesRepCustomer">← salesRepCustomer query</a>
    <a href="../salesRepCustomerOrderStatistics">salesRepCustomerOrderStatistics query →</a>
</div>
