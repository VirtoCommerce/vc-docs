# orderStatuses ==~query~==

This query allows you to retrieve information about the available order statuses.

## Arguments

| Argument                       | Description                                                                |
|--------------------------------|----------------------------------------------------------------------------|
| `cultureName`  ==String==      | The language to retrieve data in.                                          |

## Possible returns

| Possible return                                         	                    | Description                                |
|---------------------------------------------------------------------------	|------------------------------------------- |
| [`LocalizedSettingResponseType`](../objects/LocalizedSettingResponseType.md)  | Contains information about order statuses. |

## Example

<div class="grid" markdown>

```json title="Query"
{
  orderStatuses(cultureName: "de-DE") {
    items {
        key
        value
    }
  }
}
```

```json title="Return"
​{​
  "data" {​
    "orderStatuses": {
        "items": [
            {
              "key": "Cancelled",
              "value": "CancelledEN"
            },
            {
              "key": "Completed",
              "value": "Completed"
            },
            {
              "key": "Confirmed",
              "value": "Confirmed" 
            },
            // more items
        ]
      }
    }
}
```

</div>