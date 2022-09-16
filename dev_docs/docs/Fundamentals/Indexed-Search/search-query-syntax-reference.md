# Search Query Syntax Reference
Virto's unified search supports a special query syntax that is processed by our proprietary **query syntax parser** and interprets it into the Virto query object model that then gets translated into specific search engine syntax by an appropriate search adapter. This makes the **query syntax** truly search engine agnostic.

The table below shows how the syntax defines the grammar for the **.** `searchPhrase` expression:

```
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

`SearchPhrase` expressions are evaluated during query parsing, which constrains the search to specific fields or adds match criteria used during index scans.

Strings transferred to the `searchPhrase` parameter can include `keyword` for full text search and `filters` to apply additional criteria to a search in any supported language, with boolean operators, precedence operators, wildcard or prefix characters for *starts with* queries, escape characters, and URL encoding characters.

-   A _term phrase_ is a query consisting of one or more terms, where any of the terms are considered a match, such as single words like *test* or *hello*.
    
-   A _phrase phrase_ is an exact phrase enclosed in quotation marks (`" "`). For example, while `Red wine` (without quotes) would search for documents containing `Red` and/or `wine` anywhere in any order, `"Red wine"` (with quotes) will only match documents that contain the entire phrase in the appropriate order (lexical analysis still applies).
    
Depending on your search client, you might need to escape the quotation marks in a phrase search. For example, in Postman, in a POST request, a phrase search on `"Red wine"` in the request body would be specified as `"\"Red wine\""`.
    
-   A _filter phrase_ is used to apply additional criteria to a search query apart from the full text search terms.

# Full Text Search (Term and Phrase Search)
The parameter that performs full text search against the document index is `query`, and you need to provide a full text search phrase to make it work.

## Searchable Fields

The full text search runs over data in the index. All searchable text data are stored in a single `__content` field in the resulting index document, with the full text search being performed only for this field.

For instance, the product document in the index may look like this:

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

# Filters
A _filter_ provides value-based criteria for selecting which documents to include in the search results. A filter can be a single value or an expression. In contrast with the full text search, a filter succeeds only if an exact match is achieved.

Filters are specified in individual fields. A field definition must be attributed as "filterable" if you want to use it in filter expressions.

## Fields
When performing a search, you can either specify a field by typing the field name followed by a colon (`:`) and then the term you are looking for, e.g.:

`name:"My cool name" color:Black`

Specifying multiple values in one field parameter, separated by a comma, will return products in which at least one of the specified values matches (i.e. acting as an *OR* operator). The example below shows a request that filters products that are either black, grey, or blue:

`color:Black,Gey,Blue`

## Range Filtration
Range filtration enables matching products the field values  of which are between the lower and upper bound specified by a *Range* expression that can be both inclusive or exclusive. The sorting processes runs based on lexicography.

Here are a few examples:

`price:[100 TO 200]`

This will find products with prices between 100 and 200, inclusive (inclusive range queries use square brackets, while exclusive queries use round brackets).

`price:(100 TO 200]`

This will find products with prices between 100, exclusive, and 200, inclusive.

You can skip one of the values to ignore either the lower or the upper bound:

`price:(TO 100]`,

which means the price must be less than or equal to 100.

## Boolean Operators
Having multiple field terms separated by a space delimiter in a single filter expression will combine them with an *AND* operator.

The following example search request filters products of a certain brand, Onkyo, and a certain color, black.

`color:Black brand:Onkyo`

!!! warning
    * At the moment, only logical ***AND*** operators are supported for filter expressions.

## Wildcard Search
You can use single and multiple character wildcard search within a single phrase or phrase terms. To perform a single character wildcard search, use a quotation mark (`?`), while for a multiple character wildcard search use an asterisk (`*`).

For instance, with this search request:
 
`te?t`

multiple character wildcard search will look for 0 or more characters.

Alternatively, to search for, say, *test*, *tests*, or *tester*, you can use the following expression:

`test*`

You can also use wildcard search in the middle of a term, e.g.:

`te*t`

## Escaping Special Characters
Inside the double quotes block, you might use any unsafe characters; to escape double quote character, use backslash (`\`):

`\"my cool property\":\"&~!'\"`

## More Examples
Below, you can find some more examples of typical search requests:

`color:Black,White`: The color is either black or white

`color:Black color:White`: The color is both black and white

`price_usd:[100 TO 200]`: The price is between $100 and $200, inclusive

`price:(100 TO 200)`: The price in any currency is between 100 and 200, exclusive

`price:(0 TO)`: The price is greater than zero

`price:(TO 100]`: The price is less than or equal to 100

`Da?? Red*`: `?` replaces a single character, while `*` replaces zero or more characters

`color:Black price:[100 TO 200)`: Combine keywords and filters
