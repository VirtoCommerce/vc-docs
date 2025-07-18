# pickupLocations ==~query~==

This query is used to retrieve a paginated list of pickup locations available in a given store, with support for keyword filtering and sorting.

## Arguments

| Argument             | Description                                                                            |
| -------------------- | -------------------------------------------------------------------------------------- |
| `after` ==String==   | Returns results after the specified cursor, used for pagination.                       |
| `first` ==Int==      | Limits the number of results returned.  |
| `keyword` ==String== | A text keyword to filter pickup locations by name or address.                          |
| `sort` ==String==    | Defines the sort order of the results (e.g., by name or proximity).                    |
| `storeId` ==String== | The ID of the store to which the pickup locations belong.                              |

## Possible returns

| Possible return                                                      | Description                                                   |
| -------------------------------------------------------------------- | ------------------------------------------------------------- |
| [`PickupLocationConnection`](../objects/PickupLocationConnection.md) | A paginated list of pickup locations with metadata and edges. |

## Examples

=== "Query"

    ```json linenums="1"
    {
      pickupLocations(storeId: "B2B-store", after: "0", first: 3, keyword: "") {
        totalCount
        items {
          id
          isActive
          name
          description
          contactEmail
          contactPhone
          workingHours
          geoLocation
          address {
            id
            key
            name
            city
            countryCode
            countryName
            postalCode
            line1
            line2
            regionId
            regionName
            phone
            email
            outerId
            description
          }
        }
      }
    }
    ```

=== "Return"

    ```json linenums="1"
    {
      "data": {
        "pickupLocations": {
        "totalCount": 8,
        "items": [
            {
              "id": "20c64b73-ef3c-4cfd-b38d-4f9e5eced8a0",
              "isActive": true,
              "name": "Westfield World Trade Center",
              "description": null,
              "contactEmail": "pickup1@example.com",
              "contactPhone": "+10000000001",
              "workingHours": "* **Mon - Sun**: 9 - 18",
              "geoLocation": "40.711660,-74.011100",
              "address": {
                "id": "20c64b73-ef3c-4cfd-b38d-4f9e5eced8a0",
                "key": null,
                "name": "Westfield World Trade Center",
                "city": "New York",
                "countryCode": "USA",
                "countryName": "United States of America",
                "postalCode": "10001",
                "line1": "185 Greenwich St",
                "line2": "",
                "regionId": "NY",
                "regionName": "New York",
                "phone": null,
                "email": null,
                "outerId": null,
                "description": null
              }
            },
            {
              "id": "119bf02b-7ce4-4890-94cd-4e5c428358fa",
              "isActive": true,
              "name": "The Shops at Columbus Circle",
              "description": "Shopping mall",
              "contactEmail": "pickup2@example.com",
              "contactPhone": "+10000000002",
              "workingHours": "* **Mon - Sun**: 9 - 18",
              "geoLocation": "40.768044,-73.982125",
              "address": {
                "id": "119bf02b-7ce4-4890-94cd-4e5c428358fa",
                "key": null,
                "name": "The Shops at Columbus Circle",
                "city": "New York",
                "countryCode": "USA",
                "countryName": "United States",
                "postalCode": "10002",
                "line1": "10 Columbus Cir",
                "line2": null,
                "regionId": null,
                "regionName": null,
                "phone": null,
                "email": null,
                "outerId": null,
                "description": null
              }
            },
            {
              "id": "019c5065-b2b4-4183-b917-749a3fcac27f",
              "isActive": true,
              "name": "Upper East Side",
              "description": null,
              "contactEmail": "pickup96@example.com",
              "contactPhone": "+10000000096",
              "workingHours": null,
              "geoLocation": "40.7762,-73.9570",
              "address": {
                "id": "019c5065-b2b4-4183-b917-749a3fcac27f",
                "key": null,
                "name": "Upper East Side",
                "city": "New York",
                "countryCode": "USA",
                "countryName": "United States of America",
                "postalCode": "123",
                "line1": "E 79th St & 5th Ave",
                "line2": null,
                "regionId": "NY",
                "regionName": "New York",
                "phone": null,
                "email": null,
                "outerId": null,
                "description": null
              }
            }
          ]
        }
      }
    }
    ```
