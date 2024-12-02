# customerReviews ==~query~==  

This query retrieves customer reviews associated with a specific entity, such as a product or service, allowing filtering and sorting of results.  

## Arguments  

| Argument          | Description                                                                                   |  
|-------------------|-----------------------------------------------------------------------------------------------|  
| `after` ==String==       | A cursor for paginating results, pointing to the position after which to fetch data.        |  
| `first` ==Int==          | The maximum number of reviews to return.                                                  |  
| `keyword` ==String==      | A keyword to filter reviews by matching text.                                             |  
| `sort` ==String==         | A sorting parameter to order the reviews (e.g., by date or rating).                       |  
| `storeId` ==String!==     | The Id of the store associated with the reviews.                           |  
| `entityId` ==String!==    | The Id of the entity the reviews are linked to (e.g., product ID).          |  
| `entityType` ==String!==  | The type of entity the reviews are associated with (e.g., "Product").                     |  
| `filter` ==String==       | Additional filters to narrow down the reviews based on specific criteria.                 |  

## Possible Returns  

| Possible Return                                                    | Description                                                     |  
|--------------------------------------------------------------------|-----------------------------------------------------------------|  
| [`CustomerReviewConnection`](../Objects/CustomerReviewConnection.md) | A paginated list of customer reviews matching the query criteria. |  

## Examples  

=== "Query"  
    ```json linenums="1"  
    {  
      customerReviews(  
        after: "cursor123",  
        first: 10,  
        keyword: "great",  
        sort: "rating_desc",  
        storeId: "B2B-store",  
        entityId: "product-12345",  
        entityType: "Product",  
        filter: "rating:5"  
      ) {  
        totalCount  
        edges {  
          cursor  
          node {  
            id  
            rating  
            comment  
            author  
          }  
        }  
        pageInfo {  
          hasNextPage  
          hasPreviousPage  
          startCursor  
          endCursor  
        }  
      }  
    }  
    ```  

=== "Return"  
    ```json linenums="1"  
    {  
      "data": {  
        "customerReviews": {  
          "totalCount": 25,  
          "edges": [  
            {  
              "cursor": "cursor123",  
              "node": {  
                "id": "review1",  
                "rating": 5,  
                "comment": "Excellent product!",  
                "author": "John Doe"  
              }  
            }  
          ],  
          "pageInfo": {  
            "hasNextPage": true,  
            "hasPreviousPage": false,  
            "startCursor": "cursor123",  
            "endCursor": "cursor456"  
          }  
        }  
      }  
    }  
    ```  