# Wishlists ==~query~==

This query allows you to retrieve information about wishlists.

## Arguments

| Argument                       | Description                                                                |
|--------------------------------|----------------------------------------------------------------------------|
| `after` {==String==}           | The starting point for fetching the next set of results.                   |
| `first` {==Int==}              | The maximum number of carts to retrieve.                                   |
| `storeId` {==String!==}        | The ID of the store.                                                       |
| `userId`  {==String==}         | The ID of the user to retrieve pages from.                                 |
| `currencyCode` {==String==}    | A standardized code of a specific currency.                                |
| `cultureName` {==String==}     | The language to retrieve data in.                                          |
| `scope` {==String==}           | The wishlist accessibility: `Private` or `Organization`                    |
| `sort` {==String==}            | The sorting order of the returned wishlists.                               |

## Possible returns

| Possible return                                         	| Description                                             |
|---------------------------------------------------------	|--------------------------------------------------------	|
| [`WishlistConnection`](../objects/wishlist-connection.md) |  The properties and fields associated with lists.    	  |

## Examples

=== "Query"
    ```json linenums="1"
    {
    wishlists(
      after: "0", 
      first: "50", 
      userId: "3212395e-46cc-49cc-8d67-f06029b2be28") {
        totalCount
        items {
          id
          name
          items {
            id
            productId
            name
          }
        }
      }
    }      
    ```

=== "Return"
    ```json linenums="1"
    {
      "data": {
        "wishlists": {
          "totalCount": 1,
          "items": [
            {
              "id": "8b621092-f279-42a7-829d-ef4b7992c8a4",
              "name": "Wishlist1",
              "items": []
            }
          ]
        }
      }
    }  
    ```
