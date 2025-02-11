# activateBackInStockSubscription ==~mutation~==  

This mutation activates a back-in-stock subscription for a specific product in a store.  

## Arguments  

The `ActivateBackInStockSubscriptionCommandType!` provides the necessary input values to activate the subscription.  

| Argument         | Description                                      |  
|--------------|--------------------------------------------------|  
| `storeId` ==String!==   | The Id of the store where the subscription should be activated. |  
| `productId` ==String!== | The Id of the product for which the subscription should be activated. |  


## Possible returns  

| Possible return                                                    | Description                                                       |  
|--------------------------------------------------------------------|-------------------------------------------------------------------|  
| [`BackInStockSubscriptionType`](../Objects/BackInStockSubscriptionType.md) | The activated back-in-stock subscription details.                 |  

=== "Mutation"  
    ```json linenums="1"  
    mutation activateBackInStockSubscription($command: ActivateBackInStockSubscriptionCommandType!) {  
      activateBackInStockSubscription(command: $command) {  
        id  
        storeId  
        productId  
        isActive  
      }  
    }  
    ```  

=== "Variables"  
    ```json linenums="1"  
    {  
      "command": {  
        "storeId": "store123",  
        "productId": "product456"  
      }  
    }  
    ```  

