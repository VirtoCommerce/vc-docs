# Carts ==~query~==

This query allows you to retrieve information about shopping carts and wishlists.

## Arguments

| Argument                        | Description                                                                                     |
|---------------------------------|-------------------------------------------------------------------------------------------------|
| `after` ==String==              | The starting point for fetching the next set of results.                              |
| `first` ==Int==                 | The maximum number of carts to retrieve.                                                        |
| `storeId` ==String==            | The ID of the store to retrieve carts from.                                                     |
| `userId` ==String==             | The ID of the user associated with the carts.                                                   |
| `currencyCode` ==String==       | A standardized code of the currency of the carts.                                               |
| `cultureName` ==String==        | The language to retrieve data in.                                                               |
| `cartName` ==String==           | The name or the identifier of the cart.                                                         |
| `cartType` ==String==           | The type of carts being queried, allowing differentiation between different cart variations.    |
| `filter` ==String==             | A filter condition to narrow down the carts based on specific criteria.                         |
| `sort` ==String==               | The sorting order for the retrieved carts.                                                      |

## Possible returns

| Possible return                                         	| Description                                                             |
|---------------------------------------------------------	|------------------------------------------------------------------------	|
| [`CartConnection`](../objects/cart-connection.md)         |  Defines the properties and fields associated with a shopping cart.    	|

## Examples

=== "Query"

    ```json linenums="1"  
    {
      carts(
        storeId: "B2B-Store"
        userId: "d97ee2c7-e29d-440a-a43a-388eb5586087"
        cultureName: "en-Us"
        currencyCode: "USD"
        cartType: "cart"
        first: 5
        after: "0"
      ) {
        items {
          id
          name
          hasPhysicalProducts
          status
          storeId
          isAnonymous
        }
        pageInfo {
          startCursor
          endCursor
          hasNextPage
          hasPreviousPage
        }
      }
    }
    ```


=== "Return"

    ```json linenums="1"  
    {
      "data": {
        "carts": {
          "items": [
            {
              "id": "cart_id_1",
              "name": "Shopping Cart 1",
              "hasPhysicalProducts": true,
              "status": "Active",
              "storeId": "B2B-Store",
              "isAnonymous": false
            },
            {
              "id": "cart_id_2",
              "name": "Shopping Cart 2",
              "hasPhysicalProducts": false,
              "status": "Active",
              "storeId": "B2B-Store",
              "isAnonymous": true
            }
          ],
          "pageInfo": {
            "startCursor": "0",
            "endCursor": "4",
            "hasNextPage": true,
            "hasPreviousPage": false
          }
        }
      }
    }
    ```
