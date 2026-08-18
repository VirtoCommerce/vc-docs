# paymentStatuses ==~query~==

This query allows you to retrieve information about the available payment statuses.

## Arguments

| Argument                       | Description                                                                |
|--------------------------------|----------------------------------------------------------------------------|
| `cultureName`  ==String==      | The language to retrieve data in.                                          |

## Possible returns

| Possible return                                         	                    | Description                                |
|---------------------------------------------------------------------------	|------------------------------------------- |
| [`LocalizedSettingResponseType`](../objects/LocalizedSettingResponseType.md)  | Contains information about payment statuses. |

## Example


<div class="grid" markdown>

```json title="Query"
{
  paymentStatuses(cultureName: "en-US") {
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
    "paymentStatuses": {
      "items": [
      {
        "key": "Pending",
        "value": "Pending"
      },
      {
        "key": "Paid",
        "value": "Paid"
      },
      {
        "key": "Failed",
        "value": "Failed"
      },
      {
        "key": "Refunded",
         "value": "Refunded"
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