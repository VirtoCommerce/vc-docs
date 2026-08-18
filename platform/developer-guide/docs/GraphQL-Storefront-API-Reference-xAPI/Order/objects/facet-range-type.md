# FacetRangeType ==~object~==

This type represents a range within a facet used for filtering search results based on numerical or range-based attributes.

## Fields

| Field                     | Description                                                                                       |
|---------------------------|---------------------------------------------------------------------------------------------------|
| `count` ==Long!==         | The count of items within this range.                                                             |
| `from` ==Long!==          | The starting value of the range.                                                                  |
| `includeFrom` ==Boolean!== | A boolean indicating whether the starting value of the range is inclusive.                       |
| `fromStr` ==String==      | A string representation of the starting value of the range.                                       |
| `max` ==Long!==           | The maximum value within the range.                                                               |
| `min` ==Long!==           | The minimum value within the range.                                                               |
| `to` ==Long!==            | The ending value of the range.                                                                    |
| `includeTo` ==Boolean!==  | A boolean indicating whether the ending value of the range is inclusive.                          |
| `toStr` ==String==        | A string representation of the ending value of the range.                                         |
| `total` ==Long!==         | The total count of items within the entire range.                                                 |
| `label` ==String!==       | The human-readable label or display name for the range.                                           |
| `isSelected` ==Boolean!== | A boolean indicating whether this range is currently selected for filtering.                      |

