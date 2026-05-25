# TermFacet ==~object~==

This type represents a facet used for filtering search results based on terms or categories.

## Fields

| Field                         | Description                                                                                       |
|-------------------------------|---------------------------------------------------------------------------------------------------|
| `name` ==String!==            | The name or identifier of the term facet.                                                         |
| `label` ==String!==           | The human-readable label or display name of the term facet.                                       |
| `facetType` ==FacetTypes!==   | The type of facet: Terms, Range, Filter.                                                          |
| `terms` [==[FacetTermType!]!==](facet-term-type.md) | An array of terms representing the categories or terms for filtering.       |