# Property ==~object~==

The `propertyType` object represents a type or category of properties. Properties are used to provide additional information or attributes for products and variations.

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
    <td class="tg-0pky">The unique identifier of the property type.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>name</code> {==String!==}</td>
    <td class="tg-0pky">The name or title of the property type.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>hidden</code> {==Boolean!==}</td>
    <td class="tg-0pky"> Indicates whether the property type is hidden or visible.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>multivalue</code> {==Boolean!==}</td>
    <td class="tg-0pky"> Indicates whether the property type allows multiple values.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>displayOrder</code> {==Int==}</td>
    <td class="tg-0pky">The order in which the property type should be displayed.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>label</code> {==String==}</td>
    <td class="tg-0pky">The label or display name of the property type.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>type</code> {==String==}</td>
    <td class="tg-0pky">The type or category of the propertyType.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>valueType</code> {==String==}</td>
    <td class="tg-0pky">The data type of the property values.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>value</code> {==PropertyValue==}</td>
    <td class="tg-0pky">The default value or values associated with the property type.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>valueId</code> {==String==}</td>
    <td class="tg-0pky">The unique identifier of the default value for the property type.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>propertyDictItems(...)</code> {==<a href="../PropertyDictItemConnection">PropertyDictionaryItemsConnection</a>==} </td>
    <td class="tg-0pky">A connection to retrieve the dictionary items associated with the property type. </td>
</tr>
</tbody>
</table>

