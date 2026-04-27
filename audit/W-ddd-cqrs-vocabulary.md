# Group W — DDD & CQRS vocabulary

Term-usage audit: does VC's documentation *speak* DDD, or does it avoid the vocabulary?
Counts are **DOCS** (user/developer guides + site) vs **CODE** (platform/frontend source).

---

## Claim 1: "Domain model" term usage

**Context7** (`/virtocommerce/vc-docs`, query: "Does VirtoCommerce use a domain model approach? How is the domain model structured per module?"):
Rich results. The developer guide explicitly uses the term: "Module.Core contains all abstractions and domain model definitions", "Model folder includes domain model classes", Events folder "holds all domain and integration events". There is a dedicated tutorial `extending-domain-models.md` and a best-practices page titled "Identify Domain Model Boundaries for Each Module".

**WebSearch** (query: "'domain model' DDD e-commerce platform documentation terminology"):
"Domain model" is a standard, ubiquitous DDD term in e-commerce literature; Elastic Path uses the exact phrase "Extending Domain Model" (matching VC's tutorial title).

**Grep**:
- `grep -rlIi "domain model" DOCS`: **12 files**
- `grep -rhIi "domain model" DOCS`: **17 occurrences**
- `grep -rlIi "domain model" CODE`: **16 files**
- Top DOCS hits:
  - `PlatformDeveloperGuide/.../Modularity/05-best-practices.md:1` — "Identify Domain Model Boundaries for Each Module..."
  - `PlatformDeveloperGuide/.../Modularity/02-folder-structure.md:91` — "Virto uses the **Data Mapping** pattern to isolate the domain model from the persistence specific one (**Persistence Ignorance** principle)"
  - `PlatformDeveloperGuide/.../Tutorials/extending-domain-models.md:1` — "# Extend Domain Models"

**Verdict**: ✅ Well documented
**Note**: VC explicitly names the concept, ties it to Data Mapper / Persistence Ignorance, and invites readers to extend. This is the one DDD term VC owns.

---

## Claim 2: "Aggregate" / "aggregate root" usage

**Context7** (query: "What's VirtoCommerce's aggregate-root design? Does it use aggregates to group entities with consistency boundaries?"):
No relevant results. Context7 returned DB-provider and connection-string snippets, plus "Virto utilizes the Data Mapper pattern" — it **cannot** find aggregate-root material because the docs don't teach the concept.

**WebSearch** (query: "'aggregate root' DDD ecommerce architecture commercetools Spryker documentation"):
"Aggregate root" is the canonical DDD entry-point-to-a-cluster term. Standard reference works (Fowler, Evans, Microsoft DDD guide) treat it as core vocabulary.

**Grep**:
- `grep -rlIi "aggregate root|aggregateroot" DOCS`: **0 files**
- `grep -rhIi "aggregate root|aggregateroot" DOCS`: **0 occurrences**
- `grep -rlI "AggregateRoot|IAggregateRoot" CODE`: **44 files**
- `grep -rhI "AggregateRoot|IAggregateRoot" CODE`: **75 occurrences**
- Code evidence:
  - `vc-platform/.../Platform.Core/Domain/IAggregateRoot.cs:5` — `public interface IAggregateRoot : IEntity`
  - `vc-module-experience-api/.../XPurchase/CartAggregate.cs:39` — `class CartAggregate : Entity, IAggregateRoot, ICloneable`
  - `vc-module-experience-api/.../XOrder/CustomerOrderAggregate.cs:21` — `class CustomerOrderAggregate : Entity, IAggregateRoot, ICloneable`

**Verdict**: 🟠 Implemented but undocumented — **DOCS 0, CODE 75**
**Note**: VC literally ships an `IAggregateRoot` interface and `CartAggregate` / `CustomerOrderAggregate` classes, but zero user-facing docs name the pattern. Anyone reading xAPI code must already know DDD to parse it.

---

## Claim 3: "Value object" usage

**Context7** (query: "Does VirtoCommerce use value objects (immutable, identity-less types like Money, Address) in its domain modeling?"):
One single result: a caching snippet `class ComplexValueObject : ValueObject` with `GetCacheKey()`. The term is never **defined** in any doc; it just appears in a code sample.

**WebSearch** (query: "'value object' ecommerce DDD Money Address terminology prevalence"):
"Value object" is one of the most standard DDD terms in the industry; Money and Address are the textbook examples (Microsoft DDD guide, Fowler bliki, Wikipedia).

**Grep**:
- `grep -rlIi "value object" DOCS` (two-word): **0 files**
- `grep -rhI "ValueObject" DOCS` (one-word identifier, incidental): **3 occurrences** (all in one caching doc)
- `grep -rlI "ValueObject|IValueObject" CODE`: **85 files**
- `grep -rhI "ValueObject|IValueObject" CODE`: **118 occurrences**
- Evidence:
  - DOCS hits are all `Fundamentals/Caching/01-overview.md:53-62` — using `ValueObject` as a cache-key example, not as a DDD pattern.

**Verdict**: 🟠 Implemented but undocumented — **DOCS 3 (incidental), CODE 118**
**Note**: VC has a `ValueObject` base class used across the platform. Docs never introduce the DDD concept — readers see the term only as a caching-example identifier.

---

## Claim 4: "Entity" — DDD vs ORM meaning

**Context7** (query: "What does Entity mean in VirtoCommerce? Is it a DDD entity or an ORM/persistence entity?"):
Shows **both** meanings coexist. `CustomerOrder2Entity : CustomerOrderEntity` is persistence-layer (EF Core, `ToModel`/`FromModel`); `class ComplexValueObject : ValueObject` and `CartAggregate : Entity` use `Entity` as DDD base. The docs line explicitly acknowledges the split: "utilizes the **Data Mapper pattern** to isolate the domain from the persistence layer".

**WebSearch** (query: "DDD 'entity' vs ORM entity terminology confusion documentation"):
This overload is a famous DDD/ORM confusion (Matthias Noback, Tomas Tulka, Khalil Stemmler all warn about it). Best-practice platforms call them different things (e.g. `DomainEntity` vs `EntityModel`) or segregate the layers.

**Grep**:
- `grep -rlIi "\bentity\b|entities" DOCS`: **155 files**
- `grep -rhIi "\bentity\b|entities" DOCS`: **299 occurrences**
- `grep -rlI "class .*: Entity|: IEntity|EntityBase" CODE`: **161 files**
- `grep -rhI "class .*: Entity|: IEntity" CODE`: **186 occurrences**
- Key evidence of dual usage:
  - Domain sense: `vc-module-order/.../OrdersModule.Data/Model/AddressEntity.cs:8` — `class AddressEntity : Entity, IHasOuterId`
  - Persistence sense: `vc-module-order/.../Model/ConfigurationItemEntity.cs:12` — `class ConfigurationItemEntity : AuditableEntity, IDataEntity<ConfigurationItemEntity, ConfigurationItem>`
  - Docs conflation: `extending-domain-models.md` — domain extension section immediately followed by "Define New Persistence Entity Model" section inheriting `CustomerOrderEntity`.

**Verdict**: 🟡 Mentioned but semantically ambiguous
**Note**: "Entity" is used constantly (299 occurrences in docs) but the DDD-vs-ORM meaning is never disambiguated. The docs treat domain entities and persistence entities as interchangeable, with `ToModel`/`FromModel` implicitly bridging them via the Data Mapper pattern. A DDD-literate reader gets the picture; a newcomer sees the term mean two different things.

---

## Claim 5: "Specification pattern" usage

**Context7** (query: "Does VirtoCommerce use the specification pattern for querying or filtering domain objects?"):
No relevant results. Context7 returned GraphQL filtering / pagination snippets — docs never discuss the Specification pattern as a concept.

**WebSearch** (query: "'specification pattern' DDD business rules validation ecommerce"):
Specification pattern = Evans/Fowler standard DDD building block for combinable business rules (`AND`/`OR`/`NOT`), widely documented in .NET/DDD literature.

**Grep**:
- `grep -rlIi "specification pattern" DOCS`: **0 files**
- `grep -rhIi "specification pattern" DOCS`: **0 occurrences**
- `grep -rlI "ISpecification|class .*Specification\b" CODE`: **18 files**
- Code evidence:
  - `vc-platform/.../Platform.Core/Specifications/ISpecification.cs:3` — `public interface ISpecification<in T>`
  - `vc-module-experience-api/.../XPurchase/Specifications/CartHasPhysicalProductsSpecification.cs`
  - `vc-module-experience-api/.../XPurchase/Specifications/ProductIsBuyableSpecification.cs`
  - `vc-module-x-catalog/.../XCatalog.Core/Specifications/CatalogProductIsAvailableSpecification.cs`
  - Dedicated tests: `VirtoCommerce.XDigitalCatalog.Tests/Specifications/CatalogProductIsAvailableSpecificationTests.cs`

**Verdict**: 🟠 Implemented but undocumented — **DOCS 0, CODE 18 files**
**Note**: There is a generic `ISpecification<T>` interface plus half a dozen concrete specs (cart/product buyability, stock availability) with unit tests. Docs never mention the pattern exists, so extending or composing specs is invisible to a doc-only reader.

---

## Claim 6: "CQRS" usage

**Context7** (query: "Does VirtoCommerce use CQRS? How does VirtoCommerce split commands and queries in its xAPI/GraphQL layer?"):
Two direct hits: "xAPI utilizes the clean architecture principles of **CQRS and DDD**, where each command and query has a dedicated handler" and "Virto Commerce xAPI modules implement the **CQRS pattern** using MediatR". Also infrastructure-level: GraphQL queries go to read-only regions, mutations to the primary read-write region.

**WebSearch** (query: "'CQRS' 'command query' ecommerce platform architecture Sylius commercetools"):
CQRS is a standard pattern — Sylius uses it for placeOrder/addProductToCart commands; Redis/BytebyteGo/Microsoft all publish ecommerce CQRS guides.

**Grep**:
- `grep -rlIi "\bCQRS\b" DOCS`: **2 files**
- `grep -rhIi "\bCQRS\b" DOCS`: **3 occurrences**
- DOCS hits (all 3):
  - `PlatformDeveloperGuide/.../GraphQL-Storefront-API-Reference-xAPI/x-api-extensions.md:460`
  - `PlatformDeveloperGuide/.../GraphQL-Storefront-API-Reference-xAPI/custom-module-creation.md:74` & `:123`
- `grep -rlI "using MediatR|IMediator|IRequestHandler" CODE`: **354 files**
- `grep -rhI "using MediatR|IMediator|IRequestHandler" CODE`: **800 occurrences**

**Verdict**: 🟡 Mentioned but thin (docs 3/2 vs code 354 files)
**Note**: Three sentences in two xAPI sub-pages is the entire CQRS explanation for a platform that uses MediatR in 354 files. CQRS is never defined, never explained, and absent from every other module's docs. It reads like a casual label rather than a documented principle.

---

## Claim 7: "Command" / "Query" handlers usage

**Context7** (query: same as CQRS, since commands/queries are the CQRS building blocks):
Context7 returned "Replace command/query handlers" from `x-api-extensions.md` — VC documents **how** to override handlers, but only in the xAPI corner.

**WebSearch**: covered by CQRS query above — command/query handlers are the standard CQRS vocabulary pair.

**Grep**:
- `grep -rlIi "command handler|query handler|commandhandler|queryhandler" DOCS`: **9 files**
- `grep -rhIi "command handler|query handler|commandhandler|queryhandler" DOCS`: **28 occurrences**
- DOCS hits are all in `GraphQL-Storefront-API-Reference-xAPI/*` and `Tutorials-and-How-tos/How-tos/extending-cart-query-with-custom-parameter.md`
- `grep -rlI "CommandHandler|QueryHandler|IRequestHandler" CODE`: **394 files**
- `grep -rhI "class .*CommandHandler|class .*QueryHandler" CODE`: **375 class definitions**

**Verdict**: 🟡 Mentioned but thin
**Note**: Docs cover "how to replace a handler" only inside the xAPI corner. The 375 concrete handler classes elsewhere (core platform, modules) are invisible at the documentation level. A reader who never opens xAPI docs will never encounter the vocabulary.

---

## Claim 8: "Domain event" vs "integration event" usage

**Context7** (query: "Does VirtoCommerce distinguish domain events from integration events?"):
Multiple direct hits from `Fundamentals/Event-Driven-Development/using-domain-events.md`: defines `DomainEvent` POCO, shows `IEventHandler<CustomDomainEvent>`, shows `appBuilder.RegisterEventHandler<...>`. Modularity docs mention integration events: "a module may log events, while other modules can subscribe... Integration events are a lightweight manner of setting up communication between two modules."

**WebSearch** (query: "'domain event' 'integration event' difference DDD architecture"):
Industry standard: domain events stay in-process within a bounded context, integration events cross process/module boundaries and are typically asynchronous (Cesar de la Torre / Microsoft DDD-CQRS guide).

**Grep**:
- `grep -rlIi "domain event|integration event" DOCS`: **8 files**
- `grep -rhIi "domain event|integration event" DOCS`: **20 occurrences**
- `grep -rlI "DomainEvent|IntegrationEvent|IDomainEvent|IIntegrationEvent" CODE`: **56 files**
- `grep -rhI "DomainEvent" CODE`: **105 occurrences**
- `grep -rhI "IntegrationEvent" CODE`: **0 occurrences**
- Evidence of asymmetry:
  - Docs: `Modularity/02-folder-structure.md:62,89` split domain-vs-integration event folders, but the integration-event distinction is never developed.
  - Code: `DomainEvent` is a base class (e.g. `GenericChangedEntryEvent<T> : DomainEvent`, `UserLoginEvent : DomainEvent`); there is **no** `IntegrationEvent` class. The distinction exists only in prose, not in code.

**Verdict**: 🟡 Mentioned but thin / asymmetric
**Note**: VC docs do explain `DomainEvent` (one dedicated fundamentals page), but "integration event" is a passing label with no classifier class — it reads as two folders and one paragraph in the modularity overview, not a conceptual pillar.

---

## Claim 9: "Bounded context" usage

**Context7** (query: "Does VirtoCommerce use bounded contexts to separate different business domains? Is each module a bounded context?"):
No direct hits. Returns folder-structure and module-boundary best-practice content: "the primary goal is to achieve a meaningful separation guided by domain knowledge... emphasis should be on business capabilities and cohesion." Describes the concept without ever naming it.

**WebSearch** (query: "'bounded context' DDD ecommerce documentation module architecture"):
Bounded context is the central DDD pattern; ecommerce tutorials (Spring/Java, DDD samples) map `Sales → Catalog/Cart/Order` contexts explicitly.

**Grep**:
- `grep -rlIi "bounded context" DOCS`: **1 file**
- `grep -rhIi "bounded context" DOCS`: **1 occurrence**
- The one hit: `PlatformDeveloperGuide/.../Modularity/01-overview.md:175` — just a "Readmore" link to Martin Fowler's blog; the term is **never used in VC's own prose**.
- `grep -rlI "BoundedContext" CODE`: **0 files**

**Verdict**: 🔴 Absent
**Note**: VC's modularity/best-practices pages describe the idea ("domain knowledge guides module boundaries") but refuse to use the term. The only mention is an outbound link to Fowler. Modules are **de facto** bounded contexts but never labelled as such.

---

## Claim 10: "Anti-corruption layer" usage

**Context7** (query: "Does VirtoCommerce use an anti-corruption layer when integrating with legacy or external systems?"):
No relevant results — returned vc-shell widget docs and modularity prose. VC's inter-module communication is described via events and shared interfaces, never as an anti-corruption layer.

**WebSearch**: ACL is a standard DDD pattern for protecting a bounded context from foreign models (Evans, Microsoft DDD guide).

**Grep**:
- `grep -rlIi "anti-corruption layer|anticorruption layer|anti corruption layer" DOCS`: **0 files**
- `grep -rhIi "anti-corruption layer|..." DOCS + CODE`: **0 occurrences**

**Verdict**: 🔴 Absent
**Note**: Term never appears anywhere in docs or code. VC's `ToModel`/`FromModel` on persistence entities and GraphQL input-type mapping both play ACL-ish roles, but are never framed that way.

---

## Group shape

VirtoCommerce is **structurally DDD-native but linguistically DDD-shy**. It ships `IAggregateRoot`, `ValueObject`, `DomainEvent`, `ISpecification<T>`, MediatR CQRS handlers, and a Data Mapper between domain and persistence — the pattern inventory is all there. But the **documentation almost refuses to name the patterns**: it owns only two terms confidently — "domain model" (✅) and "domain event" (partially) — while the rest live in code only or get glancing one-paragraph mentions.

**Five mismatches stand out (🟠 / 🔴)**:
- **Aggregate root** — DOCS **0** / CODE **75 occurrences, 44 files** (`IAggregateRoot`, `CartAggregate`, `CustomerOrderAggregate`).
- **Value object** — DOCS **3 incidental (caching example)** / CODE **118 occurrences, 85 files**.
- **Specification pattern** — DOCS **0** / CODE **18 files** with `ISpecification<T>` and a full `XPurchase.Specifications` namespace.
- **Bounded context** — DOCS **1** (a Fowler link) / CODE **0**; the concept is described ("domain knowledge guides module boundaries") without ever being named.
- **Anti-corruption layer** — DOCS **0** / CODE **0**; pattern unnamed despite `ToModel`/`FromModel` playing the role.

**Two soft mismatches (🟡)**:
- **CQRS** — DOCS **3 mentions in 2 xAPI files** / CODE **354 files** using MediatR handlers.
- **Command/query handlers** — DOCS **28 mentions in 9 files**, all concentrated in xAPI / one tutorial / CODE **394 files, 375 handler classes**.

**One semantic overload (🟡)**: "Entity" is used 299 times in docs but never disambiguated between DDD-entity (identity) and EF-entity (table row); `Entity` appears as a base class for both.

Readers coming from commercetools/Sylius/Spryker (all explicit about DDD vocabulary) would find VC's docs architecturally competent but linguistically sparse — they'd need to read the source to discover that VC actually implements most of what they'd expect.
