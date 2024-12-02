# PageDocumentConnection ==~object~==  

This type represents a paginated list of page documents.  

## Fields  

| Field                                                             | Description                                                                   |  
|-------------------------------------------------------------------|-------------------------------------------------------------------------------|  
| `totalCount` ==Int==                                              | The total number of page documents available.                                 |  
| `pageInfo` [==PageInfo!==](../../Catalog/objects/PageInfo.md)     | Metadata about the pagination, such as cursors and page boundaries.           |  
| `edges` [==[PageDocumentEdge]==](PageDocumentEdge.md)             | A list of edges containing the page documents and their cursor information.   |  
| `items` [==[PageDocumentType]==](PageDocumentType.md)             | A flat list of the page documents.                                            |  