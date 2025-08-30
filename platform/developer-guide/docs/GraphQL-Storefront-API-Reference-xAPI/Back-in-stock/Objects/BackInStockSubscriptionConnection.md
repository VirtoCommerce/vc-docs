# BackInStockSubscriptionConnection ==~object~==  

This type represents a paginated list of back-in-stock subscriptions.  

## Fields  

| Field                     | Description                                                                                  |  
|---------------------------|----------------------------------------------------------------------------------------------|  
| `totalCount` ==Int==       | The total number of subscriptions available, ignoring pagination.<br> Returns `null` in cases where an exact count is unavailable (e.g., infinite scrolling). |  
| `pageInfo` [==PageInfo!==](../../Catalog/objects/PageInfo.md) | Metadata about pagination, including cursors and page boundaries.               |  
| `edges` [==[BackInStockSubscriptionEdge]==](BackInStockSubscriptionEdge.md) | A list of edges containing back-in-stock subscriptions and their cursor information. |  
| `items` [==[BackInStockSubscriptionType]==](BackInStockSubscriptionType.md) | A flat list of back-in-stock subscriptions.                                      |  
