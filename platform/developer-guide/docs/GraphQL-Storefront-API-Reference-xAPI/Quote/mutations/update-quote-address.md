# updateQuoteAddresses ==~mutation~==

This mutation updates a quote request address.

## Fields

The `UpdateQuoteAddressesCommandType!` is a type that represents a command for updating quote request addresses. 

| Field                                                                             | Description                                                   |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------|
| `quoteId` {==String!==}                                                           | The Id of the quote to be updated.                            |
| `addresses` [{==InputQuoteAddressType!==}](../objects/InputQuoteAddressType.md)   | An array of updated address information for the quote request.|

## Possible returns

| Possible return                                     | Description          	          |
|-----------------------------------------------------|--------------------------------	|
| [`QuoteType`](../objects/QuoteType.md)           	  |  Information about the order.  	|


=== "Mutation"
    ```json linenums="1"
    mutation UpdateQuoteAddresses($command: UpdateQuoteAddressesCommandType!) {
      updateQuoteAddresses(command: $command) {
        id
        addresses {
          name
          id
          countryCode
          addressType
          city
        }
      }
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
      "command": {
        "quoteId": "893f7cd7-75eb-4b16-9fbb-e1e3b9053f16",
        "addresses": [
          {
            "name": "SHN, city1, address 1",
            "organization": "",
            "firstName": "Test 13378",
            "lastName": "Test 13378",
            "line1": "address 1",
            "line2": "address2",
            "city": "city1",
            "countryCode": "SHN",
            "countryName": "Saint Helena, Ascension and Tristan da Cunha",
            "regionId": "",
            "regionName": null,
            "postalCode": "02558",
            "phone": "",
            "email": "tzykin.alexandr@gmail.com",
            "addressType": 2
          },
          {
            "name": "SHN, city1, address 1",
            "organization": "",
            "firstName": "Test 13378",
            "lastName": "Test 13378",
            "line1": "address 1",
            "line2": "address2",
            "city": "city1",
            "countryCode": "SHN",
            "countryName": "Saint Helena, Ascension and Tristan da Cunha",
            "regionId": "",
            "regionName": null,
            "postalCode": "02558",
            "phone": "",
            "email": "tzykin.alexandr@gmail.com",
            "addressType": 1
          }
        ]
      }
    }
    ```