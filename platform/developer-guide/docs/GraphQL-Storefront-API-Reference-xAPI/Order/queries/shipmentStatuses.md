# shipmentStatuses ==~query~==

This query allows you to retrieve information about the available shipment statuses.

## Arguments

| Argument                       | Description                                                                |
|--------------------------------|----------------------------------------------------------------------------|
| `cultureName`  ==String==      | The language to retrieve data in.                                          |

## Possible returns

| Possible return                                         	                    | Description                                |
|---------------------------------------------------------------------------	|------------------------------------------- |
| [`LocalizedSettingResponseType`](../objects/LocalizedSettingResponseType.md)  | Contains information about shipment statuses. |

## Example

<div class="grid" markdown>

```graphql title="Query"
{
  shipmentStatuses(cultureName: "en-US") {
    items {
        key
        value
    }
  }
}
```

```json title="Return"
{
  "data": {
    "shipmentStatuses": {
      "items": [
        {
          "key": "New",
          "value": "New"
        },
        {
         "key": "Pending",
          "value": "Pending"
        },
        {
          "key": "Processing",
          "value": "Processing"
        },
        {
          "key": "Cancelled",
          "value": "Cancelled"
        }
      ]
    }
  }
}
```

</div>

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../organization-orders">← OrganizationOrders query</a>
    <a href="../paymentStatuses">PaymentStatuses query →</a>
</div>
