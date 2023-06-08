# TierPriceType ==~object~==

The `TierPriceType` represents the pricing information for a specific tier or quantity range of a product. It allows setting different prices based on the quantity purchased.

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
    <td class="tg-0pky"><code>price</code> {==MoneyType==}</td>
    <td class="tg-0pky">The price of the item without any discounts or taxes applied for the specified tier or quantity range.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>priceWithTax</code> {==MoneyType==}</td>
    <td class="tg-0pky">The price of the item including taxes for the specified tier or quantity range.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>quantity</code> {==Long==}</td>
    <td class="tg-0pky">The minimum quantity required to be eligible for the price or discount defined by the tier.</td>
</tr>
</tbody>
</table>
