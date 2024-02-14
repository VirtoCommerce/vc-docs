# FacetTermType ==~object~==

The `FacetTermType` represents a term within a facet used for filtering search results.

## Fields

| Field                     | Description                                                                            |
|---------------------------|----------------------------------------------------------------------------------------|
| `term` ==String!==        | The term associated with the facet.                                                    |
| `count` ==Long!==         | The count of items associated with this term in the facet.                             |
| `isSelected` ==Boolean!== | A boolean indicating whether this term is currently selected for filtering.            |
| `label` ==String!==       | The label for the term.                                                                |