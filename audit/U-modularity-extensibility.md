# Group U — Modularity & Extensibility (incl. AbstractTypeFactory)

Scope note: this group MUST cross-check DOCS vs CODE grep counts for every claim
(per plan's 🟠 rule). Every claim below reports both.

DOCS = VirtoCommerce + PlatformUserGuide + PlatformDeveloperGuide + StorefrontUserGuide + StorefrontDeveloperGuide + MarketplaceUserGuide + DeploymentGuide + B2BExperts.
CODE = PlatformBackendSourceCode + PlatformFrontendSourceCode + FrontendSourceCode.

---

## Claim 1: "Polymorphism" term appears in docs.

**Context7** (`/virtocommerce/vc-docs`, query: "What is AbstractTypeFactory and how does polymorphism work?"):
Context7 returns AbstractTypeFactory examples but never uses the word "polymorphism". It talks about "type inheritance", "override", "derived type", "extension concept" — but the noun "polymorphism" is not surfaced.

**WebSearch** (query: "Magento 2 preferences plugins override polymorphism"):
Competitor docs and blogs (Magento/Adobe Commerce) explicitly discuss plugin chains as "polymorphism / AOP" behaviour. The word is ecosystem-common for .NET/OO devs researching "how do I replace a built-in class?".

**Grep**:
- `grep -rli "polymorphism" DOCS` → **1 file** (`PlatformDeveloperGuide/.../type-inheritance-support-in-swagger.md`)
- `grep -rli "polymorphism" CODE` → **2 files** (`vc-platform/.../SwaggerServiceCollectionExtensions.cs`, `vc-module-payment/README.md`)
- `grep -rli "polymorphic" DOCS` → **1 file** (same Swagger how-to)
- `grep -rli "polymorphic" CODE` → **14 files**, e.g.
  - `vc-platform/src/VirtoCommerce.Platform.Core/JsonConverters/PolymorphJsonContractResolver.cs`
  - `vc-platform/src/VirtoCommerce.Platform.Core/JsonConverters/PolymorphJsonConverter.cs`
  - `vc-module-order/src/VirtoCommerce.OrdersModule.Web/JsonConverters/PolymorphicOperationJsonConverter.cs`
  - `vc-platform/src/VirtoCommerce.Platform.Core/Domain/AbstractTypeFactory.cs` (referenced indirectly)
  - `vc-module-catalog/src/VirtoCommerce.CatalogModule.Core/Serialization/ProductJsonSerializer.cs`

**Verdict**: 🟠 Implemented but undocumented (as vocabulary).
**Note**: The concept is pervasive in the codebase (Polymorph* JSON converters, AbstractTypeFactory type-mapping) but docs name it "type inheritance" only. A dev searching "polymorphism" in VC docs finds nothing that explains the extension model by that name. **1 DOC file vs 15+ CODE files.**

---

## Claim 2: "Method overriding" / "override" term appears in docs.

**Context7**: Returns multiple "override" examples — `AbstractTypeFactory<>.OverrideType<>()`, `OverrideType<>.WithFactory(...)`, and the cart-validation how-to "Overriding rounding policy". The word "override" is the dominant verb in extensibility prose; "method overriding" (the OOP term) is not.

**WebSearch**: "Override" is the vocabulary competitor platforms use ("Override a core class in Magento 2", "Adobe Commerce preferences override", "Shopify theme overrides"). This matches VC's usage.

**Grep**:
- `grep -rli "override" DOCS` → **45 files**
- `grep -rli "override" CODE` → **2 783 files**
- `grep -rli "method overriding" DOCS` → **0 files**
- `grep -rli "method overriding" CODE` → **0 files**

Top DOC hits: `Extensibility/overview.md`, `Extensibility/extending-application-user.md`, `Tutorials-and-How-tos/How-tos/overriding-rounding-policy.md`, `Tutorials-and-How-tos/Tutorials/extending-domain-models.md`, `Fundamentals/Security/extensions/extending-usermanager-and-rolemanager.md`.

**Verdict**: ✅ Well documented (as "override" — industry-standard verb).
**Note**: CODE count (2 783) dwarfs DOCS count (45) but this is noise (the C# `override` keyword). The **concept** of overriding is well covered in docs. The compound noun "method overriding" never appears in either DOCS or CODE — nobody talks that way in .NET practice.

---

## Claim 3: "AbstractTypeFactory" — documented as an extensibility concept (not just API reference).

**Context7**: Returns crisp conceptual prose: "The `AbstractTypeFactory<>` is the key element of Virto's extension concept that is responsible for activating a particular type of instance based on the internal type mapping table. Each piece of code that should support domain type extensions must use `AbstractTypeFactory<BaseType>.TryCreateInstance()` instead of the `new BaseType()` statement." Full working example with `CustomerOrder` → `CustomerOrder2` in `extending-domain-models.md`, plus reuse in `customizing-cart-validation-policies.md`, `extending-application-user.md`, `extending-cart-query-with-custom-parameter.md`.

**WebSearch**: Not run — Context7 answered.

**Grep**:
- `grep -rli "AbstractTypeFactory" DOCS` → **11 files**
- `grep -rli "AbstractTypeFactory" CODE` → **693 files**

Top DOC hits:
- `PlatformDeveloperGuide/.../Extensibility/extending-application-user.md`
- `PlatformDeveloperGuide/.../Extensibility/extending-dynamic-expression-tree.md`
- `PlatformDeveloperGuide/.../Tutorials/extending-domain-models.md` (the canonical explanation)
- `PlatformDeveloperGuide/.../How-tos/customizing-cart-validation-policies.md`
- `PlatformDeveloperGuide/.../How-tos/extending-cart-query-with-custom-parameter.md`
- `PlatformDeveloperGuide/.../How-tos/type-inheritance-support-in-swagger.md`
- `PlatformDeveloperGuide/.../GraphQL-Storefront-API-Reference-xAPI/x-api-extensions.md`
- `PlatformDeveloperGuide/.../Fundamentals/SEO/add-seo-to-module.md`
- Plus release-note hits in `PlatformUserGuide/versions/v3-2025-S11.md`, `v3-2025-S12.md`.

Top CODE hits:
- `PlatformBackendSourceCode/vc-platform/src/VirtoCommerce.Platform.Core/Domain/AbstractTypeFactory.cs` (the definition)
- `.../Platform.Core/JsonConverters/PolymorphJsonContractResolver.cs`
- `.../Platform.Core/JsonConverters/PolymorphJsonConverter.cs`
- `.../Platform.Core/Security/Permission.cs` / `PermissionScope.cs`
- `.../Platform.Data/ChangeLog/ChangeLog*.cs`

**Verdict**: 🟡 Mentioned and explained, but thin relative to code prevalence.
**Note**: The concept **is** documented (11 DOC files — including a dedicated tutorial). But 693 CODE files use it vs 11 DOC files ≈ **63×** ratio. There is no single "Complete guide to AbstractTypeFactory" page that lists `.TryCreateInstance()`, `.OverrideType<>()`, `.AddType<>()`, `.WithFactory()`, `.Types`, discriminator handling, or pitfalls (call-site ordering, `PostInitialize` vs `Initialize`). It's a teach-by-example treatment only. Borderline 🟠.

---

## Claim 4: "Dependency injection" in platform's own terms is thin.

**Context7**: Returns concrete DI examples (`serviceCollection.AddTransient<IMoneyRoundingPolicy, CustomMoneyRoundingPolicy>()`) but no page titled "Dependency injection in Virto Commerce". DI is introduced implicitly inside how-tos.

**WebSearch**: Not run — standard .NET DI terminology.

**Grep**:
- `grep -rli "dependency injection" DOCS` → **11 files**
- `grep -rli "dependency injection" CODE` → **8 files** (mostly README comments)
- `grep -rli "IServiceCollection\|IUnityContainer" CODE` → **179 files**
- `grep -rli "IServiceCollection|AddSingleton|AddTransient|AddScoped" DOCS` → **30 files**
- `grep -rli "DI\|IoC" DOCS` → **16 files**

Top DOC hits: `Extensibility/overview.md`, `Fundamentals/Security/extensions/extending-authorization-policies.md`, `Tutorials-and-How-tos/How-tos/overriding-rounding-policy.md`, `GraphQL-Storefront-API-Reference-xAPI/x-api-extensions.md`, plus vc-shell composables.

**Verdict**: 🟡 Mentioned but thin.
**Note**: No first-class "Dependency injection" concept page — DI is cargo-culted into every how-to without ever being explained. A fresh .NET dev is expected to already know ASP.NET Core DI. No discussion of service lifetimes, scope boundaries, module-vs-platform service registration order, or DI pitfalls specific to VC modules. Reasonable for a seasoned .NET dev; opaque for a newcomer.

---

## Claim 5: Module / plugin anatomy is thin.

**Context7**: Returns the `module.manifest` XML structure, dependency declarations, and notes about `IModule.Initialize` / `PostInitialize`.

**WebSearch**: Not run — internal VC terminology.

**Grep**:
- `grep -rli "module manifest|module.manifest" DOCS` → **23 files**
- `grep -rli "IModule|ModuleBase" CODE` → **853 files**

DOCS has a dedicated "Modularity" section:
- `Fundamentals/Modularity/01-overview.md`
- `02-folder-structure.md`
- `03-versioning-and-dependencies.md`
- `04-loading-modules-into-app-process.md`
- `05-best-practices.md`
- `06-module-manifest-file.md`
- `optional-dependency.md`
- `IPlatformStartup.md`

**Verdict**: ✅ Well documented.
**Note**: Modularity has its own Fundamentals section with folder-structure, manifest, loading, and best-practices pages. Not thin. The word "plugin" is not used in VC — they say "module". That's a vocabulary gap for devs searching "Virto Commerce plugin" (Magento/WordPress mental model), but not a content gap.

---

## Claim 6: Dynamic properties concept vs attributes/custom fields is thin.

**Context7**: (Answered via Claim 3 query — AbstractTypeFactory links out to Dynamic Properties.)

**WebSearch**: Not run — cross-checked DOCS.

**Grep**:
- `grep -rli "dynamic properties|dynamic property" DOCS` → **58 files**
- `grep -rli "DynamicProperty" CODE` → **788 files**
- `grep -rli "custom fields|custom attributes|product attributes" DOCS` → **13 files**
- `grep -rli "dynamic property|dynamic properties" PlatformUserGuide` → 6 files

Dedicated folder: `PlatformDeveloperGuide/.../Fundamentals/Dynamic-Properties/`. Referenced from `Extensibility/overview.md` and `key-extensibility-points.md`.

**Verdict**: ✅ / 🟡 Well documented as a concept but **vocabulary collision** with industry terms.
**Note**: Docs use the proprietary "dynamic property" label 58× and never cross-map it to the industry-standard terms "custom field", "custom attribute", "EAV" (Magento), "metafield" (Shopify), "custom type" (commercetools). A dev searching "Virto Commerce custom fields" finds ~0 targeted hits. 🟠 on vocabulary bridge, ✅ on concept itself.

---

## Claim 7: Events / handlers / subscribers are thin.

**Context7**: Not re-queried (budget); covered by Modularity/Extensibility returns.

**WebSearch**: Not run.

**Grep**:
- `grep -rli "domain event|domain events" DOCS` → **6 files**
- `grep -rli "IEventHandler|DomainEvent" CODE` → **117 files**
- `Event-Driven-Development/` folder contents: `using-domain-events.md`, `event-bus.md`, `event-bus-configuration.md`, `webhooks.md` (4 pages).

**Verdict**: 🟡 Mentioned but thin.
**Note**: Four-page folder covers event bus + domain events + webhooks, but the vocabulary (`IEventHandler<T>`, `IHandler`, `Handle`, "subscriber") is almost absent in docs. 117 CODE files use it vs 6 DOC files. No comparison to "observers / subscribers" that devs from Magento/Shopify/Rails know. The term "handler" is the implementation word but "subscriber" / "listener" are never mapped in. Borderline 🟠 on vocabulary.

---

## Claim 8: Customizing / overriding a built-in entity model is thin.

**Context7**: Perfect hit — `extending-domain-models.md` is the canonical tutorial, referenced from `Extensibility/overview.md` → "Extending domain models" and linked from `customizing-cart-validation-policies.md`.

**WebSearch**: Not run.

**Grep**:
- `grep -rli "AbstractTypeFactory" DOCS` → 11 files (same set as Claim 3)
- `grep -rli "extending|extensibility" PlatformDeveloperGuide` → **49 files**
- `grep -rli "override|replace|customiz" PlatformDeveloperGuide` → broad; hits `overriding-rounding-policy.md`, `customizing-cart-validation-policies.md`, `extending-application-user.md`, `extending-domain-models.md`, `extending-database-model.md`, `extending-notification-types.md`, `extending-authorization-policies.md`, `extending-dynamic-expression-tree.md`, `extending-cart-query-with-custom-parameter.md`.

**Verdict**: ✅ Well documented.
**Note**: This is arguably the best-documented extensibility story in the repo — there is a full tutorial with `CustomerOrder`→`CustomerOrder2` including DB migration, `AbstractTypeFactory.OverrideType<>`, and DI re-registration. Not thin.

---

## Claim 9: Liquid / scripting extensibility is thin.

**Context7**: Not queried (not focus of this group).

**WebSearch**: Not run.

**Grep**:
- `grep -rli "liquid" DOCS` → **8 files** (mostly `Notifications/notification-templates.md`, theme/storefront docs)
- `grep -rli "liquid" CODE` → **33 files**

DOC coverage: Liquid is used for notification templates and storefront theme templates. No dedicated "Liquid scripting guide" or cookbook. Notification doc covers the variable set for one template type; no general Liquid reference, no filter catalog, no "custom Liquid drop" tutorial.

**Verdict**: 🟡 Mentioned but thin.
**Note**: CODE uses Liquid as a scripting surface (DotLiquid helpers, template rendering) but there is no user-facing "scripting extensibility" narrative. Gap: no "Liquid filters / tags reference", no custom-drop authoring guide. Low risk (niche extension surface) but thin.

---

## Claim 10: NuGet package publishing for custom modules is thin.

**Context7**: Returns the `vc-package.json` multi-source manifest (GithubReleases, GithubPrivateRepos, AzurePipelineArtifacts, **AzureUniversalPackages**, AzureBlob, GitlabJobArtifacts, Local) — VC's **custom** distribution system, not public nuget.org.

**WebSearch**: Not run.

**Grep**:
- `grep -rli "NuGet" DOCS` → **18 files**
- `grep -rli "NuGet" CODE` → **113 files**

Top DOC hits: `CLI-tools/package-management.md`, `CLI-tools/build-automation.md`, `CLI-tools/install-and-update-platform-and-modules.md`, `getting-to-know-platform.md`, `Back-End-Architecture/02-conceptual-overview.md`, `CLI-tools/overview.md`, `Extensibility/product-completeness-evaluator.md`.

**Verdict**: 🟠 Implemented but undocumented (as "NuGet publishing").
**Note**: VC consumes NuGet packages via `.csproj` references and distributes **modules** as zipped artifacts referenced from `vc-package.json` — **not** as public nuget.org packages. There is no "Publish your custom module on NuGet" how-to because the VC distribution model is different (zip + manifest in `modules_v3.json` + Github Releases / Azure Artifacts). This is a vocabulary gap: a dev asking "how do I publish my VC module on NuGet?" needs a doc saying "VC modules are NOT published to nuget.org; they are distributed as artifact zips. Here's how." No such page exists. **18 DOC vs 113 CODE** file-count is misleading — the 113 CODE hits are `.csproj` package references, not publishing guidance.

---

## Overall shape

- **Strong**: Modularity fundamentals (dedicated folder, manifest, folder structure, dependencies, best practices), the `extending-domain-models.md` tutorial, and the Extensibility overview — all well structured.
- **Weak (🟠)**: Vocabulary mapping. The codebase is deeply polymorphic (14+ `Polymorph*` files, 693 files touching `AbstractTypeFactory`), but docs hide this behind the phrase "type inheritance" and never use "polymorphism", "custom field", "subscriber/listener", "plugin", or "publish module to NuGet" — exactly the words a non-VC dev would search. Cross-check file counts make this stark: **polymorphism 1 DOC / 15+ CODE**, **AbstractTypeFactory 11 DOC / 693 CODE**, **DynamicProperty 58 DOC / 788 CODE**.
- **Medium**: Dependency injection is used everywhere but never explained as a standalone concept; Liquid scripting lacks a reference; events have the infra docs but miss "subscriber/listener" terminology.
