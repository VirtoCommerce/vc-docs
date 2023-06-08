# AvailabilityData ==~object~==

`AvailabilityData` refers to the information related to the availability and inventory status of a product or variation. The `AvailabilityData` object provides details about the current stock availability, purchase eligibility, and inventory tracking status of a specific product or variation.

<style type="text/css">
.tg  {border:none;border-collapse:collapse;border-spacing:0;}
.tg td{border-color:white;border-style:solid;border-width:1px;font-family:Circular Std;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:white;border-style:solid;border-width:1px;font-family:Circular Std;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0lax{border-color:#ffffff;text-align:left;vertical-align:top}
.tg .tg-0pky:nth-child(1),
.tg .tg-0lax:nth-child(1) {width: 30%;}
.tg .tg-0pky:nth-child(2),
.tg .tg-0lax:nth-child(2) {width: 70%;}
</style>
<table class="tg">
<tbody>
<tr>
    <td class="tg-0pky"><code>availableQuantity</code> {==Long!==}</td>
    <td class="tg-0pky">The quantity of product or variation that is currently available for purchase.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>isBuyable</code> {==Boolean==}</td>
    <td class="tg-0pky">Indicates whether the product or variation is available for purchase or not.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>isAvailable</code> {==Boolean==}</td>
    <td class="tg-0pky">Indicates whether the product or variation is available for selection or not.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>isInStock</code> {==Boolean==}</td>
    <td class="tg-0pky">Indicates whether the product or variation is currently in stock or not.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>isActive</code> {==Boolean==}</td>
    <td class="tg-0pky">Indicates whether the product or variation is active or not.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>isTrackInventory</code> {==Boolean==}</td>
    <td class="tg-0pky">Indicates whether the inventory of the product or variation is being tracked or not.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>inventories</code> {==<a href="../InventoryInfo">InventoryInfo</a>==}</td>
    <td class="tg-0pky">The inventory information associated with the product or variation.</td>
</tr>
</tbody>
</table>

[Read more about managing product availability](https://docs.virtocommerce.org/new/user_docs/catalog/setting-product-availability/){ .md-button }

