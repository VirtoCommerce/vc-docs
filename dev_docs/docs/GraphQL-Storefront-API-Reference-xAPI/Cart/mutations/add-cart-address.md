# AddCartAddress ==~mutation~==

This mutation adds a new address to the cart or updates an existing one through `addressType`. `AddCartAddress` supports partial update, with all fields in `command.address` being optional. 

## Arguments

The `InputAddOrUpdateCartAddressType` represents the input object type used for adding or updating an address for a cart.

| Field                     | Description                                                       |
|---------------------------|-------------------------------------------------------------------|
| `cartId` {==String==}           | The ID of the cart to which the address will be added or updated.  |
| `storeId` {==String!==}        | The ID of the store associated with the cart.                      |
| `cartName` {==String==}         | The name of the cart.                                             |
| `userId` {==String==}           | The ID of the user who owns the cart.                              |
| `currencyCode` {==String==}     | The currency code for the cart.                                   |
| `cultureName` {==String==}      | The culture or language associated with the cart.                  |
| `cartType` {==String==}         | The type of the cart.                                             |
| `address` {==InputAddressType!==} | The address object containing the details of the address to add or update. |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation addOrUpdateCartAddress ($command: InputAddOrUpdateCartAddressType!) {
        addOrUpdateCartAddress (command: $command) {
            addresses {
                addressType
                city
                countryCode
                countryName
                email
                firstName
                id
                lastName
                line1
                line2
                middleName
                name
                organization
                phone
                postalCode
                regionId
                regionName
                zip
            }
        }
    }
    ```

=== "Variables"
    ```json linenums="1"
    "command": {
        "storeId": "Electronics",
        "cartName": "default",
        "userId": "b57d06db-1638-4d37-9734-fd01a9bc59aa",
        "cultureName": "en-US",
        "currencyCode": "USD",
        "cartType": "cart",
        "address": {
        "city": "City name",
        "countryCode": "CountryCode",
        "countryName": "Country name",
        "email": "example@email.com",
        "firstName": "recipient name",
        "middleName": "recipient name",
        "lastName": "recipient name",
        "line1": "example address line 1",
        "line2": "example address line 1",
        "organization": "Organizatoin name",
        "phone": "77777-77777",
        "postalCode": "12345",
        "regionId": "RegionCode",
        "regionName": "Region name",
        "zip": "123",
        "addressType": 3
        }
    }
    ```