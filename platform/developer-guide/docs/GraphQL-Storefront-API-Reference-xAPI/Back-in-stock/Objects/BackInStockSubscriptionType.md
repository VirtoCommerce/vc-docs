# BackInStockSubscriptionType ==~object~==  

This type represents a back-in-stock subscription, containing details about the subscribed product, store, and customer.  

## Fields  

| Field                     | Description                                                                  |  
|---------------------------|------------------------------------------------------------------------------|  
| `id` ==String!==           | The unique Id of the subscription.                                  |  
| `storeId` ==String!==      | The Id of the store where the subscription was created.             |  
| `productId` ==String!==    | The Id of the subscribed product.                                   |  
| `productCode` ==String==   | The SKU or code of the subscribed product.                                  |  
| `productName` ==String==   | The name of the subscribed product.                                         |  
| `userId` ==String!==       | The Id of the user who created the subscription.                    |  
| `memberId` ==String==      | The Id of the associated customer (if applicable).                  |  
| `isActive` ==Boolean!==    | Indicates whether the subscription is active.                               |  
