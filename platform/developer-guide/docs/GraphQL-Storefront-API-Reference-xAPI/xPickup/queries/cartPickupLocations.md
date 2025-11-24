# cartPickupLocations ==~query~==

This query allows you to retrieve pickup locations where the items in a specific cart can be picked up. You can filter results by keyword, sort order, facets, and additional filters, as well as paginate through the available locations.

## Arguments

| Argument                  | Description                                                                                                    |
|---------------------------|----------------------------------------------------------------------------------------------------------------|
| `after` ==String==        | Returns results **after** the specified cursor. Useful for forward pagination.                                 |
| `first` ==Int==           | Specifies the maximum number of edges to return.  |
| `keyword` ==String==      | A keyword to filter pickup locations by name, description, or other searchable attributes.                     |
| `sort` ==String==         | A field and direction to sort results by .                                                                     |
| `cartId` ==String!==      | The ID of the cart for which to retrieve pickup locations.                                                     |
| `storeId` ==String!==     | The ID of the store in which to search for cart pickup locations.                                              |
| `cultureName` ==String!== | The culture code used to retrieve localized data (e.g., `"en-US"`).                                            |
| `facet` ==String==        | Defines facets to calculate statistical counts for faceted navigation .                                        |
| `filter` ==String==       | Applies an additional filter to the query results .                                                            |

## Possible return

| Possible return                                                             | Description                                                                                       |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [`CartPickupLocationConnection`](../objects/CartPickupLocationConnection.md) | A paginated connection containing pickup locations available for the items in the specified cart. |

## Examples

=== "Query"

    ```json linenums="1"
    {
      cartPickupLocations(
        storeId: "B2B-store"
        cultureName: "en-US"
        cartId: 
        keyword: "Center"
        first: 5
        after: null
        sort: "name:asc"
        facet: "availabilityType"
        filter: "availabilityType:InStock"
      ) {
        totalCount
        items {
          id
          name
          description
          contactEmail
          contactPhone
          workingHours
          geoLocation
          availabilityType
          availableQuantity
          availabilityNote
          address {
            id
            line1
            line2
            city
            countryName
            countryCode
            regionId
            postalCode
            phone
          }
        }
      }
    }
    ```

=== "Return"

    ```json linenums="1"
    {
      "data": {
        "cartPickupLocations": {
        "totalCount": 2,
        "items": [
          {
            "id": 
            "name": "Central Pickup Hub",
            "description": "Main pickup location for cart orders.",
            "contactEmail": "pickup@store.com",
            "contactPhone": "+1-555-0300",
            "workingHours": "Mon–Fri 9:00–18:00",
            "geoLocation": "40.7128,-74.0060",
            "availabilityType": "InStock",
            "availableQuantity": 12,
            "availabilityNote": "All cart items available",
            "address": {
                "id": 
                "line1": "200 Market St",
                "line2": "",
                "city": "Cityville",
                "countryName": "United States",
                "countryCode": "US",
                "regionId": "NY",
                "postalCode": "10002",
                "phone": "+1-555-0300"
            }
          },
          {
            "id": 
            "name": "East Side Pickup Point",
            "description": "Pickup office with limited availability for some cart items.",
            "contactEmail": "east@store.com",
            "contactPhone": "+1-555-0400",
            "workingHours": "Mon–Sat 10:00–17:00",
            "geoLocation": "40.7210,-73.9500",
            "availabilityType": "Limited",
            "availableQuantity": 3,
            "availabilityNote": "Some items may require transfer",
            "address": {
                "id": 
                "line1": "900 East St",
                "line2": "Building B",
                "city": "Cityville",
                "countryName": "United States",
                "countryCode": "US",
                "regionId": "NY",
                "postalCode": "10009",
                "phone": "+1-555-0400"
            }
          }
        ]
        }
      }
    }
    ```