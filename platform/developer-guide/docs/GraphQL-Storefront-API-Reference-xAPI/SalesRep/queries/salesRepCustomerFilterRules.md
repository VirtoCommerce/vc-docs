# salesRepCustomerFilterRules

This query returns the filters available for the customers list and customer counts.

## Arguments

| Argument | Description |
|----------|-------------|
| `storeId`  ==String== | The Id of the store. |
| `cultureName`  ==String== | A language to retrieve data in. |

## Possible returns

| Possible return | Description |
|-----------------|-------------|
| [`SalesRepCustomerFilterRuleType`](../objects/SalesRepCustomerFilterRuleType.md) | The available customer filters. |

## Example

<div class="grid" markdown>

```graphql title="Query"
{
  salesRepCustomerFilterRules(storeId: "B2B-store", cultureName: "en-US") {
    name
    localizedName
  }
}
```

```json title="Return"
{
  "data": {
    "salesRepCustomerFilterRules": [
      { "name": "all", "localizedName": "All" }
    ]
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../salesRepCartFilterRules">← salesRepCartFilterRules query</a>
    <a href="../../objects/CustomerOrderStatisticsType">CustomerOrderStatisticsType →</a>
</div>
