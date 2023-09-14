# UpdateQuoteAddressesCommandType  ==~object~==

The `UpdateQuoteAddressesCommandType` used to update the addresses associated with a specific quote.

## Fields

| Field                                                                  | Description                                                        |
| -----------------------------------------------------------------------| ------------------------------------------------------------------ |
| `quoteId` {==String!==}                                                | The Id of the quote for which addresses are being updated.         |
| `addresses` [{==[InputQuoteAddressType]!==}](InputQuoteAddressType.md) | A list of updated addresses for the quote.                         |
