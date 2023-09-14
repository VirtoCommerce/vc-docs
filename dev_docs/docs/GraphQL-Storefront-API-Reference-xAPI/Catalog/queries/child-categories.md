# childCategories ==~query~==

This query allows you to retrieve a list of child categories for a given parent category. 

## Argument

| Argument                          	| Description                                                                       	|
|-----------------------------------	|-----------------------------------------------------------------------------------	|
| `storeId` {==String==}              	| The ID of the store to retrieve pages from.                                        	|
| `userId` {==String==}               	| The current user Id.                                                              	|
| `cultureName` {==String==}          	| A language to retrieve data in.                                                      	|
| `currencyCode` {==String==}         	| A standardized code of a specific currency.                                         	|
| `categoryId` {==String==}           	| Filters the child categories based on a specific category ID.                     	|
| `maxLevel` {==Int==}                	| The maximum depth or level of child categories to retrieve.                       	|
| `onlyActive` {==Boolean==}          	| Indicates whether only active child categories should be included in the results. 	|
| `productFilter` {==String==}        	| Filtering criteria for the products within the child categories.                  	|

## Possible returns

| Possible return                                           	                    | Description                                                   	|
|-------------------------------------------------------------------------------	|---------------------------------------------------------------	|
| `ChildCategoriesQueryResponseType` 	                                            | A response for a query that retrieves child categories.           |

## Examples

=== "Query"
    ```json linenums="1"
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

=== "Return"
    ```json linenums="1"
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
            {
            "name": "Alcoholic drinks",
            "id": "6ef7c5e6-fb2d-4c68-bc45-8186c5d3dd05",
            "code": "6dd6a"
            },
            {
            "name": "Juice",
            "id": "af1347a6-5709-4d7a-bb1a-01d34d3ec5da",
            "code": "2c86c"
            },
            {
            "name": "Kitchen supplies",
            "id": "b674f311-5dbe-42f7-bc30-8076744c59bf",
            "code": "456d3"
            },
            {
            "name": "Coffee and tea",
            "id": "b718cdea-0bcb-4478-910c-f437013e93db",
            "code": "31d7d"
            },
            {
            "name": "Printers",
            "id": "d6019d4d27e44854a58ebbd5428b873b",
            "code": "b76cb"
            }
        ]
        }
    }
    }
    ```
