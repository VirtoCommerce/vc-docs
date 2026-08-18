# canLeaveFeedback ==~query~==  

This query checks if a user is eligible to leave feedback for a specific entity, such as a product or service.  

## Arguments  

| Argument          | Description                                                                   |  
|-------------------|-------------------------------------------------------------------------------|  
| `storeId` ==String!==     | The Id of the store associated with the entity.                       |  
| `entityId` ==String!==    | The Id of the entity to leave feedback for.                           |  
| `entityType` ==String!==  | The type of entity the feedback would be associated with.             |  

## Possible Returns  

| Possible Return  | Description                                |  
|------------------|--------------------------------------------|  
| `Boolean`        | Returns `true` if feedback can be left, otherwise `false`. |  

## Example

<div class="grid" markdown>

```json title="Query"
{  
  canLeaveFeedback(  
    storeId: "B2B-store",  
    entityId: "product-12345",  
    entityType: "Product"  
  )  
}  
```

```json title="Return"
{  
  "data": {  
    "canLeaveFeedback": true  
  }  
} 
```

</div>