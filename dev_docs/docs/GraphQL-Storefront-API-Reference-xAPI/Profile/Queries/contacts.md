# Contacts ==~query~==

This connection allows you to retrieve the desired list of contacts.

## Arguments

| Argument                           	| Description                                                                                                                                              	|
|------------------------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------	|
| `after` {==String==}              	| A cursor value to paginate through the results.                                                                                                         	|
| `first` {==Int==}                 	| The number of pages in a single query.                                                                                                                  	|
| `searchPhrase` {==String==}           | A search phrase to filter the organizations based on their names or other relevant attributes.                                                            |
| `sort` {==String==}               	| Specifies the sorting order of the returned organizations.                                                                                               	|

## Possible returns

| Possible return                                                       	| Description                           	|
|-----------------------------------------------------------------------	|---------------------------------------	|
| [`ContactConnection`](../Objects/ContactConnection.md)             	    | A connection to a list of contacts.  	    |

## Examples

=== "Query"
    ```json linenums="1"
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
=== "Return"
    ```json linenums="1"
    {
      "data": {
        "contacts": {
          "edges": [
            {
              "node": {
                "id": "123456",
                "name": "John Smith",
                "email": "john@example.com",
                "phone": "123-456-7890"
              }
            },
            {
              "node": {
                "id": "789012",
                "name": "John Doe",
                "email": "johndoe@example.com",
                "phone": "987-654-3210"
              }
            }
          ]
        }
      }
    }
    ```
