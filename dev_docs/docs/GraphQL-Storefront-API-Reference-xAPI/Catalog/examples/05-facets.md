# Facets

Faceted search (sometimes also called faceted navigation) allows users to navigate through a web site by applying filters for categories, attributes, price ranges and so on. The main idea behind faceted search is to present the attributes of the documents of the previous search result as filters, which can be used by the user to narrow down search results along with calculate statistical counts to aid.

Facet calculation is requested by providing facet expression via the facet query parameter. Consider for example the following two facets:

`facet: "color price:[TO 100),[100 TO 200])"`

The resulting json would be like seen here:

```json
"data": {
    "products": {
      "totalCount": 182,
      "items": [...],
      "range_facets": [
        {
          "name": "price_*-100_100-200",
          "ranges": [
            {
              "from": 0,
              "to": 100,
              "count": 5959,
              "includeTo": false,
              "includeFrom": true
            },
            {
              "from": 100,
              "to": 200,
              "count": 2143,
              "includeTo": true,
              "includeFrom": true
            }
          ]
        }
      ],
      "term_facets": [
        {
          "name": "color",
          "terms": [
            {
              "term": "EXPRESSO",
              "count": 2343
            },
            {
              "term": "Sierra Brown",
              "count": 362
            },
            ...
        }]
    }
}
```

## TermFacet Expression

To retrieve facet counts for all occurring values of a product document field the following notations can be applied:

`facet: "category.path"`

Counts the products of all categories.

`facet: "{propertyName}"`
`facet: "properties.{propertyName}"`

Counts the product documents for all occurring values of custom  properties.

## TermFacet Result

The term type facets provide the counts for each of the different values the query parameter happens to have.

`name` - represents the key of requested facet taken from facet expression.
`terms.term` - one of the values for the field specified in facet expression for which at least one product could be found
`terms.count` - amount of products  for which the term applies
`terms.isSelected` - flag indicates that requested facet term is used in `filter` expression, in order to simplify displaying the already selected facet terms on the frontend.

## RangeFacet Expression

To aggregate facet counts across ranges of values, the range qualifier can be applied analogous to the filter parameters. The `range` notation is applicable to the date, time, datetime, number and money type fields.

`facet: "price.{currency}:[TO 100),[100 TO 200])"`
Counts the products whose price falls in one of the specified ranges

`facet: "properties.{propertyName}[1 TO 100)"`
Counts the products whose values of the custom property fall in one of the specified ranges

## RangeFacet result

The range facet type counts the products for which the query value is a range specified in the range expression. Range facets are typically used to determine the minimum and maximum value for example product prices to filter products by price with a range slider.

`name`: represents the key of requested facet taken from facet expression and build from range parameters concatenated by `_`. e.g `price_*-100_100-200`
`ranges.from`: the range’s lower endpoint in number format
`ranges.to`: the range’s upper endpoint in string format
`ranges.count`: amount of products fall into the specified range
`ranges.includeTo`: flag indicates that lower bound is included
`ranges.includeFrom`: flag indicates that upper bound is included
`ranges.isSelected`: flag indicates that requested facet term is used in `filter` expression, in order to simplify displaying the already selected facet terms on the frontend.

## Querying Product Breadcrumbs

When querying breadcrumbs of the product make sure your store's `SEO Links` setting is **not** set to `None`, otherwise breadcrumbs for the store would not be created. To check the setting go to Store - select your store - Settings - SEO - SEO Links.