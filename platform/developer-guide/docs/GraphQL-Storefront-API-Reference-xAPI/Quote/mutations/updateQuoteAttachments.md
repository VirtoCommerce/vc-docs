# updateQuoteAttachments ==~mutation~==

This mutation updates the attachments associated with a quote.

## Arguments

The `UpdateQuoteAttachmentsCommandType!` represents the input required to update quote attachments.

| Field                        | Description                                    |
| ---------------------------- | -----------------------------------------------|
| `quoteId` ==String!==      | The Id of the quote to which attachments belong.|
| `urls` ==[String]!==       | A list of URLs representing the attachments.    |

## Possible returns

| Possible return                                          	| Description                                 	|
|---------------------------------------------------------	|---------------------------------------------	|
| [`QuoteType`](../objects/QuoteType.md)                   	|  Information about the updated quote.        	|