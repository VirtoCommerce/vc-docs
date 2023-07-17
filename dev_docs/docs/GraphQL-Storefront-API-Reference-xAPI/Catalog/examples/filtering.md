# Filtering
The section below explains you how to manage the filtering process in the most common scenarios.

## Filtering by category

| Query                    	| Description                                                            	| Note                                                                	|
|--------------------------	|------------------------------------------------------------------------	|---------------------------------------------------------------------	|
| `filter: "category.path:{catalog id/category path}"`<br> `filter: "category.path:catalogId/cat1d1/cat2id"`    	| Filters products that belong to<br>the exactly specified category path.   	| The search is performed against the `__path`<br>index field of the product document.  	|
| `filter: "category.subtree:{catalog id/category path}"`<br> `filter: "category.subtree:catalogId/cat1d1/cat2id"`  | Filters products that belong to<br>the specified Category or any of its<br>descendant categories. 	| The search is performed against the `__outline`<br>index field of the product document.  	|

## Filtering by price

| Query                          	| Description                                                   	| Note                                                                                                    	|
|--------------------------------	|---------------------------------------------------------------	|----------------------------------------------------------------------------------------------------------	|
| `filter: "price.{currency}.{pricelist?}:{range expression}"`<br> `filter: "price.usd:(TO 100]"`<br> `filter: "price.usd.pricelist_1:(20 TO 100]"`   `filter: "is:priced"` (keeps only products that have at least one price set) 	| Filters products based on the specified price value or range. 	| The search will be performed against<br>the `price_{currency}` and `price_{currency}_{pricelist}`<br>index fields of the product document.<br> Only the indexed prices may be used<br>for filtration. Scoped prices based on user groups<br>or dynamic expressions temporary do not support filtration. 	|

## Filtering by SKU

| Query                       	| Description                                  	|
|-----------------------------	|----------------------------------------------	|
| `filter: "sku:DLL-65789352` 	| Filters products based on the specified SKU. 	|

## Filtering Products or Variations

| Query                       	| Description                                  	|
|-----------------------------	|----------------------------------------------	|
| `filter: "is:product status:visible"`<br>`filter: "is:variation status:hidden"`	| Includes only either the products or variations in the result. If not set, it will return both types. 	|

## Filtering by Custom Properties

!!! info
	All product custom properties are stored in the index as fields with the same names as the base properties have (`{property.name}:{property.value}`).

| Query                                                                              	| Description                                                                                           	|
|------------------------------------------------------------------------------------	|-------------------------------------------------------------------------------------------------------	|
| `filter: "properties.{property name}: {value}`<br> `filter: "properties.color:red` 	| For keeping the products or variation with the custom attribute<br>matching the specified value or range. 	|
| `filter= "\"processor core (ghz)\":\"1.8 GHz Intel GTX Quad-Core\""`               	| For property name that contains spaces.                                                               	|
| `filter: "length:(10 TO 20)"`<br> `filter: "publishDate:(TO \"2020-01-28\")"`      	| For numeric and date time properties.                                                                 	|


## Filtering by Product Availability

| Query                                                                         	| Description                                                                                        	|
|-------------------------------------------------------------------------------	|----------------------------------------------------------------------------------------------------	|
| `filter: "available_in:{warehouse}"`<br>`filter: "available_in:my-warehouse"` 	| Keeps only the products or variations with the availability matching the specified value or range. 	|

### Example

=== "Sample query"
    Displays products and variations in a list from a specific category.

    ```json linenums="1"
    query {
      products(
        storeId: "B2B-store"
        cultureName: "en-US"
        first:20
        after: "0"
        filter:"status:hidden,visible category.path:7829d35f417e4dd98851f51322f32c23/4fbaca886f014767a52f3f38b9df648f"
      ) {
        items 
        {
          name
        }
        totalCount
      }}
    ```
=== "Sample return"
    ```json linenums="1"
    {
      "data": {
        "products": {
          "items": [
            {
              "name": "1-1/2\" Steel Carriage Bolt, Grade 5, Chrome Plated Finish, 1/4\"-20 Dia/Thread Size, 5 PK"
            },
            {
              "name": "1\" Steel Carriage Bolt, Grade A, Hot Dipped Galvanized Finish, 1/4\"-20 Dia/Thread Size, 1300 PK"
            },
            {
              "name": "1-1/4\" Steel Carriage Bolt, Grade A, Hot Dipped Galvanized Finish, 1/4\"-20 Dia/Thread Size, 1100 PK"
            },
            // ... more product items
          ],
          "totalCount": 26
        }
      }
    }
    ```

## Sorting

The default sorting of search results is based on their relevancy to the provided text (referred to as "score"), with the results sorted in descending order. However, you can specify an alternative sorting by using the sort query parameter, which follows the `{field}:{asc|desc}` structure. Multiple sort expressions can be combined using a semicolon `;`.

For example, to sort the results by priority in descending order, followed by price_usd in ascending order, and finally by score, you can use the following sort parameter:

`sort: "priority:desc;price_usd;score"`