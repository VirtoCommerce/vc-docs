# ProductEdge ==~object~==

The `ProductEdge` represents a connection between a product and its associated cursor.  

## Fields

| Field                                          | Description                                                                                                                                                   	|
|----------------------------------------------- |---------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| `cursor` {==String!==}                         | The cursor associated with the product node. The cursor is a unique identifier<br>that can be used for efficient pagination and traversal of the product list.	|
| `node` [{==Product==}](../ProductType.md)      | The product associated with the edge.                                                                                                                            |

