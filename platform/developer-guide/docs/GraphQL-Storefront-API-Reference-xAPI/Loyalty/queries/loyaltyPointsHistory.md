# loyaltyPointsHistory ==~query~==

This query allows you to retrieve the history of loyalty point transactions for a specific user. The results include details about earned and redeemed points, with support for pagination, filtering, and sorting.

## Arguments

| Argument                    | Description                                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `after` ==String!==         | Returns only edges after the specified cursor (for pagination).                                                    |
| `first` ==Int!==            | The maximum number of edges to return. Works with `after` for paginated results, or from the beginning if not set. |
| `keyword` ==String!==       | A keyword to filter the history records.                                                                           |
| `sort` ==String!==          | The sorting expression to order the results.                                                                       |
| `userId` ==String!==        | The Id of the user whose loyalty history is requested.                                              |
| `operationType` ==String!== | Filters results by operation type (Earned or Redeemed).                                                   |

## Possible returns

| Possible return                                                                | Description                                                               |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| [LoyaltyOperationLogConnection](../objects/LoyaltyOperationLogConnection.md) | Defines the paginated list of loyalty operation log entries with details. |

## Example

=== "Query"

    ```json linenums="1"
    {
      loyaltyPointsHistory(
        userId: "9c6a2f1a-24e7-4b2c-bb5d-ef5e2ad7c111"
        first: 5
        sort: "createdDate:desc"
        operationType: "Earned"
    ) {
        edges {
        node {
            id
            operationType
            points
            balance
            createdDate
            orderId
        }
        }
        pageInfo {
        hasNextPage
        endCursor
        }
    }
    }
    ```

=== "Return"

    ```json linenums="1"
    {
    "data": {
        "loyaltyPointsHistory": {
        "edges": [
            {
            "node": {
                "id": "op-001",
                "operationType": "Earned",
                "points": 50,
                "balance": 250,
                "createdDate": "2025-09-10T12:45:00Z",
                "orderId": "ord-123"
            }
            },
            {
            "node": {
                "id": "op-002",
                "operationType": "Earned",
                "points": 30,
                "balance": 200,
                "createdDate": "2025-09-05T09:15:00Z",
                "orderId": "ord-122"
            }
            }
        ],
        "pageInfo": {
            "hasNextPage": true,
            "endCursor": ""
        }
        }
    }
    }
    ```

