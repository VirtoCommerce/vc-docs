# addPurchaseRequestSource ==~mutation~==  

This mutation adds a source (document URLs) to a purchase request.  

## Arguments  

The `InputAddPurchaseRequestSourceType!` represents the input object for adding a source to a purchase request.  

| Field                        | Description                                                  |  
|------------------------------|--------------------------------------------------------------|  
| `purchaseRequestId` ==String!==  | The Id of the purchase request to which the source is being added. |  
| `documentUrls` ==[String!]!==    | A list of document URLs to be attached as the source.              |  

## Possible returns  

| Possible return                                          | Description                                                         |  
|----------------------------------------------------------|---------------------------------------------------------------------|  
| [`PurchaseRequestType`](../Objects/PurchaseRequestType.md) | Defines the properties and fields associated with a purchase request. |  


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation addPurchaseRequestSource($command: InputAddPurchaseRequestSource!) {  
    addPurchaseRequestSource(command: $command) {  
        id  
    }  
}  
```

```json title="Variables"
{  
    "command": {  
    "purchaseRequestId": "8a4f3656-0aa1-43b1-aafa-3545286d6f4b",  
    "documentUrls": ["/api/files/5df05423-511d-433f-bbe3-5e75ec886e01"]  
    }  
}  
```

</div>