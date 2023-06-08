# VideoConnection ==~object~==

The `VideoConnection` is a connection from an object to a list of objects of `VideoType`.

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
    <td class="tg-0pky">A count of the total number of videos in this connection, disregarding pagination. It allows a client to fetch a specific number of videos by specifying the <code>first</code> argument, and then fetch the total count to display information like "5 of 83". In cases where infinite scrolling is employed or the exact count is unknown, this field will return <code>null</code>.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>pageInfo</code> {==<a href="../../PageInfo">PageInfo!</a>==}</td>
    <td class="tg-0pky">Information about pagination in the connection.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>edges</code> {==<a href="../VideoEdge">VideoEdge</a>==}</td>
    <td class="tg-0pky">A list of edges that represent the connections between videos and other related objects.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>items</code> {==<a href="../VideoType">VideoType</a>==}</td>
    <td class="tg-0pky"> A list of all of the objects returned in the connection. This is a convenience field provided for quickly exploring the API; rather than querying for <code>{ edges { node } }</code> when no edge data is needed, this field can be used instead. Note that when clients need to fetch the <code>cursor</code> field on the edge to enable efficient pagination, this shortcut cannot be used, and the full <code>{ edges { node } }</code> version should be used instead.</td>
</tr>
</tbody>
</table>

