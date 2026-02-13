# createReview ==~mutation~==  

This mutation creates a new review for a specific entity, such as a product or service.  

## Arguments  

The `CreateReviewCommandType` represents the input data required to create a new review.  

| Field              | Description                                                                                     |
|--------------------|-------------------------------------------------------------------------------------------------|
| `storeId` ==String!== | The unique identifier of the store where the review is being created.                         |
| `entityId` ==String!== | The unique identifier of the entity (e.g., product or service) being reviewed.                |
| `entityType` ==String!== | The type of the entity being reviewed (e.g., "Product", "Service").                         |
| `review` ==String!==   | The main content of the review, describing the user's experience.                            |
| `rating` ==Int!==      | The numerical rating given by the user, typically ranging from 1 to 5.                       |  

## Possible Returns  

| Possible Return                                        | Description                                                                 |
|--------------------------------------------------------|-----------------------------------------------------------------------------|
| [`CreateReviewResult`](../Objects/createReviewResult.md) | The result of the review creation, including its status and any additional data. |  

## Example

<div class="grid" markdown>

```json title="Mutation"
mutation($command: CreateReviewCommandType!) {  
  createReview(command: $command) {  
    success  
    message  
    reviewId  
  }  
}  
```

```json title="Variables"
{  
  "command": {  
    "storeId": "B2B-store",  
    "entityId": "24caa0d5a05145f3a3433a2930fbfb0f",  
    "entityType": "Product",  
    "review": "Excellent quality, highly recommended!",  
    "rating": 5  
  }  
}  
```

</div>