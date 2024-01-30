# OrderShipmentItemType ==~object~==

The `OrderShipmentItemType` represents a specific item included in a shipment for an order.

## Field

| Field                                                         | Description                                                |
|---------------------------------------------------------------|------------------------------------------------------------|
| `id` {==String!==}                                            | The Id of the shipment item.                               |
| `lineItemId` {==String!==}                                    | The Id of the associated line item in the order.           |
| `lineItem` [{==OrderLineItemType==}](order-line-item-type.md) | The details of the associated line item in the order.      |
| `barCode` {==String==}                                        | The barcode associated with the shipment item.             |
| `quantity` {==Int!==}                                         | The quantity of this specific item included in the shipment.|
| `outerId` {==String==}                                        | The external Id for the shipment item.                      |

