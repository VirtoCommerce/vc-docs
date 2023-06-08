# VariationType ==~object~==

`VariationType` is used to differentiate or group different types of product variations.

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
    <td class="tg-0pky"><code>id</code> {==String==}</td>
    <td class="tg-0pky">The Id of the variation.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>name</code> {==String==}</td>
    <td class="tg-0pky">The name of the variation.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>code</code> {==String==}</td>
    <td class="tg-0pky">The SKU of the variation.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>productType</code> {==String==}</td>
    <td class="tg-0pky">The type of the product associated with the variation.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>minQuantity</code> {==Int==}</td>
    <td class="tg-0pky">The minimum quantity allowed for the variation.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>maxQuantity</code> {==Int==}</td>
    <td class="tg-0pky">The maximum quantity allowed for the variation.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>availabilityData</code> {==<a href="../AvailabilityData">availabilityData</a>==}</td>
    <td class="tg-0pky">The availability data for the variation. </td>
</tr>
<tr>
    <td class="tg-0lax"><code>images</code> {==<a href="../ImageType">ImageType</a>==}</td>
    <td class="tg-0lax">The images associated with the variation.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>price</code> {==<a href="../price/PriceType">PriceType</a>==}</td>
    <td class="tg-0lax">The price information for the variation.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>prices</code> {==<a href="../price/PriceType">PriceType</a>==}</td>
    <td class="tg-0lax">The prices associated with the variation.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>properties</code> {==<a href="../Property/Property">Property</a>==}</td>
    <td class="tg-0lax">The properties associated with the variation.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>assets</code> {==<a href="../Asset">Asset</a>==}</td>
    <td class="tg-0lax">The assets associated with the variation.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>outlines</code> {==<a href="../OutlineType">OutlineType</a>==}</td>
    <td class="tg-0lax">The hierarchical outlines of the variation and its ancestors.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>slug</code> {==String==}</td>
    <td class="tg-0lax">The URL slug of the variation.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>vendor</code> {==<a href="../Commonvendor/CommonVendor">CommonVendor</a>==}</td>
    <td class="tg-0lax">The vendor associated with the variation.</td>
</tr>
</tbody>
</table>


[Read more about managing product variations](https://docs.virtocommerce.org/new/user_docs/catalog/managing-product-variations/){ .md-button }