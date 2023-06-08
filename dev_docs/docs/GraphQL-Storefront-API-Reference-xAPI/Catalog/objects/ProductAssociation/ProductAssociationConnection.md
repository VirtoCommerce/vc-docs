# ProductAssociationConnection ==~object~==

The `ProductAssociationConnection` represents a connection from an object to a list of objects of the `ProductAssociation` type. It facilitates pagination and retrieval of associated product associations.

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
    <td class="tg-0pky">An integer representing the total count of objects in this connection, disregarding pagination. This count allows clients to fetch the first set of objects by specifying a limit, such as "5", and retrieve the total count to display information like "5 of 83". In cases where the exact count is unknown or infinite scrolling is implemented, this field will return <code>null</code>.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>pageInfo</code>  {==<a href="../../PageInfo">PageInfo</a>==}</td>
    <td class="tg-0pky">Information about the pagination in the connection, including details about the current page, total pages, and page size. It provides data necessary for implementing pagination logic and navigating through the associated product associations.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>edges</code> {==<a href="../ProductAssociationEdge">ProductAssociationEdge</a>==} </td>
    <td class="tg-0pky"> A list of edges that represent the connections between nodes in the `ProductAssociationConnection`.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>items</code>  {==<a href="../ProductAssociation">ProductAssociation</a>==}</td>
    <td class="tg-0pky"> A list of <code>ProductAssociation</code> objects returned in the connection. This field is provided as a convenience for quickly exploring the API. It allows fetching all the associated product associations without querying for the edges explicitly. Note that this shortcut cannot be used if clients require the <code>cursor</code> field on the edge for efficient pagination. In such cases, the full <code>{ edges { node } }</code> version should be used instead.</td>
</tr>
</tbody>
</table>

