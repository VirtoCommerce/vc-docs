# CustomerReviewConnection ==~object~==  

This type represents a paginated list of customer reviews.  

## Fields  

| Field                                                      | Description                                                                  |  
|------------------------------------------------------------|------------------------------------------------------------------------------|  
| `totalCount` ==Int==                                       | The total number of customer reviews available.                              |  
| `pageInfo` [==PageInfo!==](../../Catalog/objects/PageInfo.md) | Metadata about the pagination, such as cursors and page boundaries.        |  
| `edges` [==[CustomerReviewEdge]==](CustomerReviewEdge.md)   | A list of edges containing the customer reviews and their cursor information.|  
| `items` [==[CustomerReview]==](CustomerReview.md)           | A flat list of the customer reviews.                                         |  