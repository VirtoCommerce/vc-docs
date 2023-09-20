# deleteContact ==~mutation~==

This mutation deletes a contact.

## Arguments

The `InputDeleteContactType!` represents the input object for deleting a contact.

| Field                                                                                 | Description                                             |
|---------------------------------------------------------------------------------------|---------------------------------------------------------|
| `contactId` {==String!==}                                                             | The Id of the contact.                                  |


## Possible returns

| Possible return         | Description                                                 |
|----------------------	  |-------------------------------------------------------------|
| `Boolean`               | Indicates the success or failure of the deletion operation. |

=== "Mutation"
    ```json linenums="1"
    mutation($command: InputDeleteContactType!){
      deleteContact(command: $command)
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command": {
        "contactId": "550e9b14-ddde-46fe-bc28-0afec83ade96"
      }
    }
    ```
