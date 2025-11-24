# Orders

The Orders segment contains all orders created by the buyers. Here vendors can:

* [Edit orders.](orders.md#edit-order)
* [Process orders.](orders.md#process-order) 
* [Create shipments.](orders.md#create-shipment)

## Edit order

To edit the order:

1. Click **Orders** in the main menu to open the list of the received orders.
1. In the next blade, select the desired order. The order details will open in the next blade.
1. Offer details are displayed in the bottom right corner. Click on any item to view and edit its details: 

    ![Edit order](media/edit_order.gif)

1. Click **Save** in the toolbar to save the changes.

Your modifications have been applied. 

## Process order

The newly created orders are processed in accordance with the created [states flow](../Operator-portal/state-machines.md). In our example, the orders are processed as follows:

1. Confirm or cancel the new order. Cancelled orders cannot be further processed.
1. The confirmed order can be packaged or cancelled. Cancelled orders cannot be further processed.
1. The packaged orders can be shipped. Further processing is impossible.

    ![Statuses](media/order-statuses.png){: style="display: block; margin: 0 auto;" }

!!! note
    Once an order status changes from **New**, the edit button will no longer be available.

![Readmore](media/readmore.png){: width="25"} [Setting order states and order flows](../Operator-portal/state-machines.md)


## Create shipment

To create an order order shipment:

1. Click **Orders** in the main menu to open the list of the received orders.
1. In the next blade, select the desired order. The order details will open in the next blade.
1. In the next blade, click on the **Shipping** widget.
1. In the next blade, click **Add** to add a new shipment.

    ![Create shipment](media/create-shipping.gif)

1. In the next blade, fill in the following fields:

    ![Shipment doc fields](media/shipment-doc-fields.png){: style="display: block; margin: 0 auto;" width="500"}

1. Click **Save** in the toolbar to save the changes.

A new shipment has been created.

!!! note
    Users can also [create shipment documents in the Platform](/platform/user-guide/latest/order-management/managing-documents#create-shipment-documents).

### Add items to shipment

When creating or editing a shipment, users can add items to the shipment by clicking **Add item** at the bottom of the blade. In the new blade, users can edit the quantity of items:

![Add items to shipment](media/edit-shipment-items.gif)


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../overview">← Vendor portal overview</a>
    <a href="../quotes">Quotes →</a>
</div>