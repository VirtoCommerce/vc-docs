# Products

This connection allows you to search for products.

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