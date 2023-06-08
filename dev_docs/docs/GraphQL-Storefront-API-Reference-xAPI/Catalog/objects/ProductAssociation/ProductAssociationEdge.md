# ProductAssociationEdge ==~object~==

The `ProductAssociationEdge` represents an edge in a connection between a vendor and associated products.

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
    <td class="tg-0pky"><code>cursor</code> {==String!==}</td>
    <td class="tg-0pky">A string representing a cursor that can be used for pagination purposes. It does not denote the count of objects in the connection, but rather provides a reference point for retrieving the next set of results or navigating through the associated products. The cursor allows clients to fetch specific subsets of objects in a connection without having to retrieve all items at once.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>node</code> {==<a href="../ProductAssociation">ProductAssociation</a>==}</td>
    <td class="tg-0pky">Serves as a node in the connection graph, connecting the vendor to the associated product.</td>
</tr>
</tbody>
</table>

