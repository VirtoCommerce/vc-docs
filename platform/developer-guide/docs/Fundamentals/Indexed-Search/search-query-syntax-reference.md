# Search Query Syntax

Virto unified search has a special query syntax. It is processed by our proprietary query syntax parser. The parser interprets it into the Virto query object model. Then, an appropriate search adapter translates it into specific search engine syntax. This makes the query syntax search engine agnostic.

The syntax defines the grammar for the `searchPhrase` expression as follows:

```json
1  searchPhrase          : WS* phrase (WS phrase)* WS*;
2  phrase                : keyword | filters;
3  keyword               : String;
4  filters               : negation? (attributeFilter | rangeFilter);
5  attributeFilter       : fieldName FD attributeFilterValue;
6  rangeFilter           : fieldName FD rangeFilterValue;
7  fieldName             : String;
8  attributeFilterValue  : string (VD string)*;
9  rangeFilterValue      : range (VD range)*;
10 range                 : rangeStart WS* lower? WS* RD WS* upper? WS* rangeEnd;
11 rangeStart            : RangeStart;
12 rangeEnd              : RangeEnd;
13 lower                 : String;
14 upper                 : String;
15 string                : String;
16
17 negation              : '!';
18 FD                    : ':'; // Filter delimiter
19 VD                    : ','; // Value delimiter
20 RD                    : 'TO' | 'to'; // Range delimiter
21 RangeStart            : '[' | '(';
22 RangeEnd              : ']' | ')';
23
24 String                : SimpleString | QuotedString;
25 fragment SimpleString : ~[!":,[\]() \t]+;
26 fragment QuotedString : ('"' (Esc | ~["\\])* '"');
27 fragment Esc          : '\\' (["\\rnt]);
28
29 WS                    : [ \t]+; // Whitespace
```

The `searchPhrase` parameter accepts strings as input. These strings can contain two types of elements:

* `keyword` for full text search.
* `filters` for refining search criteria. 

The search supports any language and allows the use of boolean operators, precedence operators, wildcard or prefix characters for starts with queries, escape characters, and URL encoding characters within the `searchPhrase` parameter.

* `term phrase` is a query consisting of one or more terms, where any of the terms are considered a match, such as single words like **test** or **hello**.
* `phrase` is an exact phrase in quotation marks. 
* `filter phrase` is used to apply additional criteria to a search query apart from the full text search terms.


!!! note
    All examples in this article illustrate the unified search query syntax.
    Actual field names and supported filters depend on the specific API endpoint and indexed entity.

**Example**

| Query            | Description                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------|
| `Red wine`       | Searches for documents containing `Red` and/or `wine` anywhere in any order.                                               |
| `"Red wine"`     | Matches only the documents that contain the entire phrase in the appropriate order (lexical analysis applies).             |
| `"\"Red wine\""` | search request syntax is used to escape the quotation marks in a phrase search, for example, in Postman, in a POST request.|


## Full-text search
The parameter that performs full text search (term and phrase search) against the document index is `query`. Provide a full text search phrase to make it work.

## Searchable fields

The full text search runs over data in the index. All searchable text data are stored in a single `__content` field in the resulting index document, with the full text search being performed only for this field.

Below is an example of the product document in the index:

```
1 "__content": [
2    "JGC-85796278",
3    "ASUS ZenFone 2 ZE551ML Gold",
4    "asus",
5    "android",
6    "2.3 ghz intel gtx quad-core",
7    "micro-sim",
8    "1080"
9  ],
```

With an example request `asus`, you will get the search to find all documents where the `__content` field contains the `asus` value as an entire phrase or a part of it.

## Filters
`filter` provides value-based criteria for selecting which documents to include in the search results. A filter can be a single value or an expression. Unlike full text search, a filter succeeds only if an exact match is obtained.

Filters are specified in individual fields. A field definition must be set as **filterable** if you want to use it in filter expressions.

## Fields
When performing a search, you can:

* Specify a field by typing the field name followed by a colon (`:`) and then the term you are looking for:
    ```
    `name:"My cool name" color:Black`
    ```

* Specify multiple values in one field parameter, separated by a comma. It will return products in which at least one of the specified values matches (i.e. acting as an `OR` operator). The example below shows a request that filters products that are either black, grey, or blue:
    ```
    `color:Black,Gey,Blue`
    ```

## Range filtration
Range filtration helps you find products that have field values within a specified range. This range is defined by a range expression, which can be set to include or exclude the upper and lower bounds. Inclusive range queries use square brackets `[ ]`, while exclusive queries use round brackets `( )`.


**Example**

| Query                	| Description                                                            	|
|----------------------	|------------------------------------------------------------------------	|
| `price:[100 TO 200]` 	| Finds products with prices between 100 and 200, inclusive.             	|
| `price:(100 TO 200]` 	| Finds products with prices between 100, exclusive, and 200, inclusive. 	|
| `price:(TO 100]`     	| The price must be less than or equal to 100.                           	|

### Date and time range filtering

Date and time-based filtering must follow the unified search query syntax rules for range filters:

* Date-only values may be specified without quotes:

    ```
    createdDate:[2023-12-01 TO 2023-12-31]
    ```

* Date-time values contain special characters and must be provided as quoted strings:

    ```
    createdDate:["2026-01-19T11:47:35.4270502Z" TO "2026-01-31T11:47:35.4270502Z"]
    ```

If date-time values are not wrapped in double quotes, the range expression is not parsed correctly and returns no results.


## Boolean operators
Having multiple field terms separated by a space delimiter in a single filter expression will combine them with an `AND` operator.

The following search request filters products of a certain brand, Onkyo, and a certain color, black:

```
`color:Black brand:Onkyo`
```

![Readmore](media/readmore.png){: width="25"} [AND and OR search operators and examples](/platform/user-guide/latest/search-query-syntax)

## Wildcard search
Within a single phrase or phrase terms, you can use:

| Character 	| Function                                                                        	| Example                                                                        	|
|-----------	|---------------------------------------------------------------------------------	|--------------------------------------------------------------------------------	|
| `?`       	| Single character wildcard search.                                               	| `b?ll` finds ball, bell, or bill.                                              	|
| `*`       	| Multiple character wildcard search.<br> You can use `*` anywhere in the string. 	| `test*` finds test, tests, or tester.<br> `hea*one` finds headphone, healthone, or heartstone. |

!!! info
    Inside the double quotes block, you may use any unsafe characters.
    
    To escape double quote character, use backslash (`\`):
        ```
        `\"my cool property\":\"&~!'\"`
        ```

**Example**

| Query                            	| Description                                                               	|
|----------------------------------	|---------------------------------------------------------------------------	|
| `color:Black,White`              	| The color is either black or white.                                       	|
| `color:Black color:White`        	| The color is both black and white.                                        	|
| `price_usd:[100 TO 200]`         	| The price is between $100 and $200, inclusive.                            	|
| `price:(100 TO 200)`             	| The price in any currency is between 100 and 200, exclusive.              	|
| `price:(0 TO)`                   	| The price is greater than zero.                                           	|
| `price:(TO 100]`                 	| The price is less than or equal to 100.                                   	|
| `Da?? Red*`                      	| `?` replaces a single character.<br>`*` replaces zero or more characters. 	|
| `color:Black price:[100 TO 200)` 	| Combine keywords and filters.                                             	|


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../overview">← Indexed search overview</a>
    <a href="../indexing/overview">Indexing overview →</a>
</div>