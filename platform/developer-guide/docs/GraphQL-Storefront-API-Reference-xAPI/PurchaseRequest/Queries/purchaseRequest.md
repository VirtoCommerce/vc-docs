# purchaseRequest ==~query~==  

This query allows you to retrieve information about a purchase request.  

## Arguments  

| Argument                        | Description                                                                            |  
|---------------------------------|----------------------------------------------------------------------------------------|  
| `purchaseRequestId` ==String!== | The unique Id of the purchase request.                                                 |  

## Possible returns  

| Possible return                                        | Description                                                                          |  
|--------------------------------------------------------|--------------------------------------------------------------------------------------|  
| [`PurchaseRequestType`](../Objects/PurchaseRequestType.md) | Defines the properties and fields associated with a purchase request.                |  

## Example

<div class="grid" markdown>

```json title="Query"
{
  purchaseRequest(
    purchaseRequestId: "7a7e080d-f0ff-4358-830a-839e07b75c3b"
  ) {
      id
      createdDate
      createdBy
      modifiedDate
      modifiedBy
      number
      storeId
      customerId
      cartId
      quoteId
      sources {
        name
        url
        contentType
        size
    }
  }
}
```

```json title="Return"
{
  "data": {
    "purchaseRequest": {
      "id": "7a7e080d-f0ff-4358-830a-839e07b75c3b",
      "createdDate": "2024-01-15T12:34:56.000Z",
      "createdBy": "user123",
      "modifiedDate": "2024-01-16T14:56:22.000Z",
      "modifiedBy": "admin456",
      "number": "PR-20240115-001",
      "storeId": "MainStore",
      "customerId": "customer789",
      "cartId": "cart987",
      "quoteId": "quote654",
      "sources": [
        {
          "name": "example-file.png",
          "url": "https://example.com/files/example-file.png",
          "contentType": "image/png",
          "size": 123456
        }
      ]
    }
  }
}
```

</div>