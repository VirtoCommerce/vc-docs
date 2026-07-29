# Configuration

Background Jobs is configured under the **VirtoCommerce** node in **appsettings.json**.

{% include-markdown "../../Configuration-Reference/appsettingsjson.md" start="<!--backgroundjobs-start-->" end="<!--backgroundjobs-end-->" %}

## RabbitMQ engine

When `Provider` is **RabbitMQ**, configure the broker under the **VirtoCommerce:RabbitMQ** node:

```json title="appsettings.json"
"VirtoCommerce": {
  "RabbitMQ": {
    "HostName": "localhost",
    "Port": 5672,
    "UserName": "guest",
    "Password": "guest",
    "VirtualHost": "/",
    "UseDeadLetterQueue": true,
    "DeadLetterQueueSuffix": ".dlq"
  }
}
```

Exhausted jobs are routed to a dead-letter queue named after the original queue plus the configured suffix, for example **default.dlq**.

## Legacy Hangfire mode

When `Provider` is not Hangfire but `EnableLegacyHangfire` is **true**, two paths run side by side:

* The **active engine** runs new jobs, Map and Reduce, and platform recurring jobs.
* **Legacy Hangfire** keeps serving modules that still call the Hangfire API directly, over a separate SQL store.

To run without Hangfire, set `EnableLegacyHangfire` to **false**.

!!! note
    For durable legacy jobs, set `VirtoCommerce:Hangfire:JobStorageType` to a database provider. It defaults to **Memory**.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../extensibility">← Extensibility</a>
    <a href="../../UCP/overview">UCP →</a>
</div>
