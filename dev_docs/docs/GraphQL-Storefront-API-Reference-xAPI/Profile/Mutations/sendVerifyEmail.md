# sendVerifyEmail ==~mutation~==

This mutation allows to send emails to complete verification.

## Arguments

The `InputSendVerifyEmailType` represents the input for sending a verification email.

| Field                     | Description                                                     |
|---------------------------|-----------------------------------------------------------------|
| `storeId` {==String!==}   | The Id of the store for which the verification email is sent.   |
| `languageCode` {==String==}| The language code for the email content.                       |
| `email` {==String==}      | The email address to which the verification email is sent.      |
| `userId` {==String==}     | The Id of the user.                                             |


## Possible returns

| Possible return       | Description                               |
|-----------------------|---------------------------------------    |
| `Boolean`             | Indicates the outcome of the operation. 	|


=== "Mutation"
    ```json linenums="1"
    mutation ($command: InputSendVerifyEmailType){​
      sendVerifyEmail(command: $command)​
    }​
    ```

=== "Variables"
    ```json linenums="1"
    "command": {​
      "userId": "4162ff51-c880-4e42-bc4b-4bfd120a0bdf",​
      "storeId": "B2B-store",​
      "languageCode": "EN-US"​
    }   ​
    ```
