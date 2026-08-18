# PickupLocationEdge ==~object~==

This type represents an edge in a paginated connection, linking to a single `PickupLocation` object. It contains both the object itself and a pagination cursor.

## Fields

| Field                                                  | Description                                                                                        |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `cursor` ==String!==                                   | A unique identifier used for pagination. It marks the position of this item within the connection. |
| `node` ==[PickupLocationType](PickupLocationType.md)== | The actual pickup location object at the end of the edge.                                          |
