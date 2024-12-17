# postProcessPurchaseRequestSources ==~mutation~==  

This mutation performs post-processing actions on extracted purchase request source data, such as creating line items.  

## Arguments  

The `InputPostProcessPurchaseRequestSourcesType!` represents the input object for post-processing purchase request sources.  

| Field                        | Description                                                       |  
|------------------------------|-------------------------------------------------------------------|  
| `purchaseRequestId` ==String!==  | The Id of the purchase request for which post-processing is performed. |  

## Possible returns  

| Possible return                                              | Description                                                         |  
|--------------------------------------------------------------|---------------------------------------------------------------------|  
| [`PurchaseRequestType`](../Objects/PurchaseRequestType.md)   | Defines the properties and fields associated with a purchase request. |  


=== "Mutation"  
    ```json linenums="1"  
    mutation postProcessPurchaseRequestSources($command: InputPostProcessPurchaseRequestSourcesType!) {  
      postProcessPurchaseRequestSources(command: $command) {  
        id  
      }  
    }  
    ```  

=== "Variables"  
    ```json linenums="1"  
    {  
      "command": {  
        "purchaseRequestId": "8a4f3656-0aa1-43b1-aafa-3545286d6f4b"  
      }  
    }  
    ```