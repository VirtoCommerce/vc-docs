# PickupLocationType ==~object~==

This type represents a pickup location where customers can collect their orders. It contains identifying information, contact details, working hours, and physical address.

## Fields

| Field                                                   | Description                                                                |
| ------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id` ==String!==                                        | The unique identifier of the pickup location.                              |
| `isActive` ==Boolean!==                                 | Indicates whether the pickup location is currently active.                 |
| `name` ==String!==                                      | The display name of the pickup location.                                   |
| `description` ==String==                                | A brief description of the pickup location.                                |
| `contactEmail` ==String==                               | The email address for contacting the pickup location.                      |
| `contactPhone` ==String==                               | The phone number for contacting the pickup location.                       |
| `workingHours` ==String==                               | The working hours of the pickup location.                                  |
| `geoLocation` ==String==                                | The geographic coordinates (e.g., latitude and longitude) of the location. |
| `address` ==[PickupAddressType](PickupAddressType.md)== | The physical address of the pickup location.                               |

