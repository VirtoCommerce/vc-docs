# checkEmailUniqueness ==~query~==

This query is used to check whether a given email address is unique in the system.

## Arguments

| Field           | Description                          |
|-----------------|--------------------------------------|
| `email` ==String!== | The email address to be validated. |

## Possible returns

| Possible return | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `Boolean`       | Returns `true` if the email is unique and available, `false` otherwise.    |


## Example

<div class="grid" markdown>

```json title="Query"
query {
  checkEmailUniqueness(email: "user@example.com")
}
```

```json title="Return"
{
  "data": {
    "checkEmailUniqueness": true
  }
}
```

</div>