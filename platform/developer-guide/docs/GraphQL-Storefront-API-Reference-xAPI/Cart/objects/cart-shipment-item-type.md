# CartShipmentItemType ==~object~==

The `CartShipmentItemType` is used to define the properties of an item within a cart shipment.

## Fields

| Field                                              | Description                                                                 |
|----------------------------------------------------|-----------------------------------------------------------------------------|
| `quantity` ==Int==                              | The quantity of the shipment item.                                           |
| `lineItem` [==LineItemType==](line-item-type.md) | The associated line item in the cart, specifying the product and its details. |
