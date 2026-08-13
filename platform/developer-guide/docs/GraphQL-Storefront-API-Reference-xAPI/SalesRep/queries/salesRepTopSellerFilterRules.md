# salesRepTopSellerFilterRules

This query returns the category filters available for [salesRepTopSellers](salesRepTopSellers.md), rendered as category badges in the UI.

## Arguments

| Argument | Description |
|----------|-------------|
| `storeId`  ==String== | The Id of the store. |
| `cultureName`  ==String== | A language to retrieve data in. |

## Possible returns

| Possible return | Description |
|-----------------|-------------|
| [`SalesRepTopSellerFilterRuleType`](../objects/SalesRepTopSellerFilterRuleType.md) | The available category filters. |

## Example

<div class="grid" markdown>

```graphql title="Query"
{
  salesRepTopSellerFilterRules(storeId: "B2B-store", cultureName: "en-US") {
    name
    localizedName
  }
}
```

```json title="Return"
{
  "data": {
    "salesRepTopSellerFilterRules": [
      { "name": "power-tools", "localizedName": "Power tools" },
      { "name": "safety", "localizedName": "Safety" }
    ]
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../salesRepTopSellerSortRules">← salesRepTopSellerSortRules query</a>
    <a href="../salesRepOrderFilterRules">salesRepOrderFilterRules query →</a>
</div>
