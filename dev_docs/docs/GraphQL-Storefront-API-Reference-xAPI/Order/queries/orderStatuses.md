# orderStatuses ==~query~==

This query allows you to retrieve information about the available order statuses.

## Arguments

| Argument                       | Description                                                                |
|--------------------------------|----------------------------------------------------------------------------|
| `cultureName` {==String==}     | The language to retrieve data in.                                          |

## Possible returns

| Possible return                                         	                    | Description                                |
|---------------------------------------------------------------------------	|------------------------------------------- |
| [`LocalizedSettingResponseType`](../objects/LocalizedSettingResponseType.md)  | Contains information about order statuses. |

## Examples

=== "Query"
    ```json linenums="1"
    {
      orderStatuses(cultureName: "de-DE") {
        items {
            key
            value
        }
      }
    }
    ```

=== "Return"
    ```json linenums="1"
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
                    "value": "Complteted"
                },
                {
                    "key": "Confirmed",
                    "value": "Confirmed" 
                },
                {
                    "key": "New",
                    "value": "NewEn" 
                },
                {
                    "key": "Payment required",
                    "value": "Payment required" 
                },
                {
                    "key": "Pending",
                    "value": "Pending" 
                },
                {
                    "key": "Processing",
                    "value": "Processing" 
                }
            ]
        }
      }
    }
    ```
