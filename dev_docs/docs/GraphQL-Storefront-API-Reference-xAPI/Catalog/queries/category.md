# Category ==~query~==

This connection allows you to search for a specific category.

## Arguments

| Argument                     	| Description                                             	|
|------------------------------	|-------------------------------------------------------	|
| `id` {==String!==}           	| Identifies the category.                              	|
| `storeId` {==String!==}      	| Specifies the ID of the store to retrieve pages from. 	|
| `userId` {==String==}        	| Identifies the user.                                  	|
| `currencyCode` {==String!==} 	| A standardized code of a specific currency.           	|
| `cultureName` {==String!==}  	| Specifies the language.                               	|

## Possible returns

| Possible return                                                       	| Description                    	|
|-----------------------------------------------------------------------	|--------------------------------	|
| [`CategoryType`](../objects/category/CategoryType.md)                 	| The description of a category. 	|

**Examples**

=== "Query" 
    ```json linenums="1"
    {
        category (storeId:"B2B-store",
        id:"02fe37dcaeb2458a831011abe43fd335", 
        cultureName:"en-US", currencyCode:"USD")  
        {    
            name    
            code    
            id    
            level    
            path    
            parent    
            {      
                name    
            }  
        }
    }
    ```
=== "Return"
    ```json linenums="1"
    {
        "data": {
            "category": {
            "name": "Bolts",
            "code": "cd9312",
            "id": "02fe37dcaeb2458a831011abe43fd335",
            "level": 1,
            "path": "Bolts",
            "parent": null
            }
        }
    }
    ```
