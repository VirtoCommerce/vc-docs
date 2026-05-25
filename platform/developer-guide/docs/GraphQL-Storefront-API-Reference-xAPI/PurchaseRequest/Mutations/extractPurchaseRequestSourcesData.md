# extractPurchaseRequestSourcesData ==~mutation~==  

This mutation extracts and saves data from purchase request sources.  

## Arguments  

The `InputExtractDataFromPurchaseRequestSourcesType!` represents the input object for extracting data from purchase request sources.  

| Field                        | Description                                                       |  
|------------------------------|-------------------------------------------------------------------|  
| `purchaseRequestId` ==String!==  | The ID of the purchase request from which data will be extracted.   |  

## Possible returns  

| Possible return                                              | Description                                                         |  
|--------------------------------------------------------------|---------------------------------------------------------------------|  
| [`PurchaseRequestType`](../Objects/PurchaseRequestType.md)   | Defines the properties and fields associated with a purchase request. |  


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation extractPurchaseRequestSourcesData($command: InputExtractPurchaseRequestSourcesDataType!) {  
  extractPurchaseRequestSourcesData(command: $command) {  
    id  
  }  
}  
```

```json title="Variables"
{  
  "command": {  
    "purchaseRequestId": "8a4f3656-0aa1-43b1-aafa-3545286d6f4b"  
  }  
}  
```

</div>