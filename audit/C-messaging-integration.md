# Group C — Messaging & Integration

## Claim 1: Azure Service Bus usage is poorly documented

**Context7** (`/virtocommerce/vc-docs`, query: "How does VirtoCommerce use Azure Service Bus for messaging?"):
Context7 returned Event Bus + Azure **Event Grid** docs (the official Virto destination provider for the Event Bus module) and Redis-as-backplane docs. Nothing came back for Azure **Service Bus** as a broker. The platform's Event Bus uses Azure Event Grid (CloudEvents 1.0 payload), not Service Bus.

**WebSearch**: Not needed — Context7 definitive. Virto's official integration = Event Grid.

**Grep** (scope: DOCS):
- `grep -rli "Azure Service Bus" DOCS`: 0 files
- `grep -rli "AzureServiceBus" DOCS`: 0 files
- `grep -rli "ServiceBus" DOCS`: 0 files
- Azure Event Grid is covered: `PlatformDeveloperGuide/.../event-bus.md:22`, `event-bus-configuration.md:158` — "Destination providers. Azure Event grid".

**Verdict**: ⚪ Not applicable (claim mis-named). Azure **Service Bus** is not a Virto feature — the broker claim should be about Azure **Event Grid**, which **is** documented (albeit thinly compared to a proper "delivery guarantees / DLQ / schema registry" write-up). Treat the "Azure Service Bus" gap as an artifact of external naming confusion.
**Note**: Docs cover Event Grid as the supported destination provider. If the reviewer really meant "Service Bus is missing from docs", the absence is correct — Virto doesn't use it.

---

## Claim 2: RabbitMQ / Kafka / external broker integration is absent

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support RabbitMQ or Kafka as a message broker?"):
No RabbitMQ or Kafka hits at all. Context7 surfaced Event Bus, SMTP/SendGrid, and Redis as the eventing/notification surface. Event Bus Destination Provider list is exhausted by Azure Event Grid in public docs.

**WebSearch**: Skipped — Context7 + grep unanimous.

**Grep** (scope: DOCS):
- `grep -rli "RabbitMQ" DOCS`: 0
- `grep -rli "Kafka" DOCS`: 0
- `grep -rli "AMQP" DOCS`: 0
- `grep -rli "MassTransit|NServiceBus" DOCS`: 0

**Verdict**: 🔴 Absent
**Note**: No mention of RabbitMQ, Kafka, AMQP, MassTransit, or NServiceBus anywhere in user-facing docs. The Event Bus abstraction allows custom destination providers, but docs show only Event Grid — effectively Azure-only. Major gap for on-prem / AWS / multi-cloud customers.

---

## Claim 3: Webhooks (delivery guarantees, retries, signatures) are thinly documented

**Context7** (`/virtocommerce/vc-docs`, query: "How does VirtoCommerce deliver webhooks with retries, signatures and delivery guarantees?"):
Hits: `webhooks.md` describes the module (POST+JSON, Basic / Bearer / Custom Header auth, configurable exponential-backoff retry). Nothing on HMAC payload signatures, replay protection, or explicit at-least-once / ordering guarantees. Event Grid page has a one-liner on "at least one delivery per subscription".

**WebSearch**: Not needed for this level of specificity.

**Grep** (scope: DOCS):
- `grep -rli "webhook" DOCS`: 162 files (heavy — lots of references in CMS / Sanity / third-party integration guides)
- Retry: only one substantive line `webhooks.md:21` — "The retry policy is configurable, with intervals that increase exponentially." No numbers, no max attempts, no DLQ.
- Signatures: zero substantive hits (`HMAC`, `X-Signature`, `webhook secret` → all false positives in image URLs / JWT docs).
- `grep -rni "dead letter|at.least.once|exactly.once"` in Event/webhook docs: 0 beyond the single Event Grid line.

**Verdict**: 🟡 Mentioned but thin
**Note**: The webhook module exists and is referenced everywhere, but operational properties (signature verification, retry budget, DLQ, idempotency requirement on receiver) are under-explained. The `webhooks.md` page is 42 lines total — light for a production-critical feature. Compare to Stripe / Shopify webhooks docs.

---

## Claim 4: Outbox pattern / transactional messaging is absent

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce implement the outbox pattern for transactional messaging?"):
No direct results. Top matches were unrelated: GraphQL push messages, xAPI CQRS via MediatR, "messages are an API integration method … ensure transactional integrity" (a generic line, not outbox).

**WebSearch** (query: "e-commerce platforms outbox pattern transactional saga webhook delivery 2025"):
Outbox + Saga is the canonical reliable-event pattern in 2025 (Netflix/DoorDash/Uber/Stripe/Amazon cited). Industry expects either explicit outbox or a managed eventing service (Event Grid/Kinesis) for at-least-once delivery.

**Grep** (scope: DOCS):
- `grep -rli "outbox" DOCS`: 0 (the only `outbox` hit in the whole corpus is a JS identifier `layoutBox` inside a GraphiQL bundle — false positive).
- `grep -rli "transactional outbox|inbox pattern" DOCS`: 0

**Verdict**: 🔴 Absent
**Note**: Zero outbox/inbox pattern docs. Domain events fire via in-process dispatcher (`using-domain-events.md`); reliability across the DB↔webhook/Event-Grid boundary is not discussed. A common production question ("if my DB commits but the webhook fails, do I lose the event?") has no answer.

---

## Claim 5: Saga / process manager / long-running workflows are absent

**Context7**: Covered by the same query as Claim 4 — no saga / process-manager content returned.

**WebSearch** (shared with Claim 4): Saga pattern is industry-standard for distributed e-commerce (cart → order → payment → fulfillment).

**Grep** (scope: DOCS):
- `grep -rli "saga" DOCS`: 0 relevant (only `layoutBox` / CSS font-data false positives in bundled GraphiQL JS).
- `grep -rli "process manager|long.running workflow" DOCS`: 4 files, all about Hangfire background jobs / approval processes — not the DDD/saga concept.

**Verdict**: 🔴 Absent
**Note**: No saga / process-manager / orchestration vocabulary. Order state transitions exist but are not framed as a saga. Long-running / compensating-transaction patterns are absent from docs. Big gap when discussing multi-step checkout, split-shipment, or subscription billing.

---

## Claim 6: Idempotency keys / idempotent consumers are absent

**Context7** (`/virtocommerce/vc-docs`, query: "How does VirtoCommerce handle idempotency keys for API calls and events?"):
No hits for idempotency keys on REST/POST endpoints. Results were about generic API-key authentication, not idempotency.

**WebSearch**: Not needed — Context7 + grep show a near-total absence.

**Grep** (scope: DOCS):
- `grep -rli "idempot" DOCS`: 5 files, but only 2 substantive docs mentions:
  - `CLI-tools/overview.md:36` — "idempotent SQL scripts" (migration context, not messaging).
  - `custom-apps-development/vc-shell/Essentials/composables/useNotifications.md:144` — "Design notification handlers to be idempotent if possible, as notifications could … be delivered more than once." (Two lines; frontend context.)
- CODE has idempotent delete behavior in `CartAggregate.cs` and tests, but no docs explanation.

**Verdict**: 🔴 Absent
**Note**: Stripe-style `Idempotency-Key` header on POST endpoints, idempotent consumer patterns for webhook receivers, and deduplication guidance for domain-event handlers are not in docs. The one useful line is buried in a vc-shell composable README. Critical gap for payments / orders.

---

## Claim 7: Event bus / domain events are poorly documented

**Context7**: Rich results — `event-bus.md`, `event-bus-configuration.md`, `using-domain-events.md`, `webhooks.md`, plus user-guide `event-bus/overview.md`. Publish-subscribe model, CloudEvents 1.0, Azure Event Grid provider, domain-event POCOs + handler registration, side-effects framing.

**WebSearch**: Not needed.

**Grep** (scope: DOCS):
- `grep -rli "domain event|event bus|eventbus" DOCS` (Platform\*Guide + VirtoCommerce): 20 files.
- `PlatformDeveloperGuide/.../using-domain-events.md` is a dedicated conceptual doc.
- `Extensibility/key-extensibility-points.md:16` cross-links it.

**Verdict**: ✅ Well documented (at the "what and how to register" level)
**Note**: The Event Bus + domain-events documentation is one of the stronger areas in this group. What's missing is the operational reliability layer (outbox, DLQ, delivery guarantees beyond Event Grid's at-least-once line, error-handling strategy) — but conceptually + API-wise the event bus is covered.

---

## Claim 8: EDI / cXML / Punchout (OCI) integration is absent/thin

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support EDI, cXML, OCI punchout or B2B e-procurement integration?"):
Returned generic B2B storefront setup, "Integration middleware like Logic App transforms API messages", and the Integration Pack (Avatax, Authorize.net). No dedicated EDI / cXML / OCI / punchout module surfaced.

**WebSearch**: Skipped — Context7 + grep adequate.

**Grep** (scope: DOCS):
- `grep -rlw "EDI" DOCS`: 0 files (whole-word; case-sensitive). All lowercase "edi" hits were false positives (`editorconfig`, `extensions`, etc.).
- `grep -rni "punchout|cXML|OCI catalog"` hits:
  - `VirtoCommerce/blog.md:41` — "Virto Commerce and Greenwing Technology Join Forces to Deliver Scalable Punchout Solutions" (blog post).
  - `VirtoCommerce/our-partners.md:23` — Greenwing partner listing for punchout / Ariba / Jaggaer / Coupa.
  - `B2BExperts/docs/E-procurement-the-other-side-of-the-b2b-marketplace.md:26` — argues marketplaces *replace* the need for punchout.

**Verdict**: 🔴 Absent (developer integration docs) / 🟡 in marketing material
**Note**: Docs give a blog post + partner mention. No developer-facing guide for cXML/OCI handshake, PunchOutSetupRequest, EDI 850/855/856/810 transactions, or AS2/SFTP mapping — surprising for a B2B-first platform that lists Greenwing as a partner.

---

## Claim 9: ETL / data-pipeline integration (Kafka Connect, Airflow) is absent

**Context7**: No dedicated data-pipeline docs returned. Integration story in docs is "REST/GraphQL + webhooks + Logic Apps".

**WebSearch**: Skipped — comfortable with grep.

**Grep** (scope: DOCS):
- `grep -rlw "ETL" DOCS`: 0 files.
- `grep -rli "Airflow|Kafka Connect|Fivetran|Logstash" all docs`: 0 files.
- Integration is instead framed around "Logic App / Azure Functions / webhooks" (`multiregional-ecommerce.md`, `event-bus-configuration.md`).

**Verdict**: 🔴 Absent
**Note**: Zero mention of industry-standard data-pipeline tooling. Bulk import/export exists (Data-Import / vc-module-import), but is not positioned as an ETL surface and has no guidance for Airflow / Prefect / Dagster / Kafka Connect integration. Customers doing analytics pipelines or ERP sync must invent the pattern themselves.

---

## Claim 10: gRPC / service-to-service RPC is absent

**Context7**: No results framing VC service surface as gRPC. Only incidental mention of OTLP/gRPC as an OpenTelemetry exporter.

**WebSearch**: Skipped.

**Grep** (scope: DOCS):
- `grep -rwni "gRPC"` in user-facing docs: **2 hits**, both in OpenTelemetry docs (`opentelemetry.md:112`, `appsettingsjson.md:1647`) — describing OTLP exporter endpoint, not a VC RPC surface.
- `grep -rli "protobuf|protocol buffer" all docs`: 6 files, none are VC RPC contracts.

**Verdict**: 🔴 Absent (as a VC feature); ⚪ correctly absent (VC is not a gRPC platform)
**Note**: VC exposes REST + GraphQL only; gRPC is not offered. The absence is correct; the claim is confirmed. The only mentions are as a downstream observability protocol. Docs don't explicitly state "we don't do gRPC" — a short FAQ line would help enterprise architects evaluating MACH stacks.

---

## Overall shape

**Strong**: Domain events + Event Bus (publish/subscribe, Azure Event Grid, CloudEvents 1.0) are conceptually documented with a dedicated guide and configuration reference. Webhooks module exists and is referenced widely. Redis backplane + Hangfire scalability docs exist for cache/job coordination.

**Weak**: The *reliability* layer around messaging is almost entirely missing — no outbox/inbox, no saga/process-manager vocabulary, no idempotency keys on POST APIs, no webhook signature/HMAC guidance, no DLQ/retry-budget numbers. Broker choice is effectively Azure-only (Event Grid); RabbitMQ/Kafka/Service Bus/MassTransit have zero mentions, making non-Azure deployments a blank page. B2B-critical integrations (EDI, cXML, OCI punchout) appear only in marketing / partner pages, not as developer guides. ETL/data-pipeline positioning (Airflow, Kafka Connect) is absent. gRPC is correctly unused but that's not stated anywhere.

**Net**: The group exposes a documentation posture that is Azure-centric, in-process-events-first, and light on distributed-system reliability patterns that enterprise B2B buyers expect in 2025.
