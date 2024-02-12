# deleteFile ==~mutation~==

This mutation allows deleting a file.

## Arguments

The `DeleteFileCommandType!` represents the command to delete a file.

| Field                             | Description                                                 |
|-----------------------------------|-------------------------------------------------------------|
| `id` ==String!==                  | The ID of the file to be deleted.                           |


## Possible returns

| Possible return               | Description                                                 	|
|-------------------------------|------------------------------------------------------------	|
| `Boolean`                   	| Indicates the success or failure of the deletion operation.  	|


=== "Mutation"
    ```json linenums="1"
    mutation($command: InputAddQuoteAttachmentsType!) {
        addQuoteAttachments(command: $command)
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command": {
        "quoteId": "a73c6031-ab6a-4acc-9f16-466d287d7565",
        "urls": [
        "/api/files/699fa784949a40c1acd891f74b4223d9",
        "/api/files/4c25e506a637407782bda5a5480f26a2"
        ]
      }
    }
    ```