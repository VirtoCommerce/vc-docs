# PurchaseRequestEdge ==~object~==  

This type represents an edge in a paginated list of purchase requests, containing a node and its cursor.  

## Fields  

| Field                | Description                                                                           |  
|----------------------|---------------------------------------------------------------------------------------|  
| `cursor` ==String!== | A unique Id for the current position in the pagination.                      |  
| `node` [==PurchaseRequestType==](PurchaseRequestType.md) | The purchase request associated with this edge.                              |  