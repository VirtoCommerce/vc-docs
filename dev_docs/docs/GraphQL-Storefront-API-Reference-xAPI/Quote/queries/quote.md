
# Quote

This query allows you to get a quote by its ID and calculate the totals.

## Definition

```
quote(id: !string, storeId: !string, userId: !string, currencyCode: !string, cultureName: !string)
```

## Arguments

| Name | Type | Description |
|---|---|---|
| `id` | Non null StringGraphType | Id of the product. |
| `storeId` | Non null StringGraphType | Store Id. |
| `userId` | Non null StringGraphType | Current user Id. |
| `currencyCode` | StringGraphType | The currency for which all prices<br> data will be returned.<br> **Example**: `"USD"` |
| `cultureName` | StringGraphType | The language for which all localized<br> property dictionary items will be returned.<br> **Example**: `"en-US"` |

## Example

```
query {
  quote(id: "70e6807d-bd42-4c78-bc0d-bb2f3ff7ae65") {
    id
    number
    status
    comment
    totals {
      grandTotalInclTax {
        formattedAmount
      }
    }
    items {
      name
      salePrice {
        formattedAmount
      }
      selectedTierPrice {
        quantity
        price {
          formattedAmount
        }
      }
    }
  }
}
```
