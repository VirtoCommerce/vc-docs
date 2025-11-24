# ProductPickupLocationEdge ==~object~==

This type represents an edge within a product pickup location connection. Each edge contains a product pickup location node and a cursor used for paginating through results.

## Fields

| Field                            | Description                                                                         |
| -------------------------------- | ----------------------------------------------------------------------------------- |
| `cursor` ==String!==             | A pagination cursor that indicates the position of this edge within the result set. |
| `node` ==[ProductPickupLocation](ProductPickupLocation.md)== | The product pickup location item associated with this edge. |