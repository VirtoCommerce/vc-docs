# CartPickupLocationConnection ==~object~==

This type represents a connection from an object to a list of cart-specific pickup locations. It provides pagination details, a list of returned items, and facet information used for filtering and navigation.

## Fields

| Field                                   | Description                                                                                                                                                       |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `totalCount` ==Int==                    | The total number of pickup location objects available, ignoring pagination.                                                                                       |
| `pageInfo` ==[PageInfo!](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/PageInfo)==                | Information used to support pagination, including indicators for next/previous pages.                                        |
| `edges` ==[[ProductPickupLocationEdge](ProductPickupLocationEdge.md)]== | A list of edges in the connection, each containing a pickup location node and its pagination cursor.                              |
| `items` ==[[ProductPickupLocation](ProductPickupLocation.md)]==     | A convenience field returning the list of pickup location objects directly.                                                         |
| `term_facets` ==[[TermFacet!](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Order/objects/term-facet)]!==         | A list of term facets, giving aggregated counts for categorical filter values.                                             |
| `range_facets` ==[[RangeFacet!](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Order/objects/range-facet)]!==       | A list of range facets, providing aggregated counts for numeric/date ranges.                                              |
| `filter_facets` ==[[FilterFacet!](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Order/objects/filter-facet)]!==     | A list of filter facets, representing complex, preconfigured filters applied to the results.                             |
