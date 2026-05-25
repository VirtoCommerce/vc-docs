# VideoEdge ==~object~==

The `VideoEdge` represents an edge in queries, specifically related to videos.

## Fields

| Field                                 	| Description                                                                                        	|
|----------------------------------------	|----------------------------------------------------------------------------------------------------	|
| `cursor` {==String!==}              	    | A cursor that points to the specific position of this edge in the paginated list of video objects. 	|
| `node` [{==VideoType==}](VideoType.md) 	| The video object associated with the edge.                                                         	|
