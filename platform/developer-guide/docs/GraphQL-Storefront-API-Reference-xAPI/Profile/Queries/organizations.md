# Organizations ==~query~==

This connection allows you to retrieve the desired list of organizations, meeting your specific requirements for pagination, filtering, and sorting.

## Arguments

| Argument                           	| Description                                                                                               |
|------------------------------------	|----------------------------------------------------------------------------------------------------------	|
| `after`  ==String==               	| A cursor value to paginate through the results.                                                           |
| `first`  ==Int==                  	| The number of pages in a single query.                                                                   	|
| `searchPhrase`  ==String==            | A search phrase to filter the organizations based on their names or other relevant attributes.          |
| `sort`  ==String==                	| Specifies the sorting order of the returned organizations.                                                |

## Possible returns

| Possible return                                                       	| Description                               	|
|-----------------------------------------------------------------------	|--------------------------------------------	|
| [`OrganizationConnection`](../Objects/OrganizationConnection.md)     	    | A connection to a list of organizations.  |

## Example

<div class="grid" markdown>

```json title="Query"
query {
  organizations(
    after: "cursorValue"
    first: 10
    searchPhrase: "Company"
    sort: "name"
  ) {
    edges {
      node {
        id
        name
        ownerId
        businessCategory
      }
    }
  }
}
```

```json title="Return"
{
  "data": {
    "organizations": {
      "edges": [
        {
          "node": {
            "id": "123456",
            "name": "Company A",
            "ownerId": "789012",
            "businessCategory": "Technology"
          }
        },
        {
          "node": {
            "id": "345678",
            "name": "Company B",
            "ownerId": "901234",
            "businessCategory": "Finance"
          }
        }
      ]
    }
  }
}
```

</div>