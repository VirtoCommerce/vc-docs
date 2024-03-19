# TermFacet ==~object~==

The `TermFacet` represents a facet for filtering products based on discrete values or terms. 

## Fields

| Field                                           	| Description                                                	|
|------------------------------------------------	|------------------------------------------------------------	|
| `name`  ==String!==                            	| The name of the term facet.                                	|
| `label`  ==String!==                            	| A label of the term facet. 	                                |
| `facetType`  ==FacetTypes==                   	| The type of the term facet.                                	|
| `terms` [ ==FacetTermType== ](facetTermType.md)  	| A specific term or value within the term facet.            	|