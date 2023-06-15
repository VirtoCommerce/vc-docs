# RangeFacet ==~object~==

The `RangeFacet` represents a facet for filtering products based on a range of values.  

## Fields

| Field                                  	            | Description                                                 	|
|---------------------------------------------------	|-------------------------------------------------------------	|
| `name` {==String!==}                              	| The name of the range facet.                                	|
| `label` {==String!==}                                	| A human-readable label or display name for the range facet. 	|
| `facetType` {==FacetTypes==}                      	| The type of the range facet.                                	|
| `ranges` [{==FacetRangeType==}](FacetRangeType.md)    | A specific range within the range facet.                    	|