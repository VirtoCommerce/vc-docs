# createPurchaseRequestFromDocuments ==~mutation~==  

This mutation creates a purchase request based on the provided document URLs.  

## Arguments  

The `InputCreatePurchaseRequestFromDocumentsType!` represents the input object for creating a purchase request from documents.  

| Field                        | Description                                                          |  
|------------------------------|----------------------------------------------------------------------|  
| `documentUrls` ==[String!]!==  | A list of document URLs used to create the purchase request.       |  
| `storeId` ==String!==          | The Id of the store where the purchase request is created.         |  
| `userId` ==String!==           | The Id of the user creating the purchase request.                  |  
| `currencyCode` ==String!==     | The currency code for the purchase request.                        |  
| `cultureName` ==String!==      | The language to retreive data in.                                  |  

## Possible returns  

| Possible return                                              | Description                                                         |  
|--------------------------------------------------------------|---------------------------------------------------------------------|  
| [`PurchaseRequestType`](../Objects/PurchaseRequestType.md)   | Defines the properties and fields associated with a purchase request.      |  


=== "Mutation"  
    ```json linenums="1"  
    mutation createPurchaseRequestFromDocuments($command: InputCreatePurchaseRequestFromDocumentsType!) {  
      createPurchaseRequestFromDocuments(command: $command) {  
        id  
      }  
    }  
    ```  

=== "Variables"  
    ```json linenums="1"  
    {  
      "command": {  
        "storeId": "3a67b3dc-9eae-432d-a17d-25ef86b28aa3",  
        "userId": "444d8de1-ff99-47ca-86f9-3756a9fd788c",  
        "currencyCode": "USD",  
        "cultureName": "en-US",  
        "documentUrls": ["/api/files/5df05423-511d-433f-bbe3-5e75ec886e01"]  
      }  
    }  
    ```