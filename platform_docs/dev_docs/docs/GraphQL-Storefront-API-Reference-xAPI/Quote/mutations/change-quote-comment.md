# changeQuoteComment ==~mutation~==

This mutation changes the comment associated with a specific quote.

## Arguments

The `ChangeQuoteCommentCommandType!` represents a command for modifying quote comments.

| Field                        | Description                                              |
| ---------------------------- | -------------------------------------------------------- |
| `quoteId` {==String!==}      | The Id of the quote to be modified.                      |
| `comment` {==String!==}      | The new comment to be associated with the quote.         |

## Possible returns

| Possible return                                          	| Description                    	|
|---------------------------------------------------------	|-------------------------------	|
| [`QuoteType`](../objects/ChangeQuoteCommentCommandType.md)|  Information about the modified quote.  	|


=== "Mutation"
    ```json linenums="1"
    mutation changeComment ($command: InputChangeCommentType) {
        changeComment (command: $command) {
          id
          name
          comment
        }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command": {
        "cartId": "59d747aa-8ebf-4679-9d3e-eca3b2973cef",
        "storeId": "Electronics",
        "cartName": "default",
        "userId": "764f81d2-bd18-413d-8cce-e1db8bce0a93",
        "cartType": "null",
        "currencyCode": "USD",
        "cultureName":"en-US",
        "comment": "TEST COMMENT 1234 154"
      }
    }
    ```
