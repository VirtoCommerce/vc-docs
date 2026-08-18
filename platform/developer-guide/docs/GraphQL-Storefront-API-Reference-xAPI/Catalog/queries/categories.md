# Categories ==~query~==

This connection allows you to search for categories.

## Arguments

| Argument                           	| Description                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------	|
| `after`  ==String==               	| A cursor value to paginate through the results.                                       |
| `first`  ==Int==                  	| The number of pages in a single query.                                                |
| `storeId`  ==String==             	| The ID of the store to retrieve pages from.                                           |
| `cultureName`  ==String==         	| A language to retrieve data in.                                                       |
| `userId`  ==String==              	| The current user Id.                                                                 	|
| `currencyCode`  ==String==        	| A standardized code of a specific currency.                                           |
| `query`  ==String==               	| Performs the full-text search.                                                       	|
| `filter`  ==String==              	| Filters query results.                                                               	|
| `fuzzy`  ==Boolean==              	| If true, includes slight variations<br>of the search text in the returned products.   |
| `fuzzyLevel`  ==Int==             	| The fuzziness level is measured by the <br>Damerau-Levenshtein distance. It calculates the number of operations<br> required to transform one word into another. 	|
| `facet`  ==String==               	| Calculates statistical counts to aid in faceted navigation.                           |
| `sort`  ==String==                	| Specifies the sorting order of the returned products.                                 |
| `productIds`  ==String==          	| Identifies specific products within a given store.                                    |

## Possible returns

| Possible return                                                       	| Description                           	|
|-----------------------------------------------------------------------	|---------------------------------------	|
| [`CategoryConnection`](../objects/category/CategoryConnection.md)     	| A connection to a list of categories.  	|


## Example

<div class="grid" markdown>

```json title="Query"
{
  categories(
    storeId: "B2B-Store"
    userId: "d97ee2c7-e29d-440a-a43a-388eb5586087"
    cultureName: "en-Us"
    currencyCode: "USD"
    first: 10
    after: "10"
  ) {
    items {
      id
      name
      hasParent
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
    "categories": {
      "items": [
        {
          "id": "b674f311-5dbe-42f7-bc30-8076744c59bf",
          "name": "Kitchen supplies",
          "hasParent": false
        },
        {
          "id": "177c7dc2-7e21-4890-81fb-c7c0d37125b0",
          "name": "Coffee",
          "hasParent": true
        },
      // ... more product items
      ],
      "pageInfo": {
        "hasNextPage": true,
        "startCursor": "10"
      }
    }
  }
}
```

</div>