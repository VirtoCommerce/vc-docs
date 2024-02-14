# Wishlist ==~query~==

This query allows you to retrieve information about a product list. 

## Arguments

| Argument                     | Description                                                             |
|------------------------------|-------------------------------------------------------------------------|
| `listId` ==String!==         | The Id of the product list.                                             |
| `cultureName` ==String==     | The language to retrieve data in.                                       |

## Possible returns

| Possible return                                         	| Description                                               	|
|---------------------------------------------------------	|---------------------------------------------------------	  |
| [`WishlistType`](../objects/wishlist-type.md)             | Defines the properties and fields associated with the list.	|

## Examples

=== "Query"
    ```json linenums="1"
    {
      wishlist(
        listId: "4c9fac2c-cdbe-410d-be85-8e69b76c50e2",
        ) {
        id
        name
        storeId
        customerId
        customerName
        currency {
          code
        }
        itemsCount
        items {
          id
          productId
          name
        }
      }
    }
    ```

=== "Return"
    ```json linenums="1"
    {
      "data": {
        "wishlist": {
          "id": "4c9fac2c-cdbe-410d-be85-8e69b76c50e2",
          "name": "Whishlist1",
          "storeId": "B2B-store",
          "customerId": "22e6fc31-23c7-42fa-993a-8d4fbbe27ac6",
          "customerName": "Customer",
          "currency": {
            "code": "USD"
          },
          "itemsCount": 0,
          "items": []
        }
      }
    }
    ```
