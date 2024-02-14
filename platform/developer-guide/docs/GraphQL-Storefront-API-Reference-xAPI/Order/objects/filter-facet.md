# FilterFacet ==~object~==

The `FilterFacet` type represents a facet used for filtering search results.

## Fields

| Field                         | Description                                                                                      |
|-------------------------------|--------------------------------------------------------------------------------------------------|
| `name` ==String!==            | The name of the filter facet.                                                                    |
| `label` ==String!==           | The label or display name of the filter facet.                                                   |
| `facetType` ==FacetTypes!==   | The type of facet: Terms, Range, Filter.                                                         |
| `count` ==Int!==              | The count of items associated with this facet.                                                   |