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
      user(id: "78b0208a-bb52-4a33-9250-583d63aa1f77") {
        accessFailedCount
        contact {
          id
          name
        }
        createdDate
        email
        isAdministrator
        passwordExpiryInDays
        passwordExpired
        userName
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
            "id": "cb0a5340-f9fb-4f49-bd62-9d03518868ff",
            "name": "b2b admin"
          },
          "createdDate": "2022-04-18T13:18:33.6009031Z",
          "email": "b2badmin@test.com",
          "isAdministrator": false,
          "passwordExpiryInDays": 83,
          "passwordExpired": false,
          "userName": "b2badmin"
        }
      }
    }
    ```
