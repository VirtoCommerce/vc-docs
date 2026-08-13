# salesRepOrderFilterRules

This query returns the filters available for the orders list and order statistics.

## Arguments

| Argument | Description |
|----------|-------------|
| `storeId`  ==String== | The Id of the store. |
| `cultureName`  ==String== | A language to retrieve data in. |

## Possible returns

| Possible return | Description |
|-----------------|-------------|
| [`SalesRepOrderFilterRuleType`](../objects/SalesRepOrderFilterRuleType.md) | The available order filters. |

## Example

<div class="grid" markdown>

```graphql title="Query"
{
  salesRepOrderFilterRules(storeId: "B2B-store", cultureName: "en-US") {
    name
    localizedName
  }
}
```

```json title="Return"
{
  "data": {
    "salesRepOrderFilterRules": [
      { "name": "all", "localizedName": "All" },
      { "name": "completed", "localizedName": "Completed" },
      { "name": "processing", "localizedName": "Processing" }
    ]
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../salesRepTopSellerFilterRules">← salesRepTopSellerFilterRules query</a>
    <a href="../salesRepCartFilterRules">salesRepCartFilterRules query →</a>
</div>
