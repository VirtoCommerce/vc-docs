# salesRepCustomer

This query returns a single customer information card for an organization the rep serves.

## Arguments

| Argument | Description |
|----------|-------------|
| `organizationId`  ==String== | The Id of the customer organization. |

## Possible returns

| Possible return | Description |
|-----------------|-------------|
| [`SalesRepCustomerDetailsType`](../objects/SalesRepCustomerDetailsType.md) | A single customer's information card. |

## Example

<div class="grid" markdown>

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

```json title="Return"
{
  "data": {
    "salesRepCustomer": {
      "organizationId": "7b8c1f2a3d4e5f60",
      "organizationName": "Acme Industrial Supplies",
      "accountType": "Customer",
      "iconUrl": "https://media.example.com/orgs/acme.png",
      "phone": "+1-800-555-1234",
      "address": {
        "line1": "482 Warehouse Ave",
        "city": "Columbus",
        "regionName": "Ohio",
        "postalCode": "43004",
        "countryCode": "US"
      },
      "primaryContact": {
        "fullName": "Dana Whitfield",
        "emails": ["dana.whitfield@acme.example.com"],
        "phones": ["+1-614-555-0199"]
      }
    }
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../salesRepCustomers">← salesRepCustomers query</a>
    <a href="../salesRepOrders">salesRepOrders query →</a>
</div>
