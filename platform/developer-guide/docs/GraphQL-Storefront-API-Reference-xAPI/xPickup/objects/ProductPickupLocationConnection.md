# ProductPickupLocationConnection ==~object~==

This type defines the structure of the response returned when querying for product-specific pickup locations, including pagination details and the returned location records.

## Fields

| Field                                   | Description                                                                                                                                                       |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `totalCount` ==Int==                    | The total number of product pickup locations available, ignoring pagination. Useful for displaying results like “5 of 83”.                                        |
| `pageInfo` ==[PageInfo!](../../Catalog/objects/PageInfo.md)==                | Information that supports navigating through paginated product pickup location results.                                      |
| `edges` ==[[ProductPickupLocationEdge](ProductPickupLocationEdge.md)]== | A list of edges in the connection, each containing a product pickup location node and its associated cursor.                      |
| `items` ==[[ProductPickupLocation](ProductPickupLocation.md)]==     | A convenience list of product pickup location objects returned by the query. |
