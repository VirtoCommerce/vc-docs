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


## Example

<div class="grid" markdown>

```json title="Query"
query {
  checkUsernameUniqueness(username: "john_doe")
}
```

```json title="Return"
{
  "data": {
    "checkUsernameUniqueness": true
  }
}
```

</div>