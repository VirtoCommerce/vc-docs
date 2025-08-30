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

=== "Query"
    ```json linenums="1"
    {
      paymentStatuses(cultureName: "en-US") {
        items {
            key
            value
        }
      }
    }
    ```

=== "Return"
    ```json linenums="1"
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
