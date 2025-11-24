# PickupLocationType ==~object~==

This type represents a pickup location and contains all relevant information about its identity, status, contact details, availability, and address.

## Fields

| Field                           | Description                                                                     |
| ------------------------------- | ------------------------------------------------------------------------------- |
| `id` ==String!==                | The ID of the pickup location.                                   |
| `isActive` ==Boolean!==         | Indicates whether the pickup location is currently active.                      |
| `name` ==String!==              | The name of the pickup location.                                                |
| `description` ==String==        | A short description of the pickup location.                                     |
| `contactEmail` ==String==       | The email address associated with the pickup location.                          |
| `contactPhone` ==String==       | The phone number of the pickup location.                                        |
| `workingHours` ==String==       | The working hours for the pickup location.                                      |
| `deliveryDays` ==Int==          | The number of days until an order is ready for pickup.                          |
| `storageDays` ==Int==           | How long an order will be stored at this pickup point.                          |
| `geoLocation` ==String==        | Geographic coordinates of the pickup location. |
| `address` ==[PickupAddressType](pickupAddressType.md)== | The physical address and contact details for the pickup location.               |
