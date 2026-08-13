# salesRepCustomer

This query returns a single customer information card for an organization the rep serves.

## Arguments

| Argument | Description |
|----------|-------------|
| `organizationId`  ==String== | The Id of the customer organization. |

## Possible returns

| Possible return | Description |
|-----------------|-------------|
| Customer card | The organization's `organizationId`, `organizationName`, `accountType`, `iconUrl`, `phone`, a structured `address`, and the `primaryContact` (`fullName`, `emails`, `phones`). |

## Example

```graphql title="Query"
{
  salesRepCustomer(organizationId: "7b8c...") {
    organizationId
    organizationName
    accountType
    iconUrl
    phone
    address {
      line1
      city
      regionName
      postalCode
      countryCode
    }
    primaryContact {
      fullName
      emails
      phones
    }
  }
}
```

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../salesRepCustomers">← salesRepCustomers query</a>
    <a href="../salesRepOrders">salesRepOrders query →</a>
</div>
