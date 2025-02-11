# backInStockSubscriptions ==~query~==  

This query retrieves a list of back-in-stock subscriptions based on specified filters, such as store, product, status, and search keywords.  

## Arguments  

| Argument                    | Description                                                                 |  
|-----------------------------|-----------------------------------------------------------------------------|  
| `after` ==String!==         | Returns edges after the specified cursor for pagination.                    |  
| `first` ==Int!==            | Specifies the maximum number of edges to return. If `after` is provided, it returns results after the cursor; otherwise, it returns the first `n` edges. |  
| `keyword` ==String!==       | Filters subscriptions by a search keyword.                                  |  
| `sort` ==String!==          | Defines sorting order of the results.                                       |  
| `storeId` ==String!==       | Returns subscriptions associated with a specific store.                     |  
| `productIds` ==[String]!==  | Filters subscriptions by specific product IDs.                              |  
| `isActive` ==Boolean!==     | Filters results based on subscription status (active or inactive).          |  

## Possible returns  

| Possible return                                                        | Description                                                                            |  
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------|  
| [`BackInStockSubscriptionConnection`](../Objects/BackInStockSubscriptionConnection.md) | A paginated list of back-in-stock subscriptions, including customer details and product information. |  

## Examples  

=== "Query"  
    ```json linenums="1"  
    {  
      backInStockSubscriptions(first: 10, storeId: "store123", isActive: true) {  
        edges {  
          node {  
            id  
            productId  
            storeId  
            customerEmail  
            isActive  
          }  
        }  
      }  
    }  
    ```  

=== "Return"  
    ```json linenums="1"  
    {  
      "data": {  
        "backInStockSubscriptions": {  
          "edges": [  
            {  
              "node": {  
                "id": "sub123",  
                "productId": "prod456",  
                "storeId": "store123",  
                "customerEmail": "customer@example.com",  
                "isActive": true  
              }  
            }  
          ]  
        }  
      }  
    }  
    ```  

