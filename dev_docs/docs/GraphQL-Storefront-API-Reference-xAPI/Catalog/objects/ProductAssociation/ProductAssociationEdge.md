# ProductAssociationEdge ==~object~==

The `ProductAssociationEdge` represents an edge in a connection between a vendor and associated products.

## Fields

| Field                         	| Description           	|
|-------------------------------	|-------------------------------------------------------------------------------------------------------------------------	|
| `cursor` {==String!==}          	| A string representing a cursor that can be used for pagination purposes.<br>It does not denote the count of objects in the connection, but rather provides a reference point<br>for retrieving the next set of results or navigating through the associated products.<br>The cursor allows clients to fetch specific subsets of objects in a connection without having to<br>retrieve all items at once. 	|
| `node` [{==ProductAssociation==}](ProductAssociation.md) 	| Serves as a node in the connection graph, connecting the vendor to the associated product.           	|

