# updateMemberAddresses ==~mutation~==

This mutation updates member addresses.

## Arguments

The `InputUpdateMemberAddressType!` represents the input values for updating member addresses.

| Field                                                                              | Description                                                    |
|------------------------------------------------------------------------------------|----------------------------------------------------------------|
| `memberId`  ==String!==                                                            | The Id of the member for whom the addresses are being updated. |
| `addresses` [ ==[InputMemberAddressType]== ](../Objects/InputMemberAddressType.md) | An array of updated member addresses.                          |


## Possible returns

| Possible return                                          	| Description                                                       	|
|---------------------------------------------------------	|--------------------------------------------------------------------	|
| [`MemberType`](../Objects/MemberType.md)                  |  The updated member object with the updated addresses.             	|


=== "Mutation"
    ```json linenums="1"
    mutation updateMemberAddresses($command: InputUpdateMemberAddressType!) {
      updateMemberAddresses(command: $command) {
        addresses {
          items {
            id
            key
            city
            countryCode
            countryName
            email
            firstName
            lastName
            line1
            line2
            middleName
            name
            phone
            postalCode
            regionId
            regionName
            zip
          }
        }
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command": {
        "memberId": "820c58c5-b518-454b-aefd-2fc4616bd25e",
        "addresses": {
          "addressType": 1,
          "city": "Thousand oaks 25",
          "countryCode": "USA",
          "countryName": "United States",
          "email": "alivemenone@gmail.com",
          "firstName": "Steven",
          "key": "3b6fddca-6024-4df9-9e2a-5f13329202cb",
          "lastName": "Woodward",
          "line1": "1888, colgate dr",
          "name": "Steven Woodward  1888, colgate dr Thousand oaks California 91360 United States",
          "postalCode": "91360",
          "regionId": "CA",
          "regionName": "California"
        }
      }
    }
    ```
