# Orders

The Order segment contains all orders created by the buyers. Here vendors can:

* [Edit orders.](orders.md#edit-order)
* [Process orders.](orders.md#process-order) 
* [Create shipments.](orders.md#create-shipment)

## Edit order

To edit the order:

1. Click **Orders** in the main menu to open the list of the received orders.
1. In the next blade, select the desired order. The order details will open in the next blade.
1. Click **Edit** in the toolbar.
1. Edit the item quantity.
1. Edit unit price.

    ![Edit order](media/edit-order.png)

1. Click ![Floppy](media/floppy.png){: width="25"} in the toolbar to save the changes. Or click ![Cancel](media/cancel-changes.png){: width="25"} to cancel the changes.

Your modifications have been applied. 

!!! note
    The order image tells you how many items are there in the order:
    ![Number of items in order](media/marketplace-items.png)

## Process order

The newly created orders can be processed as follows:

1. Confirm or cancel the new order. Cancelled orders cannot be further processed.
1. The confirmed order can be packaged or cancelled. Cancelled orders cannot be further processed.
1. The packaged orders can be shipped. Further processing is impossible.

    ![Statuses](media/order-statuses.png)

!!! note
    Once an order status changes from **New**, the edit button will no longer be available.

![Readmore](media/readmore.png){: width="25"} [Setting order states and order flows](../Operator-portal/state-machines.md)


## Create shipment

To create an order order shipment:

1. Click **Orders** in the main menu to open the list of the received orders.
1. In the next blade, select the desired order. The order details will open in the next blade.
1. In the next blade, click on the **Shipping** widget.
1. In the next blade, click ![Plus](media/plus.png){: width="25"} to add a new shipment.

    ![Create shipment](media/create-shipping.png)

1. In the next blade, fill in the following fields:

    ![Shipment doc fields](media/shipment-doc-fields.png)

1. Click ![Floppy](media/floppy.png){: width="25"} in the toolbar to save the changes.

A new shipment has been created.

!!! note
    Users can also [create shipment documents in the Platform](../../../../platform/user-guide/order-management/managing-documents#create-shipment-documents).

### Add items to shipment

When creating or editing a shipment, users can add items to the shipment by clicking **Add item** at the bottom of the blade. In the new blade, users can edit the quantity of items:

![Add items to shipment](media/edit-shipment-items.png)