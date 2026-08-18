# Pages ==~query~==

This query is used to retrieve a collection of pages based on specified criteria. 

## Arguments

| Argument                | Description                                                           |
|-------------------------|-----------------------------------------------------------------------|
| `after` ==String==      | A cursor value to paginate through the results.                       |
| `first` ==Int==         | The number of pages in a single query.                                |
| `storeId` ==String!==   | The Id of the store for which to retrieve pages.                      |
| `keyword` ==String!==   | A keyword or search term used to filter pages based on their content. |
| `cultureName` ==String==| A language to retrieve data in.                                       |


## Possible returns

| Possible return                                          	| Description                             	|
|---------------------------------------------------------	|------------------------------------------	|
| [`PageConnection`](../Objects/PageConnection.md)        	|  A connection to a collection of pages.  	|


## Example

<div class="grid" markdown>

```json title="Query"
{
  pages(storeId: "B2B-store", keyword: "aliases:test", after: "0", first: 30) {
    totalCount
    items {
      relativeUrl
      name
      __typename
    }
    pageInfo {
      startCursor
      endCursor
      hasNextPage
      hasPreviousPage
    }
  }
}
```

```json title="Return"
{
  "data": {
    "pages": {
      "totalCount": 1,
      "items": [
        {
          "relativeUrl": "/testpagefrompage",
          "name": "testpagefrompage",
          "__typename": "PageType"
        }
      ],
      "pageInfo": {
        "startCursor": "0",
        "endCursor": "1",
        "hasNextPage": false,
        "hasPreviousPage": false
      }
    }
  }
}
```

</div>