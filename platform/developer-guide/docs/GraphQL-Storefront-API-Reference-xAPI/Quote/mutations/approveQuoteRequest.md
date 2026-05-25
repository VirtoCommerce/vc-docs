# approveQuoteRequest ==~mutation~==

This mutation approves a quote request.

## Arguments

The `ApproveQuoteCommandType!` represents the input required to approve a quote request.

| Field                        | Description                                    |
| ---------------------------- | -----------------------------------------------|
| `quoteId` ==String!==      | The Id of the quote request to be approved.    |

## Possible returns

| Possible return                                          	| Description                                 	|
|---------------------------------------------------------	|---------------------------------------------	|
| [`ApproveQuoteResultType`](../objects/ApproveQuoteResultType.md) |  Information about the approval result.      	|

## Example

<div class="grid" markdown>

```json title="Mutation"
mutation approveQuoteRequest($command: ApproveQuoteCommandType!) {
  approveQuoteRequest(command: $command)
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