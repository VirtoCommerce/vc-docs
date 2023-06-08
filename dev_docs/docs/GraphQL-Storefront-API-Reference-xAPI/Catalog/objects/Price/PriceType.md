# PriceType ==~object~==

The `priceType` object represents the pricing information for a product or variation.

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
    <td class="tg-0pky"><code>list</code> {==MoneyType==}</td>
    <td class="tg-0pky">The regular price of the item without any discounts or taxes applied.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>listWithTax</code> {==MoneyType==}</td>
    <td class="tg-0pky">The regular price of the item including taxes.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>sale</code> {==MoneyType==}</td>
    <td class="tg-0pky">The discounted price of the item without taxes applied.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>saleWithTax</code> {==MoneyType==}</td>
    <td class="tg-0pky">The discounted price of the item including taxes.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>actual</code> {==MoneyType==}</td>
    <td class="tg-0pky">The current actual price of the item, which may reflect a sale or promotion.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>actualWithTax</code> {==MoneyType==}</td>
    <td class="tg-0pky">The current actual price of the item including taxes.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>discountAmount</code> {==MoneyType==}</td>
    <td class="tg-0pky">The amount of discount applied to the item without taxes.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>discountAmountWithTax</code> {==MoneyType==}</td>
    <td class="tg-0pky">The amount of discount applied to the item including taxes.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>discountPercent</code> {==Decimal==}</td>
    <td class="tg-0pky">The percentage of discount applied to the item.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>currency</code> {==String==}</td>
    <td class="tg-0pky">The currency code in which the prices are expressed.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>startDate</code> {==DateTime==}</td>
    <td class="tg-0pky">The start date and time of the pricing period or promotion.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>endDate</code> {==DateTime==}</td>
    <td class="tg-0pky">The end date and time of the pricing period or promotion.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>tierPrices</code> {==<a href="../TierPriceType">TierPriceType</a>==}</td>
    <td class="tg-0pky">The tiered pricing options available for the item, which offer different prices based on quantity or customer groups.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>discounts</code> {==<a href="../CatalogDiscountType">CatalogDiscountType</a>==}</td>
    <td class="tg-0pky">The catalog-level discounts applied to the item.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>pricelistId</code> {==String==}</td>
    <td class="tg-0pky">The unique identifier of the price list to which the item's price belongs.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>minQuantity</code> {==Int==}</td>
    <td class="tg-0pky">The minimum quantity required to be eligible for the price or discount.</td>
</tr>
</tbody>
</table>


[Read more about managing images](https://docs.virtocommerce.org/new/user_docs/catalog/managing-categories/#images-widget){ .md-button }