# createQuote ==~mutation~==

This mutation creates a new quote.

## Arguments

The `CreateQuoteCommandType!` represents the input required to create a new quote.

| Field                        | Description                                    |
| ---------------------------- | -----------------------------------------------|
| `storeId` ==String!==      | The Id of the store where the quote is created.|
| `userId` ==String!==       | The Id of the user requesting the quote.       |
| `currencyCode` ==String!== | The currency code for the quote.               |
| `cultureName` ==String!==  | The culture name for the quote.                |

## Possible returns

| Possible return                                          	| Description                                 	|
|---------------------------------------------------------	|---------------------------------------------	|
| [`QuoteType`](../objects/QuoteType.md)                   	|  Information about the created quote.        	|

## Example

<div class="grid" markdown>

```graphql title="Mutation"
mutation createQuote($command: CreateQuoteCommandType!) {
  createQuote(command: $command) {
    id
    number
    status
    storeId
    userId
    currencyCode
    cultureName
  }
}
```

```json title="Variables"
{
  "command": {
    "storeId": "B2B-store",
    "userId": "user-789",
    "currencyCode": "USD",
    "cultureName": "en-US"
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../approveQuoteRequest">← ApproveQuoteRequest mutation</a>
    <a href="../declineQuoteRequest">DeclineQuoteRequest mutation →</a>
</div>
