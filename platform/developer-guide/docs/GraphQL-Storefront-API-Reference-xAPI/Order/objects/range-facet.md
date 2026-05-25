# RangeFacet ==~object~==

This type represents a facet used for filtering search results based on numerical or range-based attributes.

## Fields

| Field                             | Description                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------|
| `name` ==String!==                | The name or identifier of the range facet.                                                        |
| `label` ==String!==               | The human-readable label or display name of the range facet.                                      |
| `facetType` ==FacetTypes!==       | The type of facet, indicating its nature such as categorical, numerical, etc.                     |
| `ranges` [==[FacetRangeType!]!==](facet-range-type.md)   | An array of ranges representing the numerical or range-based attributes for filtering.            |
