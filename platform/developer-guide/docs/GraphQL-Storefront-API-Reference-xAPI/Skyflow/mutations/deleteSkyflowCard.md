# deleteSkyflowCard ==~mutation~==

This mutation deletes a stored Skyflow card by its identifier.

## Arguments

The `DeleteSkyflowCardCommandType!` represents the input object type used for deleting a Skyflow card.

| Field                   | Description                                          |
| ----------------------- | ---------------------------------------------------- |
| `skyflowId` ==String!== | The unique identifier of the Skyflow card to delete. |
| `storeId` ==String!==   | The Id of the store associated with the card.        |

## Possible returns

| Possible return | Description                                          |
| --------------- | ---------------------------------------------------- |
| `Boolean`       | Indicates whether the card was successfully deleted. |


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation($command: DeleteSkyflowCardCommandType!) {
  deleteSkyflowCard(command: $command)
}
```

```json title="Variables"
{
  "command": {
    "skyflowId": "12345",
    "storeId": "B2B-Store"
  }
}
```

</div>