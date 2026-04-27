# VirtoCommerce documentation gap audit — NEGATIVE findings

Synthesis of 24 per-group findings files under [docs/vc-gap-audit-run/](.). Every verdict is backed by Context7 queries on `/virtocommerce/vc-docs`, competitor-aware WebSearch, and grep over the crawled docs corpus (`documentation/VirtoCommerce`, `PlatformUserGuide`, `PlatformDeveloperGuide`, `StorefrontUserGuide`, `StorefrontDeveloperGuide`, `MarketplaceUserGuide`, `DeploymentGuide`, `B2BExperts`), with implementation cross-checks against `PlatformBackendSourceCode`, `PlatformFrontendSourceCode`, `FrontendSourceCode`.

Verdict scheme: 🔴 absent · 🟠 implemented but undocumented · 🟡 mentioned but thin. ✅ well-documented and ⚪ correctly absent are covered in [FINAL-positive.md](FINAL-positive.md).

Tally across 240 claims: **~99 🔴 · ~20 🟠 · ~76 🟡 · ~32 ✅ · ~8 ⚪** → roughly **60% of audited topics fail the documentation bar** and **~40% are absent outright**.

---

## Executive summary — three dominant failure modes

### 1. Implemented in code, refused by docs (vocabulary mismatch)

VirtoCommerce's codebase ships canonical .NET and DDD patterns; the docs refuse the industry names for them. This is the single most damaging pattern in the audit — an evaluator reading the docs concludes VC doesn't do something it actually does prolifically.

| Concept | DOCS hits | CODE hits | Group |
| --- | ---: | ---: | --- |
| `AbstractTypeFactory` | 11 | **693** | [U](U-modularity-extensibility.md) |
| `DynamicProperty` (vs "custom field / attribute / metafield") | 58 | **788** | [U](U-modularity-extensibility.md) |
| `IAggregateRoot` / aggregate root | **0** | 75 | [W](W-ddd-cqrs-vocabulary.md) |
| `ValueObject` | 3 incidental | **118** | [W](W-ddd-cqrs-vocabulary.md) |
| `ISpecification<T>` (specification pattern) | **0** | 18 | [W](W-ddd-cqrs-vocabulary.md) |
| MediatR / CQRS handlers | 3 files / 28 occ | **354 / 394** | [F](F-architecture-patterns.md), [W](W-ddd-cqrs-vocabulary.md) |
| Repository pattern / Unit of Work | 0 / 4 | **204 / 89** | [F](F-architecture-patterns.md) |
| Polly / circuit breaker | **0** | 39 | [F](F-architecture-patterns.md) |
| xUnit test framework | 1 | **603** | [V](V-testing-qa.md) |
| Moq (mocking) | **0** | 253 | [V](V-testing-qa.md) |
| Polymorphism (named as concept) | 1 | 15+ (`Polymorph*.cs`) | [U](U-modularity-extensibility.md) |
| SAML / enterprise SSO | 0 | 3 incidental | [E](E-security-auth.md) |
| Secret management (Key Vault etc.) | inference only | present | [E](E-security-auth.md) |
| Preorder / backorder | 0 narrative | 4 `InventoryInfo` fields | [M](M-order-inventory-fulfillment.md) |
| Apple Pay / Google Pay | 1 bullet | `vc-module-cyber-source`, `vc-module-payment`, `vc-module-datatrans` | [O](O-payments.md) |
| Payment tokenization / vaulting | vendor-only | all payment modules | [O](O-payments.md) |
| Multi-level account hierarchy (B2B) | 0 | xAPI org hierarchy | [P](P-b2b-specifics.md) |
| Vendor analytics / marketplace dashboards | screenshots only | present | [Q](Q-marketplace.md) |
| NuGet module publishing | 18 | 113 (`vc-package.json` path never stated) | [U](U-modularity-extensibility.md) |
| CMS page versioning / draft-published | 0 | present | [S](S-cms-content-i18n.md) |

### 2. Marketing-only buzzwords and feature-bullet bait-and-switch

Marketing copy asserts features or posture that the developer guides either contradict, fail to elaborate, or silently drop.

| Claim in marketing | Reality in developer guides | Group |
| --- | --- | --- |
| "Built-in OMS" ([features page](documentation/VirtoCommerce/features.md)) | `order-management/overview.md:34` — "not coded and not pre-determined ... an Order Details Editor with no validation logics" | [M](M-order-inventory-fulfillment.md) |
| "Microservices" (marketing × 5) | Dev guide: "**Modular Monolith**" in one .NET process ([Fundamentals/Modularity/01-overview.md](documentation/PlatformDeveloperGuide/platform/developer-guide/docs/Fundamentals/Modularity/01-overview.md)) | [X](X-modern-buzzwords.md) |
| "Composable commerce" / "API-first" / "Cloud-native" | 0 dev-guide substance; Vue `composables/` folders coincidentally match `composable` grep | [X](X-modern-buzzwords.md) |
| MACH-adjacent vocabulary | VC **not a MACH Alliance member** per machalliance.org/members; docs contrast Virto's "Atomic Architecture" vs MACH | [X](X-modern-buzzwords.md) |
| Marketplace: "Payments split / Advanced SEO / Flexible shipments" | 5 🔴 / 0 ✅ across the marketplace group — bullet-list without elaboration | [Q](Q-marketplace.md) |
| "Blue-green deployment" | In VC docs means **search-index swap**, not app deployment | [A](A-deployment-infra.md) |
| "Subscription module" | 3 short user-guide files totaling ~45 lines; 7 🔴 / 2 🟡 / 1 ⚪ | [T](T-subscriptions.md) |

### 3. Industry-vocabulary blackouts (term never lands in the corpus)

Features often exist, but the industry term by which a prospect searches is not in VC's vocabulary. Sample by group:

- **Commerce ops** — OMS (thin), WMS, BORIS, ship-from-store, endless aisle, ATP, RMA, click-and-collect ([M](M-order-inventory-fulfillment.md), [N](N-tax-shipping.md))
- **Catalog / content** — PIM (marketing-only), DAM, product bundle / kit, blocks & slots, draft-published page versioning, RTL, Core Web Vitals, JAMstack ([I](I-catalog-pim.md), [S](S-cms-content-i18n.md), [H](H-frontend-ux.md))
- **B2B** — Punchout (cXML / OCI), EDI, CPQ, net terms, credit limit ([P](P-b2b-specifics.md))
- **Payments** — Stripe, Adyen, PayPal, Braintree, Klarna, BNPL, SCA, 3DS2, payment orchestration, chargeback ([O](O-payments.md))
- **Marketplace money-out** — Stripe Connect, Adyen MarketPay, Mirakl Payout, KYB, drop-ship ([Q](Q-marketplace.md))
- **Subscriptions** — dunning, proration, MRR, metered, subscription box, pause-skip-cancel ([T](T-subscriptions.md))
- **Marketing / SEO** — Meta Pixel, CAPI, canonical URLs, JSON-LD, Schema.org, Klaviyo, Mailchimp, Braze, A/B testing ([R](R-marketing-seo.md))
- **Search** — Typesense, Meilisearch, stemming, stopwords, "did you mean", merchandising rules ([J](J-search-discovery.md))
- **Architecture** — aggregate root, value object, bounded context, anti-corruption layer, strangler fig ([F](F-architecture-patterns.md), [W](W-ddd-cqrs-vocabulary.md))
- **Cloud & ops** — AWS, GCP, Kubernetes/Helm, Terraform, zero-downtime, canary, rolling ([A](A-deployment-infra.md)); SLO, SLI, error budget, RED, USE, runbook, liveness-vs-readiness split ([D](D-observability.md))
- **Messaging / APIs** — outbox, saga, idempotency key, DLQ, webhook signatures, RFC 7807 / Problem+JSON, rate limiting, cursor vs offset ([C](C-messaging-integration.md), [G](G-api-surface.md))
- **Security** — SAML, WebAuthn/passkeys, MFA, TOTP, OWASP Top 10, PCI AoC, data residency ([E](E-security-auth.md))
- **Modern architecture** — MACH, Jamstack, zero-trust, service mesh, edge compute ([X](X-modern-buzzwords.md))

---

## Part A — Topics VirtoCommerce supports but poorly describes

Grouped by functional area. Each entry: *topic → verdict → one-line evidence → group*.

### A-1. Deployment & Infrastructure → [A](A-deployment-infra.md)

- **Kubernetes / Helm charts / K8s manifests** — 🟠 Marketing bullet + one `-HelmParameters` CLI flag; no public Helm chart, no manifest examples, no `kubectl` walkthrough.
- **Docker multi-stage / production compose** — 🟡 Compose documented for local dev only (`ModulesDevelop`); zero multi-stage guidance.
- **Infrastructure-as-Code** — 🟠 Only ARM templates (Azure); Terraform / Pulumi / Bicep / CloudFormation entirely absent.
- **GitOps / ArgoCD / Flux** — 🟡 Dedicated `enable-gitops.md` exists but only for managed Virto Cloud; ArgoCD named once; Flux absent.
- **Zero-downtime / blue-green / canary / rolling** — 🟠 "Blue-green" in VC docs is almost always search indexing; canary only in a McKinsey quote; rolling absent.
- **Horizontal scaling / autoscaling / LB** — 🟡 Well documented for Azure (Redis backplane, SignalR); autoscaling (HPA / KEDA / App Service rules) entirely absent.
- **Session affinity / sticky sessions** — 🟡 Clearly documented for Azure ARR Affinity; silent on AWS ALB stickiness, nginx `ip_hash`, K8s `sessionAffinity: ClientIP`, GCP.
- **CI/CD beyond GitHub Actions** — 🟡 Azure DevOps is first-class alongside GHA; GitLab only as a module-artifact source; Jenkins / Bitbucket / TeamCity / CircleCI entirely absent.

### A-2. Data, Storage, Persistence → [B](B-data-storage.md)

- **Object storage swapping** — 🟠 Azure Blob only; S3 / GCS / MinIO undocumented.
- **Backup / restore / disaster recovery** — 🟡 Admin-UI ZIP export documented; 0 hits for "disaster recovery" / RTO / RPO.
- **Data retention / GDPR right-to-be-forgotten** — 🟡 GDPR anonymization module well covered, but "data retention policy" appears only in an Application Insights context.
- **Optimistic concurrency / row-versioning** — 🟠 One `Concurrency-handling` page discusses `DbUpdateConcurrencyException` but never uses canonical terms (optimistic concurrency, rowversion, concurrency token, ETag, If-Match).

### A-3. Messaging & Integration → [C](C-messaging-integration.md)

- **Webhooks delivery guarantees** — 🟡 One line on exponential retry; zero on HMAC signatures / DLQ / ordering. `webhooks.md` is 42 lines.
- **EDI / cXML / Punchout (OCI)** — 🔴/🟡 Blog post + Greenwing partner mention; no developer guide.
- **Distributed tracing (industry naming)** — 🟡 Present under OpenTelemetry umbrella only; zero hits for Jaeger / Zipkin / Tempo; no multi-service example.

### A-4. Observability → [D](D-observability.md)

- **Prometheus / Grafana** — 🟡→🔴 Zero "Prometheus" hits; Grafana only appears as a Virto Cloud bundle and an OTel collector. Achievable via OTel + collector but never explained.
- **Structured logging non-Serilog** — 🔴 NLog / ELK / OpenSearch log sink not shown end-to-end.
- **Correlation IDs / trace IDs** — 🟡 Only one hit (frontend W3C trace IDs in `useAppInsights.md`); no HTTP header propagation story.
- **Liveness / readiness probe split** — 🔴 Those words never appear; no K8s probe YAML.
- **Distributed tracing backends** — 🟡 Zero hits for Jaeger / Zipkin / Tempo.

### A-5. Security, Auth, Compliance → [E](E-security-auth.md)

- **SAML / enterprise SSO** — 🟠 SSO is documented only via OIDC; zero SAML references in DOCS, only 3 incidental hits in code.
- **JWT claim structure** — 🟡 Validation (Authority / Audience / certs) covered; actual issued-claim structure shown only as an undecoded sample token, no claim-reference table.
- **RBAC vs ABAC vs policy-based** — 🟡 RBAC, permission-based, scope-based are real; ABAC appears once; no cross-reference of industry terminology.
- **GDPR / CCPA / data residency** — 🟡 GDPR module + user guide exists; CCPA name-dropped in 2 files; "right to be forgotten", "right to erasure", "data residency" — all zero.
- **PCI DSS / tokenization** — 🟡 Leveraged via Skyflow / CyberSource / Authorize.Net as selling points; no VC-side SAQ scope statement, no AoC, no tokenization boundary diagram.
- **Content Security Policy / anti-CSRF** — 🟡 Only `frame-ancestors` and `X-Frame-Options` configurable; CSRF dismissed via "JWT-in-header", yet documented cookie+JWT mixed-auth path reintroduces CSRF risk without anti-forgery discussion.
- **Secret management** — 🟠 Azure Key Vault inferred from a separator note; no setup tutorial.

### A-6. Architecture Patterns → [F](F-architecture-patterns.md)

- **Repository pattern / Unit of Work** — 🟠 Docs prefer "Data Mapper pattern"; never teach repository/UoW as concepts (0/4 DOCS vs 204/89 CODE).
- **CQRS** — 🟡 Named only for GraphQL/xAPI, never for REST modules that also use MediatR (2 DOCS vs 2 CODE files mentioning term; 354 MediatR-using code files).
- **MediatR / Mediator** — 🟠 3 DOCS vs 382 CODE files. Load-bearing but docs cover it only as an xAPI implementation detail; commercial-license-since-July-2025 implication not flagged.
- **Circuit breaker / Polly** — 🟠 0 DOCS for Polly/circuit breaker vs 39 CODE files (Polly 8.6.6 pinned in `VirtoCommerce.Platform.Caching.csproj`).
- **Multi-tenancy** — 🟡 6 files, concentrated in two unrelated pockets (Azure AD SSO tenancy and Intent Search per-org Weaviate isolation). SaaS-level platform isolation story missing.

### A-7. API Surface → [G](G-api-surface.md)

- **REST API reference (vs Swagger)** — 🟡 Only inline Swagger UI + hosted `swagger.json`; no curated topic-organized reference.
- **OpenAPI download / Postman collection** — 🟡 `swagger.json` + NSwag walkthrough documented; Postman collections only for GraphQL, not REST.
- **Cursor vs offset pagination** — 🟡 Both exist (Relay cursors in GraphQL, `skip`/`take` in REST search), but docs never contrast them or guide selection.

### A-8. Frontend, UX, Accessibility → [H](H-frontend-ux.md)

- **Progressive Web App** — 🟡 Only `manifest.webmanifest` documented; no service-worker / offline / push end-to-end.
- **SSR / ISR** — 🟡 VC intentionally avoids SSR in favor of Prerender.io for SEO; ISR/SSG terminology absent.
- **Design system / design tokens** — 🟡 Term "design tokens" used in `visual-theme-customization.md`; Storybook + CSS presets exist; Figma kit, token taxonomy spec, style-dictionary pipeline absent.

### A-9. Catalog, PIM, DAM → [I](I-catalog-pim.md)

- **PIM term usage** — 🟡 30 files of "PIM", 5 of "Product Information Management" — marketing + PBC descriptions only; near-silent in user/developer guides.
- **Dynamic properties vs attributes vocabulary** — 🟡 58 dynamic-property files, 162 attribute, 5 custom-field — overlapping vocabulary, no glossary reconciling with industry "attribute".
- **SKU / GTIN / UPC / EAN / ISBN** — 🟡 46/8/2/3/1 files — identifiers appear only as incidental examples inside search pages; no dedicated product-identifier reference.
- **Master + variant model** — 🟡 "master product" 3 files / 4 occurrences; each variant's independence-as-SKU is implied, not stated.
- **Asset pipeline / image derivatives** — 🟡 Thumbnails module well covered (static suffix pre-gen, WebP); no on-the-fly transforms, AVIF, srcset/responsive, or CDN integration.
- **Content localization per product** — 🟡 Feature shipped; scattered across vc-shell dev docs and changelogs; no end-to-end "localize a catalog" narrative.

### A-10. Search & Discovery → [J](J-search-discovery.md)

- **Synonym / stopword / stemming** — 🟡 Synonyms documented in Elastic App Search; stopwords and stemming 0 hits (major vocabulary gap vs Adobe / Algolia).
- **Autocomplete / typeahead / "did you mean"** — 🟡 `productSuggestions` xAPI query exists; no end-to-end tuning guide; spell-correct not documented.
- **Search analytics / zero-result report** — 🟡 Only inside App Search; no platform-wide search-analytics dashboards or CTR/conversion metrics.
- **Personalized search / merchandising rules** — 🟡 "Curations" covers pin/promote; term "merchandising rules" never used; no personalization/segmentation search doc.

### A-11. Cart & Checkout → [K](K-cart-checkout.md)

- **Guest checkout** — 🟡 Mechanism (anonymous auth) well documented in one storefront-dev page; user guides never say "guest checkout" and walk only the authenticated flow.
- **Multi-cart / saved / named carts** — 🟡 Feature exists and beats Shopify's native offering, but one bullet in overview + one whitepaper paragraph. No buyer-facing walkthrough.
- **One-page / accordion checkout** — 🟡 Storefront ships a multi-step wizard; "single-page" only appears as a pytest CLI flag.
- **Cart abandonment** — 🟡 Cron config + per-store override documented; no walkthrough of template variables, cadences, or segmentation.
- **Cart upsell / cross-sell** — 🟡 Dynamic Associations module named; nothing ties it specifically to the cart page.
- **Express checkout (Apple / Google Pay)** — 🟠 One bullet under CyberSource; no dedicated setup, no domain verification, no express-button-on-cart guidance.
- **Clienteling / assisted selling** — 🟠 Feature exists as "Login on behalf"; industry terms "clienteling" / "assisted selling" zero hits.
- **MOQ / order increments** — 🟡 Three fragmented concepts (tier-min on pricing, pack size on catalog, `minQuantity`/`maxQuantity` GraphQL); "MOQ" literal 0 hits.
- **Cart merging (guest → logged-in)** — 🟡 `mergeCart` GraphQL reference is the only coverage; no conceptual prose.

### A-12. Pricing & Promotions → [L](L-pricing-promotions.md)

- **Tier / volume pricing** — 🟠 `TierPriceType`, `minQuantity`, `SetLineItemTierPrice` all exist in xAPI; zero merchandiser-facing pages; "volume pricing" term absent.
- **Dynamic / rule-based pricing** — 🟡 Marketing bullet only; no equivalent to Magento catalog price rules.
- **Loyalty tiers** — 🟡 Points accrual + redemption solid; membership tiers (bronze/silver/gold) zero hits.
- **Catalog vs cart promotions terminology** — 🟡 `BlockCatalogCondition` + cart conditions exist; Magento-standard "catalog price rule / cart price rule" mental model never named.

### A-13. Order / Inventory / Fulfillment → [M](M-order-inventory-fulfillment.md)

- **Multi-warehouse fulfillment** — 🟡 41 files touch "fulfillment center" (data-model / xAPI strong); 7 files mention "multi-warehouse" as marketing bullets. Order-routing / allocation rules absent.
- **BOPIS** — 🟡 Dedicated BOPIS settings page + `pickupLocations` GraphQL + shipping-method UI; treated as shipping-method config only — no end-to-end journey / staff UI / no-show handling.
- **Backorder / preorder** — 🟠 4 explicit `InventoryInfo` fields (`allowPreorder`, `allowBackorder`, `preorderAvailabilityDate`, `backorderAvailabilityDate`) with no narrative / admin / storefront guide.
- **Returns / RMA** — 🟡 One short `managing-returns.md`; "RMA" never appears in first-party docs; no return lifecycle / exchanges / self-service portal / restocking logic.
- **Split shipments / partial fulfillment** — 🟡 Cart data model supports it (`InputShipmentType` with per-shipment `fulfillmentCenterId`), but no how-to page.
- **Stock reservations / ATP** — 🟡 Reservation is one sentence in `cart/overview.md:22`; ATP only in a third-party Corevist/SAP article.

### A-14. Tax & Shipping → [N](N-tax-shipping.md)

- **Tax-exempt customer groups** — 🟡 Avalara-coupled only, via a generic dynamic property; no group-based exemption matrix.
- **ShipStation / EasyPost / Shippo** — 🟡 ShipStation 1 overview page linking to external module; EasyPost / Shippo absent.
- **Free-shipping thresholds** — 🟡 Achievable via promotion rules (`$X off shipping`) but term "free shipping threshold" never used; no worked example.

### A-15. Payments → [O](O-payments.md)

- **Tokenization / vaulting (concept)** — 🟠 Covered only inside `skyflow.md` + `cybersource.md` + `appsettingsjson.md` Skyflow section; no vendor-neutral tokenization / PCI-scope-reduction guidance.
- **Saved cards / recurring billing** — 🟡 `saved-credit-cards.md` is 17 lines total; no card-on-file, MIT / CIT, or recurring-charge architecture.
- **Apple Pay / Google Pay** — 🟠 One bullet in `cybersource.md:13`; backend modules support wallets but docs say nothing about Express Checkout, Apple merchant ID, domain verification, Google Pay wiring.
- **Refunds / partial refunds / void** — 🟡 Refund UI + developer hooks + CSV refund path documented; partial-refund semantics implied (enter amount) but not formalized; chargeback / dispute handling 0 hits.

### A-16. B2B Specifics → [P](P-b2b-specifics.md)

- **Quote / RFQ flow** — 🟡 `createQuoteFromCart` xAPI mutation documented; user-guide `quotes/` dir ~200 LOC across 3 files; no RFQ lifecycle / negotiation narrative.
- **Account hierarchy / company roles** — 🟠/🟡 `requestRegistration`, `changeOrganizationContactRole`, roles `org-maintainer` / `purchasing-agent` exist; **zero** hits on "account hierarchy | company hierarch | organization hierarch" — multi-level parent/child companies invisible.
- **Approval workflow** — 🟡 Single `approveOrder` GraphQL mutation documented; no multi-step / threshold / delegation walkthrough.
- **Purchase orders / PO number** — 🟡 `purchaseOrderNumber` field on `CartType`; no user-guide topic for "PO as payment method" or PO-based checkout.
- **Contract catalogs** — 🟡 Contract prices well covered; contract catalogs (customer-specific assortment) pattern unnamed.
- **Buyer-seller negotiation** — 🟡 22 hits concentrated in marketing / B2BExperts; no counter-offer round-trip documented.

### A-17. Marketplace / Multi-vendor → [Q](Q-marketplace.md)

- **Seller onboarding / KYC** — 🟡 Vendor invite page ~35 lines; KYC / KYB / tax-ID / compliance terms 0 hits.
- **Commission / payout split** — 🟡 Commission-calc solid (3-page subfolder, 20 files); `payout` 0, `disbursement` 0. "Payments split" a one-word marketing bullet.
- **Multi-vendor single cart / order splitting** — 🟡 Asserted in one sentence + two screenshots; no data-model description, no sub-order / per-vendor-status / split-payment detail.
- **Vendor product approval** — 🟡 Binary approve/decline with reason documented; no tiered / auto / bulk / editorial-queue workflow.
- **Vendor analytics / dashboards** — 🟠 Dashboard screenshots only; no metrics / GMV / AOV / widget documentation.

### A-18. Marketing, SEO, Personalization → [R](R-marketing-seo.md)

- **Abandoned cart email** — 🟡 Single settings blade + changelog; no end-to-end guide.
- **Customer segmentation** — 🟡 User Groups works; term "segmentation" and RFM / behavioral UI absent.

### A-19. CMS / Content / i18n → [S](S-cms-content-i18n.md)

- **Multi-store / multi-brand** — 🟡 Multi-store has two tutorials; multi-brand as term appears only 3× in marketplace-marketing.
- **CMS page versioning / preview** — 🟠/🔴 Preview exists (PageBuilder iframe, Storyblok draft) but isn't flagged as "preview mode"; page versioning / version history / published-vs-draft for the Pages module 0 files.
- **Liquid templating** — 🟡 8 files, zero in StorefrontGuides; Liquid now scoped to email notifications + event-bus payload preprocessing only; transition from storefront Liquid → Vue not explained.
- **Page speed / Core Web Vitals** — 🟡→🔴 5 files all aspirational; zero LCP / CLS / INP / TTFB nomenclature, no perf budget.
- **Headless CMS comparison** — 🟠 Deep integration with Builder.io (46), Sanity (7), Storyblok; Contentful "coming soon", Strapi 0. No comparison / positioning for evaluators.

### A-20. Subscriptions → [T](T-subscriptions.md)

- **Subscription product type** — 🟡 Module exists with 95-line user-guide trio; no "product type" modelling article. GraphQL exposes cart/line-item flags `isRecuring` / `isReccuring` (two typos propagated into docs).
- **Recurring order schedule** — 🟡 Flags modelled; no article on cadence / interval / next-run.

### A-21. Modularity & Extensibility → [U](U-modularity-extensibility.md)

- **Dependency injection** — 🟡 11 files "dependency injection" + 30 `IServiceCollection` / `AddTransient` / …; no standalone DI concept page; assumes prior ASP.NET Core knowledge.
- **Events / handlers / subscribers** — 🟡 4-page Event-Driven-Development folder covers infra; 6 DOCS "domain event" vs 117 CODE `IEventHandler` / `DomainEvent`; "subscriber" / "listener" missing.
- **Liquid / scripting extensibility** — 🟡 8 DOCS vs 33 CODE; notification-only coverage; no filter / tag reference, no custom-drop tutorial.
- **NuGet publishing for custom modules** — 🟠 18 DOCS vs 113 CODE; VC modules distributed via `vc-package.json` (GitHub Releases / Azure Artifacts / Blob / Local), NOT nuget.org — never stated explicitly.

### A-22. Testing & QA → [V](V-testing-qa.md)

- **Integration testing** — 🟡 4 files say "add integration tests"; no `WebApplicationFactory` / Testcontainers walkthrough. vc-build's `Category!=IntegrationTest` filter hints at a convention docs never define.
- **Fixtures / test data** — 🟡 Dataset seeder for the Playwright module documented; .NET fixtures / `IClassFixture<>` / `AutoFixture` / `Bogus` not.
- **Visual regression testing** — 🟡 `pixelmatch` via `pytest-image-snapshot` declared as capability; no worked example or baseline-management walkthrough.

### A-23. DDD & CQRS → [W](W-ddd-cqrs-vocabulary.md)

- **Entity — DDD vs ORM ambiguity** — 🟡 `Entity` used as base for both domain types (`AddressEntity : Entity`) and EF persistence types (`ConfigurationItemEntity : AuditableEntity`); docs never disambiguate.
- **CQRS** — 🟡 3 DOCS occurrences in 2 files (both xAPI sub-pages) vs 354 CODE files using MediatR.
- **Command / Query handlers** — 🟡 28 DOCS occurrences in 9 files, all in xAPI + one cart-query how-to; 375 handler class defs across 394 CODE files.
- **Domain event vs integration event** — 🟡 Asymmetric: full `using-domain-events.md` page; "integration event" one paragraph in modularity overview with zero corresponding class in code.

### A-24. Modern buzzwords → [X](X-modern-buzzwords.md)

- **Composable commerce** — 🟡 3 marketing files, 0 dev-guide; raw "composable" dev-guide hits are Vue `composables/` folders (different concept).
- **API-first** — 🟡 11 marketing, 0 dev-guide; substance (Swagger, xAPI) exists but never labeled.
- **Cloud-native** — 🟡 11 marketing, 1 dev-guide; VC's own DeploymentGuide doesn't call VC cloud-native.
- **Microservices vs Modular Monolith** — 🟠 Marketing 5× "microservices"; dev guide 2× explicit "Modular Monolith".

---

## Part B — Terms widely used in e-commerce / dev that VC uses rarely or not at all

This section lists terms that are *absent* (🔴) or *marketing-only* in the VC docs corpus, grouped by why a reader would look them up. For each term, the number in parentheses is the top-line grep count across user-facing DOCS (guides + site); where relevant, CODE hits are noted after the slash.

### B-1. Commerce operations vocabulary

- **DAM** (5 files, all partner mentions) — [I](I-catalog-pim.md) · Assets + Thumbnails modules exist but never labeled DAM.
- **WMS** (1 file, McKinsey quote) — [M](M-order-inventory-fulfillment.md)
- **BORIS** (1, McKinsey quote) — [M](M-order-inventory-fulfillment.md)
- **Ship-from-store / endless aisle** (1 each, McKinsey) — [M](M-order-inventory-fulfillment.md)
- **ATP (Available-to-Promise)** (0 in first-party) — [M](M-order-inventory-fulfillment.md)
- **Product bundle / kit** (0 — all 35 "bundle" hits are webpack / release bundles) — [I](I-catalog-pim.md), [L](L-pricing-promotions.md)
- **Click-and-collect** (0 — pickup flow is solid as BOPIS but the European term is missing) — [N](N-tax-shipping.md)
- **Gift cards as stored-value product** (0 — "Create coupons and gift cards" is a heading with coupons-only body) — [L](L-pricing-promotions.md)
- **MOQ / order increment** (0 literal "MOQ") — [K](K-cart-checkout.md)
- **Clienteling / assisted selling** (0) — [K](K-cart-checkout.md)

### B-2. B2B vocabulary

- **Punchout (cXML / OCI)** (5 files, all marketing / partner / blog) — [P](P-b2b-specifics.md)
- **EDI** (1, a blog post; 0 AS2 / X12 / EDIFACT / 850-855-856-810 mapping) — [P](P-b2b-specifics.md)
- **CPQ** (4 marketing / blog only; 0 in user or developer guide) — [P](P-b2b-specifics.md)
- **Net terms** (2, both B2BExperts blogs; 0 checkout guide) — [P](P-b2b-specifics.md)
- **Credit limit** (0 at checkout) — [P](P-b2b-specifics.md)
- **KYB / KYC** (0 in onboarding docs) — [Q](Q-marketplace.md)

### B-3. Payments vocabulary

- **Stripe** (6 files, all incidental) — [O](O-payments.md)
- **Adyen** (0 word-boundary — all 5 "adyen" hits are "McFadyen") — [O](O-payments.md)
- **PayPal** (example-only in `new-payment-method-registration.md`) — [O](O-payments.md)
- **Braintree** (0) — [O](O-payments.md)
- **Klarna / Afterpay / Affirm / BNPL** (1 `PreparedForm` example; "buy now pay later" only in blog) — [O](O-payments.md)
- **SCA / 3DS2 / PSD2** (1 bullet in `cybersource.md:13`) — [O](O-payments.md)
- **Payment orchestration / payfac / router** (0) — [O](O-payments.md)
- **Chargeback / dispute handling** (0) — [O](O-payments.md)

### B-4. Marketplace money-out vocabulary

- **Stripe Connect** (0) — [Q](Q-marketplace.md)
- **Adyen MarketPay / Adyen for Platforms** (0) — [Q](Q-marketplace.md)
- **Mirakl Payout** (0) — [Q](Q-marketplace.md)
- **Drop-ship / dropship** (0 — only per-vendor fulfillment-center stub ~6 lines) — [Q](Q-marketplace.md)
- **Vendor pages / seller SEO / marketplace SEO** (0 files) — [Q](Q-marketplace.md)
- **Return split across vendors** (0) — [Q](Q-marketplace.md)

### B-5. Subscription / billing vocabulary

- **Dunning** (0) — [T](T-subscriptions.md)
- **Proration / prorated** (0) — [T](T-subscriptions.md)
- **MRR / ARR** (0 SaaS metrics vocabulary) — [T](T-subscriptions.md)
- **Metered / usage-based billing** (0) — [T](T-subscriptions.md)
- **Subscription box** (0) — [T](T-subscriptions.md)
- **Pause / skip / cancel lifecycle** (0 — actions never named) — [T](T-subscriptions.md)
- **Stripe Billing / Chargebee / Recurly / Zuora comparison** (0) — [T](T-subscriptions.md)

### B-6. Marketing / SEO vocabulary

- **A/B testing / experimentation** (0 — only feature-flag-based referral) — [R](R-marketing-seo.md)
- **Klaviyo / Mailchimp / Braze** (0 — only SendGrid as transactional gateway) — [R](R-marketing-seo.md)
- **Canonical URL** (0 — Open Graph + meta title/desc covered; canonical absent) — [R](R-marketing-seo.md)
- **JSON-LD / Schema.org / structured data** (0) — [R](R-marketing-seo.md)
- **Meta Pixel / Conversions API (CAPI)** (one passing mention in GA4 module) — [R](R-marketing-seo.md)
- **Segment / audience / RFM / affinity** (vocabulary missing; features hidden behind VC names) — [R](R-marketing-seo.md)

### B-7. Search vocabulary

- **Typesense** (0) — [J](J-search-discovery.md)
- **Meilisearch** (0) — [J](J-search-discovery.md)
- **Stopwords / stemming** (0) — [J](J-search-discovery.md)
- **"Did you mean" / spell correction** (0) — [J](J-search-discovery.md)
- **Merchandising rules** (0 — "Curations" covers pin/promote but not named so) — [J](J-search-discovery.md)

### B-8. Architecture / DDD vocabulary

- **Aggregate / aggregate root** (0 DOCS vs 75 CODE) — [W](W-ddd-cqrs-vocabulary.md)
- **Value object** (3 incidental vs 118 CODE) — [W](W-ddd-cqrs-vocabulary.md)
- **Specification pattern** (0 vs 18 CODE files) — [W](W-ddd-cqrs-vocabulary.md)
- **Bounded context / ubiquitous language** (1 outbound Fowler link / 0) — [W](W-ddd-cqrs-vocabulary.md), [F](F-architecture-patterns.md)
- **Anti-corruption layer** (0 DOCS, 0 CODE — despite `ToModel` / `FromModel` playing the role) — [W](W-ddd-cqrs-vocabulary.md)
- **Strangler fig pattern** (0 — real gap given VC's "replace legacy" positioning) — [F](F-architecture-patterns.md)
- **Polymorphism** (1 DOC — "type inheritance" is VC's proprietary label) — [U](U-modularity-extensibility.md)

### B-9. Cloud / ops vocabulary

- **AWS ECS / EKS / Fargate / Beanstalk** (0 in DeploymentGuide) — [A](A-deployment-infra.md)
- **GCP GKE / Cloud Run** (0) — [A](A-deployment-infra.md)
- **Terraform / Pulumi / Bicep / CloudFormation** (0) — [A](A-deployment-infra.md)
- **Helm / kubectl / K8s manifests** (marketing + one `-HelmParameters` only) — [A](A-deployment-infra.md)
- **Zero-downtime / canary / rolling** (McKinsey quote only) — [A](A-deployment-infra.md)
- **SLO / SLI / error budget / RED / USE** (0 SRE vocabulary) — [D](D-observability.md)
- **Runbook / playbook / on-call / pagerduty / incident response** (0) — [D](D-observability.md)
- **Liveness vs readiness probe** (0) — [D](D-observability.md)
- **Jaeger / Zipkin / Tempo** (0 named tracing backends) — [D](D-observability.md)
- **Prometheus** (0) — [D](D-observability.md)

### B-10. Messaging / API vocabulary

- **Outbox pattern** (0) — [C](C-messaging-integration.md)
- **Saga / process manager** (0 — only Hangfire background-job / approval-flow) — [C](C-messaging-integration.md)
- **Idempotency key / idempotent consumer** (0 — two tangential lines) — [C](C-messaging-integration.md), [G](G-api-surface.md)
- **DLQ (dead-letter queue)** (0) — [C](C-messaging-integration.md)
- **HMAC webhook signatures** (0) — [C](C-messaging-integration.md)
- **RabbitMQ / Kafka / AMQP / MassTransit / NServiceBus** (0 — Azure Event Grid only) — [C](C-messaging-integration.md)
- **Rate limiting / throttling / 429 / retry-after** (0 of substance) — [G](G-api-surface.md)
- **API versioning (URL / header / accept-version)** (0 — only module SemVer) — [G](G-api-surface.md)
- **RFC 7807 / Problem+JSON / ProblemDetails** (0 — .NET 10's default, not mentioned) — [G](G-api-surface.md)
- **gRPC** (only as OTLP exporter to OpenTelemetry collector) — [C](C-messaging-integration.md)

### B-11. Security vocabulary

- **SAML** (0 in docs; 3 incidental in code) — [E](E-security-auth.md)
- **WebAuthn / passkeys / FIDO2** (0) — [E](E-security-auth.md)
- **MFA / TOTP** (0 enrollment flow — only a `twoFactorEnabled` boolean on GraphQL `UserType`) — [E](E-security-auth.md)
- **OWASP Top 10** (0 — no XSS / SQLi / IDOR / SSRF mentions by attack name) — [E](E-security-auth.md)
- **PCI AoC / SAQ scope** (0 VC-side statement) — [E](E-security-auth.md)
- **Data residency / regional data sovereignty** (0) — [E](E-security-auth.md)
- **Zero-trust** (0) — [X](X-modern-buzzwords.md)

### B-12. Frontend / UX vocabulary

- **WCAG 2.1 AA / ARIA attributes / axe / pa11y** (13-line ADA page, 2 stray `aria-label` — material gap given EU EAA mandate 2025-06-28) — [H](H-frontend-ux.md), [V](V-testing-qa.md)
- **JAMstack** (0) — [H](H-frontend-ux.md)
- **Micro-frontend / module federation** (0) — [H](H-frontend-ux.md)
- **RTL (Arabic / Hebrew)** (0 meaningful DOCS hits; 6 RTL markers in source — capability partly exists but docs silent) — [S](S-cms-content-i18n.md)
- **LCP / CLS / INP / TTFB / Core Web Vitals** (0 nomenclature) — [S](S-cms-content-i18n.md)
- **React Native / Flutter / Swift / Kotlin mobile SDK** (0) — [H](H-frontend-ux.md)

### B-13. Content / CMS vocabulary

- **Content blocks / slots / page-composition primitives** (174 "widget" hits are admin dashboard widgets; 2 "content block" files) — [S](S-cms-content-i18n.md)
- **Draft / Published / Preview mode / page versioning** (0 for Pages module) — [S](S-cms-content-i18n.md)

### B-14. Testing vocabulary

- **Pact / contract testing / consumer-driven contracts** (0) — [V](V-testing-qa.md)
- **k6 / JMeter / load testing** (0 tooling — only prose release-gate claim) — [V](V-testing-qa.md)
- **Accessibility testing (axe-core / axe-playwright / pa11y)** (0 — ADA claim without tooling) — [V](V-testing-qa.md)
- **SAST / DAST / SBOM / dependency scanning / OWASP ZAP** (0) — [V](V-testing-qa.md)

### B-15. Modern architecture vocabulary

- **MACH** (0 dev-guide; 2 marketing mentions actually *contrast* Atomic Architecture vs MACH; VC not a MACH Alliance member) — [X](X-modern-buzzwords.md)
- **Jamstack** (0) — [X](X-modern-buzzwords.md)
- **Edge compute / edge functions** (0 — correctly absent for modular monolith; buyers never told this) — [X](X-modern-buzzwords.md)
- **Service mesh** (0 — correctly absent; never explained) — [X](X-modern-buzzwords.md)

---

## Cross-index: claim-to-verdict matrix

See each group's file for the per-claim Context7 / WebSearch / grep evidence: [A](A-deployment-infra.md) · [B](B-data-storage.md) · [C](C-messaging-integration.md) · [D](D-observability.md) · [E](E-security-auth.md) · [F](F-architecture-patterns.md) · [G](G-api-surface.md) · [H](H-frontend-ux.md) · [I](I-catalog-pim.md) · [J](J-search-discovery.md) · [K](K-cart-checkout.md) · [L](L-pricing-promotions.md) · [M](M-order-inventory-fulfillment.md) · [N](N-tax-shipping.md) · [O](O-payments.md) · [P](P-b2b-specifics.md) · [Q](Q-marketplace.md) · [R](R-marketing-seo.md) · [S](S-cms-content-i18n.md) · [T](T-subscriptions.md) · [U](U-modularity-extensibility.md) · [V](V-testing-qa.md) · [W](W-ddd-cqrs-vocabulary.md) · [X](X-modern-buzzwords.md).

## Prioritization guidance

If the remediation budget is finite, the audit suggests this priority order (highest ROI first):

1. **Close the docs-vs-code vocabulary gap.** Add industry-term aliases ("AbstractTypeFactory (a.k.a. polymorphism / typed-factory pattern)", "DynamicProperty (a.k.a. custom field / attribute / metafield)", "MediatR-based CQRS handlers", "Modular Monolith"). One glossary page + per-page cross-references fixes ~20 🟠 findings at low cost. Groups: [F](F-architecture-patterns.md), [U](U-modularity-extensibility.md), [W](W-ddd-cqrs-vocabulary.md), [V](V-testing-qa.md).
2. **Close the marketing-vs-substance gap on B2B.** Punchout, EDI, CPQ, net terms, multi-level hierarchy are table stakes for the platform's own positioning. Group [P](P-b2b-specifics.md).
3. **Write a payments-orchestration overview.** Even if Stripe/Adyen/PayPal stay out of scope, name the payment-orchestration / vaulting / 3DS2 / BNPL concepts and point at the extensibility hook. Group [O](O-payments.md).
4. **Add a subscriptions how-to.** Either a full billing guide or an honest "use Stripe Billing / Chargebee via webhooks" comparison. Group [T](T-subscriptions.md).
5. **Fix the OMS contradiction.** Either upgrade the module, or rewrite the marketing page to match the user-guide disclaimer. Group [M](M-order-inventory-fulfillment.md).
6. **Ship a WCAG 2.1 AA statement + testing guide.** EU EAA has been mandatory since 2025-06-28 for e-commerce. Groups [H](H-frontend-ux.md), [V](V-testing-qa.md).
7. **Add a deployment matrix beyond Azure.** At minimum a Kubernetes / Helm chart walkthrough and an AWS + GCP reference posture. Group [A](A-deployment-infra.md).
8. **Add operational docs** (SLO / SLI / runbooks / liveness-readiness / Prometheus scrape). Group [D](D-observability.md).
9. **Fill the API cross-cutting concerns**: rate limits, idempotency keys, API versioning strategy, RFC 7807. Group [G](G-api-surface.md).
10. **Establish CMS vocabulary** (blocks/slots, draft/published, RTL, Core Web Vitals). Group [S](S-cms-content-i18n.md).
