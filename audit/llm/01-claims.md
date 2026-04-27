# Per-group claim lists

Each claim reads as "X is poorly/absent in VC docs & site". The agent confirms or rejects.

## A — Deployment & Infrastructure
1. AWS-specific deployment (ECS/EKS/Elastic Beanstalk/Fargate) is not documented.
2. Google Cloud Platform (GKE, Cloud Run) deployment is not documented.
3. Kubernetes / Helm charts / manifests are not documented.
4. Docker multi-stage / compose for production is poorly documented.
5. Infrastructure-as-Code (Terraform, Pulumi, Bicep, ARM, CloudFormation) is absent.
6. GitOps / ArgoCD / Flux is absent.
7. Zero-downtime deployment, blue/green, canary, rolling deploys are absent.
8. Horizontal scaling / autoscaling / load balancing is poorly documented.
9. Session affinity / sticky sessions requirements are poorly documented.
10. CI/CD beyond GitHub Actions (Azure DevOps, GitLab CI, Jenkins) is absent.

## B — Data, Storage, Persistence
1. PostgreSQL support level (vs SQL Server primary) is poorly documented.
2. MySQL support is poorly documented.
3. Redis / distributed caching configuration is poorly documented.
4. Azure Blob Storage / S3 / object-store swapping is poorly documented.
5. Database migrations (how, when, versioning) are thinly documented.
6. Zero-downtime schema migrations / expand-contract pattern is absent.
7. Read replicas, sharding, multi-region are absent.
8. Backup / restore / disaster recovery is thinly documented.
9. Data retention policies (GDPR-right-to-be-forgotten) are poorly documented.
10. Optimistic concurrency / row-versioning is absent from docs.

## C — Messaging & Integration
1. Azure Service Bus usage is poorly documented.
2. RabbitMQ / Kafka / external broker integration is absent.
3. Webhooks (delivery guarantees, retries, signatures) are thinly documented.
4. Outbox pattern / transactional messaging is absent.
5. Saga / process manager / long-running workflows are absent.
6. Idempotency keys / idempotent consumers are absent.
7. Event bus / domain events are poorly documented.
8. EDI / cXML / Punchout (OCI) integration is absent/thin.
9. ETL / data-pipeline integration (Kafka Connect, Airflow) is absent.
10. gRPC / service-to-service RPC is absent.

## D — Observability & Operations
1. OpenTelemetry support is poorly documented.
2. Application Insights specifics are poorly documented.
3. Prometheus / Grafana integration is absent.
4. Structured logging (Serilog, NLog, OpenSearch) is thinly documented.
5. Correlation IDs / trace IDs across services is absent.
6. Health checks / liveness / readiness probes are poorly documented.
7. SLIs / SLOs / error budgets are absent.
8. Distributed tracing is absent.
9. Metrics (RED, USE) are absent.
10. Alerting / on-call playbooks are absent.

## E — Security, Auth, Compliance
1. OAuth2 / OIDC provider configuration is thinly documented.
2. SAML / enterprise SSO is thinly documented.
3. JWT claim structure / validation is poorly documented.
4. WebAuthn / passkeys / MFA / TOTP is absent.
5. RBAC vs ABAC vs policy-based authorization: naming unclear.
6. GDPR / CCPA / data residency statements are thin.
7. PCI DSS scope / tokenization is thin.
8. OWASP Top 10 mitigations are not called out.
9. Content Security Policy (CSP) / anti-CSRF is thin.
10. Secret management (Key Vault, AWS Secrets Manager, Vault) is poorly documented.

## F — Architecture Patterns
1. "Domain-Driven Design" explicit references in docs.
2. "Aggregate root" / "bounded context" / "ubiquitous language" usage.
3. "Repository pattern" / "unit of work" usage.
4. "CQRS" usage.
5. "Event sourcing" usage.
6. "Mediator" (MediatR) usage in docs (codebase uses it).
7. "Strangler fig pattern" for migration is absent.
8. "Circuit breaker" / "retry" / "Polly" is absent.
9. "Feature flag" / "feature toggle" is absent.
10. "Multi-tenancy" model & isolation is poorly documented.

## G — API Surface
1. REST API reference completeness (vs inline Swagger).
2. GraphQL schema reference (Experience API / XAPI) discoverability.
3. OpenAPI spec download / Postman collection is thin.
4. API versioning strategy is thin.
5. Rate limiting / throttling / API quotas are absent.
6. Idempotency keys on POST endpoints are absent.
7. Pagination / filtering / sorting conventions are thin.
8. Long-polling / webhooks / server-sent events / WebSockets are thin.
9. API pagination cursor vs offset is thin.
10. API error-model standard (Problem+JSON / RFC 7807) is absent.

## H — Frontend, UX, Accessibility
1. Progressive Web App (PWA) support is poorly documented.
2. Server-Side Rendering (SSR) / Incremental Static Regeneration (ISR) is thin.
3. JAMstack positioning is absent.
4. Micro-frontends / module federation is absent.
5. Frontend modularity & extensibility is poorly documented.
6. Design system / design tokens are thin.
7. Theming / white-label / multi-brand is thin.
8. Accessibility (WCAG, ARIA) is not called out.
9. Mobile apps / React Native / Flutter SDKs are absent.
10. Storybook / component catalog discoverability is thin.

## I — Catalog, PIM, DAM
1. "PIM" (Product Information Management) term usage.
2. "DAM" (Digital Asset Management) term usage.
3. Product variants / configurable products documentation clarity.
4. Product bundles / kits are thin.
5. Taxonomy / hierarchical categories are thin.
6. Dynamic properties vs attributes terminology collision.
7. SKU, GTIN, UPC, EAN, ISBN identifier support is thin.
8. Product grouping / master+variant model is thin.
9. Asset pipeline / image derivatives is thin.
10. Content localization per product is thin.

## J — Search & Discovery
1. Elasticsearch configuration (vs Azure Search, Lucene) is thin.
2. OpenSearch support is absent.
3. Algolia / Typesense / Meilisearch alternatives are absent.
4. Faceted search / guided navigation docs are thin.
5. Synonym / stopword / stemming tuning is thin.
6. Vector search / semantic search / embeddings is absent.
7. Autocomplete / typeahead / "did you mean" is thin.
8. Boosting / relevance tuning is thin.
9. Search analytics / zero-result report is thin.
10. Personalized search / merchandising rules are thin.

## K — Cart & Checkout
1. Guest checkout is thin.
2. Multi-cart / saved carts / named carts is thin.
3. One-page / accordion checkout guidance is thin.
4. Cart abandonment tracking / emails is thin.
5. Upsell / cross-sell on cart page is thin.
6. Express checkout (Apple Pay, Google Pay) is thin.
7. Clienteling / assisted selling is absent.
8. Minimum order quantity / order increments is thin.
9. Cart merging (guest → logged-in) is thin.
10. Save-for-later / wishlist → cart flow is thin.

## L — Pricing & Promotions
1. Tier pricing / volume pricing is thin.
2. Customer-group / contract pricing is thin.
3. Dynamic pricing / rule-based pricing is thin.
4. Discount stacking / priority rules are thin.
5. Coupon / voucher management is thin.
6. Gift-card issuance / redemption is thin.
7. Loyalty program (points, tiers) is thin.
8. Bundle pricing is thin.
9. Catalog-level vs cart-level promotions terminology is thin.
10. Price lists / currency-specific price lists are thin.

## M — Order / Inventory / Fulfillment
1. "OMS" (Order Management System) term usage.
2. "WMS" (Warehouse Management System) term usage.
3. Multi-warehouse fulfillment is thin.
4. BOPIS (Buy Online Pickup In Store) is thin.
5. BORIS (Buy Online Return In Store) is absent.
6. Ship-from-store / endless aisle is absent.
7. Backorder / preorder is thin.
8. Returns / RMA flow is thin.
9. Split shipments / partial fulfillment is thin.
10. Stock reservations / ATP (Available-to-Promise) is thin.

## N — Tax & Shipping
1. Avalara AvaTax integration is thin.
2. TaxJar / Vertex alternatives are absent.
3. EU VAT / VIES validation is thin.
4. GST (India, Australia, Canada) is thin.
5. Tax-exempt customer groups is thin.
6. Carrier integrations (UPS, FedEx, DHL, USPS) are thin.
7. ShipStation / EasyPost / Shippo are absent.
8. Shipping zones / rate tables are thin.
9. Free-shipping thresholds are thin.
10. Click-and-collect / in-store pickup is thin.

## O — Payments
1. Stripe integration is thin.
2. Adyen integration is thin.
3. PayPal / Braintree integration is thin.
4. Klarna / Afterpay / BNPL is absent.
5. SCA / 3DS2 compliance is thin.
6. Tokenization / vaulting is thin.
7. Saved cards / recurring billing is thin.
8. Apple Pay / Google Pay wallet support is thin.
9. Payment orchestration concept is absent.
10. Refunds / partial refunds / void is thin.

## P — B2B Specifics
1. Quote / RFQ flow is thin.
2. CPQ (Configure Price Quote) is absent.
3. Account hierarchy / company roles is thin.
4. Approval workflow is thin.
5. Purchase orders / PO number is thin.
6. Punchout (OCI / cXML) is thin.
7. EDI integration is thin.
8. Contract catalogs is thin.
9. Buyer-seller negotiation is thin.
10. Net terms / credit limit is thin.

## Q — Marketplace / Multi-vendor
1. Seller onboarding / KYC is thin.
2. Commission / payout split is thin.
3. Multi-vendor single cart / order splitting is thin.
4. Vendor product approval workflow is thin.
5. Marketplace SEO / vendor pages is thin.
6. Vendor analytics / dashboards is thin.
7. Return split across vendors is absent.
8. Stripe Connect / Adyen MarketPay is absent.
9. Drop-ship vendor integration is thin.
10. Vendor-specific shipping rules is thin.

## R — Marketing, SEO, Personalization
1. Personalization engine is thin.
2. Recommendation engine is thin.
3. A/B testing / experimentation is absent.
4. Abandoned cart email is thin.
5. Email marketing (Klaviyo, Mailchimp, Braze) integration is thin.
6. SEO — canonical URLs / structured data / JSON-LD are thin.
7. Sitemap generation is thin.
8. Customer segmentation is thin.
9. Google Analytics / GTM / GA4 is thin.
10. Meta pixel / conversion API is absent.

## S — CMS / Content / i18n
1. Multi-language / i18n is thin.
2. Multi-currency is thin.
3. Multi-store / multi-brand is thin.
4. Content blocks / slots / widgets is thin.
5. CMS page versioning / preview is thin.
6. Liquid templating documentation is thin.
7. RTL (Arabic, Hebrew) is absent.
8. Page speed / Core Web Vitals is absent.
9. AMP / Mobile pages is absent.
10. Headless CMS comparison (Contentful, Sanity, Strapi) is absent.

## T — Subscriptions & Recurring
1. Subscription product type is thin.
2. Recurring order schedule is thin.
3. Dunning / failed-payment recovery is absent.
4. Usage-based / metered billing is absent.
5. Subscription upgrade / downgrade is thin.
6. Pause / skip / cancel is thin.
7. Subscription boxes is absent.
8. Subscription analytics / MRR is absent.
9. Prorated billing is absent.
10. Stripe Billing / Chargebee / Recurly comparison is absent.

## U — Modularity & Extensibility (incl. AbstractTypeFactory)
1. "Polymorphism" term appears in docs.
2. "Method overriding" / "override" term appears in docs.
3. "AbstractTypeFactory" — documented as an extensibility concept (not just API reference).
4. "Dependency injection" in platform's own terms is thin.
5. Module / plugin anatomy is thin.
6. Dynamic properties concept vs attributes/custom fields is thin.
7. Events / handlers / subscribers are thin.
8. Customizing / overriding a built-in entity model is thin.
9. Liquid / scripting extensibility is thin.
10. NuGet package publishing for custom modules is thin.

## V — Testing & QA
1. Unit testing framework (xUnit, NUnit) in platform is thin.
2. Integration testing is thin.
3. E2E testing (Playwright, Cypress) is thin.
4. Load / performance testing (k6, JMeter) is absent.
5. Contract testing (Pact) is absent.
6. Mocking / test doubles is thin.
7. Test data / fixtures is thin.
8. Visual regression testing is absent.
9. Accessibility testing is absent.
10. Security testing (OWASP ZAP, Burp) is absent.

## W — DDD & CQRS vocabulary
1. "Domain model" term usage.
2. "Aggregate" / "aggregate root" usage.
3. "Value object" usage.
4. "Entity" — used, but with what meaning (DDD vs ORM)?
5. "Specification pattern" usage.
6. "CQRS" usage.
7. "Command" / "Query" handlers usage.
8. "Domain event" vs "integration event" usage.
9. "Bounded context" usage.
10. "Anti-corruption layer" usage.

## X — Modern architecture buzzwords
1. "MACH" (Microservices, API-first, Cloud-native, Headless) usage.
2. "Composable commerce" usage — VC markets this but depth?
3. "Headless commerce" usage.
4. "API-first" usage.
5. "Cloud-native" usage.
6. "Microservices" vs "modular monolith" — honest positioning in docs?
7. "Jamstack" usage.
8. "Edge compute" / "edge functions" usage.
9. "Zero-trust" usage.
10. "Service mesh" usage.
