# CustomerOrderConnection ==~object~==

The `CustomerOrderConnection` represents a connection of customer orders.

## Fields

| Field                                                             | Description                                                                                               |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `totalCount` {==Int==}                                            | The total number of customer orders in the connection, regardless of pagination.                          |
| `pageInfo` [{==PageInfo!==}](../../Catalog/objects/PageInfo.md)   | Information about the current page and navigation in the connection.                                      |
| `edges` [{==[CustomerOrderEdge]==}](customer-order-edge.md)       | An array of edges representing the individual customer orders and their cursors in the connection.        |
| `items` [{==[CustomerOrderType]==}](customer-order-type.md)       | An array of customer orders retrieved for the current page in the connection.                             |

