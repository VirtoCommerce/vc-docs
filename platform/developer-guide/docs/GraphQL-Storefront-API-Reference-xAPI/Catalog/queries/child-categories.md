# childCategories ==~query~==

This query allows you to retrieve a list of child categories for a given parent category. 

## Argument

| Argument                          	| Description                                                                       	|
|-----------------------------------	|-----------------------------------------------------------------------------------	|
| `storeId`  ==String==               	| The Id of the store to retrieve pages from.                                        	|
| `userId`  ==String==                	| The current user Id.                                                              	|
| `cultureName`  ==String==           	| A language to retrieve data in.                                                      	|
| `currencyCode`  ==String==          	| A standardized code of a specific currency.                                         	|
| `categoryId`  ==String==            	| Filters the child categories based on a specific category Id.                     	|
| `maxLevel`  ==Int==                 	| The maximum depth or level of child categories to retrieve.                       	|
| `onlyActive`  ==Boolean==           	| Indicates whether only active child categories should be included in the results. 	|
| `productFilter`  ==String==         	| Filtering criteria for the products within the child categories.                  	|

## Possible returns

| Possible return                                           	                    | Description                                                   	|
|-------------------------------------------------------------------------------	|---------------------------------------------------------------	|
| `ChildCategoriesQueryResponseType` 	                                            | A response for a query that retrieves child categories.           |

## Example

<div class="grid" markdown>

```json title="Query"
{
  childCategories(
    storeId: "B2B-Store"
    cultureName: "en-US"
    currencyCode: "USD"
    maxLevel: 2
    productFilter: "price:(0 TO) instock_quantity:(0 TO)"
  ) {
    childCategories {
      name
      id
      code
    }
  }
}
```

```json title="Return"
{
  "data": {
    "childCategories": {
    "childCategories": [
        {
        "name": "Bolts",
        "id": "02fe37dcaeb2458a831011abe43fd335",
        "code": "cd931"
        },
        {
        "name": "Snacks",
        "id": "532a6b5a-cf15-461a-836e-71bad60d49a3",
        "code": "de065"
        },
        {
        "name": "Soft Drinks",
        "id": "591e75f2-0954-49b3-90d0-077c270955c4",
        "code": "480dc"
        },
      // ... more product items
      ]
    }
  }
}
```

</div>