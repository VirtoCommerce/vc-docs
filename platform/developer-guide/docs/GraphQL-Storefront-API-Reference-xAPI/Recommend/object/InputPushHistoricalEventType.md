# InputPushHistoricalEventType ==~object~==

This type defines the structure of the input object for the `pushHistoricalEvent` mutation, which records a historical event for a user.

## Fields

| Field               | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `storeId` ==String== | The ID of the store where the event occurred.                               |
| `productId` ==String== | The ID of the product involved in the event.                               |
| `eventType` ==String== | The type of event.                  |