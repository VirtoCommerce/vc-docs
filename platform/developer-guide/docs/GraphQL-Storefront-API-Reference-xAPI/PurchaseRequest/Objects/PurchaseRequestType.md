# PurchaseRequestType ==~object~==  

This type represents a purchase request, including its details and associated sources.  

## Fields  

| Field                             | Description                                                                 |  
|-----------------------------------|-----------------------------------------------------------------------------|  
| `id` ==String!==                  | A unique Id for the purchase request.                              |  
| `createdDate` ==DateTime!==       | The date and time when the purchase request was created.              |  
| `createdBy` ==String!==           | The user who created the purchase request.                                |  
| `modifiedDate` ==DateTime==       | The date and time when the purchase request was last modified.         |  
| `modifiedBy` ==String==           | The user who last modified the purchase request.                         |  
| `number` ==String!==              | A unique number assigned to the purchase request.                          |  
| `storeId` ==String!==             | The Id of the store where the purchase request was created.                |  
| `customerId` ==String!==          | The Id of the customer associated with the purchase request.             |  
| `quoteId` ==String==              | The Id of the quote associated with the purchase request, if available.    |  
| `sources` [==[PurchaseRequestSourceType!]!==](PurchaseRequestSourceType.md) | A list of sources associated with the purchase request. |  