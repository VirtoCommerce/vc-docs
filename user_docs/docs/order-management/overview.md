The Orders Module in VirtoCommerce is a document based flexible orders management system with possibility to add unlimited number of documents related to customer order.

The Orders Module is designed to:

* Store order details.
* Manage orders created by users on client side. 

!!! info
    * This module is not designed to be a full order processing system like ERP. It serves as storage for customer orders details and can be synchronized with different external processing systems.

The order itself contains minimum details.  You will find payment, shipment, and other order details on the documents.

!!! note
    * The Order Management process in VitroCommerce OMS is not coded and not pre-determined. This system is designed as an Order Details Editor with no validation logics available. The system is implied to be an additional storage for customer orders details.

## Related Components¶

To view the source code of Virto Commerce Order module, check out our [GitHub repository](https://github.com/VirtoCommerce/vc-module-order).

To download the latest Order module release, click [here](https://github.com/VirtoCommerce/vc-module-order/releases).

## Key Features

VirtoCommerce Orders Module supports the following functionalities:

* Document based order structure. The order, being a document itself, is also a container for documents related to the order processing, shipping, and payment.
* Status update for each document type.
* Manage additional invoices.
* Changing Order products (quantity, product change, new products).
* Possibility to make changes to order product price.
* Possibility to change discounts.
* Payment history tracking. These documents allow keeping bills information and full logging of payment gateway transactions related to the order.
* Refunding possibilities.
* Possibility to change Product items.
* Save order details change history (logs).
* Save payment details (emails, phone numbers).
* Manage split shipments.
* Single shipment delivery of more than one order.
* Real time integration with Avalara Tax automation.