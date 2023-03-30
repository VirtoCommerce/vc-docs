
# Quotes

This query allows getting a specified number of quotes from a particular user.

## Definition

```
quotes(userId: !string, storeId: !string, currencyCode: !string, cultureName: !string, sort: !string, first: !int):
```

## Arguments


| Name | Type | Description |
|---|---|---|
| `userId` | Non null StringGraphType | Id of the product. |
| `storeId` | Non null StringGraphType | Store Id. |
| `currencyCode` | StringGraphType | The currency for which all<br> prices data will be returned.<br> **Example**: `"USD"` |
| `cultureName` | StringGraphType | The language for which all<br> localized property dictionary<br> items will be returned.<br> **Example**: `"en-US"` |
| `sort` | StringGraphType | The sort expression. |
| `first` | Int | The maximum number of<br> edges to return.  |

## Example

```
query {
  quotes(
    userId: "edec910a-122f-4391-b026-831771c3c947"
    storeId:"B2B-store",
    currencyCode:"USD",
    cultureName:"en-US",
    sort: "createdDate"
    first: 10
  ) {
    totalCount
    items {
      id
      number
      status
      totals {
        grandTotalInclTax {
          formattedAmount
        }
      }
    }
  }
}
```
