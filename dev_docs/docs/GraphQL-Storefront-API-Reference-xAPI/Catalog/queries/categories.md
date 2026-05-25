# Categories ==~query~==

This connection allows you to search for categories.

## Arguments

| Argument                           	| Description                                                                                                                                              	|
|------------------------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------	|
| `after` {==String==}              	| A cursor value to paginate through the results.                                                                                                         	|
| `first` {==Int==}                 	| The number of pages in a single query.                                                                                                                  	|
| `storeId` {==String==}            	| The ID of the store to retrieve pages from.                                                                                                              	|
| `cultureName` {==String==}        	| A language to retrieve data in.                                                                                                                          	|
| `userId` {==String==}             	| The current user Id.                                                                                                                                    	|
| `currencyCode` {==String==}       	| A standardized code of a specific currency.                                                                                                   	|
| `query` {==String==}              	| Performs the full-text search.                                                                                                                          	|
| `filter` {==String==}             	| Filters query results.                                                                                                                  	|
| `fuzzy` {==Boolean==}             	| If true, includes slight variations<br>of the search text in the returned products.                                                                      	|
| `fuzzyLevel` {==Int==}            	| The fuzziness level is measured by the <br>Damerau-Levenshtein distance. It calculates the number of operations<br> required to transform one word into another. 	|
| `facet` {==String==}              	| Calculates statistical counts to aid in faceted navigation.                                                                                             	|
| `sort` {==String==}               	| Specifies the sorting order of the returned products.                                                                                                   	|
| `productIds` {==String==}         	| Identifies specific products within a given store.                                                                                                      	|

## Possible returns

| Possible return                                                       	| Description                           	|
|-----------------------------------------------------------------------	|---------------------------------------	|
| [`CategoryConnection`](../objects/category/CategoryConnection.md)     	| A connection to a list of categories.  	|

## Examples

=== "Query"
    ```json linenums="1"
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
=== "Return"
    ```json linenums="1"
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
            {
              "id": "12240a74-ebc2-40cf-baea-5ba1a6408713",
              "name": "Tea",
              "hasParent": true
            },
            {
              "id": "782ed5be-08a6-4609-908a-d54f6cd15cd6",
              "name": "Gift cards",
              "hasParent": true
            },
            {
              "id": "e411f61f-f688-41db-80a0-fa804beb670f",
              "name": "Chocolate",
              "hasParent": true
            },
            {
              "id": "1df5e23c-6eef-4fa8-bf79-fa6777f19114",
              "name": "Cookie",
              "hasParent": true
            }
          ],
          "pageInfo": {
            "hasNextPage": true,
            "startCursor": "10"
          }
        }
      }
    }
    ```
