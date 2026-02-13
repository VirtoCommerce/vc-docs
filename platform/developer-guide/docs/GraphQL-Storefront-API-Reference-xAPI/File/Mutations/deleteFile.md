# deleteFile ==~mutation~==

This mutation allows deleting a file.

## Arguments

The [DeleteFileCommandType!](../Objects/DeleteFileCommandType.md) represents the command to delete a file.

| Field                             | Description                                                 |
|-----------------------------------|-------------------------------------------------------------|
| `id` ==String!==                  | The ID of the file to be deleted.                           |


## Possible returns

| Possible return               | Description                                                 	|
|-------------------------------|------------------------------------------------------------	|
| `Boolean`                   	| Indicates the success or failure of the deletion operation.  	|

## Example

<div class="grid" markdown>

```json title="Mutation"
mutation DeleteFile($command: DeleteFileCommandType!) {
  deleteFile(command: $command)
}
```

```json title="Variables"
{
  "command": {
    "id": "file-12345"
  }
}
```

</div>