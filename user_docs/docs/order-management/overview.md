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

## Key Features (IN PROGRESS)

VirtoCommerce Orders Module supports the following functionalities:

* Status update for each document type.
* Document based order structure. The order, being a document itself, is also a container for all documents related to the order processing: shipping, payment, custom documents.
* Ability to view and manage fulfillment, packages, pick-up and shipments documents.
* Dynamic extensibility of the 'Order Documents' (possibility to add custom fields). It is relatively easy to implement additional data for existent documents and new kinds of custom documents to the order container.
* Manage additional invoices.
* Save order drafts (postponed confirmation of order changes).
* Changing Order products (quantity, product change, new products).
* Possibility to make changes to order product price.
* Possibility to change discounts.
* Add promotion coupons to order.
* Payment history tracking. Orders contain document type "Payment". Using this type of documents allows keeping bills information and full logging of payment gateway transactions related to the order.
* Refunding possibilities.
* Possibility to change Product items.
* Save order details change history (logs).
* Save payment details (cards, links, phone numbers).
* Manage split shipments.
* Single shipment delivery of more than one order.