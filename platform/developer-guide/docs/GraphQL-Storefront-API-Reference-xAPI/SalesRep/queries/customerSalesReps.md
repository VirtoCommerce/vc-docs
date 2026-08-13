# customerSalesReps

This query returns the sales representatives supporting the caller's organization.

## Arguments

| Argument | Description |
|----------|-------------|
| `storeId`  ==String== | The Id of the store. |
| `after`  ==String== | The cursor value to paginate through the results. |
| `first`  ==Int== | The number of items to return. |

## Possible returns

| Possible return | Description |
|-----------------|-------------|
| Sales rep connection | A paged list of the reps supporting the caller's organization, each with `id`, `fullName`, `about`, `photoUrl`, `emails`, and `phones`. |

## Example

```graphql title="Query"
{
  customerSalesReps(storeId: "B2B-store", first: 10) {
    totalCount
    items {
      id
      fullName
      about
      photoUrl
      emails
      phones
    }
  }
}
```

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../overview">← Sales Rep module overview</a>
    <a href="../salesRepCustomers">salesRepCustomers query →</a>
</div>
