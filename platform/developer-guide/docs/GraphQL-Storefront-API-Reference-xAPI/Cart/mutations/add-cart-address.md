# addCartAddress ==~mutation~==

This mutation adds a new address to the cart or updates an existing one through `addressType`. `AddCartAddress` supports partial update, with all fields in `command.address` being optional. 

## Arguments

The `InputAddOrUpdateCartAddressType!` represents the input object type used for adding or updating an address for a cart.

| Field                         | Description                                                       |
|-------------------------------|-------------------------------------------------------------------|
| `cartId` ==String==           | The Id of the cart to which the address will be added or updated. |
| `storeId` ==String!==         | The Id of the store associated with the cart.                     |
| `cartName` ==String==         | The name of the cart.                                             |
| `userId` ==String==           | The Id of the user who owns the cart.                             |
| `currencyCode` ==String==     | The currency code for the cart.                                   |
| `cultureName` ==String==      | The culture or language associated with the cart.                 |
| `cartType` ==String==         | The type of the cart.                                             |
| `address` ==InputAddressType!== | The address object containing the details of the address to add or update. |

## Possible returns

| Possible return                                          	| Description                                                 	|
|---------------------------------------------------------	|------------------------------------------------------------	|
| [`CartType`](../objects/cart-type.md)                   	|  The properties and fields associated with a shopping cart.  	|


=== "Mutation"
    ```json linenums="1"
    mutation($command: InputAddOrUpdateCartAddressType!) {
      addCartAddress(command: $command) {
        id
        addresses {
          addressType
          city
          countryCode
          countryName
          email
          firstName
          lastName
          line1
          line2
          name
          organization
          phone
          postalCode
          regionId
          regionName
        }
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    "command": {
      "storeId": "B2B-store",
      "cartName": "default",
      "userId": "c50e5237-8a4c-41fe-b878-8e5a72390a08",
      "currencyCode": "USD",
      "cultureName": "en-US",
      "cartType": "",
      "cartId": "e6a7d5af-6378-44a6-b645-af9ecf702c05",
      "address": {
        "city": "city name test",
        "countryCode": "123",
        "countryName": "country name",
        "email": "email@email",
        "firstName": "test first name",
        "lastName": "test last name",
        "line1": "line1",
        "line2": "line2",
        "name": "address name",
        "organization": "organization",
        "phone": "777-777-7777",
        "postalCode": "13456",
        "regionId": "region1",
        "regionName": "region name",
        "addressType": 1
      }
    }
    ```