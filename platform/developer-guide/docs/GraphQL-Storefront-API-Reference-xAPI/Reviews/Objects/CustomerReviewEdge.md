# CustomerReviewEdge ==~object~==  

This type represents an edge in a paginated list of customer reviews, containing a review and its cursor for pagination.  

## Fields  

| Field               | Description                                                       |  
|---------------------|-------------------------------------------------------------------|  
| `cursor` ==String!==| The cursor for this edge, used for pagination.                   |  
| `node` [==CustomerReview==](CustomerReview.md) | The customer review associated with this edge.                    |  