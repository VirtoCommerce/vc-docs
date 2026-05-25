# PageDocumentEdge ==~object~==  

This type represents an edge in a paginated list of page documents, containing a node and its cursor.  

## Fields  

| Field             | Description                                               |  
|-------------------|-----------------------------------------------------------|  
| `cursor` ==String!==          | A unique identifier for the current position in the pagination. |  
| `node` [==PageDocumentType==](PageDocumentType.md)   | The page document associated with this edge.                   |  