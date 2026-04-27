# VirtoCommerce documentation gap audit — POSITIVE findings

Companion to [FINAL-negative.md](FINAL-negative.md). This report collects the **~32 ✅ well-documented** and **~8 ⚪ correctly-absent-by-design** verdicts across the 24 audited groups, plus the structural strengths those verdicts imply. Source files per group are linked inline.

The purpose: when someone reads the negative report, they should not conclude "VC's docs are bad". VC's docs are *unevenly* good — some areas are competitive with the best commerce platforms, and the negative findings should be read against this baseline.

---

## Executive summary — three strengths

### 1. GraphQL / xAPI is a first-class reference

Every audited group that touches the API surface ([G](G-api-surface.md)) highlighted the GraphQL / xAPI side as strong: a dedicated reference tree (`GraphQL-Storefront-API-Reference-xAPI/`, 104+ files), embedded GraphiQL per-module, Relay-style cursor connections, subscriptions, Postman collections for sorting / extensibility tests, and consistent `searchPhrase` / `filter` / `sort` + `search-query-syntax-reference.md` conventions. This is VC's single strongest documentation asset.

### 2. Merchandiser-facing commerce features are documented in depth

A consistent pattern across groups: once a feature lives behind an admin-UI module, its user-guide page usually gets genuine depth. Strongest examples:

- **Promotions rule engine** ([L](L-pricing-promotions.md)) — `combining-active-promotions.md` cleanly explains Best-reward vs Stackable policies + priority-based fallback; 31 files on coupons with manual + CSV bulk import; full `addCoupon` / `promotionCoupons` / `PromotionCouponType` GraphQL surface. Best-explained rule engine in the audit.
- **Contract pricing** ([L](L-pricing-promotions.md), [P](P-b2b-specifics.md)) — Dedicated Contracts module (4 pages) + Pricing example + user-group conditions; automatic contract → user-group → price-list wiring.
- **Search provider matrix** ([J](J-search-discovery.md)) — Elasticsearch 7/8/9/10, OpenSearch (first-class module, 11 files), Elastic App Search, Lucene, Azure Cognitive Search, Algolia (full provider module), Weaviate via Intent Search, ELSER semantic search all documented with working `appsettings.json` samples. Faceted search is first-class in xAPI (51 files).
- **Wishlist / save-for-later** ([K](K-cart-checkout.md)) — ~25 GraphQL reference docs + GA-event integration + `moveWishlistItem` flow + dedicated storefront user-guide page. The cleanest pass in Group K.
- **Personalization + recommendations** ([R](R-marketing-seo.md)) — Catalog Personalization module + Dynamic Content + `xRecommend` (79 files), GraphQL `recommendations` / `pushHistoricalEvent`.
- **Sitemaps** ([R](R-marketing-seo.md)) — Dedicated Sitemaps module + custom `robots.txt` page.
- **GA4 / GTM** ([R](R-marketing-seo.md)) — Native integration module + config-reference force-global settings.
- **Theming / white-label / multi-brand** ([H](H-frontend-ux.md)) — Dedicated White Labeling module with admin UI, xAPI surface, multi-store setup, SCSS variable themes with `useTheme`.
- **Storybook component catalog** ([H](H-frontend-ux.md)) — Two published Storybooks (storefront + VC-Shell), embedded per-component via iframe, Atomic Design structure.

### 3. Honest internal documentation where it matters

A counter-pattern worth surfacing: in a few places, VC's developer guides are more honest than its marketing copy. These are credibility assets, not bugs.

- The `Fundamentals/Modularity/01-overview.md` calls VirtoCommerce a **Modular Monolith** — contradicting marketing's "microservices" framing but accurately describing the one-process .NET architecture ([X](X-modern-buzzwords.md)).
- The `order-management/overview.md:34` explicitly states the Order module is "not coded and not pre-determined ... an Order Details Editor with no validation logics" — contradicting the "Built-in OMS" marketing bullet but telling solution architects the truth ([M](M-order-inventory-fulfillment.md)).
- The MACH coverage in the marketing corpus actually *contrasts* Virto's "Atomic Architecture" with MACH rather than falsely claiming membership ([X](X-modern-buzzwords.md)).

These should be the template for the rest of the corpus.

---

## Part A — Well-documented topics (✅)

### A-1. Data, Storage, Persistence → [B](B-data-storage.md)

- **PostgreSQL as primary DB option** — Dedicated setup page, version requirement, config reference, PG-specific how-to.
- **MySQL support** — Symmetric coverage to PostgreSQL; two connection-string styles, min version 5.7+.
- **Redis / distributed caching** — `appsettings` reference + full scalability-on-Azure guide covering SignalR backplane and memory-cache sync.
- **Database migrations** — EF `Add-Migration` tutorials, `grab-migrator` CLI, cold-start-and-data-migration page, custom-SQL-in-migration patterns.

### A-2. Messaging & Integration → [C](C-messaging-integration.md)

- **Event bus / domain events** — Dedicated guides (`event-bus.md`, `event-bus-configuration.md`, `using-domain-events.md`). Strongest area in Group C.

### A-3. Observability → [D](D-observability.md)

- **OpenTelemetry** — Dedicated `opentelemetry.md` + `appsettings.json` reference + troubleshooting (18 files).
- **Application Insights** — Full backend config + adaptive sampling + Serilog sink + frontend `useAppInsights` walkthrough (28 files).
- **Serilog structured logging** — Dedicated Fundamentals / Logging section (9 files).
- **`/health` endpoint** — 15 files, dedicated how-to.

### A-4. Security, Auth, Compliance → [E](E-security-auth.md)

- **OAuth2 / OIDC** — Dedicated module, per-provider guides (Google, Azure AD, Microsoft), full `appsettings` reference.

### A-5. Architecture Patterns → [F](F-architecture-patterns.md)

- **Feature flags** — Dedicated `feature-flags.md` + Azure App Configuration cross-ref + JS `FeatureFlags` helper class + GraphQL schema + navigation-menu example (10 files). The one architecture pattern documented properly.

### A-6. API Surface → [G](G-api-surface.md)

- **GraphQL / xAPI schema discoverability** — Dedicated tree under `GraphQL-Storefront-API-Reference-xAPI/`, GraphiQL per-module, 104+ files.
- **Pagination / filtering / sorting conventions** — Per-query `searchPhrase` / `filter` / `sort`, Postman sorting collection, `search-query-syntax-reference.md`.
- **Webhooks + WebSockets** — Dedicated webhooks module page + SignalR + WebSocket config block in `appsettings.json` reference + GraphQL subscriptions.

### A-7. Frontend, UX → [H](H-frontend-ux.md)

- **Frontend modularity & extensibility** — Full customization folder + VC-Shell modularity + Page Builder + Builder.io / Storyblok integrations.
- **Theming / white-label / multi-brand** — Dedicated White Labeling module, admin UI, xAPI surface, multi-store setup, SCSS variable themes with `useTheme`.
- **Storybook component catalog** — Two published Storybooks, per-component iframe embedding, Atomic Design structure.

### A-8. Catalog → [I](I-catalog-pim.md)

- **Product variants / configurable products** — 59 files / 263 occurrences of "variant"; dedicated `managing-product-variations.md` + `managing-product-configurations.md`; xAPI mutations documented.
- **Taxonomy / hierarchical categories** — 45 taxonomy hits, 21 virtual-catalog hits, 790 category hits; subtree / path filters, `childCategories` query, master / virtual catalog split.

### A-9. Search & Discovery → [J](J-search-discovery.md)

- **Search provider matrix** — Elasticsearch / Azure Search / Lucene / OpenSearch / Algolia / Weaviate all with `appsettings.json` recipes.
- **Faceted search / guided navigation** — Dedicated `faceted-search.md` + xAPI facet examples (51 files).
- **Vector / semantic search** — Dedicated Intent Search module (Weaviate) + ELSER-based semantic search in Elasticsearch docs (33 files).
- **Boosting / relevance tuning** — In Elastic App Search + `SearchBoost` presets.

### A-10. Cart & Checkout → [K](K-cart-checkout.md)

- **Wishlist / save-for-later** — Dedicated storefront user-guide page, ~25 GraphQL reference docs, GA-event integration, `moveWishlistItem` flow.

### A-11. Pricing & Promotions → [L](L-pricing-promotions.md)

- **Customer-group / contract pricing** — Dedicated Contracts module (4 pages) + Pricing example + user-group conditions; automatic contract → user-group → price-list wiring.
- **Discount stacking / priority** — `combining-active-promotions.md` cleanly explains Best-reward vs Stackable policies + priority-based fallback.
- **Coupon / voucher management** — 31 files; manual + CSV bulk import; full `addCoupon` / `promotionCoupons` / `PromotionCouponType` GraphQL.
- **Price lists / currency-specific** — 25 files in PlatformUserGuide; multi-currency architecture page explicit.

### A-12. Tax & Shipping → [N](N-tax-shipping.md)

- **Avalara AvaTax integration** — Dedicated 5-page folder, 108 mentions, `appsettings` + deployment + store-config references.
- **Click-and-collect under BOPIS** — 14 occurrences, full admin + storefront flow.

### A-13. B2B Specifics → [P](P-b2b-specifics.md)

- **Contract prices** — Dedicated `contracts/` user-guide dir with 4 how-to files + overview driven by user-group + price-list mechanism.

### A-14. Marketing, SEO, Personalization → [R](R-marketing-seo.md)

- **Personalization engine** — Catalog Personalization module + Dynamic Content + xRecommend (75 files).
- **Recommendation engine** — xRecommend module, GraphQL `recommendations`, `pushHistoricalEvent` (79 files).
- **Sitemap generation** — Dedicated Sitemaps module + custom `robots.txt` page.
- **GA / GTM / GA4** — Native integration module + config-reference force-global settings.

### A-15. CMS / Content / i18n → [S](S-cms-content-i18n.md)

- **Multi-language / i18n** — Full i18n stack on both storefront (`localization.md`, JSON locale files) and VC-Shell (`vue-i18n`, `useLanguages`, `internationalization.md`). 27 files on multi-language, 64 on localization, 46 on locale.
- **Multi-currency** — Price lists are single-currency-by-design; GraphQL carries `currencyCode`; `multiregional-ecommerce.md` walks a USD / CAD / EUR three-store example (158 currency files).

### A-16. Modularity & Extensibility → [U](U-modularity-extensibility.md)

- **Module / plugin anatomy** — Dedicated 8-page `Fundamentals/Modularity/` folder; `IModule` / `ModuleBase` canonical.
- **Override / method-overriding as practice** — 45 DOCS files covering override scenarios (across modularity + extension docs).
- **Customizing / overriding a built-in entity model** — `extending-domain-models.md` with full `CustomerOrder → CustomerOrder2` walkthrough. Best extensibility tutorial in the corpus.
- **Dynamic properties as concept** — 58 files and a first-class admin UI, even though the industry term "custom field / attribute / metafield" bridge is missing.

### A-17. Testing & QA → [V](V-testing-qa.md)

- **E2E Playwright harness** — 435-line `testing.md` covers codegen, trace viewer, Allure, retries, 80 tests (54 GraphQL + 25 E2E UI + WebAPI). VC's best testing asset.

### A-18. DDD & CQRS → [W](W-ddd-cqrs-vocabulary.md)

- **Domain model term** — 12 files / 17 occurrences; dedicated tutorial + best-practices page; explicit Data Mapper framing.

### A-19. Modern buzzwords → [X](X-modern-buzzwords.md)

- **Headless** — 24 marketing + 6 dev-guide files; defined as an "architectural pillar" in `PlatformDeveloperGuide/.../getting-to-know-platform.md`. The one MACH-era buzzword with real substance.

---

## Part B — Correctly absent (⚪)

Topics and terms whose absence is consistent with VC's architecture and is not a documentation gap. Worth flagging so readers don't misread them as omissions.

- **Event sourcing** (0 DOCS / 0 CODE) — VC is CRUD + domain events; not an event-sourced system. Absence is correct. Group [F](F-architecture-patterns.md).
- **Azure Service Bus** — VC uses Azure Event Grid, not Service Bus. The "Service Bus" claim in the audit was mis-named; its absence is not a gap. Group [C](C-messaging-integration.md).
- **gRPC as a feature** — Two hits are OTLP exporter to OpenTelemetry collector, not a service-to-service RPC surface. VC is a modular monolith; external gRPC endpoints are outside scope. Group [C](C-messaging-integration.md).
- **SSE (server-sent events)** — WebSockets + webhooks + GraphQL subscriptions cover the push scenarios; SSE is a design choice elsewhere. Group [G](G-api-surface.md).
- **AMP / Mobile AMP pages** — Industry-deprecated since 2021. Absence is current. Group [S](S-cms-content-i18n.md).
- **Edge compute / edge functions** — Modular monolith runs in one .NET process; edge is out of scope. (Worth a one-line note in docs so buyers don't waste a conversation on it.) Group [X](X-modern-buzzwords.md).
- **Service mesh** — Same reason as edge compute; consistent with the modular-monolith posture. Group [X](X-modern-buzzwords.md).
- **Native mobile app first-party SDK (RN / Flutter)** — Arguably not a gap if the official story is "use GraphQL / xAPI from any mobile client"; today the docs neither affirm nor deny this, so mobile is ambiguous — upgrade target. Group [H](H-frontend-ux.md).

---

## Structural strengths worth naming

Reading across the 24 groups, five structural choices keep showing up on the positive side. Documentation strategy should preserve and extend these rather than change them.

1. **Provider-matrix pages.** Search, payments, tax, and object storage all use the "pick-a-provider, here's an `appsettings.json` block per choice" pattern. When used (search especially) it's genuinely competitive. Missing providers (Typesense, Meilisearch, S3, GCS, TaxJar, Vertex) should follow the same template.
2. **xAPI mutation-and-type reference per module.** Every module's GraphQL surface gets an auto-generated reference with examples and argument tables. This carries a lot of weight and partially masks the weaker topic-narrative docs.
3. **Pre-compiled Langfuse prompts + embedded GraphiQL + Storybook iframes.** VC docs lean on live explorers and in-browser tooling instead of static code dumps. The reader-experience is closer to Shopify's developer portal than to a static Markdown site.
4. **Dedicated Modularity / Extensibility section with an end-to-end tutorial** (`extending-domain-models.md`). This is the one place in the corpus where a custom-VC-vocabulary concept (AbstractTypeFactory) gets the narrative treatment it deserves. Expand this pattern to the other proprietary concepts (DynamicProperty, vc-package.json publishing, Liquid extensibility scope).
5. **Honest internal positioning ("Modular Monolith", "Order module is an editor with no validation logics").** When developer guides contradict marketing, preserve the developer-guide truth and rewrite marketing — do not smooth the contradiction by downgrading dev-guide honesty.

---

## Cross-links

Per-group findings: [A](A-deployment-infra.md) · [B](B-data-storage.md) · [C](C-messaging-integration.md) · [D](D-observability.md) · [E](E-security-auth.md) · [F](F-architecture-patterns.md) · [G](G-api-surface.md) · [H](H-frontend-ux.md) · [I](I-catalog-pim.md) · [J](J-search-discovery.md) · [K](K-cart-checkout.md) · [L](L-pricing-promotions.md) · [M](M-order-inventory-fulfillment.md) · [N](N-tax-shipping.md) · [O](O-payments.md) · [P](P-b2b-specifics.md) · [Q](Q-marketplace.md) · [R](R-marketing-seo.md) · [S](S-cms-content-i18n.md) · [T](T-subscriptions.md) · [U](U-modularity-extensibility.md) · [V](V-testing-qa.md) · [W](W-ddd-cqrs-vocabulary.md) · [X](X-modern-buzzwords.md).

Methodology and scope: [00-plan.md](00-plan.md) · Per-group claim lists: [01-claims.md](01-claims.md) · Negative report (the other half of this pair): [FINAL-negative.md](FINAL-negative.md).
