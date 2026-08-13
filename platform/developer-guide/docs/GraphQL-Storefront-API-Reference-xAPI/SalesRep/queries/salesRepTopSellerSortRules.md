# salesRepTopSellerSortRules

This query returns the ranking options available for [salesRepTopSellers](salesRepTopSellers.md), for example `by-units` (default) and `by-revenue`.

## Arguments

| Argument | Description |
|----------|-------------|
| `storeId`  ==String== | The Id of the store. |
| `cultureName`  ==String== | A language to retrieve data in. |

## Possible returns

| Possible return | Description |
|-----------------|-------------|
| [`SalesRepTopSellerSortRuleType`](../objects/SalesRepTopSellerSortRuleType.md) | The available ranking options. |

## Example

<div class="grid" markdown>

```graphql title="Query"
{
  salesRepTopSellerSortRules(storeId: "B2B-store", cultureName: "en-US") {
    name
    localizedName
  }
}
```

```json title="Return"
{
  "data": {
    "salesRepTopSellerSortRules": [
      { "name": "by-units", "localizedName": "By units" },
      { "name": "by-revenue", "localizedName": "By revenue" }
    ]
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../salesRepTopSellers">← salesRepTopSellers query</a>
    <a href="../salesRepTopSellerFilterRules">salesRepTopSellerFilterRules query →</a>
</div>
