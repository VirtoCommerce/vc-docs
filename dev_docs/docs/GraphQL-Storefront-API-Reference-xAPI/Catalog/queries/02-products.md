# Products ==~query~==

This connection allows you to search for products.

## Arguments

| Argument                        	      | Description                                                                                                                                             	|
|---------------------------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------	|
| `after`<br>{==String==}               	| Defines a cursor value to paginate through the results.                                                                                                 	|
| `first` <br>{==Int==}                 	| Indicates the number of pages in a single query.                                                                                                        	|
| `storeId` <br>{==String!==}           	| Specifies the ID of the store to retrieve pages from.                                                                                                   	|
| `userId` <br>{==String==}             	| Identifies the user.                                                                                                                                    	|
| `currencyCode` <br>{==String==}       	| A standardized code representing a specific currency.                                                                                                   	|
| `query` <br>{==String==}              	| Performs the full-text search.                                                                                                                          	|
| `cultureName` <br>{==String==}        	| Specifies the language.                                                                                                                                 	|
| `filter` <br>{==String==}             	| Applies a filter to the query results.                                                                                                                  	|
| `fuzzy` <br>{==Boolean==}             	| If true, includes slight variations of the search text<br>in the returned products.                                                                        	|
| `fuzzyLevel` <br>{==Int==}            	| The fuzziness level is measured by the Damerau-Levenshtein distance.<br>It calculates the number of operations required to transform one word into another. 	|
| `facet` <br>{==String==}              	| Calculates statistical counts to aid in faceted navigation.                                                                                             	|
| `sort` <br>{==String==}               	| Specifies the sorting order of the returned products.                                                                                                   	|
| `productIds` <br>{==String==}         	| Identifies specific products within a given store.                                                                                                      	|

## Possible returns

| Possible return                                          	| Description                           	|
|---------------------------------------------------------	|---------------------------------------	|
| [`ProductConnection`](../objects/ProductConnection/ProductConnection.md)            	|  A connection to a list of products.   	|

## Examples
<hr />
=== "Query"
    ```json
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
    ```json
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
