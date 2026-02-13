# deactivateBackInStockSubscription ==~mutation~==  

This mutation deactivates a back-in-stock subscription for a specific product in a store.  

## Arguments  

The `DeactivateBackInStockSubscriptionCommandType!` provides the necessary input values to deactivate the subscription.  

| Argument         | Description                                      |  
|-----------------|--------------------------------------------------|  
| `storeId` ==String!==   | The Id of the store where the subscription should be deactivated. |  
| `productId` ==String!== | The Id of the product for which the subscription should be deactivated. |  

## Possible returns  

| Possible return                                                    | Description                                                       |  
|--------------------------------------------------------------------|-------------------------------------------------------------------|  
| [`BackInStockSubscriptionType`](../Objects/BackInStockSubscriptionType.md) | The deactivated back-in-stock subscription details.               |  


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation deactivateBackInStockSubscription($command: DeactivateBackInStockSubscriptionCommandType!) {  
  deactivateBackInStockSubscription(command: $command) {  
    id  
    storeId  
    productId  
    isActive  
  }  
}  
```

```json title="Variables"
{  
  "command": {  
    "storeId": "store123",  
    "productId": "product456"  
  }  
}  
```

</div>