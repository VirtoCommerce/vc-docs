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

## Examples

=== "Query"
    ```json linenums="1"
    {
      shipmentStatuses(cultureName: "en-US") {
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
