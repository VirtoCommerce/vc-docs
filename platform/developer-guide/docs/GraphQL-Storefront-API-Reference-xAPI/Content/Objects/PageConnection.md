# PageConnection ==~object~==

This type represents a connection to a collection of pages. It provides structured information and pagination controls for retrieving and managing pages within the system. 

## Fields

| Field                                                           | Description                                            |
|-----------------------------------------------------------------|--------------------------------------------------------|
| `totalCount` ==Int==                                            | The total number of pages in the connection.           |
| `pageInfo` [==PageInfo!==](../../Catalog/objects/PageInfo.md)   | The information about the current page.                |
| `edges` [==PageEdge==](PageEdge.md)                             | An array of page edges.                                |
| `items` [==PageType==](PageType.md)                             | An array of actual page objects.                       |