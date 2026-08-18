# CustomerReview ==~object~==  

This type represents a customer review, including details about the reviewer, the reviewed entity, and the review content.  

## Fields  

| Field                          | Description                                                                |  
|--------------------------------|----------------------------------------------------------------------------|  
| `id` ==String!==               | The unique identifier of the customer review.                              |  
| `createdDate` ==DateTime!==    | The date and time when the review was created.                             |  
| `modifiedDate` ==DateTime==    | The date and time when the review was last modified.                       |  
| `storeId` ==String!==          | The ID of the store where the review was submitted.                        |  
| `userId` ==String!==           | The ID of the user who submitted the review.                               |  
| `userName` ==String!==         | The name of the user who submitted the review.                             |  
| `entityId` ==String!==         | The ID of the entity being reviewed.                                       |  
| `entityType` ==String!==       | The type of the entity being reviewed (e.g., product, page).               |  
| `entityName` ==String!==       | The name of the entity being reviewed.                                     |  
| `title` ==String==             | The title of the review.                                                   |  
| `review` ==String!==           | The text content of the review.                                            |  
| `rating` ==Int!==              | The rating given in the review, typically on a predefined scale.           |  
| `reviewStatus` ==CustomerReviewStatus== | The status of the review (e.g., new, approved, or rejected).      |  