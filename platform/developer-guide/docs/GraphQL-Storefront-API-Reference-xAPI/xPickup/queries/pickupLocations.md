# pickupLocations ==~query~==

This query allows you to retrieve pickup locations available in a specific store, with optional pagination, keyword filtering, and sorting.

## Arguments

| Argument              | Description                                                                             |
|-----------------------|-----------------------------------------------------------------------------------------|
| `after` ==String==    | Returns results **after** the specified cursor. Useful for forward pagination.          |
| `first` ==Int==       | Specifies the maximum number of edges to return.                                        |
| `keyword` ==String==  | A text keyword to filter pickup locations by name, address, or other searchable fields. |
| `sort` ==String==     | A field and direction to sort results by.                                               |
| `storeId` ==String!== | The ID of the store for which to retrieve pickup locations.                             |

## Possible return

| Possible return                                                     | Description                                                                        |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [`PickupLocationConnection`](../objects/pickupLocationConnection.md) | Defines the structure for paginated pickup locations, including edges and cursors. |

## Examples

=== "Query"

    ```json linenums="1"
    {
    pickupLocations(
        storeId: "B2B-store"
        first: 5
        keyword: "Downtown"
        sort: 
    ) {
        edges {
        cursor
        node {
            id
            name
            address
            geoPoint {
            latitude
            longitude
            }
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
        "pickupLocations": {
        "edges": [
            {
            "cursor": 
            "node": {
                "id": 
                "name": "Downtown Pickup Point",
                "address": "123 Main Street, Cityville",
                "geoPoint": {
                "latitude":
                "longitude":
                }
            }
            },
            {
            "cursor": 
            "node": {
                "id": 
                "name": "Downtown South",
                "address": "500 South St, Cityville",
                "geoPoint": {
                "latitude": 
                "longitude": 
                }
            }
            }
        ],
        "pageInfo": {
            "hasNextPage": true,
            "endCursor":
        }
        }
    }
    }
    ```