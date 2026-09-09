# Overview

The **Loyalty** module provides a flexible loyalty program and mission management system for the Virto Commerce Platform. It enables store managers to create loyalty programs, launch goal-based missions, reward customers with points, and track loyalty transactions. Customers can earn points through purchases and completed missions, view their available rewards, and use loyalty points to pay for eligible orders.

The module includes two complementary loyalty mechanisms:

* [Loyalty programs](enable-and-configure-loyalty-programs.md): Configurable programs that award points based on order conditions or purchases of specific products.
* [Loyalty missions](managing-loyalty-missions.md): Goal-driven campaigns that automatically award a predefined number of points when customers achieve a specific target, such as reaching an order value, placing a certain number of orders, or purchasing specific SKUs.

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-loyalty)

[![Download](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-loyalty/releases)

## Key features

The Loyalty module provides the following capabilities:

* **Manage loyalty programs**: Create and configure two program types:

    * **Order Loyalty** rewards customers based on order conditions.
    * **Product Points Loyalty** rewards customers for purchasing specific products.

  Both program types support conditions, reward rules (fixed points or a percentage of the order value), priorities, activation periods, and localized names.

* **Manage loyalty missions**: Create goal-based campaigns that monitor customer orders and automatically award points when customers complete a defined goal.

* **Reward specific products**: Assign per-product multiplier factors and vary them by customer group. For example, VIP or LUX customers can earn points at different rates for the same product.

* **Show earnable points**: Display the number of loyalty points a customer can earn for a product while browsing the catalog.

* **Offer a loyalty catalog**: Provide a dedicated catalog where products are priced in loyalty points instead of the store's standard currency.

* **Track loyalty transactions**: Record point accruals and redemptions and monitor customer activity, including changes to loyalty balances.

* **Enable loyalty payments**: Use the built-in **LoyaltyPaymentMethod** to allow customers to pay for orders with loyalty points.

    * Customers can use points only when their balance fully covers the order amount.
    * The conversion rate is **1 point = 1 unit of order currency**.


The diagram below illustrates the key functionalities of the Virto Commerce Loyalty module:

![Payment options](media/key-entities.png)

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../generic-export/overview">← Generic Export module overview</a>
    <a href="../enable-loyalty">Enabling loyalty features →</a>
</div>