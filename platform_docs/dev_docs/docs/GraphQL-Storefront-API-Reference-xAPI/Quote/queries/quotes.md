# Quotes

This query allows getting a specified number of quotes from a particular user.

## Arguments

| Argument                    | Description                                                                                           |
|-----------------------------|-------------------------------------------------------------------------------------------------------|
| `after` {==String==}        | The cursor value to paginate through the results.                                                     |
| `first` {==Int==}           | The number of pages in a single query.                                                                |
| `keyword` {==String==}      | The keyword that will be used to filter the quotes.                                                   |
| `sort` {==String==}         | The sorting order of the returned quotes.                                                             |
| `storeId` {==String==}      | The Id of the store.                                                                                  |
| `userId` {==String==}       | The Id of the user.                                                                                   |
| `currencyCode` {==String==} | A standardized code of a specific currency.                                                           |
| `cultureName` {==String==}  | A language to retrieve data in.                                                                       |
| `filter` {==String==}       | The query result filter.                                                                              |

## Possible returns

| Possible return                                          	              | Description                                             |
|-----------------------------------------------------------------------	|-------------------------------------------------------	|
| [`QuoteConnection`](../objects/QuoteConnection.md)                      |  A list of quotes that match the specified criteria.   	|

## Example

=== "Query"

    ```json linenums="1"
    query {
      quotes(
        userId: "edec910a-122f-4391-b026-831771c3c947"
        storeId:"B2B-store",
        currencyCode:"USD",
        cultureName:"en-US",
        sort: "createdDate"
        first: 10
      ) {
        totalCount
        items {
          id
          number
          status
          totals {
            grandTotalInclTax {
              formattedAmount
            }
          }
        }
      }
    }
    ```

=== "Return"

    ```json linenums="1"
    {
      "data": {
        "quotes": {
          "totalCount": 10,
          "items": [
            {
              "id": "5e6f7g8h",
              "number": "Q789012",
              "status": "Approved",
              "totals": {
                "grandTotalInclTax": {
                  "formattedAmount": "$2,345.67"
                }
              }
            },
            {
              "id": "9i0j1k2l",
              "number": "Q345678",
              "status": "Pending",
              "totals": {
                "grandTotalInclTax": {
                  "formattedAmount": "$3,456.78"
                }
              }
            },
            {
              "id": "3m4n5o6p",
              "number": "Q901234",
              "status": "Declined",
              "totals": {
                "grandTotalInclTax": {
                  "formattedAmount": "$4,567.89"
                }
              }
            },
          ]
        }
      }
    }
    ```