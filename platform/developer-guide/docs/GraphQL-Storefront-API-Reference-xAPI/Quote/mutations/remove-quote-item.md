# removeQuoteItem ==~mutation~==

This mutation removes a product item from the quote request. 

## Arguments

The `RemoveQuoteItemCommandType!` represents a command for removing a product item from the quote request.

| Field                        | Description                                              |
| ---------------------------- | -------------------------------------------------------- |
| `quoteId` ==String!==      | The Id of the quote request to be updated.               |
| `lineItemId` ==String!==   | The Id of the specific line item to be modified.         |

## Possible returns

| Possible return                                          	| Description                    	|
|---------------------------------------------------------	|-------------------------------	|
| [`QuoteType`](../objects/QuoteType.md)                   	|  Information about the order.  	|


=== "Mutation"
    ```json linenums="1"
    mutation RemoveQuoteItem($command: RemoveQuoteItemCommandType!) {
      removeQuoteItem(command: $command) {
        id
        items
        {
          id
        }
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command": {
        "quoteId": "893f7cd7-75eb-4b16-9fbb-e1e3b9053f16",
        "lineItemId": "d8a7ecf3-c112-4778-8fb3-e3fcd01ac063"
      }
    }
    ```