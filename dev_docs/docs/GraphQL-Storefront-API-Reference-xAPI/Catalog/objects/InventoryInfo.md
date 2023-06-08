# InventoryInfo ==~object~==

The `InventoryInfo` provides essential data for tracking and managing inventory levels and ensuring accurate stock availability for customers.

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
    <td class="tg-0pky"><code>inStockQuantity</code> {==Long==}</td>
    <td class="tg-0pky">The quantity of the item that is currently in stock and available for sale.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>reservedQuantity</code> {==Long==}</td>
    <td class="tg-0pky">The quantity of the item that has been reserved or allocated for pending orders.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>fullfillmentCenterId</code> {==String!==}</td>
    <td class="tg-0pky"> The unique identifier of the fulfillment center where the item is stored or managed.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>fullfillmentCenterName</code> {==String!==}</td>
    <td class="tg-0pky"> The name of the fulfillment center where the item is stored or managed.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>allowPreorder</code> {==Boolean==}</td>
    <td class="tg-0pky">Indicates whether preordering of the item is allowed.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>allowBackorder</code> {==Boolean==}</td>
    <td class="tg-0pky">Indicates whether backordering of the item is allowed.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>preorderAvailabilityDate</code> {==DateTime==}</td>
    <td class="tg-0pky">The date and time when the item will be available for preorder, if applicable.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>backorderAvailabilityDate</code> {==DateTime==}</td>
    <td class="tg-0pky">The date and time when the item will be available for backorder, if applicable.</td>
</tr>
</tbody>
</table>

