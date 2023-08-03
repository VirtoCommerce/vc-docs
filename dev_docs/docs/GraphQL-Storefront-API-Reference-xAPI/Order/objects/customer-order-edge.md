# CustomerOrderEdge ==~object~==

The `CustomerOrderEdge` represents an edge in a connection of customer orders.

## Fields

| Field                                                     | Description                                                              |
|-----------------------------------------------------------|--------------------------------------------------------------------------|
| `cursor` {==String!==}                                    | The Id representing the current node in the list.                        |
| `node` [{==CustomerOrderType==}](customer-order-type.md)  | The `CustomerOrderType` node, which represents a single customer order.  |