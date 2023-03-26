# Basic order processing scenarios

Order processing includes the steps involved in fulfilling a customer's order: receiving and reviewing the order, verifying payment and stock availability, picking and packing the items, shipping the order, and updating the customer on the order status. Below are the basic order processing scenarios.

## Getting invoice PDF

To get an invoice in PDF format:

1. Go to **Orders**.
2. Select the requried invoice.
3. Click **Get invoics PDF**. 

![Get invoice PDF](media/get-invoice-pdf.png)

The invoice PDF opens in a new window.

## Creating a New Shipment Document

To create a new shipment document:

1. Select the required order and click **New document**.

    ![New document](media/new-document.png)

1. In the new blade, click **Shipment**.

    ![New shipment document](media/new-shipment-document.png)

1. Fill in the fields of the new shipment document. Don't forget to switch the **Approved** option to on.

    ![New shipment document](media/shipment-document-processing.png)

    !!! note
        * Select the required value in the **Fullfillment center**, **Status**, and **Vendor** fields from a drop-down list or add a new value by clicking ![Edit](media/pencil.png).
    
    1. To see, add, or remove shipment items, click **Shipment items**, make changes, and click **OK**.

        ![New shipment document](media/add-remove-items.png)
    
    1. To see, add, or delete delivery address, click **Delivery address**, fill in the fields, and click **OK**.

    ![New shipment document](media/delivery-address.png)

1. Click **OK** to save changes.

1. To see all the shipment documents for the selected order, scroll down to shipment and payment documents section and click **Shipment**.

    ![New shipment document](media/shipment-documents-stored.png)

## Creating a New Payment Document

To create a new payment document:

1. Select the required order and click **New document**.

    ![New document](media/new-document.png)

1. In the new blade, click **PaymentIn**.

    ![New payment document](media/new-payment-document.png)

1. Fill in the fields of the new payment document. Don't forget to switch the **Approved** option to on.

    ![New payment document](media/payment-document-processing.png)

    !!! note
        * Select the required value in the **Status** and **Vendor** fields from a drop-down list or add a new value by clicking ![Edit](media/pencil.png).    

    1. To view, edit, or add a payment address, click **Payment address**. 

        ![New payment address](media/new-payment-address.png)

    1. Fill in the fields in the **Manage billing address** blade and click **OK**.

        ![Manage billing address](media/manage-billing-address.png)

    1. To view the list of all payment gateway interactions, click **Transactions**.

        ![View transactions](media/transactions.png)

1. Click **OK** to save changes.

1. To see all the payment documents for the selected order, scroll down to shipment and payment documents section and click **PaymentIn**.

    ![Payment document stored](media/payment-document-stored.png)

## Tracking Order Changes

To view the order changes history, including payment, shipment, and other modifications:

1. Select the required order and click **Changes**.

    ![New payment document](media/order-history.png)

1. Information about order placement, payment, shipment, etc. appears in the new blade. Select additional information fields from the drop-down list in the upper right corner.

    ![New payment document](media/order-changes.png)

## Creating Returns

To create a return for a particular order:

1. Select the order and click **Create return**.
1. In the new blade, check the items that require a return. Enter the return reason, if necessary.
1. Click **Make return**.
![Creating a return](media/make-return-1.png)

1. The return specifications opens in a new blade.
![Return specification](media/make-return-2.png)

## Processing Returns

To process the received returns:

1. Select the required order and click **Returns**.

    ![Return processing](media/return-processing.png)

1. A list of returns appears in the new blade. Click the required return.

    ![Selecting a return](media/return-selecting.png)

1. In the new blade, change the return status, enter your resolution, click **Save**.

    ![Saving a return](media/return-saving.png)

## Sending Order Information to AvaTax

To send the order information to AvaTax manually:

1. Click the button:

    ![General order information](media/send-to-avalara.png)

1. In the new blade, click **Send to AvaTax**. 

    ![General order information](media/send-to-avalara1.png)

1. Check the updated information on the button:

    ![General order information](media/avatax.png)

To set automatic tax calculation, see [AvaTax module](../integrations/avalara/taxes-calculation.md). 

## Indexation

To start indexation:

1. Click the button with the last indexation date:

    ![General order information](media/avatax.png)

1. In the new blade, click **Build index**.

    ![Build index](media/new-indexation.png)

1. The notification of successful indexation appears.

    ![Indexation completed](media/indexation-completed.png)
