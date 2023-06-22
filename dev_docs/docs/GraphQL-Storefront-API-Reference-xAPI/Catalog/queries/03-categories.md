# Categories ==~query~==

This connection allows you to search for categories.

## Arguments

| Argument                              	| Description                                                                                                                                              	|
|---------------------------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------	|
| `after` {==String==}              	| Defines a cursor value to paginate through the results.                                                                                                 	|
| `first` {==Int==}                 	| Indicates the number of pages in a single query.                                                                                                        	|
| `storeId` {==String==}            	| Specifies the ID of the store to retrieve pages from.                                                                                                   	|
| `cultureName` {==String==}        	| Specifies the language.                                                                                                                                 	|
| `userId` {==String==}             	| Identifies the user.                                                                                                                                    	|
| `currencyCode` {==String==}       	| A standardized code representing a specific currency.                                                                                                   	|
| `query` {==String==}              	| Performs the full-text search.                                                                                                                          	|
| `filter` {==String==}             	| Applies a filter to the query results.                                                                                                                  	|
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
            storeId: "Electronics"
            userId: "d97ee2c7-e29d-440a-a43a-388eb5586087"
            cultureName: "en-Us"
            currencyCode: "USD"
      	    first: 10
  	        after: "10")
        {
            items
            {
                id
                name
                hasParent
            }
            pageInfo
            {
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
                  "id": "0d133bb06cc7437cb33402124719029b",
                  "name": "SunBriteTV",
                  "hasParent": true
                },
                {
                  "id": "c8eacb22b7754e83be794713e3fb175a",
                  "name": "Vizio",
                  "hasParent": true
                },
                {
                  "id": "d70d0ecf-6aa9-420a-99fc-d6f1c93bb4b5",
                  "name": "X-category",
                  "hasParent": false
                },
                {
                  "id": "62303567-745e-4ecf-89f3-35246e5b5156",
                  "name": "B-category",
                  "hasParent": false
                },
                {
                  "id": "bb06b0cb-4555-4a45-a3ff-b7db8325d38f",
                  "name": "D-category",
                  "hasParent": false
                }
            ],
            "pageInfo": {
              "hasNextPage": false,
              "startCursor": "10"
            }
        }
      }
    }
    ```
