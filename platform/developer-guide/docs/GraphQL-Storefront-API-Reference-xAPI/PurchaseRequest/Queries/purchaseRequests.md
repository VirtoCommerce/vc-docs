# purchaseRequests ==~query~==  

This query allows you to retrieve a list of purchase requests based on specific filters and sorting options.  

## Arguments  

| Argument            | Description                                                                                   |  
|---------------------|-----------------------------------------------------------------------------------------------|  
| `after` ==String==  | The cursor for pagination to retrieve records after the specified position.                   |  
| `first` ==Int==     | The number of purchase requests to retrieve.                                                  |  
| `keyword` ==String== | A search term to filter purchase requests by matching text in relevant fields.               |
| `sort` ==String==   | The sorting criteria. Example: `desc:createDate` for descending order by creation date.       |  
| `storeId` ==String==| The ID of the store to retrieve purchase requests from.                                       |  
| `customerId` ==String==| The Id of the customer to filter purchase requests.                                        |  

## Possible returns  

| Possible return                                              | Description                                                                            |  
|--------------------------------------------------------------|----------------------------------------------------------------------------------------|  
| [`PurchaseRequestConnection`](../Objects/PurchaseRequestConnection.md) | A list of purchase request objects matching the specified filters and sort criteria.   |  

## Examples  

=== "Query"  
    ```json linenums="1"
    {
      purchaseRequests(
        after: "10"
        first: 5
        sort: "desc:createDate"
        storeId: "B2B-store"
        customerId: "83a6c535-810a-4c67-8447-b1c324d615b6"
      ) {
        totalCount
        items {
          id
          ...
        }
      }
    }
    ```  

=== "Return"  
    ```json linenums="1"
    {
      "data": {
        "purchaseRequests": {
          "totalCount": 123,
          "items": [
            {
              "id": "7a7e080d-f0ff-4358-830a-839e07b75c3b",
              ...
            },
            {
              "id": "8b7e080d-f0ff-4358-830a-839e07b75c3c",
              ...
            }
          ]
        }
      }
    }
    ```  