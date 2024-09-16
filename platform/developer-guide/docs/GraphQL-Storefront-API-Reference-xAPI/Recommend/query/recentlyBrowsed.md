# recentlyBrowsed ==~query~==

This query allows you to retrieve a list of products recently browsed by the user.

## Arguments

| Argument                       | Description                                                                                     |
|--------------------------------|-------------------------------------------------------------------------------------------------|
| `storeId` ==String!==          | The ID of the store to retrieve recently browsed products from.                                  |
| `cultureName` ==String==       | The language to retrieve data in.                                                               |
| `currencyCode` ==String==      | A standardized code for the specific currency.                                                  |
| `maxProducts` ==Int==          | The maximum number of recently browsed products to return.                                      |

## Possible return

| Possible return                                                   | Description                                                               |
|-------------------------------------------------------------------|---------------------------------------------------------------------------|
| [`GetRecentlyBrowsedResponseType`](../object/GetRecentlyBrowsedResponseType.md)  | Defines the properties and fields associated with the recently browsed products response. |

## Example

=== "Query"
    ```json linenums="1"
    {
      recentlyBrowsed(
        storeId: "Electronics"
        cultureName: "en-US"
        currencyCode: "USD"
        maxProducts: 5
      ) {
        products {
          id
          name
          code  
        }
      }
    }
    ```

=== "Return"
    ```json linenums="1"
    {
      "data": {
        "recentlyBrowsed": {
          "products": [
            {
              "id": "product-1",
              "name": "Laptop Pro",
              "code": "LP123"
            },
            {
              "id": "product-2",
              "name": "Headphones XYZ",
              "code": "HP456"
            }
          ]
        }
      }
    }
    ```