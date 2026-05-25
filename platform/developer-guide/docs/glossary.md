# Glossary

This glossary maps Virto Commerce developer vocabulary to the industry terms used in other ecommerce platforms. Use it as a reverse lookup when searching for a concept you know by a different name.

For business and operations vocabulary, such as Catalog, Order, or Fulfillment Center, see the [User guide glossary](/platform/user-guide/latest/glossary).

## App module
A self-contained slice of a VC-Shell custom app: a Vue 3 unit that bundles its blades, composables, locales, and side effects under a single `defineAppModule({ blades, locales })` declaration in **index.ts**. The host app installs an app module by importing it in **main.ts**, or by loading it at runtime through Module Federation when the module is shipped as a remote. App modules are the frontend counterpart of a Platform module (which is .NET, server-side, and ships in **module.manifest**); the two are independent units with separate release cycles. The same Platform may serve many apps, each composed of many app modules.

See also [Modules concept](custom-apps-development/vc-shell/concepts/modules.md) and [Module Federation concept](custom-apps-development/vc-shell/concepts/module-federation.md).

## Catalog property
A user-defined field added at runtime to a catalog, category, product, or product variation. Values are persisted in a separate table (the Entity-Attribute-Value pattern) and cascade down the catalog hierarchy, so a variation receives its product's properties, a product its category's, and a category its catalog's. Catalog properties support multi-value, multilingual, and dictionary (lookup) modifiers, plus validation rules and display ordering. Values can be of one of the predefined types (text, number, measure, etc.).

Equivalent in other ecommerce platforms:

| Virto Commerce | Shopify | Adobe Commerce (Magento) | commercetools | BigCommerce |
| --- | --- | --- | --- | --- |
| Catalog property | Product option | n/a (uses EAV) | Attribute definition | Product option |

See also [Manage Properties](/platform/user-guide/latest/catalog/managing-properties) for the configuration walkthrough.

## Dynamic property
A user-defined field added at runtime to any domain object that implements `IHasDynamicProperties`, scoped by an `ObjectType` discriminator. Values are persisted in a separate table rather than as columns on the object (the Entity-Attribute-Value pattern), so adding or removing such properties on an object requires no schema migration. Dynamic properties support multi-value, multilingual, and dictionary (lookup) modifiers. Values can be of one of the predefined types (text, number, etc.).

Equivalent in other ecommerce platforms:

| Virto Commerce | Shopify | Adobe Commerce (Magento) | commercetools | BigCommerce |
| --- | --- | --- | --- | --- |
| Dynamic property | Metafield | Custom attribute (EAV) | Custom field | Metafield |

See also [Managing Dynamic Properties](Fundamentals/Dynamic-Properties/overview.md) for the object model.

## Module
A self-contained .NET project that plugs into the Virto Commerce Platform process at runtime to deliver a single bounded slice of functionality (Catalog, Pricing, Orders, etc.) end-to-end: back-end services, REST endpoints, persistence, and Admin UI extensions. Each module implements `IModule` (lifecycle methods `Initialize`, `PostInitialize`, `Uninstall`) and ships a **module.manifest** file declaring its identifier, version, and dependencies. The Platform follows the Modular Monolith pattern with vertical slices: it is composed from the modules a solution needs, with cross-module communication through integration events, shared services, or extension points rather than direct references. A module is distinct from a custom App built on the VC-Shell SDK, which is a standalone web UI that talks to the Platform over its public APIs.

Equivalent in other ecommerce platforms:

| Virto Commerce | Shopify | Adobe Commerce (Magento) | commercetools | BigCommerce |
| --- | --- | --- | --- | --- |
| Module | n/a (uses Apps) | Module | n/a (composable architecture) | n/a (uses Apps) |

See also [Modular Architecture Overview](Fundamentals/Modularity/01-overview.md) for the architecture deep-dive and [VC-Shell custom apps overview](custom-apps-development/overview.md) for the App concept.

## Workspace
A top-level blade in a VC-Shell custom app, declared with `isWorkspace: true` on its `defineBlade` config. A workspace blade is the first frame the user sees when they enter a section from the main menu: typically a list view from which child blades open to the right in the blade stack. Non-workspace blades cannot be opened directly from the menu; they require a parent workspace to host them. Within a single app, there is one active workspace at a time, and switching workspaces collapses the blade stack of the previous one.

See also [Blade Navigation concept](custom-apps-development/vc-shell/concepts/blade-navigation.md).
