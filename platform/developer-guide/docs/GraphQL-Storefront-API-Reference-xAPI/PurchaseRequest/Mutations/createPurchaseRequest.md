# createPurchaseRequest ==~mutation~==  

This mutation creates an empty purchase request for a user in a specific store.  

## Arguments  

The `InputChangePurchaseOrderNumber` represents the input object type used for creating a purchase request.

| Field                         | Description                                                        |
|-------------------------------|--------------------------------------------------------------------|
| `storeId` ==String!==         | The Id of the store where the purchase request will be created.    |
| `userId` ==String!==          | The Id of the user creating the purchase request.                  |
| `currencyCode` ==String!==    | The currency code for the purchase request.                  |
| `cultureName` ==String!==     | The culture or language associated with the purchase request.  |

## Possible returns  

| Possible return                                          	   | Description                                                 	      |
|--------------------------------------------------------------|----------------------------------------------------------------------|
| [`PurchaseRequestType`](../Objects/PurchaseRequestType.md)   | Defines the properties and fields associated with a purchase request.|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation createPurchaseRequest($storeId: String!, $userId: String!, $currencyCode: String!, $cultureName: String!) {  
    createPurchaseRequest(storeId: $storeId, userId: $userId, currencyCode: $currencyCode, cultureName: $cultureName) {  
        id  
        number  
    }  
}  
```

```json title="Variables"
{  
    "storeId": "3a67b3dc-9eae-432d-a17d-25ef86b28aa3",  
    "userId": "444d8de1-ff99-47ca-86f9-3756a9fd788c",  
    "currencyCode": "USD",  
    "cultureName": "en-US"  
}  
```

</div>