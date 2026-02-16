# changeQuoteItemQuantity ==~mutation~==

This mutation changes the items quantity in the quote request.

## Arguments

The `ChangeQuoteItemQuantityCommandType!` represents a command for adjusting item quantities in a quote request.

| Field                        | Description                                              |
| ---------------------------- | -------------------------------------------------------- |
| `quoteId` ==String!==      | The Id of the quote request to be updated.               |
| `lineItemId` ==String!==   | The Id of the specific line item to be modified.         |
| `quantity` ==Int!==        | The new quantity for the line item.                      |

## Possible returns

| Possible return                                          	| Description                    	|
|---------------------------------------------------------	|-------------------------------	|
| [`QuoteType`](../objects/QuoteType.md)                   	|  Information about the order.  	|



## Example

<div class="grid" markdown>

```json title="Mutation"
mutation ChangeQuoteItemQuantity($command: ChangeQuoteItemQuantityCommandType!) {
  changeQuoteItemQuantity(command: $command) {
    id
    items
    {
      id
      comment
      name
      sku
    }
  }
}
```

```json title="Variables"
{
  "command": {
    "quoteId": "893f7cd7-75eb-4b16-9fbb-e1e3b9053f16",
    "lineItemId": "c7d05308-1761-4d61-bcb7-d3d341c7feff",
    "quantity": 12
  }
}
```

</div>