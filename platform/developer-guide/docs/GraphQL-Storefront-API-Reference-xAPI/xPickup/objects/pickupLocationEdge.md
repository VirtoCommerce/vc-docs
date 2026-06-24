# PickupLocationEdge ==~object~==

This type represents an edge in a pickup location connection. Each edge includes a pagination cursor and the pickup location node it points to.

## Fields

| Field                         | Description                                                   |
| ----------------------------- | ------------------------------------------------------------- |
| `cursor` ==String!==          | A cursor used for paginating through pickup location results. |
| `node` ==[PickupLocationType](pickupLocationType.md)== | The pickup location object associated with this edge.         |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../CartPickupLocationConnection">← cartPickupLocationConnection</a>
    <a href="../ProductPickupAvailabilityType">productPickupAvailabilityType →</a>
</div>
