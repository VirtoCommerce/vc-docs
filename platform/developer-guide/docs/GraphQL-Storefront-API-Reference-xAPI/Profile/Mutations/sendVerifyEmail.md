# sendVerifyEmail ==~mutation~==

This mutation allows to send emails to complete verification.

## Arguments

The `InputSendVerifyEmailType` represents the input for sending a verification email.

| Field                     | Description                                                     |
|---------------------------|-----------------------------------------------------------------|
| `storeId`  ==String!==    | The Id of the store for which the verification email is sent.   |
| `languageCode`  ==String== | The language code for the email content.                       |
| `email`  ==String==       | The email address to which the verification email is sent.      |
| `userId`  ==String==      | The Id of the user.                                             |


## Possible returns

| Possible return       | Description                               |
|-----------------------|---------------------------------------    |
| `Boolean`             | Indicates the outcome of the operation. 	|


## Example

<div class="grid" markdown>

```graphql title="Mutation"
mutation ($command: InputSendVerifyEmailType){​
  sendVerifyEmail(command: $command)​
}​
```

```json title="Variables"
"command": {​
  "userId": "4162ff51-c880-4e42-bc4b-4bfd120a0bdf",​
  "storeId": "B2B-store",​
  "languageCode": "EN-US"​
}   ​
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../confirmEmail">← ConfirmEmail mutation</a>
    <a href="../createUser">CreateUser mutation →</a>
</div>
