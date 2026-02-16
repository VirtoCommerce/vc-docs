# addQuoteAttachments ==~mutation~==

This mutation adds new attachments to a quote.

## Arguments

The `AddQuoteAttachmentsCommandType!` represents the input required to add attachments to a quote.

| Field                        | Description                                    |
| ---------------------------- | -----------------------------------------------|
| `quoteId` ==String!==      | The Id of the quote to which attachments will be added.|
| `urls` ==[String]!==       | A list of URLs representing the new attachments. |

## Possible returns

| Possible return                                          	| Description                                 	|
|---------------------------------------------------------	|---------------------------------------------	|
| [`QuoteType`](../objects/QuoteType.md)                   	|  Information about the updated quote.        	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation addQuoteAttachments($command: AddQuoteAttachmentsCommandType!) {
  addQuoteAttachments(command: $command)
}
```

```json title="Variables"
{
  "command": {
    "quoteId": "quote-12345",
    "urls": [
      "https://example.com/files/specification.pdf",
      "https://example.com/files/contract-draft.docx"
    ]
  }
}
```

</div>