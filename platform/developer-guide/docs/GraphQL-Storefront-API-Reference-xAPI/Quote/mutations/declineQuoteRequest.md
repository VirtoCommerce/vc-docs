# declineQuoteRequest ==~mutation~==

This mutation declines a quote request.

## Arguments

The `DeclineQuoteCommandType!` represents the input required to decline a quote request.

| Field                        | Description                                    |
| ---------------------------- | -----------------------------------------------|
| `quoteId` ==String!==         | The Id of the quote request to be declined.    |

## Possible returns

| Possible return                                          	| Description                                 	|
|---------------------------------------------------------	|---------------------------------------------	|
| [`QuoteType`](../objects/QuoteType.md)                   	|  Information about the declined quote.       	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation declineQuoteRequest($command: DeclineQuoteCommandType!) {
  declineQuoteRequest(command: $command)
}
```

```json title="Variables"
{
  "command": {
    "quoteId": "quote-12345"
  }
}
```

</div>