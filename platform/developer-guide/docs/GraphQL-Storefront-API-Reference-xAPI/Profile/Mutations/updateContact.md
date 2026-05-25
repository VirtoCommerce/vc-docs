# updateContact ==~mutation~==

This mutation updates a contact.

## Arguments

The `InputUpdateContactType!` represents the fields that can be updated for a contact.

| Field                                                                           | Description                                                                   |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `id`  ==String==                                                                | The Id of the contact.                                                        |
| `name`  ==String==                                                              | The name of the contact.                                                      |
| `memberType`  ==String==                                                        | The type of the contact member.                                               |
| `addresses` [ ==InputMemberAddressType== ](../Objects/InputMemberAddressType.md)| An array of `InputMemberAddressType` objects representing the addresses associated with the contact.  |
| `phones` [ ==String== ]                                                         | An array of phone numbers associated with the contact.                        |
| `emails` [ ==String== ]                                                         | An array of email addresses associated with the contact.                      |
| `groups` [ ==String== ]                                                         | An array of group names that the contact belongs to.                          |
| `dynamicProperties` [ ==InputDynamicPropertyValueType== ](../Objects/InputDynamicPropertyValueType.md)| The dynamic properties associated with the contact.     |
| `fullName`  ==String==                                                          | The full name of the contact.                                                 |
| `firstName`  ==String==                                                         | The first name of the contact.                                                |
| `lastName`  ==String==                                                          | The last name of the contact.                                                 |
| `middleName`  ==String==                                                        | The middle name of the contact.                                               |
| `salutation`  ==String==                                                        | The salutation or title for the contact.                                      |
| `photoUrl`  ==String==                                                          | The URL of the photo associated with the contact.                             |
| `timeZone`  ==String==                                                          | The time zone of the contact.                                                 |
| `defaultLanguage`  ==String==                                                   | The default language for the contact.                                         |
| `about`  ==String==                                                             | Additional information or description about the contact.                      |
| `organizations` [ ==String== ]                                                  | An array of organization names that the contact is associated with.           |


## Possible returns

| Possible return                                          	| Description                                                       	|
|---------------------------------------------------------	|--------------------------------------------------------------------	|
| [`ContactType`](../Objects/ContactType.md)                | A contact and various fields to describe the contact's information.  	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation updateContact($command: InputUpdateContactType!) {
  updateContact(command: $command) {
    fullName
    id
    lastName
    name
  }
}
```

```json title="Variables"
{
"command": {
  "id": "916abee5-1b4d-4f1f-80f2-8be0a55cf011",
  "name": "UserA",
  "memberType": "Contact",
  "addresses": [],
  "fullName": "UserA",
  "firstName": "UserA",
  "lastName": "UserA"
  }
}
```

</div>