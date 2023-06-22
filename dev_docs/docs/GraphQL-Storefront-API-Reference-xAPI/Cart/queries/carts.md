# Carts ==~query~==

This query allows you to retrieve information about shopping carts and wishlists.

## Arguments

| Argument                        | Description                                                                                     |
|---------------------------------|-------------------------------------------------------------------------------------------------|
| `after` {==String==}            | Specifies the starting point for fetching the next set of results.                              |
| `first` {==Int==}               | The maximum number of carts to retrieve.                                                        |
| `storeId` {==String==}          | The ID of the store to retrieve carts from.                                                     |
| `userId` {==String==}           | The ID of the user associated with the carts.                                                   |
| `currencyCode` {==String==}     | A standardized code of the currency of the carts.                                               |
| `cultureName` {==String==}      | The language to retrieve data in.                                                               |
| `cartName` {==String==}         | The name or the identifier of the cart.                                                         |
| `cartType` {==String==}         | The type of carts being queried, allowing differentiation between different cart variations.    |
| `filter` {==String==}           | A filter condition to narrow down the carts based on specific criteria.                         |
| `sort` {==String==}             | The sorting order for the retrieved carts.                                                      |

## Possible returns

| Possible return                                         	| Description                                                              	|
|---------------------------------------------------------	|------------------------------------------------------------------------	|
| [`CartConnection`](../objects/cart-connection.md)         |  Defines the properties and fields associated with a shopping cart.    	|

## Examples

```json linenums="1"
{
  carts(
    storeId: "Electronics"
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
