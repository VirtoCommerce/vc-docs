# checkUsernameUniqueness ==~query~==

This query is used to check whether a given username is unique in the system.

## Arguments

| Field                  | Description                          |
|------------------------|--------------------------------------|
| `username` ==String!== | The username to be validated.        |

## Possible returns

| Possible return | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `Boolean`       | Returns `true` if the username is unique and available, `false` otherwise.  |

## Examples

=== "Query"
    ```json linenums="1"
    query {
      checkUsernameUniqueness(username: "john_doe")
    }
    ```
=== "Return"
    ```json linenums="1"
    {
      "data": {
        "checkUsernameUniqueness": true
      }
    }
    ```
