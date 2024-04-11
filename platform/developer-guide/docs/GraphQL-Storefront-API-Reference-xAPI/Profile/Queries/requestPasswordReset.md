# requestPasswordReset  ==~query~==

This connection is used to initiate a password reset process for a user.

## Arguments

| Field                        | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| `loginOrEmail`  ==String!==  | The login or email of the user for whom the password reset is requested.    |
| `urlSuffix`  ==String==      | An optional URL suffix that can be appended to the password reset URL.      |


## Possible returns

| Possible return | Description                           	                                  |
|-----------------|--------------------------------------------------------------------------	|
| `Boolean`     	| Indicates whether the password reset request was successfully initiated.	|

## Examples

=== "Query"
    ```json linenums="1"
    query {
      requestPasswordReset(
        loginOrEmail: "User_1"
        urlSuffix: "reset-password/reset"
      )
    }
    ```
=== "Return"
    ```json linenums="1"
    {
      "data": {
        "requestPasswordReset": true
      }
    }
    ```

