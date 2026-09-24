# Restrict Order Prices

An administrator can be given full access to orders while being unable to see the money on them. Prices are removed by the server before the order leaves it, so there is nothing to recover from the payload, the Admin UI, or an export.

This differs from simply not granting the **order:read_prices** permission in two ways:

* **Coverage is complete.** The price rule applies everywhere an order is read or written: search, indexed search, get by ID, number or outer ID, save, patch, export, and import.
* **The rule is replaceable.** By default, price visibility depends on the global **order:read_prices** permission, but this can be replaced with a custom rule, for example, one based on store, store type, or organization. This makes per-distributor price restriction possible, rather than all-or-nothing access.

## Set up price-blind role

To create a role for order administrators who must not see prices:

1. Click **Security** in the main menu.
1. In the next blade, click **Add** to create a new role.
1. Assign the permissions the job requires, for example, **order:create**, **order:update**, **order:delete**, **order:update_shipments**, **order:capture_payment**, or **order:refund**.
1. Make sure the role also has the following base permissions:

    * **customer:read**
    * **order:access**
    * **order:read**
    * **platform:module:read**
    * **platform:setting:read**
    * **store:read**

1. Do **not** grant **order:read_prices**.
1. Click **Save**.

The default price-visibility rule reads the **order:read_prices** permission and hides prices for any role that lacks it.

![Readmore](media/readmore.png){: width="25"} [Creating new role](/platform/user-guide/latest/security/roles-and-permissions/#creating-new-role)

## What user sees

Every monetary value is masked across the Admin UI for a user whose role lacks **order:read_prices** — the order list **Total** column, the line items, the order-totals widget, the shipment and payment blades, and the operation tree. Masked values render as `#` / `#.##` rather than `0.00`, so a withheld price is visually distinct from an order that genuinely costs nothing.

Saving is safe: if such a user edits an order and saves it, the prices they could not see are restored from storage before the write, so a price-blind save cannot destroy data. The same applies to a backup taken by such a user and later restored — the archive carries the withheld marker, and the restore puts the real values back.

## Restrict invoice downloads

The invoice is a document about money, so downloading it requires its own permission, **order:invoice:download**. Without it, the **Invoice** button is hidden in the UI, and the endpoint returns a 403 error.

Grant **order:invoice:download** together with **order:read_prices**. A user who has the download permission but not the price permission receives an invoice with zero amounts — correct behavior, since there is no point masking values inside a PDF, but not a useful document. If someone must not see prices, do not give them the invoice.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../permissions">← Permissions</a>
    <a href="../settings">Order module settings →</a>
</div>