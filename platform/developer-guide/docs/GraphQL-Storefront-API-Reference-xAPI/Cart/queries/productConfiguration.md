# productConfiguration ==~query~==  

This query allows you to retrieve configuration options for a specific configurable product. It calculates all fields based on the parameters being sent.  

## Arguments  

| Argument                   | Description                                                          |  
|----------------------------|----------------------------------------------------------------------|  
| `configurableProductId` ==String!== | The Id of the configurable product.                         |  
| `storeId` ==String!==               | The Id of the store where the product configurations apply. |  
| `userId` ==String==                 | The current user Id.                                        |  
| `cultureName` ==String==            | A language to retrieve data in.                             |  
| `currencyCode` ==String==           | A standardized code for a specific currency.                |  

## Possible return  

| Possible return                                                   | Description                                                   |  
|-------------------------------------------------------------------|---------------------------------------------------------------|  
| [`ConfigurationQueryResponseType`](../objects/ConfigurationQueryResponseType.md) | The response type containing configuration options for the product. |  

## Examples  

=== "Query"  
    ```json linenums="1"
    {
      productConfiguration (
        configurableProductId: "d733871c-f763-44b2-99c9-5f55edf28c16"
        storeId:"Electronics"
        cultureName: "en-US"
        currencyCode: "USD"
      ) {
          configurationSections {
          id
          type
          name
          description
          isRequired
          options {
            quantity
            extendedPrice {
              amount
            }
            product {
              id
              name
              properties {
                name
                value
              }
            }
          }
        }
      }
    }
    ```  

=== "Return"  
    ```json linenums="1"
    {
      "data": {
        "productConfiguration": {
          "configurationSections": [
            {
              "id": "5b9f20f2-fd30-4b74-a47e-fbb3378ce947",
              "name": "Pillows",
              "options": [
                {
                  "id": "fd45b6ca-2b60-4de2-9c93-249c8eec9f0c",
                  "quantity": 2,
                  "listPrice": { "amount": 30.00 },
                  "salePrice": { "amount": 30.00 },
                  "extendedPrice": { "amount": 60.00 },
                  "product": {
                    "name": "Pillow 50X60",
                    "id": "7de77e67-efab-41c9-a879-6ee466d2e7a7",
                    "code": "MZY-86395030"
                  }
                }
              ]
            },
           ...
          ]
        }
      }
    }
    ```