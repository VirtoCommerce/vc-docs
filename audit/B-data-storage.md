# Group B — Data, Storage, Persistence

## Claim 1: PostgreSQL support level (vs SQL Server primary) is poorly documented

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support PostgreSQL as the primary database, or is it SQL Server only? How to configure PostgreSQL?"):
Multiple concrete hits. DB-agnostic architecture is explicitly called out; supports SQL Server, MySQL, PostgreSQL. Dedicated page `Fundamentals/Persistence/DB-Agnostic/configuring-vc-with-db-providers.md` with minimum version (PostgreSQL 12+), connection-string example, appsettings snippet, and a how-to for case-insensitive search on PostgreSQL. `system-requirements.md` lists it as a first-class option. Default provider is SqlServer but PostgreSQL is treated as equal.

**WebSearch**: skipped — Context7 fully covered the claim.

**Grep** (scope: DOCS):
- `grep -rliI "postgres|postgresql" DOCS`: 14 files
- Top hits: `PlatformDeveloperGuide/.../Persistence/DB-Agnostic/configuring-vc-with-db-providers.md:60-79`, `.../Configuration-Reference/appsettingsjson.md:261-265,298,1076`, `.../Back-End-Architecture/02-conceptual-overview.md:21`, `.../Getting-Started/system-requirements.md`, `PlatformUserGuide/.../sql-queries/overview.md:17`, `Tutorials-and-How-tos/How-tos/adding-case-sensitive-search-support-for-postgre.md`.

**Verdict**: ✅ Well documented
**Note**: Dedicated setup page, config-reference coverage, and a known-gotcha how-to. Claim rejected.

---

## Claim 2: MySQL support is poorly documented

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support MySQL? How to configure MySQL as the database provider and what are production considerations?"):
MySQL is documented symmetrically to PostgreSQL. `configuring-vc-with-db-providers.md` includes a dedicated MySQL section with two connection-string styles, minimum version (5.7+), and appsettings snippet. Listed in system requirements and DatabaseProvider enum.

**WebSearch**: skipped — Context7 conclusive.

**Grep** (scope: DOCS):
- `grep -rliI "mysql" DOCS`: 11 files
- Top hits: `PlatformDeveloperGuide/.../Persistence/DB-Agnostic/configuring-vc-with-db-providers.md`, `.../Persistence/DB-Agnostic/transforming-custom-module.md:9`, `appsettingsjson.md:1076`, `system-requirements.md`.

**Verdict**: ✅ Well documented
**Note**: Same depth as PostgreSQL. Production considerations (perf tuning, charset) aren't called out separately, but setup and config are covered.

---

## Claim 3: Redis / distributed caching configuration is poorly documented

**Context7** (`/virtocommerce/vc-docs`, query: "How do I configure Redis distributed cache for VirtoCommerce? What caching options are supported in production?"):
Multiple hits. `appsettingsjson.md` covers `Redis.ChannelName` / `BusRetryCount`. `Fundamentals/Scalability/scaling-configuration-on-azure-cloud.md` has end-to-end Redis backplane config for SignalR push notifications and memory-cache synchronization across multiple instances, including Authoring-App and Frontend-App variants.

**WebSearch**: skipped — Context7 conclusive.

**Grep** (scope: DOCS):
- `grep -rliI "redis" DOCS`: 22 files
- Top hits: `PlatformDeveloperGuide/.../Fundamentals/Scalability/scaling-configuration-on-azure-cloud.md`, `appsettingsjson.md`, multiple scalability pages.

**Verdict**: ✅ Well documented
**Note**: Covered primarily as a SignalR/push-notification backplane and memory-cache sync layer. "Distributed cache" as a first-class cache-aside pattern is not framed that way, but the configuration surface is fully documented.

---

## Claim 4: Azure Blob Storage / S3 / object-store swapping is poorly documented

**Context7** (`/virtocommerce/vc-docs`, query: "How to swap Azure Blob Storage to AWS S3 or another object store for VirtoCommerce asset storage?"):
Only two providers surface: `FileSystem` and `AzureBlobStorage`. Dedicated page `Getting-Started/Post-Installation-Steps/03-configuring-asset-blob-storage.md` covers Azure Blob for production. No S3 / MinIO / GCS option is documented.

**WebSearch**: skipped — Context7 conclusive; absence is the finding.

**Grep** (scope: DOCS):
- `grep -rliI "azure blob|blob storage" DOCS`: 32 files
- `grep -rliI "\bS3\b|AWS S3|AmazonS3" DOCS`: 1 file — and that hit (`maintenance-tasks-for-sql.md:188` "two S3 databases") is unrelated to object storage (it's a typo'd SQL-pool tier reference).
- Asset provider pages: `PlatformDeveloperGuide/.../Configuration-Reference/appsettingsjson.md`, `.../Getting-Started/Post-Installation-Steps/03-configuring-asset-blob-storage.md`, `PlatformUserGuide/.../assets/overview.md`.

**Verdict**: 🟠 Implemented-for-Azure-only, S3/other object stores undocumented
**Note**: Azure Blob is well documented, but "swapping" is a two-option menu (FileSystem vs Azure Blob). Anyone deploying to AWS/GCP gets no guidance. Third-party Amazon-S3 asset-provider modules exist in the VC ecosystem but aren't referenced in docs.

---

## Claim 5: Database migrations (how, when, versioning) are thinly documented

**Context7** (`/virtocommerce/vc-docs`, query: "How does VirtoCommerce handle database schema migrations, Entity Framework migrations, versioning and upgrades for the platform and custom modules?"):
Solid hits. `Tutorials/create-new-module-from-scratch.md` shows `Add-Migration`. `Tutorials/extending-domain-models.md` covers derived DbContext + manual edits. `extending-database-model.md` shows raw SQL in migrations. A dedicated `CLI-tools/grab-migrator.md` utility extracts idempotent SQL from platform + modules for pre-apply ordering. `cold-start-and-data-migration.md` exists (marked WIP). `How-tos/adding-case-sensitive-search-support-for-postgre.md` shows migration-level patching.

**WebSearch**: skipped — Context7 covered.

**Grep** (scope: DOCS):
- `grep -rliI "migration|migrations" DOCS`: 52 files
- `grep -rliI "entity framework|EF migration|dotnet ef|add-migration|update-database" DOCS`: 14 files
- Top hits: `PlatformDeveloperGuide/.../CLI-tools/grab-migrator.md`, `.../CLI-tools/cold-start-and-data-migration.md`, `.../Tutorials/extending-domain-models.md`, `.../Tutorials/extending-database-model.md`.

**Verdict**: ✅ Well documented
**Note**: "How" is covered. "When" (at module install/update via vc-build) is implicit in install-and-update docs. "Versioning" equates to Platform/module version strings in the manifest — fine. Claim rejected.

---

## Claim 6: Zero-downtime schema migrations / expand-contract pattern is absent

**Context7** (`/virtocommerce/vc-docs`, query: "How do I perform zero-downtime database schema migrations in VirtoCommerce using the expand-contract pattern or blue-green database strategy?"):
No relevant results. Context7 returned general migration snippets but nothing on zero-downtime schema evolution, expand-contract, backwards-compatible migrations, or online DDL.

**WebSearch** (query: `commercetools Shopify "zero downtime" database migration expand contract pattern documentation`):
Expand-contract / strangler patterns are standard industry practice (Medium, dev.to, Domaine, commercetools blog). Competitors explicitly address this; VC does not.

**Grep** (scope: DOCS):
- `grep -rliI "zero.downtime|expand.contract|expand and contract" DOCS`: 3 files — all are `blue-green indexing` or a McKinsey quote in B2BExperts, none are about DB schema.
- `grep -rliI "blue.green|blue/green" DOCS`: 9 files — all relate to **search-index** blue-green (`Indexed-Search/indexing/blue-green-indexing.md`) or VC Cloud deployment overview, not DB schema migrations.

**Verdict**: 🔴 Absent
**Note**: VC has blue-green for the search index but is silent on application-level zero-downtime DB schema evolution. Given that `vc-build update` takes the app offline and runs EF migrations in-place, docs implicitly assume a maintenance window.

---

## Claim 7: Read replicas, sharding, multi-region are absent

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce support read replicas, database sharding, or multi-region active-active database deployments?"):
No hits for replicas/sharding/multi-region DB. Answers returned generic DB-agnostic scalability claims ("unlimited scalability") and Kubernetes-on-Azure VC Cloud overview — none address data-tier topology.

**WebSearch**: skipped — confidence high from Context7 + grep.

**Grep** (scope: DOCS):
- `grep -rliI "read.replica|read replicas" DOCS`: **0 files**
- `grep -rliI "sharding|shard" DOCS`: **0 files**
- `grep -rliI "multi.region|geo.replication|geo-redundant" DOCS`: 15 files — **all are marketing "multi-regional e-commerce"** (B2B Cadillac/KW case study, marketplace, international-ecommerce) referring to business footprint, not DB topology. Zero hits for `\bRTO\b` or `\bRPO\b`.

**Verdict**: 🔴 Absent
**Note**: No data-tier HA guidance. Business-level "multi-region" vocabulary exists and will mislead readers.

---

## Claim 8: Backup / restore / disaster recovery is thinly documented

**Context7** (`/virtocommerce/vc-docs`, query: "How does VirtoCommerce handle backup, restore, and disaster recovery for production databases and assets? What is the DR runbook?"):
`platform/user-guide/docs/backup-and-restore.md` covers admin-UI export/import of Platform data as a ZIP. `CLI-tools/virto-cloud-overview.md` lists "Backup routines" as a Virto Cloud feature bullet. `vc-build install`/`update` auto-snapshots files (`-skip Backup` flag).

**WebSearch**: skipped — absence pattern is clear.

**Grep** (scope: DOCS):
- `grep -rliI "backup|restore" DOCS`: 24 files (many are file-backup in vc-build or blue-green-indexing "backup index" swap terminology, not DR).
- `grep -rniE "disaster recovery|\bRTO\b|\bRPO\b" DOCS`: **0 real hits** after filtering substrings.
- Key hits: `PlatformUserGuide/.../backup-and-restore.md`, `PlatformDeveloperGuide/.../CLI-tools/install-and-update-platform-and-modules.md:215-220`, `.../CLI-tools/virto-cloud-overview.md:28`, `.../CLI-tools/package-management.md:143`.

**Verdict**: 🟡 Mentioned but thin
**Note**: Admin-export feature documented; DR (RTO/RPO, cross-region failover, PITR, backup cadence, restore drills) is not. Virto Cloud mentions backups without detail.

---

## Claim 9: Data retention policies (GDPR right-to-be-forgotten) are poorly documented

**Context7** (`/virtocommerce/vc-docs`, query: "How does VirtoCommerce support GDPR right to be forgotten, data retention policies, and customer data deletion workflows?"):
Strong hits for GDPR-as-a-module. `platform/user-guide/docs/gdpr/overview.md` + `manage-personal-data.md` cover anonymization ("remove personal details by anonymizing"), download-as-JSON export, plus admin-UI flow. Maps to `vc-module-gdpr` on GitHub.

**WebSearch**: skipped.

**Grep** (scope: DOCS):
- `grep -rliI "gdpr|right.to.be.forgotten|data.retention|data.erasure" DOCS`: 25 files
- `grep -rliI "data retention|retention policy|retention policies" DOCS`: 3 files — only `implementing-telemetry-with-useappinsights.md:493` (Application Insights retention, not e-commerce data) and a McKinsey quote.
- Key hits: `PlatformUserGuide/.../gdpr/overview.md`, `.../gdpr/manage-personal-data.md`, `PlatformUserGuide/.../generic-export/overview.md:28`.

**Verdict**: 🟡 Mentioned but thin
**Note**: Right-to-be-forgotten is covered via the GDPR module. **Retention policies** per-entity (order-history TTL, audit-log retention, session/log pruning, CCPA) are not specified — only App-Insights telemetry retention is called out, and only in passing.

---

## Claim 10: Optimistic concurrency / row-versioning is absent from docs

**Context7** (`/virtocommerce/vc-docs`, query: "How does VirtoCommerce handle optimistic concurrency control, row-versioning, ETag or concurrency tokens in its data layer and APIs?"):
One real hit: `Fundamentals/Persistence/Concurrency-handling/concurrency-handling.md` — describes overriding `CommitAsync` to catch `DbUpdateConcurrencyException`. Does **not** use the terms "optimistic concurrency", "row version", "concurrency token", or "ETag".

**WebSearch**: skipped.

**Grep** (scope: DOCS):
- `grep -rliI "optimistic concurrency|rowversion|concurrency token|\bETag\b" DOCS`: 1 file (the concurrency-handling page — and only `DbUpdateConcurrencyException` triggered it; no "optimistic" / "rowversion" / "ETag" strings present).
- `grep -rniI "optimistic concurrency|rowversion|\bETag\b" DOCS`: 0 hits.
- Code (CODE scope): `[Timestamp]`, `IsConcurrencyToken`, `RowVersion`, `ConcurrencyCheck` present in platform source (MySQL migrations + `SecurityDbContextModelSnapshot`), so the mechanism **is** implemented.

**Verdict**: 🟠 Implemented but undocumented (term-wise)
**Note**: There's a single page discussing `DbUpdateConcurrencyException` handling, but none of the canonical vocabulary (optimistic concurrency, rowversion, ETag, If-Match) appears. Developers searching for these terms will find nothing.
