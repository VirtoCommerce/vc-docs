# Filters

Filters can be applied to search results as an optional step, occurring at the conclusion of a search request. These filters are implemented after all facets have been calculated, ensuring that they do not affect the facet counts.

## Terms
In a query, terms can be either Single Terms or Phrases. Single Terms are individual words, while Phrases are groups of words enclosed in double quotes. To create more complex queries, multiple terms can be combined using Boolean Operators. For example, the query test AND "hello dolly" combines a Single Term "test" with a Phrase "hello dolly" using the Boolean Operator "AND".

| Term Type          | Description                                                                                               |
|--------------------|-----------------------------------------------------------------------------------------------------------|
| Single Term        | A single word, such as "test" or "hello".                                                                 |
| Phrase             | A collection of words enclosed in double quotes, such as "hello dolly".                                   |

## Fields
| Expression                            	| Description                                                                                      	| Example                            	                        |
|---------------------------------------	|--------------------------------------------------------------------------------------------------	|-----------------------------------------------------------	|
| `field_name:value`                    	| Specifies a field by entering the field name followed by a colon `:` and then the desired value. 	| `name:"My cool name"  color:Black`<br> Filters products based on the field values provided. |
| `field_name:value1,value2,value3,...` 	| Specifies multiple values in a field parameter, separated by a comma.                            	| `color:Black,Grey,Blue`<br> Retrieves products where the color is "black", "grey", or "blue" (acting as an OR-operator for the value))" 	|

## Range filtration

Range filtering enables the matching of products whose field values fall within the specified lower and upper bounds. The Range filter expression can be inclusive or exclusive of the upper and lower bounds. Sorting is performed in lexicographic order. 

The key rules are as follows:

* Inclusive range queries are represented by square brackets.
* Exclusive range queries are represented by round brackets. 
* The lower or upper bounds can be omitted by leaving the corresponding value empty.

| Range filter         	| Description                                                                      	|
|----------------------	|----------------------------------------------------------------------------------	|
| `price:[100 TO 200]` 	| Retrieves products with prices ranging from 100 to 200, including both endpoints. 	|
| `price:(100 TO 200]` 	| Retrieves products with prices ranging from greater than 100 to 200, inclusive.   	|
| `price:(TO 100]`     	| Retrieves products with prices less than or equal to 100.                         	|

## Boolean operators

By including multiple field terms in a single filter expression separated by a space delimiter, they will be combined using an **AND** operator.

For example, the following search request filters products that belong to the brand "Onkyo" AND have the color "Black":

`color:Black brand:Onkyo`

!!! note 
	Currently, the filter expressions only support the **AND** logical operator.

## Wildcard search

You can use single and multiple character wildcard searches within single or phrase terms.

| Symbol     	| Function                                                                        	| Example                                                                        	|
|-----------	|---------------------------------------------------------------------------------	|--------------------------------------------------------------------------------	|
| `?`       	| Single character wildcard search.                                               	| `b?ll` finds ball, bell, or bill.                                              	|
| `*`       	| Multiple character wildcard search.<br> You can use `*` anywhere in the string. 	| `test*` finds test, tests, or tester.<br> `hea*one` finds headphone, , healthone, or heartstone. |


## Escaping special characters

When using a double quotes block, you have the freedom to include any unsafe characters. To escape the double quote character itself, use the backslash `\`.

For example, `\"my cool property\":\"&~!'\"` searches "my cool property", and the value being matched is &~!'. The backslashes \ before the double quotes " are used to escape the double quotes and ensure they are treated as part of the search term.

[Read more](https://spec.graphql.org/June2018/#sec-String-Value){ .md-button }

## More Examples

| Query                                 | Description                                                                                   |
|---------------------------------------|-----------------------------------------------------------------------------------------------|
| `color:Black,White`                    | Retrieves products where the color is either 'Black' or 'White'.                               |
| `color:Black color:White`              | Retrieves products where the color is both 'Black' and 'White'.                                |
| `price_usd:[100 TO 200]`               | Retrieves products where the price is in USD and between the values 100 and 200 (inclusive).  |
| `price:(100 TO 200)`                   | Retrieves products where the price is in any currency and between the values 100 and 200 (exclusive). |
| `price:(0 TO)`                         | Retrieves products where the price is greater than zero.                                       |
| `price:(TO 100]`                       | Retrieves products where the price is less than or equal to 100.                              |
| `Da?? Red*`                           | Retrieves products where the name matches the pattern "Da" followed by any two characters, followed by " Red" with any number of characters after it. |
| `color:Black price:[100 TO 200)`       | Retrieves products where the color is 'Black' and the price is between 100 and 200 (inclusive).|

=== "Sample query"

    Filters products based on specific criteria. It includes products with the color "Black" or "Blue," a price range of $100 (inclusive) to $200 (exclusive), and names that start with "ASUS ZenFone 2."
    ```json linenums="1"
    {
      products(filter: "color:Black,Blue price.usd:[100 TO 200) name:\"ASUS ZenFone 2*\" {
          totalCount
          items
          {
            name
            properties
            {
                name
                values
            }
          }
      }
    }
    ```
=== "Sample return"
    ```json linenums="1"
    {
      "products": {
        "totalCount": 7,
        "items": [
          {
            "name": "ASUS ZenFone 2",
            "properties": [
              {
                "name": "Color",
                "values": ["Black"]
              },
              {
                "name": "Price",
                "values": ["$199.99"]
              }
            ]
          },
          {
            "name": "ASUS ZenFone 2 Deluxe",
            "properties": [
              {
                "name": "Color",
                "values": ["Black", "Blue"]
              },
              {
                "name": "Price",
                "values": ["$189.99"]
              }
            ]
          },
          // ... more product items
        ]
      }
    }
    ```
