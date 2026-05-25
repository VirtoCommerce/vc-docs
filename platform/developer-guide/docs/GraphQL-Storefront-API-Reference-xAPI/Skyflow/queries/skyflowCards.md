# skyflowCards ==~query~==

This query allows you to retrieve stored Skyflow cards for a specific store.

## Arguments

| Argument              | Description                                 |
| --------------------- | ------------------------------------------- |
| `storeId` ==String!== | The Id of the store to retrieve cards from. |

## Possible returns

| Possible return                                                       | Description                                                      |
| --------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [`SkyflowCardResponseType`](../objects/SkyflowCardResponseType.md) | Defines the properties and fields associated with Skyflow cards. |


## Example

<div class="grid" markdown>

```json title="Query"
{
skyflowCards(storeId: "B2B-Store") {
    id
    cardType
    maskedNumber
    expirationMonth
    expirationYear
  }
}
```

```json title="Return"
{
  "data": {
    "skyflowCards": [
      {
        "id": "1",
        "cardType": "Visa",
        "maskedNumber": "**** **** **** 1234",
        "expirationMonth": "12",
        "expirationYear": "2026"
      }
    ]
  }
}
```

</div>