# Integration Failure Handling

Virto Commerce integrates with external systems (ERPs, CRMs, OMSs, warehouse-management systems, tax engines) through a small set of primitives. Each primitive has its own retry, failed-message, and observability story. This page consolidates them.

!!! note
    There is no first-class "ERP integration" feature in the Platform. The patterns here apply to any outbound integration code, regardless of which external system sits on the other side.

## Integration primitives

Virto Commerce exposes four primitives for outbound and inbound integration with external systems:

| Primitive | Used for | Failure surface |
| --- | --- | --- |
| Webhooks | Push domain events to external HTTP endpoints. | Delivery error log in the Admin UI. |
| Hangfire background jobs | Scheduled or fire-and-forget background work, including most custom outbound integrations. | Hangfire **Failed** tab in the dashboard. |
| Domain event handlers | In-process reactions to domain events within the same Platform process. | Application logs only. |
| Inbound REST and GraphQL | External systems calling into the Platform. | HTTP response status; caller-side concern. |

The rest of this page covers each primitive against four operational questions: retry policy, where failures surface, how to wire alerts, and where incident history lives.

## Retry policy

Each primitive applies retry differently.

### Webhooks

The Webhooks module retries failed deliveries with intervals that increase exponentially. Retry attempts and the backoff schedule are configured globally for the Webhooks module via **Settings** → **Webhooks** → **General**; there is no per-webhook override. See [Webhooks settings](/platform/user-guide/latest/webhooks/settings/) for the configuration surface, and [Webhooks module overview](/platform/user-guide/latest/webhooks/overview/) for the broader feature description.

### Hangfire background jobs

Hangfire wraps each job execution in its own retry policy with exponential backoff. The retry count and intervals are configurable per job in code via the `[AutomaticRetry]` attribute. Verify the exact attempt count and intervals against the job's source before relying on a specific number.

### Domain event handlers

In-process domain event handlers run once. There is no built-in retry layer. If a handler must survive transient failures, wrap its work in a Hangfire job and let Hangfire retry the job. See [Using domain events](../Fundamentals/Event-Driven-Development/using-domain-events.md).

### Inbound REST and GraphQL

The Platform does not retry inbound requests. The caller owns retry, idempotency, and backoff. Custom inbound endpoints that depend on retried submissions should accept an idempotency key and deduplicate server-side.

## Failed-message surface

When retries are exhausted, failures land in one of these places:

| Primitive | Where to look |
| --- | --- |
| Webhooks | Admin UI: [Webhooks](/platform/user-guide/latest/webhooks/overview/) module → delivery error log. |
| Hangfire jobs | Admin UI: [System Operations](/platform/user-guide/latest/system-operations/overview/) → **Hangfire** → **Failed** tab. |
| Domain event handlers | Application logs (Serilog targets: console, Application Insights, Seq). |
| Inbound REST and GraphQL | Application logs and HTTP response codes captured by telemetry. |

The Webhooks module preserves the error message and response payload for each failed delivery, so an operator can read the actual server response without re-triggering the call. The Hangfire dashboard shows each failed attempt with its stack trace and runtime, and exposes a manual retry action.

### Dead-letter queue

The Platform does not ship a first-class dead-letter queue. Functionally, the Hangfire **Failed** tab and the Webhooks error log fill the same role. They hold messages whose retries are exhausted and that need human attention. Manual retry is available in both surfaces.

If you need true DLQ semantics (automatic quarantine, separate metrics, replay tooling), that is a custom build on top of these primitives.

## Alerting hookups

The Platform does not include a first-party alerting feature. Alerts are wired through the logging integrations:

* [Application Insights](../Fundamentals/Logging/application-insights.md). Configure Azure Monitor alert rules over log queries.
* [Seq module](../Fundamentals/Logging/seq-module.md). Configure Seq alerts on signals or queries.

Both targets can route to email, Slack, PagerDuty, or Microsoft Teams via their respective alert channels. Webhook and Hangfire failures both log structured errors that are queryable from these tools. Setting up the alert rule is the operator's responsibility; the Platform does not ship default rules.

## Incident history and forensics

Retention varies by source.

| Source | Retention | Note |
| --- | --- | --- |
| Webhook error log | Persisted in the Platform database. | Available until manually cleared. |
| Hangfire job history | Persisted in the Platform database. | Subject to Hangfire's retention configuration. |
| Application Insights | Per the workspace's retention policy. | Azure default 90 days; configurable. |
| Seq | Per the Seq retention configuration. | Operator-controlled. |

There is no unified "integration incident" view that stitches these together. Forensics requires correlating timestamps across the relevant stores.

## What Platform does not provide

For operators sizing the Platform against an integration-heavy environment, the honest gaps are:

* No central integration-failure dashboard. Three or four surfaces to check and no unified view across them.
* No first-class dead-letter queue. Failed jobs and webhook deliveries persist, but there is no quarantine, no DLQ-specific tooling, and no built-in replay-from-DLQ workflow.
* No first-party alerting policy. No default alert rules ship with the Platform; alerting is delegated to Application Insights or Seq and configured per deployment.
* No documented retry semantics for domain event handlers or inbound APIs. Custom integration code must follow ASP.NET, MediatR, and Hangfire conventions directly.
* No incident timeline or postmortem feature. Operators reconstruct events from logs.

## On-call runbook: integration failure

When paged about a failing outbound integration:

1. Open Platform → Developer Tools → **System Operations** → **Hangfire** and check the **Failed** tab. If the integration runs as a Hangfire job, this is the most common landing site for the error.
1. If the integration uses Webhooks, open the **Webhooks** module and inspect the delivery error log for the failing endpoint.
1. If neither shows the failure, query the structured logs in Application Insights or Seq, filtered by the integration's log scope or correlation ID.
1. Run the Platform [health check](../Tutorials-and-How-tos/How-tos/health-checks.md) to rule out a broader Platform issue such as database connectivity, asset storage, or the search backend.
1. After identifying the root cause, decide whether to retry manually (the Hangfire dashboard and the Webhooks UI both expose retry actions) or to escalate.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../maintenance-tasks-for-sql">← Maintenance tasks for SQL</a>
    <a href="../../Tutorials-and-How-tos/overview">Tutorials and how-tos  →</a>
</div>
