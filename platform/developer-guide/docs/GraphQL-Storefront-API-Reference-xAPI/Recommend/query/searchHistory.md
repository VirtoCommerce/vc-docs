# searchHistory ==~query~==

This query allows you to retrieve the most recent search terms entered by a specific user within a given store.

## Arguments

| Argument              | Description                                                            |
| --------------------- | ---------------------------------------------------------------------- |
| `storeId` ==String!== | The ID of the store for which search history should be retrieved.      |
| `maxCount` ==Int!==   | The maximum number of recent search queries to return.                 |

## Possible return

| Possible return                                                    | Description                                                                 |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| [`SearchHistoryResultType`](../object/SearchHistoryResultType.md)  | A list of search terms previously entered by the user in the given context. |

## Example

<div class="grid" markdown>

```graphql title="Query"
query {
  searchHistory(storeId: "b2b-store", maxCount: 5) {
    queries
  }
}
```

```json title="Return"
{
  "data": {
    "searchHistory": {
      "queries": [
        "apple",
        "epson",
        "samsung",
        "xiaomi",
        "kodak"
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
    <a href="../recentlyBrowsed">← RecentlyBrowsed query</a>
    <a href="../../object/GetRecommendationsResponseType">GetRecommendationsResponseType →</a>
</div>
