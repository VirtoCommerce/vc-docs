# salesRepCartFilterRules

This query returns the filters available for cart statistics.

## Arguments

| Argument | Description |
|----------|-------------|
| `storeId`  ==String== | The Id of the store. |
| `cultureName`  ==String== | A language to retrieve data in. |

## Possible returns

| Possible return | Description |
|-----------------|-------------|
| [`SalesRepCartFilterRuleType`](../objects/SalesRepCartFilterRuleType.md) | The available cart filters. |

## Example

<div class="grid" markdown>

```graphql title="Query"
{
  salesRepCartFilterRules(storeId: "B2B-store", cultureName: "en-US") {
    name
    localizedName
  }
}
```

```json title="Return"
{
  "data": {
    "salesRepCartFilterRules": [
      { "name": "active-carts", "localizedName": "Active carts" }
    ]
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../salesRepOrderFilterRules">← salesRepOrderFilterRules query</a>
    <a href="../salesRepCustomerFilterRules">salesRepCustomerFilterRules query →</a>
</div>