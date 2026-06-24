# ChangeQuoteItemQuantityCommandType ==~object~==

This type is used to change the quantity of a specific item within a quote. 

## Fields

| Field                     | Description                                         |
| ------------------------- | --------------------------------------------------- |
| `quoteId`  ==String!==    | The Id of the quote containing the item.            |
| `lineItemId`  ==String!==  | The Id of the item within the quote.               |
| `quantity`  ==Int!==      | The new quantity to set for the item within the quote.|

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../ChangeQuoteCommentCommandType">← ChangeQuoteCommentCommandType</a>
    <a href="../CreateQuoteFromCartCommandType">CreateQuoteFromCartCommandType →</a>
</div>
