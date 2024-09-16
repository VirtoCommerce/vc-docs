# PushHistoricalEvent ==~mutation~==

This mutation logs a historical event for a user, such as product views or purchases, in order to enhance the recommendation engine. The historical event helps track user interactions and optimize future recommendations.

## Fields

The `InputPushHistoricalEventType` is a type that represents the input object for pushing a historical event.

| Field                                                                                   | Description                                                       |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| `command` [ ==InputPushHistoricalEventType!== ](../object/InputPushHistoricalEventType.md)  | The details of the historical event to be recorded.               |

## Possible returns

| Possible return                                                       | Description          	|
|-----------------------------------------------------------------------|---------------------	|
| `Boolean`                                                             | A boolean value indicating whether the event was successfully recorded. 	|

## Example

=== "Mutation"
    ```json linenums="1"
    mutation pushHistoricalEvent($command: InputPushHistoricalEventType!) {
    pushHistoricalEvent(command: $command)
    }
    ```

=== "Variables"
    ```json linenums="1"
    {
    "command": {
        "userId": "user-123",
        "eventType": "ProductViewed",
        "productId": "product-456",
        "eventDate": "2024-09-16T10:00:00Z"
    }
    }
    ```
