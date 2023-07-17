# User ==~query~==

This connection allows you to get the user by several arguments.

## Arguments

| Argument                           	| Description                                                      	|
|------------------------------------	|-----------------------------------------------------------------	|
| `id` {==String==}              	    | The Id of the user.                                              	|
| `userName` {==String==}             | The nsme of the user.                                            	|
| `email` {==String==}            	  | The email of the user.                                           	|
| `loginProvider` {==String==}        | The login provider associated with the user.                    	|
| `providerKey` {==String==}          | The provider key associated with the user's login provider.      	|


## Possible returns

| Possible return                          	| Description                           	|
|------------------------------------------	|---------------------------------------	|
| [`UserType`](../Objects/UserType.md)     	|  The user's information and attributes.	|

## Examples

=== "Query"
    ```json linenums="1"
    {
      user(id: "9b605a3096ba4cc8bc0b8d80c397c59f") {
        accessFailedCount
        contact {
          id
          name
        }
        createdDate
        email
        isAdministrator
        passwordHash
      }
    }
    ```
=== "Return"
    ```json linenums="1"
    {
      "data": {
        "user": {
          "accessFailedCount": 0,
          "contact": {
            "id": "9b605a3096ba4cc8bc0b8d80c397c59f",
            "name": "John Doe"
          },
          "createdDate": "2022-05-15T12:30:00Z",
          "email": "johndoe@example.com",
          "isAdministrator": true,
          "passwordHash": "**********"
        }
      }
    }
    ```
