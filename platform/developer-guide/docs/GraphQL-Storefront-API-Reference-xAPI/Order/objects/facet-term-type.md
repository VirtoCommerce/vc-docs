# FacetTermType ==~object~==

This type represents a term within a facet used for filtering search results.

## Fields

| Field                     | Description                                                                            |
|---------------------------|----------------------------------------------------------------------------------------|
| `term` ==String!==        | The term associated with the facet.                                                    |
| `count` ==Long!==         | The count of items associated with this term in the facet.                             |
| `isSelected` ==Boolean!== | A boolean indicating whether this term is currently selected for filtering.            |
| `label` ==String!==       | The label for the term.                                                                |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../term-facet">← TermFacet</a>
    <a href="../facet-range-type">FacetRangeType →</a>
</div>
