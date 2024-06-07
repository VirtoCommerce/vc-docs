# addQuoteAttachments ==~mutation~==

This mutation adds new attachments to a quote.

## Arguments

The `AddQuoteAttachmentsCommandType!` represents the input required to add attachments to a quote.

| Field                        | Description                                    |
| ---------------------------- | -----------------------------------------------|
| `quoteId` {==String!==}      | The Id of the quote to which attachments will be added.|
| `urls` {==[String]!==}       | A list of URLs representing the new attachments. |

## Possible returns

| Possible return                                          	| Description                                 	|
|---------------------------------------------------------	|---------------------------------------------	|
| [`QuoteType`](../objects/QuoteType.md)                   	|  Information about the updated quote.        	|