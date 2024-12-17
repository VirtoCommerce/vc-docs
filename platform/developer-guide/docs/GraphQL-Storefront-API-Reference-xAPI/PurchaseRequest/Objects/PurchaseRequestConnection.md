# PurchaseRequestConnection ==~object~==  

This type represents a paginated list of purchase requests, providing information about the total count, pagination, and associated edges or items.  

## Fields  

| Field                  | Description                                                                 |  
|------------------------|-----------------------------------------------------------------------------|  
| `totalCount` ==Int==   | The total number of purchase requests in the connection.                   |  
| `pageInfo` [==PageInfo!==](../../Catalog/objects/PageInfo.md) | Information about the pagination state for the connection.              |  
| `edges` [==PurchaseRequestEdge==](PurchaseRequestEdge.md) | A list of edges containing purchase request nodes and their cursors.        |  
| `items` [==PurchaseRequestType==](PurchaseRequestType.md) | A list of purchase requests retrieved in the current page.                  |  