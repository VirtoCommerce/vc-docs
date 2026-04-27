# Group D — Observability & Operations

## Claim 1: OpenTelemetry support is poorly documented

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support OpenTelemetry for distributed tracing? How do I enable OTEL export to Jaeger or Zipkin?"):
Strong result. A dedicated page exists: `platform/developer-guide/docs/Extensibility/opentelemetry.md`. Module `VirtoCommerce.OpenTelemetry.Web`, requires Platform 3.1002.0+, exports via OTLP gRPC. Compatible collectors named (Grafana Alloy, OpenTelemetry Collector, Aspire Dashboard). Covers metrics, distributed tracing, Serilog-to-OTLP structured logs. Settings documented in `appsettingsjson.md` (`OpenTelemetry.Enabled`, `Endpoint`, `ServiceName`). Troubleshooting section included.

**WebSearch**: not needed (Context7 conclusive).

**Grep** (scope: DOCS):
- `grep -rli "OpenTelemetry|OTLP|OTEL"`: **18 files**.
- Key hits: `PlatformDeveloperGuide/.../Extensibility/opentelemetry.md:3` — "The Open Telemetry module provides OpenTelemetry observability for Virto Commerce Platform (metrics, distributed tracing, and structured logging via OTLP exporter)."
- `PlatformDeveloperGuide/.../Configuration-Reference/appsettingsjson.md:1638` — `### OpenTelemetry` section.
- `PlatformDeveloperGuide/.../Extensibility/opentelemetry.md:73` — Serilog → OTLP with trace/span IDs for correlation.

**Verdict**: ✅ **Well documented**
**Note**: Claim rejected. There is a dedicated module page, a configuration reference entry, a troubleshooting matrix, and cross-links from adjacent extensibility pages. Distributed-tracing scope (ASP.NET Core, HttpClient, EF Core, Hangfire, Elasticsearch, Redis) is spelled out.

---

## Claim 2: Application Insights specifics are poorly documented

**Context7** (`/virtocommerce/vc-docs`, query: "How do I configure Azure Application Insights telemetry for a VirtoCommerce platform deployment?"):
Multiple hits. Backend: `VirtoCommerce:ApplicationInsights` section in `appsettings.json` with adaptive-sampling parameters (`MaxTelemetryItemsPerSecond`, `InitialSamplingPercentage`, ...), plus a Serilog ApplicationInsights sink. Frontend: VC-Shell `useAppInsights` composable with full walkthrough including instrumentation key, cloud role, conditional telemetry, performance/custom event/error tracking helpers.

**WebSearch**: not needed.

**Grep** (scope: DOCS):
- `grep -rli "Application Insights|ApplicationInsights|AppInsights"`: **28 files**.
- Backend: `PlatformDeveloperGuide/.../Configuration-Reference/appsettingsjson.md:55,91,135` — entire `### Application Insights` section plus Serilog sink wiring.
- Dedicated page: `PlatformDeveloperGuide/.../Fundamentals/Logging/application-insights.md` (linked from `key-extensibility-points.md:35`).
- Frontend: `.../custom-apps-development/vc-shell/Essentials/Usage-Guides/implementing-telemetry-with-useappinsights.md` — full tutorial.

**Verdict**: ✅ **Well documented**
**Note**: Claim rejected. Coverage is broad (backend Serilog sink + adaptive sampling parameters + frontend composable with usage patterns).

---

## Claim 3: Prometheus / Grafana integration is absent

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce expose Prometheus metrics? Is there a Grafana dashboard or scrape endpoint?"):
No direct Prometheus scrape endpoint is documented. Grafana is mentioned twice: (a) as an OTLP collector option (Grafana Alloy), (b) in Virto Cloud overview as the bundled metrics visualization backend. No `/metrics` endpoint, no exporter, no dashboard library.

**WebSearch** (query: "commercetools Shopify Magento Prometheus metrics endpoint observability documentation"):
Competitor landscape — commercetools explicitly supports Prometheus via OpenTelemetry Collector. Magento has community Prometheus exporters. Shopify's stack uses Prometheus internally. Direct Prometheus exposure is common in the space.

**Grep** (scope: DOCS):
- `grep -rliE "prometheus|grafana"`: **2 files** (both Grafana only).
- `PlatformDeveloperGuide/.../CLI-tools/virto-cloud-overview.md:52` — "Grafana: For monitoring and metrics visualization." (Virto Cloud managed offering.)
- `PlatformDeveloperGuide/.../Extensibility/opentelemetry.md:92` — Grafana Alloy listed as one OTLP collector.
- Zero hits for `prometheus` (case-insensitive) in the full DOCS scope.

**Verdict**: 🟡 **Mentioned but thin** (leaning 🔴 for self-hosters).
**Note**: Prometheus scraping is achievable indirectly via the OpenTelemetry module + a Prometheus-capable collector, but docs never spell this out, never mention the word "Prometheus," and don't ship dashboards. Grafana is present only as a managed-cloud feature or OTLP collector, not as a self-hosted how-to.

---

## Claim 4: Structured logging (Serilog, NLog, OpenSearch) is thinly documented

**Context7** (`/virtocommerce/vc-docs`, query: "How do I configure Serilog structured logging in VirtoCommerce? Where are the logs written and how to ship to OpenSearch or ELK?"):
Good coverage for Serilog itself: dedicated `Fundamentals/Logging/overview.md`, `extended-logging.md`, `how-to-update.md`, plus the `appsettings.json` reference. Configuration samples for Console / Debug / ApplicationInsights sinks. No dedicated NLog page. No explicit ELK/OpenSearch *logging sink* guide (OpenSearch hits are only for the search provider).

**WebSearch**: not needed.

**Grep** (scope: DOCS):
- `grep -rli "serilog"`: **9 files**.
- Top hits: `PlatformDeveloperGuide/.../Fundamentals/Logging/overview.md`, `.../extended-logging.md`, `.../how-to-update.md`, `Configuration-Reference/appsettingsjson.md:2343` (`### Serilog` config table + example).
- Zero hits for `NLog` in DOCS.

**Verdict**: ✅ **Well documented** (Serilog), 🔴 for NLog.
**Note**: Serilog is first-class. Claim of "thinly documented" is rejected for Serilog but confirmed for NLog — NLog simply isn't mentioned, which is likely correct because the platform standardized on Serilog. Shipping to OpenSearch/ELK as a *log sink* is not shown end-to-end; user would have to infer from the Serilog.Sinks.ApplicationInsights example.

---

## Claim 5: Correlation IDs / trace IDs across services is absent

**Context7** (`/virtocommerce/vc-docs`, query: "How do I propagate correlation IDs and trace IDs across VirtoCommerce services for request tracing?"):
Partial. OpenTelemetry page states that structured logs forwarded via Serilog include "trace and span ID fields… crucial for correlating them with distributed traces." Frontend VC-Shell composable generates W3C trace IDs per page view. No standalone "correlation ID" concept or middleware page.

**WebSearch**: not needed.

**Grep** (scope: DOCS):
- `grep -rliE "correlation[- ]id|correlationId|trace[- ]id|traceId|W3C trace"`: **1 file**.
- Only hit: `.../custom-apps-development/vc-shell/Essentials/composables/useAppInsights.md:103,105` — "Generates unique W3C trace IDs for each page view to enable distributed tracing."
- Zero matches for `correlation id` or `correlationId` in DOCS.

**Verdict**: 🟡 **Mentioned but thin**
**Note**: Trace IDs show up only in the VC-Shell composable context and as a side-effect of the OTel module. No HTTP header documentation (`traceparent`, `X-Correlation-ID`), no guidance on custom propagation between platform ↔ storefront ↔ external services, no middleware example.

---

## Claim 6: Health checks / liveness / readiness probes are poorly documented

**Context7** (`/virtocommerce/vc-docs`, query: "What health check endpoints does VirtoCommerce expose? Are there liveness and readiness probes for Kubernetes?"):
Strong for the `/health` endpoint: dedicated `Tutorials-and-How-tos/How-tos/health-checks.md`, module-level check registration example (`AddHealthChecks().AddCheck<X>("...")`), Docker `HEALTHCHECK` directive, unhealthy JSON response example, Azure App Configuration check, module-loading health check. **No** explicit terms "liveness" or "readiness" / no Kubernetes probe YAML.

**WebSearch**: not needed.

**Grep** (scope: DOCS):
- `grep -rliE "health[- ]?check|liveness|readiness"`: **15 files**.
- Key: `PlatformDeveloperGuide/.../Tutorials-and-How-tos/How-tos/health-checks.md` — dedicated how-to.
- `PlatformDeveloperGuide/.../Fundamentals/Modularity/04-loading-modules-into-app-process.md:123-125` — built-in `/health` endpoint.
- `PlatformDeveloperGuide/.../Fundamentals/Modularity/azure-app-configuration.md:111` — `Degraded` vs `Unhealthy` distinction.
- Zero hits for the word "liveness"; "readiness" appears once in a DevOps context, not a probe context.

**Verdict**: 🟡 **Mentioned but thin** — for `/health` it's ✅; for liveness/readiness split it's 🔴.
**Note**: ASP.NET Core health checks are well covered. The Kubernetes idiom of separate `livenessProbe` / `readinessProbe` (and `startupProbe`) against distinct endpoints is never demonstrated — a self-hoster must map one `/health` to both, which is an anti-pattern the docs don't warn against.

---

## Claim 7: SLIs / SLOs / error budgets are absent

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce define SLIs, SLOs, error budgets, or SRE practices? Any recommended service level objectives?"):
Nothing on SLIs/SLOs/error budgets. Results were best-practice fragments on frontend architecture and API client design — not SRE.

**WebSearch** (query: "commercetools Shopify SLO SLI error budget published service level"):
Competitors publish SLAs (commercetools 99.9% availability SLA). Even commercial SLAs differ from internal SLOs/error budgets, which are an SRE vocabulary VC does not use.

**Grep** (scope: DOCS):
- `grep -rliE "\bSLI\b|\bSLO\b|error budget|service level objective|service level indicator"`: **0 files**.

**Verdict**: 🔴 **Absent**
**Note**: No SRE vocabulary anywhere in user-facing docs. "Uptime," "error budget," "SLO" — none of them. Virto Cloud page mentions "monitoring and alerting" as a managed service but doesn't quantify.

---

## Claim 8: Distributed tracing is absent

**Context7** (`/virtocommerce/vc-docs`, query: "How do I enable distributed tracing with Jaeger, Zipkin, or W3C trace context across VirtoCommerce microservices?"):
Distributed tracing *is* documented, but via OpenTelemetry only. No Jaeger/Zipkin-specific instructions; only "any OTLP-compatible collector." W3C trace-context propagation is mentioned inside the `useAppInsights` composable for frontend.

**WebSearch**: not needed.

**Grep** (scope: DOCS):
- `grep -rliE "distributed tracing|jaeger|zipkin"`: **2 files** (only `opentelemetry.md` and `useAppInsights.md`).
- Zero hits for `jaeger` or `zipkin`.

**Verdict**: 🟡 **Mentioned but thin**
**Note**: Claim partially rejected — distributed tracing as a concept is present under the OTel umbrella. But named backends (Jaeger, Zipkin, Tempo) and an end-to-end example showing a trace spanning platform → storefront → external API are missing. Given VC is not a microservices platform but a modular monolith, the "across microservices" framing of the claim is slightly off, but cross-service (platform ↔ storefront ↔ indexer) tracing is still undocumented.

---

## Claim 9: Metrics (RED, USE) are absent

**Context7** (`/virtocommerce/vc-docs`, query: "What operational metrics does VirtoCommerce track? RED metrics (rate, errors, duration) or USE metrics (utilization, saturation, errors)?"):
Application Insights "Key Metrics to Track" list (page load time, API response time, error rate, feature usage) is the closest match — but framed as product analytics, not SRE RED/USE. No explicit RED or USE taxonomy. OpenTelemetry module "collects metrics" but specifies no catalog.

**WebSearch**: not needed.

**Grep** (scope: DOCS):
- `grep -rliE "RED metric|USE metric|utilization saturation|rate errors duration"`: **0 files**.

**Verdict**: 🔴 **Absent** (as vocabulary); 🟡 for the underlying signals
**Note**: The metrics themselves are collectable via OTel (ASP.NET Core, HttpClient, EF Core, Hangfire, Redis, Elasticsearch instrumentation — per `opentelemetry.md`), but the SRE taxonomy/terminology (RED, USE, golden signals) is entirely absent. A user wanting a shortlist of "what to alert on" gets no guidance.

---

## Claim 10: Alerting / on-call playbooks are absent

**Context7** (`/virtocommerce/vc-docs`, query: "Where are the alerting rules and on-call runbooks for VirtoCommerce production operations? Incident response playbooks?"):
Only two mentions of "monitoring and alerting," both in the `virto-cloud-overview.md` page advertising Virto Cloud as a managed offering ("Provides preconfigured logging, monitoring, and alerting for all environments"). No rules, no thresholds, no runbooks, no incident response guide.

**WebSearch**: not needed.

**Grep** (scope: DOCS):
- `grep -rliE "\balerting\b|runbook|playbook|on-call|oncall|pagerduty|opsgenie|incident response"`: **9 files**.
- Of those 9, most are non-operational (e.g., `displaying-toast-notifications.md` = UI alerts, `notifications.md` = in-app toasts, a `cms-integrations` file references "publishing workflow readiness"). Only `virto-cloud-overview.md:11,27` are legitimate.
- Zero hits for `runbook`, `playbook`, `pagerduty`, `opsgenie`, `on-call`, `oncall`, `incident response`.

**Verdict**: 🔴 **Absent**
**Note**: The grep count of 9 is inflated by UI/"toast alert" matches. Actual operational alerting content is two bullet points advertising a managed-cloud feature. Self-hosters get no alert-rule catalog, no threshold guidance, no runbook template, no incident response flow.

---

## Summary

**Group shape**: VC docs are strong on the *integrations* tier (OpenTelemetry module + Application Insights + Serilog + `/health` endpoint), but weak on the *operations* tier (no SRE vocabulary, no alert rules, no runbooks, no liveness/readiness split, no Prometheus-first workflow, no named backends like Jaeger/Zipkin/Tempo). The pattern is "here's a wire, good luck" — the integration points exist and are documented, but the operational reasoning of "what should you actually monitor, what should you alert on, what do you do when it fires" is delegated to Virto Cloud as a paid managed offering.
