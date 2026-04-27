# Group F — Architecture Patterns

## Claim 1: "Domain-Driven Design" explicit references in docs
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce follow Domain-Driven Design? aggregates, bounded contexts, ubiquitous language?"):
Returned generic "SOLID + clean code" tech-stack blurb and Data Mapper references. Zero explicit DDD framing. xAPI doc (seen under claim 4) does say "CQRS and DDD principles" in passing.

**WebSearch**: not required — Context7 returned a result; term prevalence in .NET e-commerce confirmed under claim 4.

**Grep** (DOCS):
- `grep -rli "domain-driven design|domain driven design"` DOCS: **0 files**
- `grep -rliw "DDD"` DOCS: **2 files**
  - `PlatformDeveloperGuide/.../Fundamentals/Modularity/01-overview.md:177` — outbound link to infoq "Context mapping pattern" (uses `ddd-contextmapping` in URL only)
  - `PlatformDeveloperGuide/.../GraphQL-Storefront-API-Reference-xAPI/x-api-extensions.md:460` — "xAPI is built using the clean architecture based on CQRS and DDD principles"

**Grep** (CODE):
- `grep -rli "domain-driven design|domain driven design"` CODE: **0 files**

**Verdict**: 🔴 **Absent** (DDD as explicit architectural framing). Two bare "DDD" acronym drops don't qualify as documentation of the approach.
**Note**: Docs repeatedly use DDD vocabulary (domain, repository, aggregate in class names) without ever *naming* DDD as the mental model.

---

## Claim 2: "Aggregate root" / "bounded context" / "ubiquitous language" usage
**Context7**: (folded into claim 1 query) — no hits for any of the three phrases.

**WebSearch**: not required.

**Grep** (DOCS):
- `grep -rli "aggregate root|aggregateroot"` DOCS: **0 files**
- `grep -rli "bounded context"` DOCS: **1 file** (`Modularity/01-overview.md` — outbound link anchor only, not body prose)
- `grep -rli "ubiquitous language"` DOCS: **0 files**

**Grep** (CODE):
- `grep -rli "aggregate root|aggregateroot"` CODE: **0 files**
- `grep -rli "bounded context"` CODE: **0 files**
- `grep -rli "ubiquitous language"` CODE: **0 files**

**Verdict**: 🔴 **Absent**. Core DDD building-block vocabulary is nowhere in VC docs, site, or source trees crawled.
**Note**: VC modules *implement* aggregate boundaries (Order aggregate with line items, Cart aggregate, Catalog aggregate) but the docs never label them as such.

---

## Claim 3: "Repository pattern" / "unit of work" usage
**Context7** (`/virtocommerce/vc-docs`, query: "repository pattern unit of work in VirtoCommerce; how is IRepository used?"):
Strong results. VC officially uses `DbContextRepositoryBase`, `IOrderRepository`, `IUnitOfWork` as first-class extensibility points. "Virto Commerce utilizes the **Data Mapper pattern** to isolate the domain from the persistence layer" (extending-domain-models.md). Sample code `public BlogRepository(MyCoolModuleDbContext dbContext, IUnitOfWork unitOfWork = null)`.

**WebSearch**: not required — Context7 + grep sufficient.

**Grep** (DOCS):
- `grep -rli "repository pattern"` DOCS: **0 files** (term itself never appears)
- `grep -rli "unit of work|unitofwork"` DOCS: **4 files** — concurrency-handling.md, creating-custom-module.md (x2), extending-domain-models.md (all via code examples calling `IUnitOfWork` / `repository.UnitOfWork.CommitAsync()`)

**Grep** (CODE):
- `grep -rli "IRepository"` CODE: **204 files** (243 occurrences)
- `grep -rli "UnitOfWork"` CODE: **89 files** (66 `IUnitOfWork` occurrences in backend)

**Verdict**: 🟠 **Implemented but undocumented by name**. Pattern is foundational in VC (every module has repositories + UoW), samples exist, but neither "repository pattern" nor "unit of work" is ever explained *as a pattern* in the docs — only used in code snippets. Docs do prefer the term "Data Mapper pattern" which is related but distinct.
**Note**: A developer searching "VirtoCommerce repository pattern" would find nothing in user-facing docs.

---

## Claim 4: "CQRS" usage
**Context7** (captured under claim 6): "Virto Commerce xAPI modules implement the CQRS pattern using MediatR for handling queries and mutations." "xAPI is built using the clean architecture based on CQRS and DDD principles."

**WebSearch** (query: ".NET e-commerce platform architecture CQRS MediatR Polly feature flags 2026 prevalence"): CQRS + MediatR is *the* canonical modern-.NET-commerce stack; virtually every reference implementation (eShopOnContainers, codewithmukesh, aspnetrun) pairs them. MediatR went commercial July 2025 — worth noting.

**Grep** (DOCS):
- `grep -rliw "CQRS"` DOCS: **2 files** (both under `GraphQL-Storefront-API-Reference-xAPI/`) — `custom-module-creation.md:74,123` and `x-api-extensions.md:460`

**Grep** (CODE):
- `grep -rliw "CQRS"` CODE: **2 files** (sparse — the pattern is implemented throughout but the acronym itself is rare in source)

**Verdict**: 🟡 **Mentioned but thin**. CQRS is explicitly named *only* in the xAPI / GraphQL corner — never as a general platform architectural concept. No dedicated page explains command vs. query, handlers, pipeline behaviors, or validation placement.
**Note**: For the primary `vc-module-*` REST services CQRS framing is never surfaced to readers even though MediatR handlers are shipped in modules like customer-review.

---

## Claim 5: "Event sourcing" usage
**Context7** (covered under claim 1): no event-sourcing references returned.

**WebSearch**: not required — grep conclusive.

**Grep** (DOCS):
- `grep -rli "event sourcing|eventsourcing"` DOCS: **0 files**

**Grep** (CODE):
- `grep -rli "event sourcing|eventsourcing"` CODE: **0 files**

**Verdict**: ⚪ **Not applicable**. VC doesn't do event sourcing — it's a CRUD/EF Core platform with domain events on top. Absence is correct positioning, not a gap.
**Note**: Worth a one-line "VC is not event-sourced; state is current-value CRUD with domain-event notifications" disambiguation for developers arriving from eShopOnContainers-style stacks.

---

## Claim 6: "Mediator" (MediatR) usage in docs (codebase uses it)
**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce use MediatR mediator pattern for command/query handlers?"):
Yes, explicit: "xAPI modules implement the CQRS pattern using MediatR", `services.AddMediatR(...)`, `OverrideCommandType<...>().WithCommandHandler<...>()`. Documented only within the xAPI/GraphQL chapter.

**WebSearch**: see claim 4 — MediatR is ubiquitous in modern .NET e-commerce; MediatR going commercial (July 2025) is industry-relevant context VC docs don't flag.

**Grep** (DOCS):
- `grep -rliw "MediatR|Mediator"` DOCS: **3 files** — `update-xapi-modules.md:207,233`, `custom-module-creation.md:74,75,123`, `x-api-extensions.md` (implicit via CQRS)

**Grep** (CODE):
- `grep -rliw "MediatR|IMediator"` CODE: **382 files** (massive: every xAPI module has MediatR handlers, command builders, pipeline behaviors)

**Verdict**: 🟠 **Implemented but undocumented** outside xAPI. MediatR is a load-bearing dependency across xAPI and many modules, but docs treat it as a GraphQL-extension-only concern. No guidance on writing a plain REST MediatR handler, pipeline behaviors, validators, or the commercial-license implications.
**Note**: 382 code files vs. 3 doc files is the sharpest code-vs-docs mismatch in this group.

---

## Claim 7: "Strangler fig pattern" for migration is absent
**Context7** (covered under claim 8): not mentioned.

**WebSearch**: not required — zero hits anywhere.

**Grep** (DOCS):
- `grep -rli "strangler"` DOCS: **0 files**

**Grep** (CODE):
- `grep -rli "strangler"` CODE: **0 files**

**Verdict**: 🔴 **Absent**. Industry-standard term for migrating from legacy monoliths (Shopify, commercetools, SAP migrations routinely reference it). VC has nothing on incremental migration from Magento/Hybris/SAP/Adobe despite positioning as a replacement.
**Note**: Real gap given VC's "replace your legacy commerce" go-to-market.

---

## Claim 8: "Circuit breaker" / "retry" / "Polly" is absent
**Context7** (`/virtocommerce/vc-docs`, query: "feature flags, circuit breaker, Polly retries, strangler fig"):
Feature-flag content returned (see claim 9). Nothing on Polly, retry, or circuit breaker.

**WebSearch** (claim 4 query): Polly + IHttpClientFactory is the canonical .NET resilience combo — every serious .NET 8/10 architecture guide covers it.

**Grep** (DOCS):
- `grep -rli "circuit breaker|Polly|polly.retry"` DOCS: **0 files**
- `grep -rli "retry polic"` DOCS: **3 files** (all generic mentions in non-resilience contexts — indexing, recurring jobs)

**Grep** (CODE):
- `grep -rli "\bPolly\b"` in PlatformBackendSourceCode: **39 files** — `VirtoCommerce.Platform.Caching.csproj` references `Polly 8.6.6`; `vc-module-core` uses `using Polly;`; DLLs ship in module.ignore; `vc-module-ai-categorization/*.md` even discusses "retry/circuit breaker patterns" in roadmap documents
- `grep -rni "circuit breaker"` CODE: **10 hits** across ai-categorization roadmap/integrations/weaviate-refactor

**Verdict**: 🟠 **Implemented but undocumented**. Polly 8.6.6 is a platform-wide dependency and is used in the core module, yet resilience/retry/circuit-breaker guidance is zero in the developer-facing docs. The ai-categorization module's *internal* roadmap discusses circuit breakers but the user docs never do.
**Note**: A dev asking "does VC HTTP-out have retries?" can't answer from docs alone.

---

## Claim 9: "Feature flag" / "feature toggle" is absent
**Context7** (same query as claim 8): strong hits — dedicated page `Tutorials-and-How-tos/How-tos/feature-flags.md`, plus `azure-app-configuration.md`, plus `building-navigation-menus-with-usemenuservice.md` referencing `isFeatureEnabled`. Explicit JS `FeatureFlags` class example, GraphQL schema for querying them.

**WebSearch**: not required — Context7 returned comprehensive hits.

**Grep** (DOCS):
- `grep -rli "feature flag|feature toggle"` DOCS: **10 files** — flagship: `feature-flags.md` defines the concept ("also known as feature toggles or feature switches") with A/B testing, rollback control, modularity rationale; `overriding-rounding-policy.md:38` cross-links to it; `azure-app-configuration.md` covers Azure-hosted flags

**Grep** (CODE):
- `grep -rli "feature flag|feature toggle|FeatureManagement|IFeatureManager"` CODE: **10 files**

**Verdict**: ✅ **Well documented**. Claim rejected — there's a dedicated page, a JS helper class example, GraphQL integration, and Azure App Configuration cross-reference.
**Note**: VC's model is "module = feature flag" rather than `Microsoft.FeatureManagement` / LaunchDarkly — a perspective difference worth noting but the content is there.

---

## Claim 10: "Multi-tenancy" model & isolation is poorly documented
**Context7** (`/virtocommerce/vc-docs`, query: "How does VirtoCommerce handle multi-tenancy, tenant isolation, multiple stores?"):
Strong results on multi-store / multi-region (multiple stores, domains, themes, catalogs on one platform install). Explicit "multi-tenant" appears in (a) Azure AD SSO config ("multi-tenant Azure AD app"), (b) Intent Search module ("Multi-tenant design: organization-based tenancy, Weaviate tenant isolation, complete data isolation at the database level").

**WebSearch**: not required.

**Grep** (DOCS):
- `grep -rli "multi-tenan|multitenan"` DOCS: **6 files** — concentrated in two narrow pockets: Azure-AD-SSO page (5 hits) and Intent Search overview (3 hits)

**Grep** (CODE):
- `grep -rli "multi-tenan|multitenan"` CODE: **22 files**

**Verdict**: 🟡 **Mentioned but thin**. Platform-level isolation story is missing: no doc explains whether a single VC deployment isolates *customers* (tenants), only *stores*. Multi-store ≠ multi-tenant: multiple stores share one DB, one user pool, one settings namespace. The only true multi-tenant isolation documented is (a) SSO identity tenancy and (b) Intent Search module's per-org Weaviate tenant. SaaS-style hard isolation (per-tenant DB, per-tenant encryption keys, cross-tenant noisy-neighbor) is not addressed.
**Note**: This is the question most prospects/SaaS-resellers will ask first; the current docs implicitly assume single-tenant-per-deployment without ever saying so.

---

## Summary counts

| Claim | Term | DOCS files | CODE files | Verdict |
| --- | --- | --- | --- | --- |
| 1 | DDD / "domain-driven design" | 2 (acronym only) | 0 | 🔴 |
| 2 | aggregate root / bounded context / ubiquitous language | 0 / 1 / 0 | 0 / 0 / 0 | 🔴 |
| 3 | repository pattern / unit of work | 0 / 4 | 204 / 89 | 🟠 |
| 4 | CQRS | 2 | 2 | 🟡 |
| 5 | event sourcing | 0 | 0 | ⚪ |
| 6 | MediatR / Mediator | 3 | 382 | 🟠 |
| 7 | strangler fig | 0 | 0 | 🔴 |
| 8 | circuit breaker / Polly | 0 | 39 (+10 circuit-breaker hits) | 🟠 |
| 9 | feature flag / toggle | 10 | 10 | ✅ |
| 10 | multi-tenancy | 6 | 22 | 🟡 |
