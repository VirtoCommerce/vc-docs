# SalesRepCustomerDetailsType ==~object~==

This type represents a single customer's information card.

## Fields

| Field | Description |
|-------|-------------|
| `organizationId`  ==String!== | The Id of the customer organization. |
| `organizationName`  ==String== | The name of the customer organization. |
| `iconUrl`  ==String== | A link to the organization's icon. |
| `phone`  ==String== | The organization's phone number. |
| `accountType`  ==String== | The account type of the organization. |
| `address` [ ==SalesRepAddressType== ](SalesRepAddressType.md) | The organization's address. |
| `primaryContact` [ ==SalesRepContactType== ](SalesRepContactType.md) | The organization's primary contact. |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../SalesRepCustomerType">← SalesRepCustomerType</a>
    <a href="../SalesRepOrderType">SalesRepOrderType →</a>
</div>
