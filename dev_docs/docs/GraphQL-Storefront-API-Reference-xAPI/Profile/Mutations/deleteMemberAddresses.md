# deleteMemberAddress ==~mutation~==

This mutation deletes member addresses.

## Arguments

The `InputDeleteMemberAddressType!` represents the input fields required to delete member addresses.

| Field                                                                                | Description                                             |
|--------------------------------------------------------------------------------------|---------------------------------------------------------|
| `memberId` {==String!==}                                                             | The Id of the member whose addresses are to be deleted. |
| `addresses` [{==[InputMemberAddressType]!==}](../Objects/InputMemberAddressType.md)  | An array of addresses to be deleted.                    |


## Possible returns

| Possible return                                         | Description                                                       	         |
|-------------------------------------------------------- |---------------------------------------------------------------------------	 |
| [`MemberType`](../Objects/MemberType.md)                |  The member object with the deleted addresses.                               |


=== "Mutation"
    ```json linenums="1"
    mutation deleteMemberAddresses ($command: InputDeleteMemberAddressType!) {
    deleteMemberAddresses (command: $command) {
    id
        name
        addresses
        {
        items{
        id
        }}
    }
        }
    ```

=== "Variables"
    ```json linenums="1"
    {
    "command": {
        "memberId": "393ceb5d-125c-479f-b993-81e2b9679dea",
        "addresses": [
        {
            "key": "0afd4d27-488c-487e-adea-01b818f4ee8e",
            "city": "third",
            "countryCode": "AFG",
            "countryName": "Islamic Republic of Afghanistan",
            "email": "",
            "firstName": "third",
            "lastName": "second",
            "line1": "third",
            "name": "ALB, first, first, first",
            "postalCode": "third",
            "regionName": "third"
        }
        ]
    }
    }
    ```
