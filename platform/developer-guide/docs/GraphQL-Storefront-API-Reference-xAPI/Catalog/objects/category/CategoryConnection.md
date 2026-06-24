# CategoryConnection ==~object~==

This type represents a connection to a list of categories. 

## Fields

| Field                                           	| Description                                                                 	|
|------------------------------------------------	|-----------------------------------------------------------------------------	|
| `totalCount`  ==Int==                            	| The total number of categories in the connection, regardless of pagination. 	|
| `pageInfo` [ ==PageInfo!== ](../PageInfo.md)     	| The information about the current page.                                         	|
| `edges` [ ==CategoryEdge== ](CategoryEdge.md) 	| A connection between a category and the cursor associated with it.          	|
| `items` [ ==Category== ](CategoryType.md)     	| The actual categories returned in the connection.                           	|

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../CategoryType">← CategoryType</a>
    <a href="../CategoryEdge">CategoryEdge →</a>
</div>
