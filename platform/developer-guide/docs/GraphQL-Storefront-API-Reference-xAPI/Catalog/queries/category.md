# Category ==~query~==

This connection allows you to search for a specific category.

## Arguments

| Argument                     	| Description                                             	|
|------------------------------	|-------------------------------------------------------	|
| `id`  ==String!==            	| The category Id.                                        	|
| `storeId`  ==String!==       	| The ID of the store to retrieve pages from.            	|
| `userId`  ==String==         	| The current user Id.                                  	|
| `currencyCode`  ==String!==  	| A standardized code of a specific currency.           	|
| `cultureName`  ==String!==   	| A language to retrieve data in.                         	|

## Possible returns

| Possible return                                                       	| Description                    	|
|-----------------------------------------------------------------------	|--------------------------------	|
| [`CategoryType`](../objects/category/CategoryType.md)                 	| The description of a category. 	|

## Example


<div class="grid" markdown>

```json title="Query"
{
  category(
    storeId: "B2B-store"
    id: "02fe37dcaeb2458a831011abe43fd335"
    cultureName: "en-US"
    currencyCode: "USD"
  ) {
    name
    code
    id
    level
    path
    parent {
      name
    }
  }
}
```

```json title="Return"
{
  "data": {
    "category": {
      "name": "Bolts",
      "code": "cd931",
      "id": "02fe37dcaeb2458a831011abe43fd335",
      "level": 1,
      "path": "Bolts",
      "parent": null
    }
  }
}
```

</div>