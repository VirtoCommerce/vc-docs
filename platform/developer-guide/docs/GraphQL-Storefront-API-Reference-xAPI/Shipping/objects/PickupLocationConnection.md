# PickupLocationConnection ==~object~==

This type defines the structure of the paginated response returned by the `pickupLocations` query. It includes metadata for pagination and provides access to the list of pickup location entries.

## Fields

| Field                                  | Description                                                                                                                                                                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `totalCount` ==Int==                | The total number of pickup locations in the connection, ignoring pagination.<br>Useful for showing totals like "5 of 83". May return `null` in cases like infinite scrolling. |
| `pageInfo` ==[PageInfo](../../Catalog/objects/PageInfo.md)== | Metadata to assist in pagination,<br> such as whether there are more pages and what the cursor positions are.                                        |
| `edges` ==[PickupLocationEdge](PickupLocationEdge.md)==  | A list of edges, each containing a `node` (pickup location) <br> and a `cursor` used for pagination. Required when clients need to access cursor data.   |
| `items` ==[PickupLocationType](PickupLocationType.md)==      | A list of pickup location objects. Provided as a convenience <br> when edge metadata is not required. Use `edges` if cursor-based pagination is needed.|
