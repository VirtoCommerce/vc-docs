# QuoteConnection ==~object~==

This type is an object used to manage and retrieve quotes. 

## Fields

| Field                     | Description               |
| ------------------------- | ------------------------- |
| `totalCount`  ==Int==     | The total number of quotes.|
| `pageInfo` [ ==PageInfo!== ](../../Catalog/objects/PageInfo.md)| Pagination information.   |
| `edges` [ ==[QuoteEdge]== ](QuoteEdge.md) | Connections to quotes.    |
| `items` [ ==[QuoteType]== ](QuoteType.md) | Individual quotes .       |
