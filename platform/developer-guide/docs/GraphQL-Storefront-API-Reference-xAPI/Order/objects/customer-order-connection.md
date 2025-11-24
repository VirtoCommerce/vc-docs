# CustomerOrderConnection ==~object~==

This type represents a connection of customer orders.

## Fields

| Field                                                             | Description                                                                                               |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `totalCount` ==Int==                                              | The total number of customer orders in the connection, regardless of pagination.                          |
| `pageInfo` [==PageInfo!==](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/PageInfo)     | Information about the current page and navigation in the connection.                                      |
| `edges` [==[CustomerOrderEdge]==](customer-order-edge.md)         | An array of edges representing the individual customer orders and their cursors in the connection.        |
| `items` [==[CustomerOrderType]==](customer-order-type.md)         | An array of customer orders retrieved for the current page in the connection.                             |
| `term_facets` [==[TermFacet!]!==](term-facet.md)                  | Faceted search results grouped by terms or categories.                                                    |
| `range_facets` [==[RangeFacet!]!==](range-facet.md)               | Faceted search results grouped by numerical or range-based attributes.                                    |
| `filter_facets` [==[FilterFacet!]!==](filter-facet.md)            | Faceted search results grouped by filter criteria.                                                        |
