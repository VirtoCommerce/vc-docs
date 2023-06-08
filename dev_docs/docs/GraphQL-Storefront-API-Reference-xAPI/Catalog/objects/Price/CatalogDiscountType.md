# CatalogDiscountType ==~object~==

The `CatalogDiscountType` represents a discount applied to a catalog or specific items within a catalog.

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
    <td class="tg-0pky"><code>coupon</code> {==String==}</td>
    <td class="tg-0pky">The coupon code associated with the catalog discount.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>description</code> {==String==}</td>
    <td class="tg-0pky">The description or details of the catalog discount.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>promotionId</code> {==String==}</td>
    <td class="tg-0pky">The identifier of the promotion associated with the catalog discount.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>amount</code> {==Decimal==}</td>
    <td class="tg-0pky">The amount of discount applied to the item without taxes.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>moneyAmount</code> {==MoneyType==}</td>
    <td class="tg-0pky">The amount of discount applied to the item without taxes, represented as a monetary value.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>amountWithTax</code> {==Decimal==}</td>
    <td class="tg-0pky">The amount of discount applied to the item including taxes.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>moneyAmountWithTax</code> {==MoneyType==}</td>
    <td class="tg-0pky">The amount of discount applied to the item including taxes, represented as a monetary value.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>promotion</code> {==Promotion==}</td>
    <td class="tg-0pky">The promotion object associated with the catalog discount.</td>
</tr>
</tbody>
</table>


[Read more about managing promotions](https://docs.virtocommerce.org/new/user_docs/marketing/managing-promotions/){ .md-button }