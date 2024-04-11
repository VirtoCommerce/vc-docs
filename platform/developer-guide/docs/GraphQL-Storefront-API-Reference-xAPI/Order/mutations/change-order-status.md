# ChangeOrderStatus  ==~mutation~==

This mutation changes order status.

## Arguments

The `InputChangeOrderStatusType!` represents the input object for changing the status of an order.

| Field                  | Description                                              |
|------------------------|----------------------------------------------------------|
| `orderId`  ==String==  | The Id of the order for which the status will be changed.|
| `status`  ==String==   | The new status to be assigned to the order.              |


## Possible returns

| Possible return       | Description                                          	|
|-----------------------|------------------------------------------------------	|
| `Boolean`           	|  Indicates the success or failure of the operation.  	|


=== "Mutation"
    ```json linenums="1"
    mutation changeOrderStatus ($command: InputChangeOrderStatusType!) {
    changeOrderStatus (command: $command) }
    ```

=== "Variables"
    ```json linenums="1"
    "command": {
    "orderId":  "2be32440-ee84-4dd5-aa9b-fcbe35bf61f0",
    "status":  "Paid"
    }
    ```

