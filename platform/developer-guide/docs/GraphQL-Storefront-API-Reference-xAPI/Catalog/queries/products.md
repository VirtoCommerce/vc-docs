# Products ==~query~==

This connection allows you to search for products.

## Arguments

| Argument                     	      | Description                                                                                                                                             	|
|------------------------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------	|
| `after`  ==String==                	| A cursor value to paginate through the results.                                                                                                 	|
| `first`  ==Int==                  	| The number of pages in a single query.                                                                                                        	|
| `storeId`  ==String!==            	| The ID of the store to retrieve pages from.                                                                                                   	|
| `userId`  ==String==              	| The current user Id.                                                                                                                                    	|
| `currencyCode`  ==String==        	| A standardized code of a specific currency.                                                                                                   	|
| `query`  ==String==               	| Performs the full-text search.                                                                                                                          	|
| `cultureName`  ==String==         	| A language to retrieve data in.                                                                                                                                 	|
| `filter`  ==String==              	| Filters query results.                                                                                                                  	|
| `fuzzy`  ==Boolean==              	| If true, includes slight variations of the search text<br>in the returned products.                                                                       |
| `fuzzyLevel`  ==Int==             	| The fuzziness level is measured by the Damerau-Levenshtein distance.<br>It calculates the number of operations required to transform one word into another.|
| `facet`  ==String==               	| Calculates statistical counts to aid in faceted navigation.                                                                                             	|
| `sort`  ==String==                	| Specifies the sorting order of the returned products.                                                                                                   	|
| `productIds`  ==String==          	| Identifies specific products within a given store.                                                                                                      	|

## Possible returns

| Possible return                                                         	| Description                           	|
|--------------------------------------------------------------------------	|---------------------------------------	|
| [`ProductConnection`](../objects/ProductConnection/ProductConnection.md)  |  A connection to a list of products.   	|

## Examples

=== "Query 1"
    ```json linenums="1"
    {
      products(
        storeId: "B2B-Store"
        userId: "d97ee2c7-e29d-440a-a43a-388eb5586087"
        cultureName: "en-Us"
        currencyCode: "USD"
        first: 10
        after: "10"
      ) {
        items {
          id
          code
        }
        pageInfo {
          hasNextPage
          startCursor
        }
      }
    }
    ```

=== "Return 1"
    ```json linenums="1"
    {
      "data": {
        "products": {
          "items": [
            {
              "id": "120bd04d270a42f1b6f490f0cafd4ca7",
              "code": "5ZU94"
            },
            {
              "id": "74f89c449ad44d52a148123e587212c2",
              "code": "5ZE93"
            },
            {
              "id": "439218e0d5ca4e748cabdd7190e9ccc2",
              "code": "3JWN8"
            },
            {
              "id": "9fc0bb2a9be646778952d0adf4c862e1",
              "code": "41MY53"
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

=== "Query 2"
    ```json linenums="1"
    {
      products(
        storeId: "B2B-store"
        filter: "productfamilyid:baa4931161214690ad51c50787b1ed94 status:hidden,visible"
        query: "Stainless Steel Carriage Bolt"
        first: 23
        after: "0"
      ) {
        totalCount
        items {
          id
          code
        }
      }
    }
    ```

=== "Return 2"
    ```json linenums="1"
    {
      "data": {
        "products": {
          "totalCount": 4,
          "items": [
            {
              "id": "330e7e41055b4781a9f4d3868557c093",
              "code": "53MF89"
            },
            {
              "id": "72c69a42-4c24-40c9-baa8-6922106be6bf",
              "code": "OBV-20813041"
            },
            {
              "id": "baa4931161214690ad51c50787b1ed94",
              "code": "53MF87"
            },
            {
              "id": "6ba8b1a9b2a54298a1ec1aea6a4bb3b2",
              "code": "53MF88"
            }
          ]
        }
      }
    }
    ```