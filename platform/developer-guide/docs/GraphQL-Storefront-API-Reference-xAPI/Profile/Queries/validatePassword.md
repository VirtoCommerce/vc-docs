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

## Example

<div class="grid" markdown>

```json title="Query"
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

```json title="Return"
{
  "data": {
    "validatePassword": {
      "succeeded": true,
      "errors": []
    }
  }
}
```

</div>