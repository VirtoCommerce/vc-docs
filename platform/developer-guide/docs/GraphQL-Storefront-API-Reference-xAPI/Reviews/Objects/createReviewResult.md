# CreateReviewResult ==~object~==  

This type represents the result of a review creation process, including the review's identifier, user details, and any validation errors encountered.  

## Fields  

| Field                                                     | Description                                                                 |
|-----------------------------------------------------------|-----------------------------------------------------------------------------|
| `id` ==String==                                           | The unique identifier of the created review.                                |
| `userName` ==String==                                     | The name of the user who submitted the review.                              |
| `validationErrors` [==[ReviewValidationErrorType]==](ReviewValidationErrorType.md) | A list of validation errors, if any, encountered during review creation. |  