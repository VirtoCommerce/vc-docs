# CartPickupLocationConnection ==~object~==

This type represents a connection from an object to a list of cart-specific pickup locations. It provides pagination details, a list of returned items, and facet information used for filtering and navigation.

## Fields

| Field                                   | Description                                                                                                                                                       |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `totalCount` ==Int==                    | The total number of pickup location objects available, ignoring pagination.                                                                                       |
| `pageInfo` ==[PageInfo!](../../Catalog/objects/PageInfo.md)==                | Information used to support pagination, including indicators for next/previous pages.                                        |
| `edges` ==[[ProductPickupLocationEdge](ProductPickupLocationEdge.md)]== | A list of edges in the connection, each containing a pickup location node and its pagination cursor.                              |
| `items` ==[[ProductPickupLocation](ProductPickupLocation.md)]==     | A convenience field returning the list of pickup location objects directly.                                                         |
| `term_facets` ==[[TermFacet!](../../Order/objects/term-facet.md)]!==         | A list of term facets, giving aggregated counts for categorical filter values.                                             |
| `range_facets` ==[[RangeFacet!](../../Order/objects/range-facet.md)]!==       | A list of range facets, providing aggregated counts for numeric/date ranges.                                              |
| `filter_facets` ==[[FilterFacet!](../../Order/objects/filter-facet.md)]!==     | A list of filter facets, representing complex, preconfigured filters applied to the results.                             |
