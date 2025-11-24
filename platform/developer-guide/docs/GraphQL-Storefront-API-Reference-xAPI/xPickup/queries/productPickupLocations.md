# productPickupLocations ==~query~==

This query allows you to retrieve pickup locations where a specific product is available. You can filter the results by keyword, sort order, and paginate through locations.

## Arguments

| Argument                  | Description                                                                            |
|---------------------------|----------------------------------------------------------------------------------------|
| `after` ==String==        | Returns results **after** the specified cursor.                                        |
| `first` ==Int==           | Specifies the maximum number of edges to return.                                       |
| `keyword` ==String==      | A keyword to filter pickup locations by name, description, or other searchable fields. |
| `sort` ==String==         | A field and direction to sort results by .                                             |
| `productId` ==String!==   | The ID of the product for which pickup locations are requested.                        |
| `storeId` ==String!==     | The ID of the store in which to search for available pickup locations.                 |
| `cultureName` ==String!== | The culture code used to retrieve localized data (e.g., `"en-US"`).                    |

## Possible return

| Possible return                                                                   | Description                                                                                  |
| --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| [`ProductPickupLocationConnection`](../objects/ProductPickupLocationConnection.md) | A paginated connection containing pickup locations where the specified product is available.|

## Examples

=== "Query"

    ```json linenums="1"
    {
      productPickupLocations(
        storeId: "B2B-store"
        cultureName: "en-US"
        productId: 
        keyword: "Center"
        first: 5
        after: 
        sort: 
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
        "productPickupLocations": {
        "totalCount": 2,
        "items": [
            {
              "id": 
              "name": "Central Warehouse Pickup",
              "description": "Main pickup location for high-stock items.",
              "contactEmail": "pickup@store.com",
              "contactPhone": 
              "workingHours":
              "geoLocation": 
              "availabilityType": 
              "availableQuantity": 14,
              "availabilityNote": "Available for same-day pickup",
              "address": {
                "id": 
                "line1": "123 Main St",
                "line2": "Suite A",
                "city": "Cityville",
                "countryName": "United States",
                "countryCode": "US",
                "regionId": "NY",
                "postalCode": 
                "phone": 
              }
            },
            {
              "id": 
              "name": "North Pickup Point",
              "description": "Regional pickup office with limited stock.",
              "contactEmail": 
              "contactPhone": 
              "workingHours":
              "geoLocation": 
              "availabilityType": 
              "availableQuantity": 3,
              "availabilityNote":
              "address": {
                "id": 
                "line1": "500 North Ave",
                "line2": "",
                "city": "Cityville",
                "countryName": "United States",
                "countryCode": "US",
                "regionId": "NY",
                "postalCode": 
                "phone": 
              }
            }
        ]
        }
      }
    }
    ```
