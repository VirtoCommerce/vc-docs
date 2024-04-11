# validatePassword ==~query~==

This connection is used to check the validity of a password.

## Arguments

| Field                   | Description                    |
|-------------------------|--------------------------------|
| `password` ==String==   | The password to be validated.  |


## Possible returns

| Possible return                          	                            | Description                           	  |
|---------------------------------------------------------------------	|------------------------------------------	|
| [`CustomIdentityResultType`](../Objects/CustomIdentityResultType.md) 	|  Outcome of identity-related operations.	|

## Examples

=== "Query"
    ```json linenums="1"
    query {
      validatePassword(password: "tew1WEEEEr") {
        succeeded
        errors {
          code
          parameter
          description
        }
      }
    }
    ```
=== "Return"
    ```json linenums="1"
    {
      "data": {
        "validatePassword": {
          "succeeded": true,
          "errors": []
        }
      }
    }
    ```
