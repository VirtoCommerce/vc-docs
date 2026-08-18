# PickupLocationConnection ==~object~==

This type defines the structure of the response returned when querying for pickup locations, including pagination details and the list of returned location records.

## Fields

| Field                            | Description                                                                                                                                                           |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `totalCount` ==Int==             | The total number of pickup locations available, ignoring pagination. Useful for showing results like “5 of 83”.                                                       |
| `pageInfo` ==[PageInfo](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/PageInfo)!==         | Information used for navigating through paginated results, such as whether more pages are available.                             |
| `edges` ==[[PickupLocationEdge](pickupLocationEdge.md)]== | A list of edges in the connection, each containing a pickup location node and its associated cursor.                                         |
| `items` ==[[PickupLocationType](pickupLocationType.md)]== | A convenience list of pickup location objects returned by the query. It can be used instead of `edges` when cursor information is not needed.|
