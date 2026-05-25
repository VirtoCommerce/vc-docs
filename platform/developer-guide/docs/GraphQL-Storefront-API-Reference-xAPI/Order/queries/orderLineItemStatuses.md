# orderLineItemStatuses ==~query~==

This query allows you to retrieve information about the available order line item statuses.

## Arguments

| Argument                       | Description                                                                |
|--------------------------------|----------------------------------------------------------------------------|
| `cultureName`  ==String==      | The language to retrieve data in.                                          |

## Possible returns

| Possible return                                         	                    | Description                                |
|---------------------------------------------------------------------------	|------------------------------------------- |
| [`LocalizedSettingResponseType`](../objects/LocalizedSettingResponseType.md)  | Contains information about order line item statuses. |

## Example

<div class="grid" markdown>

```json title="Query"
{
  orderLineItemStatuses(cultureName: "en-US") {
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
    "orderLineItemStatuses": {
      "items": [
        {
        "key": "New",
        "value": "New"
        },
        {
        "key": "Processing",
        "value": "Processing"
        },
        {
        "key": "Shipped",
        "value": "Shipped"
        },
        {
        "key": "Cancelled",
        "value": "Cancelled"
        },
        {
        "key": "Returned",
        "value": "Returned"
        }
      ]
    }
  }
}
```

</div>