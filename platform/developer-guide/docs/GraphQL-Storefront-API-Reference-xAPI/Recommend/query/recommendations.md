# Recommendations ==~query~==

This query allows you to retrieve product recommendations based on various criteria.

## Arguments

| Argument                       | Description                                                                                     |
|--------------------------------|-------------------------------------------------------------------------------------------------|
| `storeId` ==String!==          | The ID of the store to retrieve recommendations from.                                           |
| `userId`  ==String==           | The ID of the user.                                                                             |
| `cultureName` ==String==       | The language to retrieve data in.                                                               |
| `currencyCode` ==String!==     | A standardized code for the specific currency.                                                  |
| `productId` ==String==         | The ID of the product for which recommendations are requested.                                  |
| `model` ==String==             | The recommendation model to use (e.g., **related-products**).                                     |
| `fallbackProductsFilter` ==String== | A filter to apply when no recommendations are found.                                    |
| `maxRecommendations` ==String== | The maximum number of recommendations to return.                                                |

## Possible returns

| Possible return                                         	| Description                                                              	|
|---------------------------------------------------------	|------------------------------------------------------------------------	|
| [`GetRecommendationsResponseType`](../object/GetRecommendationsResponseType.md)  | Defines the properties and fields associated with the recommendations response. 	|

## Examples

=== "Query"
    ```json linenums="1"
    {
      recommendations(
        storeId: "Electronics"
        cultureName: "en-US"
        model: "related-products"
        productId: "Product-ID-12345"
        currencyCode: "USD"
        maxRecommendations: 5
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
        "recommendations": {
          "products": [
            {
              "id": "product-1",
              "name": "Smartphone XYZ",
              "code": "XYZ123"
            },
            {
              "id": "product-2",
              "name": "Smartphone ABC",
              "code": "ABC456"
            }
          ]
        }
      }
    }
    ```

