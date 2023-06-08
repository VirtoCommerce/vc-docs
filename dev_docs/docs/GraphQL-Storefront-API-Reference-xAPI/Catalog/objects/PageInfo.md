# PageInfo ==~object~==

The `PageInfo` provides information about pagination in a connection.
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
    <td class="tg-0pky"><code>hasNextPage</code> {==Boolean!==}</td>
    <td class="tg-0pky">Indicates whether there is a next page of data available.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>hasPreviousPage</code> {==Boolean!==}</td>
    <td class="tg-0pky">Indicates whether there is a previous page of data available.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>startCursor</code> {==String==}</td>
    <td class="tg-0pky"> The cursor or identifier of the first item in the current page.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>endCursor</code> {==String==}</td>
    <td class="tg-0pky"> The cursor or identifier of the last item in the current page.</td>
</tr>
</tbody>
</table>

