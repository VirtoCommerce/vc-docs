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