# FacetTermtype ==~object~==

The `FacetTermType` represents a specific term or value within a term facet, allowing users to filter products based on discrete values associated with a particular attribute or property. 

## Fields

| Field                      	| Description                                                        	|
|-----------------------------	|--------------------------------------------------------------------	|
| `term` {==String==}        	| The specific term or value within the facet.                       	|
| `count` {==Long==}         	| The count or number of products associated with the specific term. 	|
| `isSelected` {==Boolean==} 	| Indicates whether the term is currently selected as a filter.      	|
| `label` {==String!==}      	| A human-readable label or display name for the term.               	|