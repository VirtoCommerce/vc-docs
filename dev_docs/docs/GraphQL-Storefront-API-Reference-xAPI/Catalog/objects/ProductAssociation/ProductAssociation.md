# ProductAssociation ==~object~==

The `ProductAssociation` represents the association between products in queries.

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
    <td class="tg-0pky"><code>type</code> {==String==}</td>
    <td class="tg-0pky">The type of the association between products.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>priority</code> {==Int==}</td>
    <td class="tg-0pky">The priority of the product association.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>quantity</code> {==Int==}</td>
    <td class="tg-0pky">The quantity or count associated with the product association.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>associatedObjectId</code> {==String==}</td>
    <td class="tg-0pky">The ID of the associated object.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>associatedObjectType</code> {==String==}</td>
    <td class="tg-0pky">The type of the associated object.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>tags</code> {==String==}</td>
    <td class="tg-0pky">Tags or labels associated with the product association.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>product</code> {==<a href="../../01-ProductType">Product</a>==}</td>
    <td class="tg-0pky">The product object associated with the association.</td>
</tr>
</tbody>
</table>

