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

## Examples

=== "Query"

    ```json linenums="1"
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

=== "Return"

    ```json linenums="1"
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
