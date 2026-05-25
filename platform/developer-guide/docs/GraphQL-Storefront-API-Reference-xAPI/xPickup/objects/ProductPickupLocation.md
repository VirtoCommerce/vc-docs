# ProductPickupLocation ==~object~==

This type represents a pickup location for a specific product, including its availability, contact details, address, and operational information.

## Fields

| Field                                                | Description                                                                                  |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `id` ==String!==                                     | The unique identifier of the product pickup location.                                        |
| `isActive` ==Boolean!==                              | Indicates whether the pickup location is currently active.                                   |
| `name` ==String!==                                   | The name of the pickup location.                                                             |
| `description` ==String==                             | A short description of the pickup location.                                                  |
| `contactEmail` ==String==                            | The email address associated with the pickup location.                                       |
| `contactPhone` ==String==                            | The phone number of the pickup location.                                                     |
| `workingHours` ==String==                            | The working hours for the pickup location.                                                   |
| `deliveryDays` ==Int==                               | The number of days until the product is ready for pickup.                                    |
| `storageDays` ==Int==                                | How long an order will be stored at this pickup point.                                       |
| `geoLocation` ==String==                             | Geographic coordinates of the pickup location.              |
| `address` ==[PickupLocationAddressType](PickupLocationAddressType.md)==              | The physical address and contact details for the pickup location.  |
| `availabilityType` ==[ProductPickupAvailabilityType](ProductPickupAvailabilityType.md)== | Indicates the availability status of the product at this location. |
| `availabilityNote` ==String==                        | Additional notes regarding the product’s availability.                                       |
| `availableQuantity` ==Long==                         | The number of units available for pickup at this location.                                   |
