# Group G — API Surface (REST/GraphQL/OpenAPI)

## Claim 1: REST API reference completeness (vs inline Swagger)
**Context7** (`/virtocommerce/vc-docs`, query: "Where can I find the complete REST API reference for VirtoCommerce? Is there a standalone API doc site or just inline Swagger UI?"):
Docs direct readers to the live Swagger UI at `https://virtostart-demo-admin.govirto.com/docs/index.html`. A how-to page `swagger-api.md` explains how Swagger is auto-generated from modules, how to enable/disable it via `VirtoCommerce:Swagger` in `appsettings.json`, and that the aggregated spec is served at `/docs/PlatformUI/swagger.json`. There is no written reference prose (no per-endpoint narrative).

**Grep** (scope: DOCS):
- `grep -rli "swagger" DOCS`: 22 files
- `grep -rli "REST API" DOCS`: 23 files
- `grep -rli "openapi" DOCS`: 8 files
- Top hits: `PlatformDeveloperGuide/.../index.md:13` links out to the hosted Swagger and to a GraphQL page; `Tutorials-and-How-tos/How-tos/swagger-api.md:1` — single how-to page, no narrative reference.

**Verdict**: 🟡
**Note**: REST API is discoverable via Swagger UI only — there is no curated reference site or topic-organized endpoint documentation. Developers are pointed at the live Swagger JSON and told to explore.

---
## Claim 2: GraphQL schema reference (Experience API / XAPI) discoverability
**Context7** (`/virtocommerce/vc-docs`, query: "Where is the GraphQL schema reference for VirtoCommerce xAPI / Experience API? Is the schema published as SDL, introspection, or via GraphiQL?"):
Strong coverage — multiple pages under `GraphQL-Storefront-API-Reference-xAPI/`: `getting-started.md`, `graphiql.md`, `curl.md`, `postman.md`, `best-practices.md`, `troubleshooting.md`, `x-api-extensions.md`, plus per-domain folders (`Cart/`, `Catalog/`, `Order/`, `Profile/`, `Back-in-stock/`). GraphiQL ships at `http://{platform}/ui/graphiql`, module-scoped schemas at `/ui/graphiql/{module}`. Schema is exposed via introspection, imported into Postman from GraphiQL.

**Grep** (scope: DOCS):
- `grep -rli "graphql" DOCS`: 124 files
- `grep -rli "xapi|x-api|experience api|graphiql" DOCS`: 104 files
- Dedicated reference tree: `PlatformDeveloperGuide/.../GraphQL-Storefront-API-Reference-xAPI/` with per-type `.md` files (Objects, Queries, Mutations, Subscriptions).

**Verdict**: ✅
**Note**: Easily the best-documented part of the VC API surface. Topic tree mirrors the schema; GraphiQL is front-and-center.

---
## Claim 3: OpenAPI spec download / Postman collection is thin
**Context7** (`/virtocommerce/vc-docs`, query: "How do I download the VirtoCommerce OpenAPI spec file or import a Postman collection?"):
OpenAPI JSON download is explicitly documented: platform-wide at `/docs/PlatformUI/swagger.json` and per-module at `/docs/{module-id}/swagger.json`. A how-to `generating-c-sharp-client.md` walks through feeding it to NSwag. Postman is covered **for GraphQL only** — `.postman_collection.json` files exist for sorting examples and extensibility tests (`GraphQL-Storefront-API-Reference-xAPI/sorting_examples.postman_collection.json`, `postman_extensibility_tests.json`). No REST Postman collection.

**Grep** (scope: DOCS):
- `grep -rli "postman" DOCS`: 10 files
- `grep -rni "swagger.json|openapi.json|postman collection"`: swagger.json documented at `swagger-api.md:16-21`, `generating-c-sharp-client.md:12`; two Postman `.json` collections checked in for GraphQL.

**Verdict**: 🟡
**Note**: OpenAPI download is documented, but there's no curated/versioned Postman collection for REST endpoints (competitors like Shopify/BigCommerce publish these).

---
## Claim 4: API versioning strategy is thin
**Context7** (`/virtocommerce/vc-docs`, query: "How does VirtoCommerce version its REST API? Are breaking changes signaled with a v1/v2 URL prefix or header?"):
No REST/GraphQL API versioning strategy found. What's documented is **module versioning** (SemVer MAJOR.MINOR.PATCH per NuGet module) and **Stable vs Edge bundles** released every ~3 months with migration guides. xAPI upgrade guide `update-xapi-modules.md` describes C# breaking changes (e.g. `AsyncFieldResolver`→`FuncFieldResolver`) but not URL/header versioning. `api-client-integration.md` advises custom clients to "include API version information" without pointing at a canonical version header.

**WebSearch** (query: "Shopify commercetools BigCommerce REST API rate limiting documentation versioning strategy"):
Shopify uses dated versions (`2019-07`) with deprecation schedules; commercetools uses project limits; BigCommerce documents V3 vs V2. VC has no analogue in its docs.

**Grep** (scope: DOCS):
- `grep -rni "API versioning|/api/v1|/api/v2|api-version" DOCS`: 0 meaningful hits.
- `getting-to-know-platform.md:98` — section titled "Versioning and update strategy" but about module/bundle SemVer, not HTTP API.

**Verdict**: 🔴
**Note**: REST/GraphQL URL versioning strategy is absent from docs. VC ties compatibility to module/platform SemVer releases, which is a different mental model than what a Shopify/BigCommerce integrator expects.

---
## Claim 5: Rate limiting / throttling / API quotas are absent
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce rate-limit or throttle REST/GraphQL API calls? Are there API quotas per client or tenant?"):
No rate-limit, throttle, or quota documentation returned. Tool returned unrelated GraphQL query examples.

**WebSearch** (see claim 4 query):
Shopify documents a leaky-bucket limiter with `X-Shopify-Shop-Api-Call-Limit` header and `429 + Retry-After`; BigCommerce documents per-endpoint quotas; commercetools documents per-project limits. All three publish rate-limit pages.

**Grep** (scope: DOCS):
- `grep -rli "rate limit|throttl|quota" DOCS`: 6 files — **all false positives** ("quotation marks", "disk quota" log example, "RFQ (request for quotation)").

**Verdict**: 🔴
**Note**: Completely absent. No 429 handling guidance, no client-side backoff strategy, no note that VC is self-hosted and therefore rate-limiting is the operator's problem — which itself would be valuable documentation.

---
## Claim 6: Idempotency keys on POST endpoints are absent
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support idempotency keys for POST API calls to prevent duplicate order creation?"):
No results addressing idempotency keys. Context7 returned the `createOrderFromCart` mutation spec (which does not describe idempotency semantics).

**Grep** (scope: DOCS):
- `grep -rli "idempoten" DOCS`: 2 files. Spot-check shows these are generic mentions, not documented idempotency-key header contracts (Stripe-style `Idempotency-Key`).

**Verdict**: 🔴
**Note**: No documented idempotency-key mechanism for non-idempotent POSTs (order creation, payment submission, cart mutation). Industry baseline (Stripe, Shopify checkout) expects this.

---
## Claim 7: Pagination / filtering / sorting conventions are thin
**Context7** — already covered above; GraphQL connection edges, cursors, and `searchPhrase`/`filter`/`sort` arguments are documented per-query.

**Grep** (scope: DOCS, within `GraphQL-Storefront-API-Reference-xAPI/`):
- 37 files mention sort/filter/filtering; per-type `.md` files (`contacts.md:11`, `organizations.md:11`) define `searchPhrase` / `filter` / `sort` arguments.
- Dedicated Postman sorting-examples collection checked in (`sorting_examples.postman_collection.json`).
- `search-query-syntax-reference.md` documents the `phrase` search syntax used in both REST and GraphQL.

**Verdict**: ✅
**Note**: For GraphQL the conventions are clear (Relay-style connections + `searchPhrase` + `sort` string). REST-side conventions are inferred from the Swagger JSON rather than documented narratively, but at least one reference (`search-query-syntax-reference.md`) exists.

---
## Claim 8: Long-polling / webhooks / server-sent events / WebSockets are thin
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support webhooks, server-sent events, or WebSockets for real-time notifications on orders and inventory?"):
Strong coverage across three mechanisms: (a) **Webhooks** module — dedicated `Fundamentals/Event-Driven-Development/webhooks.md` describing POST-based delivery, JSON payload, Basic/Bearer/Custom Header auth; (b) **SignalR/WebSockets** for push notifications (`pushNotificationHub`, `RedisBackplane`/`AzureSignalRService` scalability modes, `ForceWebSockets` flag); (c) **GraphQL subscriptions** over WebSockets (e.g., `orderStatusChanged`).

**Grep** (scope: DOCS):
- `grep -rli "webhook|server-sent|websocket|signalr|long.?poll" DOCS`: 41 files.
- `appsettingsjson.md:1753-1769` — full SignalR/WebSockets config block.
- Sanity CMS integration (`sanity-setup.md`) is a concrete webhook consumer example.

**Verdict**: ✅
**Note**: All three channels documented. No SSE, but SSE is genuinely unused (⚪ for SSE specifically). Webhook retry/signing semantics are still thin — see also Group C claim 3.

---
## Claim 9: API pagination cursor vs offset is thin
**Context7** — covered via claims 2/7.

**Grep** (scope: DOCS):
- `grep -rni "cursor" PlatformDeveloperGuide`: 144 hits across the GraphQL reference tree — cursor-based Relay connections are the idiomatic GraphQL pattern (`ProductEdge.cursor`, `PageInfo`, `before`/`after` args).
- `grep -rni "skip.*take"`: explicit offset pagination (`skip`, `take`, `MaxResultWindow`) documented in `appsettingsjson.md:1043`, `x-api-extensions.md:238`, `event-bus-configuration.md:146`.

**Verdict**: 🟡
**Note**: Both conventions are used — cursor in GraphQL storefront API, skip/take in REST search — but the docs never explicitly contrast them or tell readers when to use which. Developer has to infer.

---
## Claim 10: API error-model standard (Problem+JSON / RFC 7807) is absent
**Context7** (`/virtocommerce/vc-docs`, query: "What is the API error response format in VirtoCommerce? Does it follow Problem+JSON / RFC 7807 ProblemDetails standard?"):
No mention of Problem+JSON / RFC 7807 / `ProblemDetails`. Docs return HTTP status-code lists (204/400/403/404 for PATCH; GraphQL `errors[]` field) but no standardized error-envelope spec.

**Grep** (scope: DOCS):
- `grep -rli "problem.?json|rfc 7807|rfc7807|problemdetails" DOCS`: 0 files.
- `grep -rni "problem\+json|application/problem|problemdetails" DOCS`: 0 hits.
- HTTP status lists exist (`update-using-patch.md`) but no unified error schema.

**Verdict**: 🔴
**Note**: RFC 7807 `application/problem+json` is the default in ASP.NET Core since .NET 7 (and VC runs on .NET 10 per `upgrading-to-dot-net-10.md`), so responses likely are ProblemDetails-shaped at the framework level, but docs neither confirm nor document the envelope. Developers coding against errors have to discover the shape empirically.

---

