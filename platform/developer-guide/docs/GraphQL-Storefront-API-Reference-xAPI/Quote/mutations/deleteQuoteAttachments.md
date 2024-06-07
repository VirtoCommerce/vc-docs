# deleteQuoteAttachments ==~mutation~==

This mutation deletes attachments from a quote.

## Arguments

The `DeleteQuoteAttachmentsCommandType!` represents the input required to delete attachments from a quote.

| Field                        | Description                                    |
| ---------------------------- | -----------------------------------------------|
| `quoteId` ==String!==      | The Id of the quote from which attachments will be deleted.|
| `urls` ==[String]!==       | A list of URLs representing the attachments to be deleted. |

## Possible returns

| Possible return                                          	| Description                                 	|
|---------------------------------------------------------	|---------------------------------------------	|
| [`QuoteType`](../objects/QuoteType.md)                   	|  Information about the updated quote.        	|