# OderShipmentPackageType ==~object~==

The `OrderShipmentPackageType` represents a package used for shipping items in an order.

## Fields

| Field                                                                 | Description                                           |
|-----------------------------------------------------------------------|-------------------------------------------------------|
| `id`  ==String!==                                                     | The Id of the shipment package.                       |
| `barCode`  ==String==                                                 | The barcode associated with the shipment package.     |
| `packageType`  ==String==                                             | The type of the package.                              |
| `weightUnit`  ==String!==                                             | The unit of weight used for the package.              |
| `weight`  ==Decimal==                                                 | The weight of the package.                            |
| `measureUnit`  ==String!==                                            | The unit of measurement used for package dimensions.  |
| `height`  ==Decimal==                                                 | The height of the package.                            |
| `length`  ==Decimal==                                                 | The length of the package.                            |
| `width`  ==Decimal==                                                  | The width of the package.                             |
| `items` [ ==[OrderShipmentItemType]== ](order-shipment-item-type.md)  | Shipment items included in the package.               |

