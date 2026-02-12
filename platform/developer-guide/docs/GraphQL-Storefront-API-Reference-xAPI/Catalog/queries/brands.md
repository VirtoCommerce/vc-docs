# Brands ==~query~==

This connection allows you to retrieve a list of brands, supporting pagination, localization, sorting, and keyword-based search.

## Arguments

| Argument                  | Description                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------- |
| `after` ==String==        | A cursor value to paginate through the results.                                                       |
| `first` ==Int==           | The number of brands to retrieve in a single query.                                                   |
| `storeId` ==String!==     | The ID of the store to retrieve brands from. (Required)                                               |
| `userId` ==String==       | The ID of the current user.                                                                           |
| `currencyCode` ==String== | A standardized code of a specific currency. Not used in brand filtering but included for consistency. |
| `cultureName` ==String==  | The language to retrieve data in.                                                                     |
| `sort` ==String==         | Specifies the sorting order of the returned brands.                                                   |
| `keyword` ==String==      | Filters brands by the keyword in their name or description.                                           |

## Possible returns

| Possible return                                    | Description                       |
| -------------------------------------------------- | --------------------------------- |
| [`BrandConnection`](../objects/BrandConnection.md) | A connection to a list of brands. |


## Example

<div class="grid" markdown>

```json title="Query"
{
  brands(
    storeId: "B2B-Store"
    cultureName: "en-US"
    first: 5
    sort: "name"
  ) {
      items {
        id
        name
        featured
        logoUrl
      }
      pageInfo {
        hasNextPage
        startCursor
      }
    }
}
```

```json title="Return"
{
  "data": {
    "brands": {
      "items": [
        {
          "id": "68162d61-2faa-454c-8d79-a3fdf99eedef",
          "name": "Absolut",
          "featured": true,
          "logoUrl": "https://qademovc3.blob.core.windows.net/catalog/4f354/8df2b/Absolute.png"
        },
        {
          "id": "d33aba5f-b256-4824-98ad-e55b93c10830",
          "name": "Affligem",
          "featured": true,
          "logoUrl": "https://qademovc3.blob.core.windows.net/catalog/4f354/61c01/abbaye-de-affligem.svg"
        },
        // ... more product items
    ],
    "pageInfo": {
        "hasNextPage": true,
        "startCursor": "0"
    }
    }
  }
}
```

</div>