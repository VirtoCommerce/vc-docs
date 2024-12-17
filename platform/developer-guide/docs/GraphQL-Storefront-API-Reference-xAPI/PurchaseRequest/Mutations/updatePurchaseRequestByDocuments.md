# updatePurchaseRequestByDocuments ==~mutation~==  

This mutation updates a purchase request using the provided document URLs.  

## Arguments  

The `InputUpdatePurchaseRequestByDocumentsType!` represents the input object for updating a purchase request with documents.  

| Field                        | Description                                                       |  
|------------------------------|-------------------------------------------------------------------|  
| `purchaseRequestId` ==String!==  | The Id of the purchase request to be updated.                     |  
| `documentUrls` ==[String!]!==    | A list of document URLs used to update the purchase request.       |  

## Possible returns  

| Possible return                                              | Description                                                         |  
|--------------------------------------------------------------|---------------------------------------------------------------------|  
| [`PurchaseRequestType`](../Objects/PurchaseRequestType.md)   | Defines the properties and fields associated with a purchase request.  |  


=== "Mutation"  
    ```json linenums="1"  
    mutation updatePurchaseRequestByDocuments($command: InputUpdatePurchaseRequestByDocumentsType!) {  
      updatePurchaseRequestByDocuments(command: $command) {  
        id  
      }  
    }  
    ```  

=== "Variables"  
    ```json linenums="1"  
    {  
      "command": {  
        "purchaseRequestId": "",  
        "documentUrls": []  
      }  
    }  
    ```  