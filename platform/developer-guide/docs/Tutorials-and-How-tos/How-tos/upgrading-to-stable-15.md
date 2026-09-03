# Upgrade to Stable 15

Stable 15 upgrades the Platform to version 3.1039.0 and refreshes the bundle modules. It removes code that was marked obsolete in earlier releases and introduces two platform-driven migrations that affect any module built with `TreatWarningsAsErrors`. This guide explains the removal policy and how to adapt downstream code.

To perform the upgrade itself, see the [Stable releases](/platform/developer-guide/latest/Updating-Virto-Commerce-Based-Project/stable-releases/) guide. This page covers only the breaking changes.

## Removal policy

A member marked with the `[Obsolete]` attribute is removed in Stable 15 when it has no diagnostic ID, or a diagnostic ID from VC0001 through VC0011. Members marked VC0012 and higher are kept as obsolete for a future release.

* If your code calls a removed member, replace it as described below. The build fails until you do.
* If your code calls a member that is kept but obsolete, it still compiles, but plan to migrate it before the next stable release.

## Platform changes

The Platform, updated to version 3.1039.0, removes five obsolete members. None were used inside the Platform itself, so the impact is downstream only.

| Removed member | Replacement |
| --- | --- |
| `StringExtensions.EqualsInvariant(string, string)` | `EqualsIgnoreCase()` |
| `IHasLanguage` | `VirtoCommerce.Platform.Core.Common.IHasLanguageCode` |
| `ConsoleLog` | Serilog `Log.Logger`, or an injected `ILogger` |
| `PlatformDbContext._idLength64` | `DbContextBase.Length64` or `UserNameLength` |
| `PlatformDbContext._idLength2048` | `DbContextBase.Length2048` |

How to adapt:

* `EqualsInvariant` to `EqualsIgnoreCase`. A mechanical rename. The signature and semantics are identical (`string.Equals(a, b, StringComparison.OrdinalIgnoreCase)`).
* `IHasLanguage` to `IHasLanguageCode`. The `LanguageCode` member is unchanged. Verify your implementers expose `LanguageCode { get; }`.
* `ConsoleLog`. Replace `ConsoleLog.BeginOperation` and `EndOperation` with `ILogger` logging.
* Length constants. Derived `DbContext` classes should use the public `DbContextBase.Length64`, `Length2048`, and `UserNameLength` constants.

## Core module changes

The Core module, updated to version 3.1007.0, removes two condition-tree helpers and relocates the SEO and Outlines types to their own modules.

| Removed member | Replacement |
| --- | --- |
| `ConditionTree.WithAvailConditions(params IConditionTree[])` | `WithAvailableChildren()` |
| `ConditionTree.WithChildrens(params IConditionTree[])` | `WithChildren()` |

### SEO and Outlines relocation

The SEO and Outlines types move out of Core into the Seo and Catalog modules. Update your `using` directives and type references.

| Removed Core type | Replacement |
| --- | --- |
| `Seo.ISeoSupport` | `VirtoCommerce.Seo.Core.Models.ISeoSupport` |
| `Seo.ISeoResolver` | `VirtoCommerce.Seo.Core.Services.ISeoResolver` |
| `Seo.ISeoDuplicatesDetector` | `VirtoCommerce.Seo.Core.Services.ISeoDuplicatesDetector` |
| `Seo.CompositeSeoResolver`, `CompositeSeoBySlugResolver` | `VirtoCommerce.Seo.Core.Services.ICompositeSeoResolver` |
| `Seo.SeoSearchCriteria` | `VirtoCommerce.Seo.Core.Models.SeoSearchCriteria` |
| `Data.Seo.NullSeoDuplicateDetector` | `VirtoCommerce.Seo.Data.Services.NullSeoDuplicateDetector` |
| `Outlines.IHasOutlines` | `VirtoCommerce.CatalogModule.Core.Outlines.IHasOutline` |
| `Outlines.Outline`, `OutlineItem` | `VirtoCommerce.CatalogModule.Core.Outlines.Outline`, `OutlineItem` |

### Types kept as bridges

Two SEO types stay in Core for Stable 15 so external modules have one more release to migrate. Both are obsolete and will be removed in the next stable release.

* `Seo.ISeoBySlugResolver` (interface only). Its Core implementation, `CompositeSeoBySlugResolver`, is already removed. Migrate off the interface to `ICompositeSeoResolver` or `ISeoResolver`.
* `Seo.SeoInfo`. Retained because it is the return type of `ISeoBySlugResolver.FindSeoBySlugAsync`. It no longer derives from `IHasLanguage`, but keeps its `LanguageCode` property.

## Module changes

### Assets module

AzureBlobAssets, updated to version 3.1006.0, removes the dead `ConvertToBlobInfo(BlobItem, Uri)` and `ConvertToBlobFolder(BlobHierarchyItem, Uri, BlobContainerProperties)` overloads. Use the base-URI overloads instead. The `CdnUrl` alias is kept for now.

### Search module

ElasticSearch8, updated to version 3.1006.0, removes obsolete overloads. Use the `documentType`-parameter overloads or `IElasticSearchDocumentConverter`.

| Removed member | Replacement |
| --- | --- |
| `UpdateMappingAsync(string, Properties)` | the `documentType` overload |
| `ConvertToProviderDocument(IndexDocument, IDictionary)` | `IElasticSearchDocumentConverter` |
| `CreateIndexAsync(string, string)` | the `documentType` overload |
| `ConfigureIndexSettings(IndexSettingsDescriptor)` | internal, removed with `CreateIndexAsync` |

### Cart module

Cart, updated to version 3.1006.0, removes the `WishlistCartType` constant.

### Store module

Store, updated to version 3.1005.0, removes an SEO resolver and a REST action.

| Removed member | Replacement |
| --- | --- |
| `StoreSeoBySlugResolver` | `VirtoCommerce.Seo.Core.Services.ISeoResolver`. Store's `StoreSeoResolver` supersedes it. |
| `StoreModuleController.GetStores()` REST action | `POST api/stores/search` |

### Catalog module

Catalog, updated to version 3.1029.0, removes the following:

| Removed member | Replacement |
| --- | --- |
| `CatalogSeoBySlugResolver` | `CatalogSeoResolver` |
| `ModuleConstants.OutlineDelimiter` | `OutlineString.NameDelimiter` |
| `Data.Model.LocalizedStringEntity<T>` | `Platform.Data.Model.LocalizedStringEntity<T>` |
| `GetAllChildrenCategoriesIdsAsync` (raw command) | `GetChildCategoriesAsync` |
| `ProductDocumentBuilder` four-argument constructor | the current constructor |
| `CategoryService.PreloadCategoryBranchAsync`, `SearchCategoriesHierarchyAsync` | dead code, no replacement |
| `Category.Path` obsolete setter | removed |

### xAPI module

xAPI, updated to version 3.1011.0, removes `IHasLanguageExtensions.FirstBestMatchForLanguage(IEnumerable<IHasLanguage>)`, which depended on the removed platform `IHasLanguage`. Use the `IHasLanguageCode` overload.

### xOrder module

xOrder, updated to version 3.1005.0, stops calling the obsolete `CartAggregate.ValidateAsync(CartValidationContext, ruleSet)` and calls the non-obsolete `ValidateAsync(string ruleSet)` instead, which builds the validation context internally.

* Public API change. `CreateOrderFromCartCommandHandler`'s constructor no longer takes an `ICartValidationContextFactory` parameter. Subclasses and direct constructor calls must drop that argument. DI registration is unaffected.
* Behavioral change (intended). Validation now runs against the products reresolved for the cart's current items at validation time, so it reflects the cart as it will be ordered.

## Migrate ICancellationToken to CancellationToken

This is a forced migration rather than a removal. The Platform keeps `ICancellationToken` marked obsolete (VC0014), but with `TreatWarningsAsErrors` any module that uses it fails to build once it references the new Platform version. The Platform's `IExportSupport` and `IImportSupport` now expose a modern `CancellationToken` overload, while the `ICancellationToken` overload throws by default.

To migrate a module:

1. Implement the modern `CancellationToken` overload of `IExportSupport` and `IImportSupport`, typically in the module's export/import helper and the **Module.cs** export and import methods.
1. At Hangfire job boundaries, replace `new JobCancellationTokenWrapper(jobToken)` with `jobToken.ShutdownToken`.
1. Remove null-conditional access on the token, since it is now a struct.
1. Update unit tests to pass a real `CancellationToken`, `CancellationToken.None`, or a cancelled `CancellationTokenSource` instead of mocked, null, or wrapped tokens.

This change applies across most bundle modules.

The module now builds against the modern `CancellationToken` overloads with `TreatWarningsAsErrors` enabled.

## Query installed modules

The Platform deprecated the read-only module-query path, `IModuleCatalog` (VC0014), and the static `ModuleBootstrapper.Instance`. The new interfaces live in `VirtoCommerce.Platform.Core.Modularity`, so drop the `using VirtoCommerce.Platform.Modules;` import.

* From controllers, handlers, or services, inject `IModuleService` from DI.
* From a module's **Module.cs** during `Initialize` or `PostInitialize`, implement `IHasModuleService`. The loader sets the property before `Initialize` runs.

```csharp
public class Module : IModule, IHasModuleService
{
    public IModuleService ModuleService { get; set; }

    public void PostInitialize(IApplicationBuilder appBuilder)
    {
        if (ModuleService.IsInstalled("VirtoCommerce.WhiteLabeling"))
        {
            // ...
        }
    }
}
```

Both replace the obsolete `IModuleCatalog` and the static `ModuleBootstrapper.Instance`.

## Deferred removals

The following members are kept as obsolete in Stable 15 to avoid a large cascading migration. They still compile, but plan to migrate them before the next stable release, when they are removed.

* `Seo.ISeoBySlugResolver` and `Seo.SeoInfo` in Core.
* `CdnUrl` in AzureBlobAssets.
* `ItemResponseGroup.Variations` and `WithVariations`, and the `ProductDocumentBuilder.CreateDocument` sync-to-async change with `IndexLocalizedName`, in Catalog.
* Inventory interface-method consolidations, for example `SearchInventoriesAsync` to `SearchAsync`, and `GetByIdsAsync` to `GetAsync`.
* Several xAPI members, for example `SeoInfo` extensions, `StoreSettings` properties, `SlugInfoQuery.Slug`, and `IUserManagerCore.CheckUserState`.
* `Customer.SelectedAddressId`, which is a persisted database column.
* `CartAggregate.ValidateAsync(CartValidationContext, ruleSet)` in xCart (VC0009).

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../Tutorials/extending-domain-models">← Extending domain models</a>
    <a href="../upgrading-to-dot-net-10">Upgrading to Virto Commerce on .NET 10 →</a>
</div>
