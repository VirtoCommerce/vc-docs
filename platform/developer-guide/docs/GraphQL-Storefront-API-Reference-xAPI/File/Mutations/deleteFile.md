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

```graphql title="Mutation"
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

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../Objects/DeleteFileCommandType">← DeleteFileCommandType</a>
    <a href="../../../xFrontend/overview">xFrontend module overview →</a>
</div>
