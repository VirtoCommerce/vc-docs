# submitQuoteRequest ==~mutation~==

This mutation confirms and submits quotes request.

## Arguments

The `SubmitQuoteCommandType!` represents .

| Field                        | Description                                |
| ---------------------------- | -------------------------------------------|
| `quoteId` ==String!==      | The Id of the quote request to be updated. |
| `comment` ==String!==      | A comment associated with the submission.  |

## Possible returns

| Possible return                                          	| Description                    	|
|---------------------------------------------------------	|-------------------------------	|
| [`QuoteType`](../objects/QuoteType.md)                   	|  Information about the order.  	|

=== "Mutation"
    ```json linenums="1"
    mutation SubmitQuoteRequest($command: SubmitQuoteCommandType!) {
      submitQuoteRequest(command: $command) {
        id
        status
        coupon
        comment
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command": {
        "quoteId": "80d92257-5286-4fe2-933c-e1280d16677f",
        "comment": "this is a comment"
      }
    }
    ```
 
