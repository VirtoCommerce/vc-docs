# FacetTermtype ==~object~==

This type represents a specific term or value within a term facet, allowing users to filter products based on discrete values associated with a particular attribute or property. 

## Fields

| Field                      	| Description                                                        	|
|-----------------------------	|--------------------------------------------------------------------	|
| `term`  ==String==         	| The specific term within the facet.                                	|
| `count`  ==Long==          	| The count or number of products associated with the specific term. 	|
| `isSelected`  ==Boolean==  	| Indicates whether the term is currently selected as a filter.      	|
| `label`  ==String!==       	| A label of the term.                                                 	|