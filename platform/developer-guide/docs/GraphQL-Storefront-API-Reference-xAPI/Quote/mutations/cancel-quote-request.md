# cancelQuoteRequest ==~mutation~==

This mutation cancels a specific quote request.

## Arguments

The `CancelQuoteCommandType!` is used for a command to cancel a quote.

|Field|	Description|
|-----|------------|
|`quoteId` ==String!==|	The Id of the quote to be cancelled.|
|`comment` ==String!==|	A comment or reason for cancelling the quote.|


## Possible returns

| Possible return                                          	| Description                     |
|---------------------------------------------------------	|---------------------------------|
| [`QuoteType`](../objects/QuoteType.md)                   	| Information about the order.  	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation cancelQuoteRequest($command: CancelQuoteCommandType!) {
  cancelQuoteRequest(command: $command)
}
```

```json title="Variables"
{
  "command": {
    "quoteId": "quote-12345",
    "comment": "The customer decided to postpone the purchase."
  }
}
```

</div>