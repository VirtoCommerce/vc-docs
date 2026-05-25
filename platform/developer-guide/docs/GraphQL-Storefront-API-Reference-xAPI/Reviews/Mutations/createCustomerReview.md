# createCustomerReview ==~mutation~==  

This mutation creates a new customer review for a specific entity, such as a product or service.  

## Arguments  

The `CreateCustomerReviewCommandType` represents the input data required to create a new customer review.  

| Field                    | Description                                                            |
|--------------------------|------------------------------------------------------------------------|
| `storeId` ==String!==    | The Id of the store where the review is being created.                 |
| `userId` ==String!==     | The Id of the user submitting the review.                              |
| `userName` ==String!==   | The name of the user submitting the review.                            |
| `entityId` ==String!==   | The Id of the entity being reviewed.                                   |
| `entityType` ==String!== | The type of the entity being reviewed.                                 |
| `entityName` ==String!== | The name of the entity being reviewed.                                 |
| `title` ==String!==      | The title of the review, summarizing the user's feedback.              |
| `review` ==String!==     | The main content of the review, describing the user's experience.      |
| `rating` ==Int!==        | The numerical rating given by the user, typically ranging from 1 to 5. |

## Possible Returns  

| Possible Return                                   | Description                                                                 |
|---------------------------------------------------|-----------------------------------------------------------------------------|
| [`CustomerReview`](../Objects/CustomerReview.md)  | The newly created customer review, including all its details.               |  

## Example

<div class="grid" markdown>

```json title="Mutation"
mutation($command: CreateCustomerReviewCommandType!) {  
  createCustomerReview(command: $command) {  
    id  
    userName  
    entityName  
    review  
    rating  
    createdDate  
    reviewStatus  
  }  
}  
```

```json title="Variables"
{  
  "command": {  
    "storeId": "B2B-store",  
    "userId": "c50e5237-8a4c-41fe-b878-8e5a72390a08",  
    "userName": "JohnDoe",  
    "entityId": "24caa0d5a05145f3a3433a2930fbfb0f",  
    "entityType": "Product",  
    "entityName": "Television",  
    "title": "Great Product",  
    "review": "The TV quality is excellent and meets my expectations.",  
    "rating": 5  
  }  
}  
```

</div>