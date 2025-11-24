# Manage Product Availability

Product inventories are shown in Frontend Application:

* Under each product card in the catalog. You can apply **Show in stock** filter to see only products in stock.
* In the cart after adding the products. 
* When processing orders.

The product's availability displayed in the Frontend Application is determined by the information configured in:

* The **Catalog** module, where availability settings are established using switches.
* The **Inventory** module, storing the actual quantity of the product in stock. 

??? "See details"

    The diagram below illustrates the sequential process of how the product's availability is initially defined in the **Catalog** module through the use of switches, and then updated in the **Inventory** module with the specific stock quantity.
    ![Availability setting diagram](../inventory/media/tracking-inventory-diagram.png)

## Set availability

To set product's availability:

1. Click **Catalog** in the main menu.
1. In the next **Manage catalogs** blade, select the required catalog to open the **Categories and Items** blade.
1. Click the product you need to set availability for.
1. In the new blade, set the product's availability statuses by switching the toggles on and off in the order they are listed in the table below:


    | Switch | Status | Availability status|
    |---|---|---|
    | **Visible**  | <ul><li>Off</li><li>On</li></ul> | <ul><li>Sold out. **Can be purchased** and **Track inventory** switches do not influence the stock, even if on.</li><li>Depends on **Can be purchased**.</li></ul> |
    | **Can be purchased**  | <ul><li>Off</li><li>On</li></ul> | <ul><li>Out of stock. **Track inventory** does not influence the stock, even if on.</li><li>Depends on **Track inventory**.</li></ul> |
    | **Track inventory**  | <ul><li>Off</li><li>On</li></ul> | <ul><li>In stock.</li><li>Depends on the amount specified in the **Inventory** module.</li></ul> |

    !!! info 
        Track inventory switch can be applied to both digital and physical products. By default, the switch is off for digital products, on for physical ones. 

1. In the same blade, click on the **Fulfillment centers** widget.

    ![add-inventory](media/inventory-path.png){: style="display: block; margin: 0 auto;" }

1. Fill in the following fields:

    ![Edit inventory](../inventory/media/edit-inventory.png){: style="display: block; margin: 0 auto;" }

1. Click **Save** to save changes.   

The product's availability has been set.

Try our interactive demo to explore key features in action:

<div>
  <script async src="https://js.storylane.io/js/v2/storylane.js"></script>
  <div class="sl-embed" style="position:relative;padding-bottom:calc(49.22% + 25px);width:100%;height:0;transform:scale(1)">
    <iframe loading="lazy" class="sl-demo" src="https://virtocommerce.storylane.io/demo/vorljmcpyz7y?embed=inline" name="sl-embed" allow="fullscreen" allowfullscreen style="position:absolute;top:0;left:0;width:100%!important;height:100%!important;border:1px solid rgba(63,95,172,0.35);box-shadow: 0px 0px 18px rgba(26, 19, 72, 0.15);border-radius:10px;box-sizing:border-box;"></iframe>
  </div>
</div>


## Check availability

To check product's availability:

1. Follow steps 1-3 from the instruction above.
1. In the next blade, click on the **Index** widget.

    ![Index widget](media/index-widget.png){: style="display: block; margin: 0 auto;" width="500"}

1. Find the **availability** line. The **availability** statuses can be as follows:
    * **InStock**.
    * **OutOfStock**.
    * **SoldOut**.

    ![Availability status](media/availability-status.png){: style="display: block; margin: 0 auto;" }


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../managing-product-configurations">← Managing product configurations</a>
    <a href="../managing-properties">Managing properties →</a>
</div>