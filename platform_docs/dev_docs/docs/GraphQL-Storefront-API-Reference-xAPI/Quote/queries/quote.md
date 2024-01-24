
# Quote ==~query~==

This query is used to get a quote by its Id.​

## Arguments

| Argument                  | Description                     |
|---------------------------|---------------------------------|
| `id` {==String==}         | The Id of the query.            |
| `storeId` {==String==}    | The Id of the store.            |
| `userId` {==String==}     | The Id of the user.             |
| `currency code` {==String==}     | The code of the currency related to the query.|
| `cultureName` {==String==}| A language to retrieve data in. |

## Possible returns

| Possible return                                         | Description                                   |
|---------------------------------------------------------|----------------------------------------------	|
| [`QuoteType`](../objects/QuoteType.md)                  | The structured data for quote information.   	|

## Examples

=== "Query"

    ```json linenums="1"
    query {
      quote(id: "70e6807d-bd42-4c78-bc0d-bb2f3ff7ae65") {
        id
        number
        status
        totals {
          grandTotalInclTax {
            formattedAmount
          }
        }
        items {
          name
          salePrice {
            formattedAmount
          }
          selectedTierPrice {
            quantity
            price {
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
        "quote": {
          "id": "70e6807d-bd42-4c78-bc0d-bb2f3ff7ae65",
          "number": "Q12345",
          "status": "Approved",
          "totals": {
            "grandTotalInclTax": {
              "formattedAmount": "$1,234.56"
            }
          },
          "items": [
            {
              "name": "Product A",
              "salePrice": {
                "formattedAmount": "$99.99"
              },
              "selectedTierPrice": {
                "quantity": 1,
                "price": {
                  "formattedAmount": "$99.99"
                }
              }
            },
            {
              "name": "Product B",
              "salePrice": {
                "formattedAmount": "$49.99"
              },
              "selectedTierPrice": {
                "quantity": 5,
                "price": {
                  "formattedAmount": "$44.99"
                }
              }
            }
          ]
        }
      }
    }
    ```