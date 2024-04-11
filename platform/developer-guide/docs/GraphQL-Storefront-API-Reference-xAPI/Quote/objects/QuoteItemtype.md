# QuoteItemType ==~object~==

The `QuoteItemType` is an object that provides information about a specific item within a quote.

## Fields

| Field                                                                 | Description                                       |
| -------------------------------------------------------------         | ------------------------------------------------- |
| `id`  ==String!==                                                     | The Id of the quote item.                         |
| `sku`  ==String!==                                                    | The Stock Keeping Unit (SKU) of the item.         |
| `productId`  ==String!==                                              | The Id of the associated product.                 |
| `catalogId`  ==String!==                                              | The Id of the catalog to which the item belongs.  |
| `categoryId`  ==String==                                              | The Id of the category to which the item belongs. |
| `name`  ==String!==                                                   | The name or title of the item.                    |
| `comment`  ==String==                                                 | A comment about the item.                         |
| `imageUrl`  ==String==                                                | The URL of an image representing the item.        |
| `taxType`  ==String==                                                 | The type of tax associated with the item.         |
| `listPrice` [ ==MoneyType== ](../../Cart/objects/money-type.md)       | The list price of the item.                       |
| `salePrice` [ ==MoneyType== ](../../Cart/objects/money-type.md)       | The sale price of the item.                       |
| `selectedTierPrice` [ ==QuoteTierPriceType== ](QuoteTierPriceType.md) | The selected tier price for the item.             |
| `proposalPrices` [ ==[QuoteTierPriceType]== ](QuoteTierPriceType.md)  | A list of proposal prices for the item.           |
| `product` [ ==Product== ](../../Catalog/objects/ProductType.md)       | Information about the associated product.         |

