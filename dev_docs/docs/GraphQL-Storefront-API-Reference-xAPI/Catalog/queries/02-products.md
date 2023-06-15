# Products

This connection allows you to search for products.

<<<<<<< Updated upstream
## Definition

```
products(productIds: string[], storeId: !string, userId: !string, currencyCode: string, cultureName: string, query: string, filter: string, fuzzy: bool, fuzzyLevel: int, facet: string, sort: string)
```

## Arguments

|# |Name        |Type                     |Description                |
|--|------------|-------------------------|---------------------------|
| 1|productIds  |List of  StringGraphType |Products Ids               |
| 2|storeId     |Non null StringGraphType |Store Id                   |
| 3|userId      |Non null StringGraphType |Current user Id            |
| 4|currencyCode|StringGraphType          |Currency code (e.g. "USD") |
| 5|cultureName |StringGraphType          |Culture name (e.g. "en-US")|
| 6|query       |StringGraphType          |The query parameter performs the full-text search|
| 7|filter      |StringGraphType          |This parameter applies a filter to the query results|
| 8|fuzzy       |BooleanGraphType         |When the fuzzy query parameter is set to true the search endpoint will also return products that contain slight differences to the search text|
| 9|fuzzyLevel  |IntGraphType             |The fuzziness level is quantified in terms of the Damerau-Levenshtein distance, this distance being the number of operations needed to transform one word into another|
|10|facet       |StringGraphType          |Facets calculate statistical counts to aid in faceted navigation|
|11|sort        |StringGraphType          |The sort expression|

#### Example

```json
{
    products(
        storeId: "Electronics"
        userId: "d97ee2c7-e29d-440a-a43a-388eb5586087"
        cultureName: "en-Us"
        currencyCode: "USD"
  	    first: 10
  	    after: "10")
=======
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
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
}
```
=======
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
>>>>>>> Stashed changes
