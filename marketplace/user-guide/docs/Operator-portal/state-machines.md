# State Machines

The State machines segment manages and automates the various states and transitions of orders within the marketplace. 

To add or configure order flows:

1. Click **State machines** in the main menu.
1. The next blade lists all the available order state flows. Select the flow you need to edit or click **Add** in the toolbar to add a new flow.
1. In the next blade, configure the following fields:

    ![Edit states](media/add-view-state.png)

1. Click **Save** in the toolbar to save the changes.

Expand the example below to see an order processing workflow algorithm and its JSON representation.


??? Example

    !!! inline end "Order states transition"

        ![Algorithm](media/order-states-transitioning.png)

    ```json
    [
    {
        "name": "New",
        "type": "StateMachineState",
        "description": "Just created order",
        "isInitial": true,
        "isFinal": false,
        "stateData": {},
        "transitions": [
        {
            "trigger": "Confirm",
            "description": "If you want to confirm order",
            "toState": "Confirmed",
            "icon": "far fa-check-circle"
        },
        {
            "trigger": "Cancel",
            "description": "If you want cancel order",
            "toState": "Cancelled",
            "icon": "fas fa-times-circle"
        }
        ]
    },
    {
        "name": "Confirmed",
        "type": "StateMachineState",
        "description": "Confirmed by a vendor order",
        "isInitial": false,
        "isFinal": false,
        "stateData": {},
        "transitions": [
        {
            "trigger": "Pack",
            "description": "Packed & Ready to Ship order",
            "toState": "Packaged",
            "icon": "fas fa-box"
        },
        {
            "trigger": "Cancel",
            "description": "If you want cancel order",
            "toState": "Cancelled",
            "icon": "fas fa-times-circle"
        }
        ]
    },
    {
        "name": "Packaged",
        "type": "StateMachineState",
        "description": "Packed & Ready to be shipped by a Vendor",
        "isInitial": false,
        "isFinal": false,
        "stateData": {},
        "transitions": [
        {
            "trigger": "Ship",
            "description": "Ready to Ship the order",
            "toState": "Shipped",
            "icon": "fas fa-shipping-fast"
        }
        ]
    },
    {
        "name": "Shipped",
        "type": "StateMachineState",
        "description": "Already shipped order",
        "isInitial": false,
        "isFinal": true,
        "stateData": {},
        "transitions": []
    },
    {
        "name": "Cancelled",
        "type": "StateMachineState",
        "description": "Cancelled order",
        "isInitial": false,
        "isFinal": true,
        "stateData": {},
        "transitions": []
    }
    ]
    ```
