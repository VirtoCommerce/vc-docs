# changeQuoteComment ==~mutation~==

This mutation changes the comment associated with a specific quote.

## Arguments

The `ChangeQuoteCommentCommandType!` represents a command for modifying quote comments.

| Field                        | Description                                              |
| ---------------------------- | -------------------------------------------------------- |
| `quoteId` ==String!==      | The Id of the quote to be modified.                      |
| `comment` ==String!==      | The new comment to be associated with the quote.         |

## Possible returns

| Possible return                                          	| Description                    	|
|---------------------------------------------------------	|-------------------------------	|
| [`QuoteType`](../objects/ChangeQuoteCommentCommandType.md)|  Information about the modified quote.  	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation changeQuoteComment($command: ChangeQuoteCommentCommandType!) {
  changeQuoteComment(command: $command)
}
```

```json title="Variables"
{
  "command": {
    "quoteId": "quote-12345",
    "comment": "Updated comment: pricing conditions adjusted after customer discussion."
  }
}
```

</div>