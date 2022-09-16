# AddCartAddress

This mutation adds a new address to the cart or updates an existing one through `addressType`. `AddCartAddress` supports partial update, with all fields in `command.address` being optional. 

## Query

```json
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

## Variables

```json
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