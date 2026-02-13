# Contacts ==~query~==

This connection allows you to retrieve the desired list of contacts.

## Arguments

| Argument                           	| Description                             |
	|---------------------------------------------------------------------------	|
| `after`  ==String==               	| A cursor value to paginate through the results.                                                               |
| `first`  ==Int==                  	| The number of pages in a single query.                                                                        |
| `searchPhrase`  ==String==            | A search phrase to filter the organizations based on their names or other relevant attributes.              |
| `sort`  ==String==                	| Specifies the sorting order of the returned organizations.                                                    |

## Possible returns

| Possible return                                                       	| Description                           	|
|-----------------------------------------------------------------------	|---------------------------------------	|
| [`ContactConnection`](../Objects/ContactConnection.md)             	    | A connection to a list of contacts.  	  |


## Example

<div class="grid" markdown>

```json title="Query"
query {
  contacts(
    after: "cursorValue"
    first: 10
    searchPhrase: "John"
    sort: "name"
  ) {
    edges {
      node {
        id
        name
        email
        phone
      }
    }
  }
}
```

```json title="Return"
{
  "data": {
    "contacts": {
      "edges": [
        {
          "node": {
            "id": "contact1",
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "123-456-7890"
          }
        },
        {
          "node": {
            "id": "contact2",
            "name": "John Smith",
            "email": "john.smith@example.com",
            "phone": "987-654-3210"
          }
        },
        {
          "node": {
            "id": "contact3",
            "name": "John Walker",
            "email": "johnny@example.com",
            "phone": "555-555-5555"
          }
        }
      ]
    }
  }
}
```

</div>