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
| [`SalesRepContactType`](../objects/SalesRepContactType.md) | A paged list of the reps supporting the caller's organization. |

## Example

<div class="grid" markdown>

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

```json title="Return"
{
  "data": {
    "customerSalesReps": {
      "totalCount": 2,
      "items": [
        {
          "id": "a1b2c3d4e5f60718",
          "fullName": "Jordan Blake",
          "about": "Serving industrial supply accounts in the Midwest.",
          "photoUrl": "https://media.example.com/reps/jordan-blake.jpg",
          "emails": ["jordan.blake@example.com"],
          "phones": ["+1-312-555-0142"]
        },
        {
          "id": "b2c3d4e5f6071829",
          "fullName": "Priya Nair",
          "about": null,
          "photoUrl": null,
          "emails": ["priya.nair@example.com"],
          "phones": []
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
    <a href="../../overview">← Sales Rep module overview</a>
    <a href="../salesRepCustomers">salesRepCustomers query →</a>
</div>
