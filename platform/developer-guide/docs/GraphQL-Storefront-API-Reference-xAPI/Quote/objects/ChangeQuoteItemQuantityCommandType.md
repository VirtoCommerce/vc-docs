# ChangeQuoteItemQuantityCommandType ==~object~==

The `ChangeQuoteItemQuantityCommandType` is used to change the quantity of a specific item within a quote. 

## Fields

| Field                     | Description                                         |
| ------------------------- | --------------------------------------------------- |
| `quoteId` {==String!==}   | The Id of the quote containing the item.            |
| `lineItemId` {==String!==} | The Id of the item within the quote.               |
| `quantity` {==Int!==}     | The new quantity to set for the item within the quote.|
