# PushHistoricalEvent ==~mutation~==

This mutation logs a historical event for a user, such as product views or purchases, in order to enhance the recommendation engine. The historical event helps track user interactions and optimize future recommendations.

## Fields

The `InputPushHistoricalEventType` is a type that represents the input object for pushing a historical event.

| Field                     | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `storeId` ==String==      | The ID of the store where the event occurred.                               |
| `productId` ==String==    | The ID of the product involved in the event.                               |
| `productIds` ==[String]== | A list of product IDs associated with the event, used for multi-product actions like bulk views or purchases. |
| `sessionId` ==String==    | The identifier of the user's session during which the event occurred.|
| `eventType` ==String==    | The type of event.                  |

## Possible returns

| Possible return                                                       | Description          	|
|-----------------------------------------------------------------------|---------------------	|
| `Boolean`                                                             | A boolean value indicating whether the event was successfully recorded. 	|


## Example

<div class="grid" markdown>

```json title="Mutation"
mutation pushHistoricalEvent($command: InputPushHistoricalEventType!) {
pushHistoricalEvent(command: $command)
}
```

```json title="Variables"
{
  "command": {
    "userId": "user-123",
    "eventType": "ProductViewed",
    "productId": "product-456",
    "eventDate": "2024-09-16T10:00:00Z"
  }
}
```

</div>