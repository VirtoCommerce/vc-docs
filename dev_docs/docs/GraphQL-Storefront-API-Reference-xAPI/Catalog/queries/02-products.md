# Products ==~query~==

This connection allows you to search for products.

## Arguments

| Argument                     	      | Description                                                                                                                                             	|
|------------------------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------	|
| `after` {==String==}               	| A cursor value to paginate through the results.                                                                                                 	|
| `first` {==Int==}                 	| The number of pages in a single query.                                                                                                        	|
| `storeId` {==String!==}           	| The ID of the store to retrieve pages from.                                                                                                   	|
| `userId` {==String==}             	| The user Id.                                                                                                                                    	|
| `currencyCode` {==String==}       	| A standardized code of a specific currency.                                                                                                   	|
| `query` {==String==}              	| Performs the full-text search.                                                                                                                          	|
| `cultureName` {==String==}        	| The language to retrieve data in.                                                                                                                                 	|
| `filter` {==String==}             	| Filters query results.                                                                                                                  	|
| `fuzzy` {==Boolean==}             	| If true, includes slight variations of the search text<br>in the returned products.                                                                       |
| `fuzzyLevel` {==Int==}            	| The fuzziness level is measured by the Damerau-Levenshtein distance.<br>It calculates the number of operations required to transform one word into another.|
| `facet` {==String==}              	| Calculates statistical counts to aid in faceted navigation.                                                                                             	|
| `sort` {==String==}               	| Specifies the sorting order of the returned products.                                                                                                   	|
| `productIds` {==String==}         	| Identifies specific products within a given store.                                                                                                      	|

## Possible returns

| Possible return                                                         	| Description                           	|
|--------------------------------------------------------------------------	|---------------------------------------	|
| [`ProductConnection`](../objects/ProductConnection/ProductConnection.md)  |  A connection to a list of products.   	|

## Examples

=== "Query"
    ```json linenums="1"
    {
        products(
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
                code
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
        "products": {
          "items": [
            {
              "id": "7c835a9b1c8e4445aa118dae659231c3",
              "code": "SAG920F32GBB"
            },
            {
              "id": "8db64bd60a354c4c96e25e61d7361565",
              "code": "LG65EG9600"
            },
            {
              "id": "8e3a763a3cff407b97e2a2f6390b4048",
              "code": "SAHTJ5500W"
            },
            {
              "id": "92e671024a8648de97dedcd488f58455",
              "code": "SUDS3214PSL"
            },
            {
              "id": "be4ab6701f84440ea84ccd09210cbe0a",
              "code": "VIM70C3"
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
