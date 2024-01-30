# lockOrganizationContact ==~mutation~==

This mutation locks an organization contact.

## Arguments

The `InputLockUnlockOrganizationContactType!` provides the necessary input values to lock or unlock an organization contact.

| Field                                                                                 | Description                                             |
|---------------------------------------------------------------------------------------|---------------------------------------------------------|
| `userId` {==String==}                                                                 | The Id of the user.                                     |

## Possible returns

| Possible return                                          	| Description                                                       	|
|---------------------------------------------------------	|--------------------------------------------------------------------	|
| [`ContactType`](../Objects/ContactType.md)                | A contact and various fields to describe the contact's information.  	|


=== "Mutation"
    ```json linenums="1"
    mutation lockContact($command: InputLockUnlockOrganizationContactType!){
      lockOrganizationContact(command: $command){
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command": {
        "userId":"5f807280-bb1a-42b2-9a96-ed107269ea06"
      }
    }
    ```
