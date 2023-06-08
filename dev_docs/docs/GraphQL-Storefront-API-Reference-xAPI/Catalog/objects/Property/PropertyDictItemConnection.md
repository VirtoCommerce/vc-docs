# PropertyDictionaryItemConnection ==~object~==

The `PropertyDictionaryItemConnection` is a connection type that facilitates pagination and retrieval of `PropertyDictionaryItem` objects.
<br>
<br>
<br>
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
    <td class="tg-0pky"><code>totalCount</code> {==Int==}</td>
    <td class="tg-0pky"> An integer representing the total count of objects in this connection, disregarding pagination. Clients can use this information to fetch a specific number of objects and display the total count. In cases where the count is unknown or infinite scrolling is employed, this field will return `null`.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>PageInfo</code> {==<a href="../../PageInfo">PageInfo!</a> ==}</td>
    <td class="tg-0pky">Information about pagination in the connection, such as the current page, total pages, and page size.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>PropertyDictionaryItemEdge</code> {==<a href="../PropertyDictItemEdge">PropertyDictionaryItemEdge</a>==}</td>
    <td class="tg-0pky"> A list of edges that represent the connections between nodes in the `PropertyDictionaryItemConnection`. Each edge contains a cursor for pagination and the corresponding `PropertyDictionaryItem`.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>items</code> {==<a href="../PropertyDictItem">PropertyDictionaryItem</a>==}</td>
    <td class="tg-0pky"> A list of all of the objects returned in the connection.</td>
</tr>
</tbody>
</table>
